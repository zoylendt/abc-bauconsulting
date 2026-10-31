#!/usr/bin/env python3
"""Configure or disable this repository's GitHub Pages site using the REST API."""

import argparse
import json
import os
import re
import sys
from urllib.error import HTTPError
from urllib.parse import urlsplit, urlunsplit
from urllib.request import Request, urlopen

from .prepare_site import site_url


def repository():
    value = os.environ.get("GITHUB_REPOSITORY", "")
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", value):
        raise ValueError("GITHUB_REPOSITORY must identify the target owner/repository.")
    return value


def confirmation(repo):
    if os.environ.get("DELETE_CONFIRMATION", "") != f"DELETE {repo}":
        raise ValueError("Deletion requires the exact confirmation: DELETE owner/repository")


def custom_domain(value):
    value = value.strip().lower()
    if not value:
        return None
    labels = value.split(".")
    if (len(labels) < 2 or len(value) > 253
            or any(not re.fullmatch(r"[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?", label) for label in labels)):
        raise ValueError("Custom domain must be a hostname only, without scheme, path or port; use punycode for international domains.")
    return value


def request(method, repo, body=None, allow_missing=False):
    token = os.environ.get("PAGES_ADMIN_TOKEN", "")
    if not token:
        raise ValueError("Set the PAGES_ADMIN_TOKEN secret to a repository-scoped Pages administration token.")
    endpoint = os.environ.get("GITHUB_API_URL", "https://api.github.com").rstrip("/")
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
        "Content-Type": "application/json",
    }
    data = json.dumps(body).encode() if body is not None else None
    try:
        with urlopen(Request(f"{endpoint}/repos/{repo}/pages", data=data, headers=headers, method=method), timeout=30) as response:
            content = response.read()
            return json.loads(content) if content else None
    except HTTPError as error:
        error.close()
        if error.code == 404 and allow_missing:
            return None
        raise RuntimeError(f"GitHub Pages API {method} failed (HTTP {error.code}); check token permissions, repository settings and domain/DNS configuration.") from error


def configure(repo, domain):
    existing = request("GET", repo, allow_missing=True)
    if existing is None:
        request("POST", repo, {"build_type": "workflow"})
    request("PUT", repo, {"build_type": "workflow", "cname": domain})
    configured = request("GET", repo)
    if configured.get("cname") != domain or configured.get("build_type") != "workflow":
        raise RuntimeError("GitHub did not apply the requested Pages configuration.")
    parsed = urlsplit(configured["html_url"])
    public_url = site_url(urlunsplit(("https", parsed.netloc, parsed.path, "", "")))
    expected_host = domain or f"{repo.split('/')[0].lower()}.github.io"
    if urlsplit(public_url).hostname != expected_host:
        raise RuntimeError(
            f"GitHub reports a Pages URL outside the requested hostname {expected_host}. "
            "For github.io deployment, remove any inherited custom domain from the owner's "
            "user/organization Pages site, or use a different account."
        )
    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with open(output, "a", encoding="utf-8") as file:
            file.write(f"site_url={public_url}\n")
    print("GitHub Pages configured; DNS and HTTPS certificate readiness must be checked in Settings > Pages.")
    return public_url


def delete(repo):
    confirmation(repo)
    request("GET", repo)
    request("DELETE", repo)
    if request("GET", repo, allow_missing=True) is not None:
        raise RuntimeError("GitHub still reports an enabled Pages site after deletion.")
    print("GitHub Pages disabled. Remove or update custom-domain DNS records separately to avoid dangling DNS.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=["configure-pages", "configure-custom", "delete"])
    args = parser.parse_args()
    try:
        repo = repository()
        if args.operation == "delete":
            delete(repo)
        else:
            domain = None
            if args.operation == "configure-custom":
                domain = custom_domain(os.environ.get("CUSTOM_DOMAIN", ""))
                if domain is None:
                    raise ValueError("Custom-domain deployment requires a custom_domain input or PAGES_CUSTOM_DOMAIN variable.")
            configure(repo, domain)
    except (OSError, ValueError, RuntimeError) as error:
        print(f"Pages operation failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
