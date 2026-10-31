#!/usr/bin/env python3
"""Publish/remove only manifest-owned files in a dedicated STRATO directory."""

import argparse
import ftplib
import hashlib
import io
import json
import os
import re
import ssl
import stat
import sys
import tempfile
from contextlib import contextmanager
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit

from .github_pages import confirmation, repository
from .prepare_site import ROOT, site_url

MARKER = ".abc-deployment.json"


def required(name):
    value = os.environ.get(name, "")
    if not value:
        raise ValueError(f"Missing required secret: {name}")
    return value


def remote_directory(value):
    if (not re.fullmatch(r"/[A-Za-z0-9_~-][A-Za-z0-9._~/-]*", value)
            or value.endswith("/") or "//" in value or any(part in (".", "..") for part in value.split("/"))):
        raise ValueError("STRATO_REMOTE_DIR must be a dedicated absolute subdirectory, e.g. /abc-static (never / or a dot path).")
    return value


def relative_path(value):
    if (not isinstance(value, str) or not value or value == MARKER or value.startswith("/")
            or "\\" in value or any(ord(char) < 32 or ord(char) == 127 for char in value)
            or any(part in ("", ".", "..") for part in value.split("/"))):
        raise ValueError("Unsafe path in deployment manifest or site build.")
    return value


def owner_id(repo, public_url):
    return hashlib.sha256(f"{repo}\n{public_url}".encode()).hexdigest()


class SFTP:
    def __init__(self, client):
        self.client = client

    def list(self, path):
        return {
            entry.filename: "dir" if stat.S_ISDIR(entry.st_mode) else "file" if stat.S_ISREG(entry.st_mode) else "other"
            for entry in self.client.listdir_attr(path)
        }

    def mkdir(self, path):
        self.client.mkdir(path)

    def read(self, path):
        with self.client.open(path, "rb") as file:
            return file.read(2_000_001)

    def write(self, path, content):
        with self.client.open(path, "wb") as file:
            file.write(content)

    def remove(self, path):
        self.client.remove(path)

    def rmdir(self, path):
        self.client.rmdir(path)


class FTPS:
    def __init__(self, client):
        self.client = client

    def list(self, path):
        return {
            name: facts["type"] if facts["type"] in ("dir", "file") else "other"
            for name, facts in self.client.mlsd(path, facts=["type"])
            if facts["type"] not in ("cdir", "pdir")
        }

    def mkdir(self, path):
        self.client.mkd(path)

    def read(self, path):
        content = io.BytesIO()

        def append(chunk):
            if content.tell() + len(chunk) > 2_000_000:
                raise ValueError("Deployment manifest is too large.")
            content.write(chunk)

        self.client.retrbinary(f"RETR {path}", append)
        return content.getvalue()

    def write(self, path, content):
        self.client.storbinary(f"STOR {path}", io.BytesIO(content))

    def remove(self, path):
        self.client.delete(path)

    def rmdir(self, path):
        self.client.rmd(path)


@contextmanager
def connection():
    protocol = os.environ.get("STRATO_PROTOCOL", "") or "sftp"
    if protocol not in ("sftp", "ftps"):
        raise ValueError("STRATO_PROTOCOL must be sftp or explicit ftps. Unencrypted FTP is not supported.")
    host, user, password = required("STRATO_HOST"), required("STRATO_USERNAME"), required("STRATO_PASSWORD")
    if not re.fullmatch(r"[A-Za-z0-9.-]+", host):
        raise ValueError("STRATO_HOST must be a hostname, not a URL.")
    port = int(os.environ.get("STRATO_PORT", "") or ("22" if protocol == "sftp" else "21"))
    if not 1 <= port <= 65535:
        raise ValueError("STRATO_PORT must be between 1 and 65535.")
    if protocol == "sftp":
        import paramiko

        with tempfile.TemporaryDirectory() as directory:
            known_hosts = Path(directory) / "known_hosts"
            known_hosts.write_text(required("STRATO_KNOWN_HOSTS"))
            known_hosts.chmod(0o600)
            with paramiko.SSHClient() as ssh:
                ssh.load_host_keys(str(known_hosts))
                ssh.set_missing_host_key_policy(paramiko.RejectPolicy())
                ssh.connect(host, port=port, username=user, password=password,
                            allow_agent=False, look_for_keys=False,
                            timeout=30, auth_timeout=30, banner_timeout=30)
                with ssh.open_sftp() as sftp:
                    sftp.get_channel().settimeout(60)
                    yield SFTP(sftp)
    else:
        with ftplib.FTP_TLS(context=ssl.create_default_context(), timeout=30) as ftp:
            ftp.connect(host, port)
            ftp.login(user, password)
            ftp.prot_p()
            yield FTPS(ftp)


def listing(remote, path):
    entries = remote.list(path)
    for name in entries:
        if not name or name in (".", "..") or "/" in name or "\\" in name or any(ord(char) < 32 for char in name):
            raise ValueError("Server returned an unsafe directory entry.")
    return entries


def ensure_directory(remote, path, create):
    current = ""
    for part in PurePosixPath(path).parts[1:]:
        parent = current or "/"
        entries = listing(remote, parent)
        current += "/" + part
        if part not in entries:
            if not create:
                raise ValueError("The deployment directory does not exist.")
            remote.mkdir(current)
        elif entries[part] != "dir":
            raise ValueError("A remote path component is not a real directory (symlinks are refused).")


