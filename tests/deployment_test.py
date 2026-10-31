import contextlib
import io
import json
import os
import ssl
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch
from urllib.error import HTTPError
from urllib.parse import unquote, urlsplit

from scripts import deploy_strato as strato
from scripts import github_pages as pages
from scripts import prepare_site as prepare


class PrepareTests(unittest.TestCase):
    def test_url_validation(self):
        self.assertEqual(prepare.site_url("https://example.com/repo/"), "https://example.com/repo")
        self.assertEqual(prepare.site_url("https://EXAMPLE.com:443/"), "https://example.com")
        for value in ["", "http://example.com", "https://user:pass@example.com", "https://example.com/?q=x",
                      "https://example.com/#x", "https://example.com/../x", "https://example.com/%2e%2e",
                      "https://example.com:8080", "https://example.com/\nx", 'https://bad"host.com']:
            with self.subTest(value=value), self.assertRaises(ValueError):
                prepare.site_url(value)

    def test_local_urls_are_explicit_relative_files(self):
        self.assertEqual(prepare.mapped_url("/kontakt/?q=a#details", "suche/index.html", "local"),
                         "../kontakt/index.html?q=a#details")
        self.assertEqual(prepare.mapped_url("/", "index.html", "local"), "index.html")
        self.assertEqual(prepare.mapped_url("/assets/images/a%20b.jpg", "suche/index.html", "local"),
                         "../assets/images/a%20b.jpg")
        for value in ["#content", "mailto:a@example.com", "https://elsewhere.test/", "//elsewhere.test/x"]:
            self.assertEqual(prepare.mapped_url(value, "index.html", "local"), value)
        with self.assertRaises(ValueError):
            prepare.mapped_url("/%2e%2e/secret", "index.html", "local")

    def test_web_subpath_and_canonical(self):
        parser = prepare.RewriteHTML("kontakt/index.html", "web", "https://owner.github.io/repo")
        parser.feed('<link rel="canonical" href="https://old.test/kontakt/"><a href="/suche/?q=A&amp;x=B">'
                    '<svg><circle r="2"/><path d="M0 0"/></svg></a>')
        result = "".join(parser.parts)
        self.assertIn('href="https://owner.github.io/repo/kontakt/"', result)
        self.assertIn('href="/repo/suche/?q=A&amp;x=B"', result)
        self.assertIn('<circle r="2" /><path d="M0 0" />', result)

    def test_local_bundle_contains_no_fetch_based_search(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, output = root / "source", root / "output"
            (source / "suche").mkdir(parents=True)
            (source / "assets/js").mkdir(parents=True)
            (source / "pagefind").mkdir()
            (source / "pagefind/pagefind.js").write_text("not copied")
            (source / "index.html").write_text(
                '<h1 id="page-title">Title &amp; text</h1><main data-pagefind-body>Visible'
                '<aside data-pagefind-ignore>Hidden</aside><p>Text</p></main><a href="/suche/">Search</a>')
            (source / "suche/index.html").write_text(
                '<link rel="stylesheet" href="/pagefind/pagefind-ui.css">'
                '<script defer src="/pagefind/pagefind-ui.js"></script>'
                '<script defer src="/assets/js/search.js"></script>')
            prepare.prepare(source, output, "local")
            self.assertFalse((output / "pagefind").exists())
            search = (output / "suche/index.html").read_text()
            self.assertNotIn("pagefind", search)
            self.assertIn('src="../assets/js/search-index.js"', search)
            self.assertIn('src="../assets/js/search-local.js"', search)
            index = (output / "assets/js/search-index.js").read_text()
            records = json.loads(index.removeprefix("window.ABC_LOCAL_SEARCH = ").rstrip(";\n"))
            self.assertEqual(records, [{"title": "Title & text", "text": "Visible Text", "url": "../index.html"}])
            self.assertTrue((output / "OPEN-ME.txt").is_file())
            prepare.prepare(source, output, "local")
            with self.assertRaises(ValueError):
                prepare.prepare(source, source.parent, "local")

    def test_complete_build_exports_have_no_broken_internal_links(self):
        class Links(prepare.HTMLParser):
            def __init__(self):
                super().__init__()
                self.urls = []

            def handle_starttag(self, tag, attrs):
                self.urls.extend(value for key, value in attrs if key in ("href", "src", "action") and value)

        with tempfile.TemporaryDirectory() as directory:
            for mode, base_url in [("local", ""), ("web", "https://example.com"),
                                   ("web", "https://owner.github.io/repository")]:
                with self.subTest(mode=mode, base_url=base_url):
                    output = Path(directory) / "output"
                    prepare.prepare(prepare.ROOT / "_site", output, mode, base_url)
                    for file in output.rglob("*.html"):
                        parser = Links()
                        parser.feed(file.read_text(encoding="utf-8"))
                        for value in parser.urls:
                            parsed = urlsplit(value)
                            if parsed.scheme or parsed.netloc or not parsed.path:
                                continue
                            if mode == "local":
                                self.assertFalse(parsed.path.startswith("/"), (file, value))
                                target = (file.parent / unquote(parsed.path)).resolve()
                            else:
                                prefix = urlsplit(base_url).path + "/"
                                self.assertTrue(parsed.path.startswith(prefix), (file, value))
                                target = output / unquote(parsed.path.removeprefix(prefix))
                                if parsed.path.endswith("/"):
                                    target /= "index.html"
                            target = target.resolve()
                            self.assertTrue(target.is_relative_to(output.resolve()), (file, value))
                            self.assertTrue(target.is_file(), (file, value, target))
                    if mode == "web":
                        sitemap = (output / "sitemap.xml").read_text(encoding="utf-8")
                        self.assertIn(f"<loc>{base_url}/</loc>", sitemap)
                        self.assertIn(f"Sitemap: {base_url}/sitemap.xml", (output / "robots.txt").read_text())


class PagesTests(unittest.TestCase):
    def setUp(self):
        quiet = contextlib.redirect_stdout(io.StringIO())
        quiet.__enter__()
        self.addCleanup(quiet.__exit__, None, None, None)

    def test_custom_domain(self):
        self.assertIsNone(pages.custom_domain(""))
        self.assertEqual(pages.custom_domain("WWW.Example.com"), "www.example.com")
        for value in ["https://example.com", "example.com/a", "example.com:443", "bad-.com", "example.com\ninjected=x"]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                pages.custom_domain(value)

    @patch.dict(os.environ, {"DELETE_CONFIRMATION": "wrong"})
    @patch.object(pages, "request")
    def test_delete_requires_confirmation_before_any_api_call(self, request):
        with self.assertRaises(ValueError):
            pages.delete("owner/repo")
        request.assert_not_called()

    @patch.dict(os.environ, {"DELETE_CONFIRMATION": "DELETE owner/repo"})
    @patch.object(pages, "request")
    def test_delete_disables_only_the_requested_repository(self, request):
        request.side_effect = [{"html_url": "https://owner.github.io/repo/"}, None, None]
        pages.delete("owner/repo")
        self.assertEqual([call.args[:2] for call in request.call_args_list],
                         [("GET", "owner/repo"), ("DELETE", "owner/repo"), ("GET", "owner/repo")])

    @patch.object(pages, "request")
    def test_configure_create_and_custom_domain(self, request):
        request.side_effect = [None, None, None, {
            "cname": "example.com", "build_type": "workflow", "html_url": "http://example.com/",
        }]
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "output"
            with patch.dict(os.environ, {"GITHUB_OUTPUT": str(output)}):
                self.assertEqual(pages.configure("owner/repo", "example.com"), "https://example.com")
            self.assertEqual(output.read_text(), "site_url=https://example.com\n")
        self.assertEqual(request.call_args_list[1].args, ("POST", "owner/repo", {"build_type": "workflow"}))
        self.assertEqual(request.call_args_list[2].args[2], {"build_type": "workflow", "cname": "example.com"})

    @patch.object(pages, "request")
    def test_remove_custom_domain_and_use_project_url(self, request):
        request.side_effect = [{"cname": "old.test"}, None, {
            "cname": None, "build_type": "workflow", "html_url": "https://owner.github.io/repo/",
        }]
        with patch.dict(os.environ, {"GITHUB_OUTPUT": ""}):
            self.assertEqual(pages.configure("owner/repo", None), "https://owner.github.io/repo")
        self.assertIsNone(request.call_args_list[1].args[2]["cname"])

    @patch.object(pages, "request")
    def test_default_user_site_uses_root_url(self, request):
        request.side_effect = [{}, None, {
            "cname": None, "build_type": "workflow", "html_url": "http://owner.github.io/",
        }]
        with patch.dict(os.environ, {"GITHUB_OUTPUT": ""}):
            self.assertEqual(pages.configure("owner/owner.github.io", None), "https://owner.github.io")

    @patch.object(pages, "request")
    def test_inherited_custom_domain_cannot_silently_replace_github_io(self, request):
        request.side_effect = [{}, None, {
            "cname": None, "build_type": "workflow", "html_url": "https://company.example/repo/",
        }]
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "output"
            with patch.dict(os.environ, {"GITHUB_OUTPUT": str(output)}):
                with self.assertRaisesRegex(RuntimeError, "inherited custom domain"):
                    pages.configure("owner/repo", None)
            self.assertFalse(output.exists())

    @patch.dict(os.environ, {"GITHUB_REPOSITORY": "owner/repo", "CUSTOM_DOMAIN": "ignored.example"})
    @patch.object(pages, "configure")
    def test_default_mode_ignores_custom_domain_environment(self, configure):
        with patch.object(pages.sys, "argv", ["github_pages", "configure-pages"]):
            self.assertEqual(pages.main(), 0)
        configure.assert_called_once_with("owner/repo", None)

    @patch.dict(os.environ, {"GITHUB_REPOSITORY": "owner/repo", "CUSTOM_DOMAIN": "WWW.Example.com"})
    @patch.object(pages, "configure")
    def test_custom_mode_uses_validated_domain(self, configure):
        with patch.object(pages.sys, "argv", ["github_pages", "configure-custom"]):
            self.assertEqual(pages.main(), 0)
        configure.assert_called_once_with("owner/repo", "www.example.com")

    @patch.dict(os.environ, {"GITHUB_REPOSITORY": "owner/repo"})
    @patch.object(pages, "request")
    def test_custom_mode_rejects_empty_or_invalid_domain_before_api_calls(self, request):
        for value in ["", "   ", "https://example.com", "example.com/path"]:
            with self.subTest(value=value), patch.dict(os.environ, {"CUSTOM_DOMAIN": value}):
                with patch.object(pages.sys, "argv", ["github_pages", "configure-custom"]):
                    with contextlib.redirect_stderr(io.StringIO()) as stderr:
                        self.assertEqual(pages.main(), 1)
                    self.assertIn("Pages operation failed:", stderr.getvalue())
        request.assert_not_called()

    @patch.dict(os.environ, {"GITHUB_REPOSITORY": "owner/repo", "CUSTOM_DOMAIN": ""})
    @patch.object(pages, "delete")
    def test_delete_does_not_require_a_custom_domain(self, delete):
        with patch.object(pages.sys, "argv", ["github_pages", "delete"]):
            self.assertEqual(pages.main(), 0)
        delete.assert_called_once_with("owner/repo")

    @patch.dict(os.environ, {"PAGES_ADMIN_TOKEN": "test-token"})
    @patch.object(pages, "urlopen")
    def test_api_errors_are_not_silently_ignored(self, urlopen):
        urlopen.side_effect = HTTPError("https://api.github.com", 403, "Forbidden", {}, None)
        with self.assertRaisesRegex(RuntimeError, "HTTP 403"):
            pages.request("GET", "owner/repo", allow_missing=True)
        urlopen.side_effect = HTTPError("https://api.github.com", 404, "Missing", {}, None)
        self.assertIsNone(pages.request("GET", "owner/repo", allow_missing=True))
        with self.assertRaises(RuntimeError):
            pages.request("DELETE", "owner/repo")


class MemoryRemote:
    def __init__(self):
        self.files = {}
        self.directories = {"/"}
        self.other = set()
        self.fail_on = None

    def list(self, path):
        if path not in self.directories:
            raise FileNotFoundError(path)
        prefix = path.rstrip("/") + "/"
        result = {}
        for paths, kind in [(self.directories, "dir"), (self.files, "file"), (self.other, "other")]:
            for entry in paths:
                if entry.startswith(prefix) and "/" not in entry[len(prefix):] and entry != path:
                    result[entry[len(prefix):]] = kind
        return result

    def mkdir(self, path):
        if str(Path(path).parent) not in self.directories:
            raise FileNotFoundError(path)
        self.directories.add(path)

    def read(self, path):
        return self.files[path]

    def write(self, path, content):
        if path == self.fail_on:
            raise OSError("Simulated interrupted upload")
        self.files[path] = content

    def remove(self, path):
        del self.files[path]

    def rmdir(self, path):
        if self.list(path):
            raise OSError("Directory not empty")
        self.directories.remove(path)


class StratoTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.source = Path(self.temporary.name)
        (self.source / "index.html").write_text("Home")
        (self.source / "assets").mkdir()
        (self.source / "assets/test.svg").write_text("<svg/>")
        self.remote = MemoryRemote()
        self.owner = strato.owner_id("owner/repo", "https://example.com")
        self.root = "/abc-static"
        self.quiet = contextlib.redirect_stdout(io.StringIO())
        self.quiet.__enter__()
        self.addCleanup(self.quiet.__exit__, None, None, None)

    def deploy(self):
        strato.deploy(self.remote, self.root, self.source, self.owner)

    def test_paths_refuse_roots_traversal_and_command_injection(self):
        for value in ["/", "", ".", "/.", "/../x", "/x/../y", "//x", "/x/", "/x\nDELE index.html"]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                strato.remote_directory(value)
        self.assertEqual(strato.remote_directory("/sites/abc-static"), "/sites/abc-static")
        for value in ["../other", "/other", "x/../../other", "x\\y", "x//y", ".abc-deployment.json", "x\r\nDELE other"]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                strato.relative_path(value)

    def test_round_trip_updates_stale_files_and_preserves_unmanaged_files(self):
        self.remote.directories.add("/wordpress")
        self.remote.files["/wordpress/index.php"] = b"unrelated site"
        self.deploy()
        self.remote.files[self.root + "/keep.txt"] = b"unmanaged"
        self.remote.files[self.root + "/assets/keep.svg"] = b"unmanaged"
        (self.source / "assets/test.svg").unlink()
        (self.source / "index.html").write_text("Updated")
        self.deploy()
        self.assertNotIn(self.root + "/assets/test.svg", self.remote.files)
        self.assertEqual(self.remote.files[self.root + "/index.html"], b"Updated")
        strato.delete(self.remote, self.root, self.owner)
        self.assertEqual(self.remote.files, {
            "/wordpress/index.php": b"unrelated site", self.root + "/keep.txt": b"unmanaged",
            self.root + "/assets/keep.svg": b"unmanaged",
        })
        self.assertIn(self.root, self.remote.directories)

    def test_wrong_owner_and_nonempty_unowned_directory_are_refused(self):
        self.remote.directories.add(self.root)
        self.remote.files[self.root + "/index.php"] = b"Existing WordPress"
        with self.assertRaisesRegex(ValueError, "nonempty"):
            self.deploy()
        self.assertEqual(len(self.remote.files), 1)
        self.remote.files.clear()
        self.deploy()
        with self.assertRaisesRegex(ValueError, "ownership"):
            strato.delete(self.remote, self.root, strato.owner_id("other/repo", "https://example.com"))
        with self.assertRaisesRegex(ValueError, "ownership"):
            strato.delete(self.remote, self.root, strato.owner_id("owner/repo", "https://other.example.com"))

    def test_unmanaged_path_collision_is_refused_before_changes(self):
        self.deploy()
        (self.source / "new.html").write_text("New page")
        self.remote.files[self.root + "/new.html"] = b"Unmanaged"
        before = self.remote.files.copy()
        with self.assertRaisesRegex(ValueError, "unmanaged"):
            self.deploy()
        self.assertEqual(self.remote.files, before)

    def test_symlinks_in_target_or_parent_are_refused(self):
        self.remote.other.add(self.root)
        with self.assertRaisesRegex(ValueError, "symlinks"):
            self.deploy()
        self.remote.other.clear()
        self.deploy()
        self.remote.other.add(self.root + "/linked")
        with self.assertRaisesRegex(ValueError, "symlink"):
            strato.delete(self.remote, self.root, self.owner)

    def test_malicious_manifest_is_refused_without_deleting_anything(self):
        self.deploy()
        marker = self.root + "/" + strato.MARKER
        for files in [["../../wordpress/index.php"], ["/index.php"], ["x\\y"], ["a", "a"], [123]]:
            self.remote.files[marker] = json.dumps({"schema": 1, "owner": self.owner, "files": files}).encode()
            before = self.remote.files.copy()
            with self.subTest(files=files), self.assertRaises(ValueError):
                strato.delete(self.remote, self.root, self.owner)
            self.assertEqual(self.remote.files, before)

    def test_interrupted_upload_can_be_deleted_or_retried(self):
        self.remote.fail_on = self.root + "/index.html"
        with self.assertRaises(OSError):
            self.deploy()
        self.assertIn(self.root + "/" + strato.MARKER, self.remote.files)
        self.remote.fail_on = None
        self.deploy()
        strato.delete(self.remote, self.root, self.owner)
        self.assertEqual(self.remote.files, {})
        self.assertEqual(self.remote.directories, {"/", self.root})

    def test_delete_handles_planned_but_never_created_directories(self):
        self.remote.directories.add(self.root)
        strato.write_manifest(self.remote, self.root, self.owner, {"never/created/index.html"})
        strato.delete(self.remote, self.root, self.owner)
        self.assertEqual(self.remote.files, {})

    def test_delete_confirmation_is_checked_before_connecting(self):
        with patch.dict(os.environ, {"GITHUB_REPOSITORY": "owner/repo", "DELETE_CONFIRMATION": ""}), \
                patch.object(strato, "connection") as connect, patch("sys.argv", ["deploy_strato", "delete"]), \
                contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(strato.main(), 1)
        connect.assert_not_called()

    def test_ftp_tls_checks_certificates_and_encrypts_data_channel(self):
        env = {"STRATO_PROTOCOL": "ftps", "STRATO_HOST": "server.test", "STRATO_USERNAME": "user",
               "STRATO_PASSWORD": "password", "STRATO_PORT": ""}
        with patch.dict(os.environ, env), patch.object(strato.ftplib, "FTP_TLS") as client:
            with strato.connection() as remote:
                self.assertIsInstance(remote, strato.FTPS)
            context = client.call_args.kwargs["context"]
            self.assertEqual(context.verify_mode, ssl.CERT_REQUIRED)
            self.assertTrue(context.check_hostname)
            client.return_value.__enter__.return_value.prot_p.assert_called_once()

    def test_sftp_requires_pinned_host_key_without_key_auto_discovery(self):
        module = SimpleNamespace(SSHClient=MagicMock(), RejectPolicy=MagicMock())
        env = {"STRATO_PROTOCOL": "sftp", "STRATO_HOST": "server.test", "STRATO_USERNAME": "user",
               "STRATO_PASSWORD": "password", "STRATO_PORT": "", "STRATO_KNOWN_HOSTS": "server.test ssh-ed25519 TEST"}
        with patch.dict(os.environ, env), patch.dict("sys.modules", {"paramiko": module}):
            with strato.connection():
                ssh = module.SSHClient.return_value.__enter__.return_value
                known = Path(ssh.load_host_keys.call_args.args[0])
                self.assertEqual(known.read_text(), env["STRATO_KNOWN_HOSTS"])
                self.assertEqual(known.stat().st_mode & 0o777, 0o600)
            self.assertFalse(known.exists())
            ssh.set_missing_host_key_policy.assert_called_once()
            self.assertFalse(ssh.connect.call_args.kwargs["look_for_keys"])
            self.assertFalse(ssh.connect.call_args.kwargs["allow_agent"])
        with patch.dict(os.environ, {**env, "STRATO_KNOWN_HOSTS": ""}), patch.dict("sys.modules", {"paramiko": module}):
            with self.assertRaisesRegex(ValueError, "STRATO_KNOWN_HOSTS"), strato.connection():
                pass

    def test_plain_ftp_and_missing_connection_secrets_fail(self):
        with patch.dict(os.environ, {"STRATO_PROTOCOL": "ftp"}):
            with self.assertRaisesRegex(ValueError, "Unencrypted"), strato.connection():
                pass
        with patch.dict(os.environ, {"STRATO_PROTOCOL": "sftp", "STRATO_HOST": ""}):
            with self.assertRaisesRegex(ValueError, "STRATO_HOST"), strato.connection():
                pass

    def test_apache_custom_404_and_private_manifest(self):
        config = strato.apache_config("https://example.com/subpath")
        self.assertIn("ErrorDocument 404 /subpath/404.html", config)
        self.assertIn('Files ".abc-deployment.json"', config)
        self.assertIn("Require all denied", config)


if __name__ == "__main__":
    unittest.main()