def inventory(remote, root):
    result = {}

    def visit(path, prefix=""):
        for name, kind in listing(remote, path).items():
            relative = prefix + name
            if relative != MARKER:
                relative_path(relative)
            if kind not in ("file", "dir"):
                raise ValueError("The deployment directory contains a symlink or unsupported entry.")
            result[relative] = kind
            if kind == "dir":
                visit(path + "/" + name, relative + "/")

    visit(root)
    return result


def load_manifest(remote, root, entries, owner):
    if MARKER not in entries:
        if entries:
            raise ValueError("Refusing to adopt a nonempty directory without this deployment's ownership manifest.")
        return set()
    if entries[MARKER] != "file":
        raise ValueError("The deployment marker is not a regular file.")
    content = remote.read(root + "/" + MARKER)
    if len(content) > 2_000_000:
        raise ValueError("Deployment manifest is too large.")
    data = json.loads(content)
    if not isinstance(data, dict) or data.get("schema") != 1 or data.get("owner") != owner:
        raise ValueError("Deployment ownership does not match this repository and target URL.")
    files = data.get("files")
    if not isinstance(files, list) or len(files) > 10000:
        raise ValueError("Invalid deployment manifest file list.")
    validated = {relative_path(file) for file in files}
    if len(validated) != len(files):
        raise ValueError("Duplicate manifest paths.")
    for file in validated:
        if entries.get(file, "file") != "file":
            raise ValueError("A managed file has been replaced by a directory.")
        if any(entries.get(str(parent), "dir") != "dir" for parent in PurePosixPath(file).parents if str(parent) != "."):
            raise ValueError("A managed parent has been replaced by a file.")
    return validated


def write_manifest(remote, root, owner, files):
    remote.write(root + "/" + MARKER, json.dumps({
        "schema": 1, "owner": owner, "files": sorted(files),
    }).encode())


def remove_files(remote, root, files, entries):
    for file in sorted(files):
        if file in entries:
            remote.remove(root + "/" + file)
    directories = {str(parent) for file in files for parent in PurePosixPath(file).parents if str(parent) != "."}
    for directory in sorted(directories, key=lambda value: (value.count("/"), value), reverse=True):
        path = root + "/" + directory
        if entries.get(directory) == "dir" and not listing(remote, path):
            remote.rmdir(path)


def deploy(remote, root, source, owner):
    files = {}
    for file in sorted(source.rglob("*")):
        if file.is_symlink():
            raise ValueError("Local build contains a symlink.")
        if file.is_file():
            files[relative_path(file.relative_to(source).as_posix())] = file.read_bytes()
    if "index.html" not in files:
        raise ValueError("No built index.html found.")
    if len(files) > 10000:
        raise ValueError("The site exceeds the deployment manifest file limit.")
    ensure_directory(remote, root, create=True)
    entries = inventory(remote, root)
    previous = load_manifest(remote, root, entries, owner)
    if len(previous | files.keys()) > 10000:
        raise ValueError("The combined old/new site exceeds the deployment manifest file limit.")
    for file in files:
        if file in entries and file not in previous:
            raise ValueError("Refusing to overwrite an unmanaged remote file or directory.")
        for parent in PurePosixPath(file).parents:
            if str(parent) != "." and entries.get(str(parent), "dir") != "dir":
                raise ValueError("A new file path conflicts with an existing remote file.")
    # Persist the union first so interrupted uploads can be retried or deleted.
    write_manifest(remote, root, owner, previous | files.keys())
    parents = {str(PurePosixPath(file).parent) for file in files if str(PurePosixPath(file).parent) != "."}
    for parent in sorted(parents, key=lambda value: (value.count("/"), value)):
        ensure_directory(remote, root + "/" + parent, create=True)
    for file, content in files.items():
        remote.write(root + "/" + file, content)
    remove_files(remote, root, previous - files.keys(), entries)
    write_manifest(remote, root, owner, files)
    print(f"Published {len(files)} managed files; removed {len(previous - files.keys())} obsolete paths.")


def delete(remote, root, owner):
    ensure_directory(remote, root, create=False)
    entries = inventory(remote, root)
    if MARKER not in entries:
        raise ValueError("No ownership manifest found; refusing deletion.")
    previous = load_manifest(remote, root, entries, owner)
    remove_files(remote, root, previous, entries)
    remote.remove(root + "/" + MARKER)
    print("Removed this deployment's managed files. The target directory and any unmanaged files were preserved.")


def apache_config(public_url):
    prefix = urlsplit(public_url).path
    return (
        "DirectoryIndex index.html\n"
        f"ErrorDocument 404 {prefix}/404.html\n"
        '<Files ".abc-deployment.json">\nRequire all denied\n</Files>\n'
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=["deploy", "delete"])
    args = parser.parse_args()
    try:
        repo = repository()
        if args.operation == "delete":
            confirmation(repo)
        root = remote_directory(required("STRATO_REMOTE_DIR"))
        public_url = site_url(required("STRATO_SITE_URL"))
        owner = owner_id(repo, public_url)
        source = ROOT / "dist/web-site"
        if args.operation == "deploy":
            if not (source / "index.html").is_file():
                raise ValueError("Prepare the web site before deploying.")
            (source / ".htaccess").write_text(apache_config(public_url))
        with connection() as remote:
            if args.operation == "deploy":
                deploy(remote, root, source, owner)
            else:
                delete(remote, root, owner)
    except (ValueError, OSError, RuntimeError, ImportError, ftplib.Error) as error:
        print(f"STRATO operation failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
