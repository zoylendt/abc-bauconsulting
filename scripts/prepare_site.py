#!/usr/bin/env python3
"""Prepare a fresh _site build for file:// browsing or a configurable HTTPS URL."""

import argparse
import html
import json
import os
import posixpath
import re
import shutil
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


def site_url(value):
    if any(char.isspace() for char in value):
        raise ValueError("The site URL must not contain whitespace.")
    parsed = urlsplit(value)
    if (parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password
            or parsed.query or parsed.fragment or parsed.port not in (None, 443)):
        raise ValueError("The site URL must be an HTTPS URL without credentials, query, fragment or custom port.")
    if any(not re.fullmatch(r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?", label)
           for label in parsed.hostname.split(".")):
        raise ValueError("The site URL must contain a valid hostname; use punycode for international domains.")
    if not re.fullmatch(r"/(?:[A-Za-z0-9._~-]+/)*[A-Za-z0-9._~-]*", parsed.path or "/"):
        raise ValueError("The site URL path must contain simple slash-separated URL segments.")
    if any(part in (".", "..") for part in parsed.path.split("/")):
        raise ValueError("The site URL must not contain dot segments.")
    return urlunsplit(("https", parsed.hostname.lower(), parsed.path.rstrip("/"), "", ""))


def mapped_url(value, current_file, mode, base_url=""):
    parsed = urlsplit(value)
    if parsed.scheme or parsed.netloc or not parsed.path.startswith("/"):
        return value
    decoded = unquote(parsed.path)
    if any(part in (".", "..") for part in decoded.split("/")):
        raise ValueError(f"Unsafe internal URL: {value}")
    if mode == "web":
        path = urlsplit(base_url).path + parsed.path
    else:
        target = decoded.lstrip("/")
        if decoded.endswith("/"):
            target += "index.html"
        path = quote(posixpath.relpath(target, posixpath.dirname(current_file) or "."), safe="/-._~")
    return urlunsplit(("", "", path, parsed.query, parsed.fragment))


class RewriteHTML(HTMLParser):
    def __init__(self, current_file, mode, base_url=""):
        super().__init__(convert_charrefs=False)
        self.current_file = current_file
        self.mode = mode
        self.base_url = base_url
        self.parts = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        rewritten = []
        for key, value in attrs:
            if value is not None and key in ("href", "src", "action", "poster"):
                if tag == "link" and values.get("rel") == "canonical":
                    if self.mode == "web":
                        route = "/" + self.current_file.removesuffix("index.html")
                        value = self.base_url + route
                else:
                    value = mapped_url(value, self.current_file, self.mode, self.base_url)
            rewritten.append(key if value is None else f'{key}="{html.escape(value, quote=True)}"')
        self.parts.append("<" + tag + (" " if rewritten else "") + " ".join(rewritten) + ">")

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.parts[-1] = self.parts[-1][:-1] + " />"

    def handle_endtag(self, tag):
        self.parts.append(f"</{tag}>")

    def handle_data(self, data):
        self.parts.append(data)

    def handle_entityref(self, name):
        self.parts.append(f"&{name};")

    def handle_charref(self, name):
        self.parts.append(f"&#{name};")

    def handle_comment(self, data):
        self.parts.append(f"<!--{data}-->")

    def handle_decl(self, decl):
        self.parts.append(f"<!{decl}>")


class SearchText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.title = []
        self.text = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID_TAGS:
            self.stack.append((tag, dict(attrs)))

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                del self.stack[index:]
                break

    def handle_data(self, data):
        if any(attrs.get("id") == "page-title" for _, attrs in self.stack):
            self.title.append(data)
        if (any("data-pagefind-body" in attrs for _, attrs in self.stack)
                and not any("data-pagefind-ignore" in attrs or tag in ("script", "style")
                            for tag, attrs in self.stack)):
            self.text.append(data)


def prepare(source, destination, mode, base_url=""):
    source, destination = source.resolve(), destination.resolve()
    if not (source / "index.html").is_file():
        raise ValueError("No built site found. Run npm run build first.")
    if source == destination or source in destination.parents or destination in source.parents or destination == Path(destination.anchor):
        raise ValueError("Input and output must be separate, non-root directories.")
    if mode == "web":
        base_url = site_url(base_url)
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True)
    records = []
    for file in sorted(source.rglob("*")):
        if file.is_symlink():
            raise ValueError("Build artifacts must not contain symlinks.")
        if not file.is_file():
            continue
        relative = file.relative_to(source)
        if mode == "local" and relative.parts[0] == "pagefind":
            continue
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if file.suffix != ".html":
            shutil.copyfile(file, target)
            continue
        content = file.read_text(encoding="utf-8")
        if mode == "local":
            text = SearchText()
            text.feed(content)
            body = " ".join(" ".join(text.text).split())
            if body:
                records.append({
                    "title": " ".join(" ".join(text.title).split()),
                    "text": body,
                    "url": quote(posixpath.relpath(relative.as_posix(), "suche"), safe="/-._~"),
                })
            content = re.sub(r'<link\b[^>]*href="/pagefind/pagefind-ui\.css"[^>]*>', "", content)
            content = re.sub(r'<script\b[^>]*src="/pagefind/pagefind-ui\.js"[^>]*></script>', "", content)
            content = content.replace(
                '<script defer src="/assets/js/search.js"></script>',
                '<script defer src="/assets/js/search-index.js"></script>'
                '<script defer src="/assets/js/search-local.js"></script>',
            )
        parser = RewriteHTML(relative.as_posix(), mode, base_url)
        parser.feed(content)
        parser.close()
        target.write_text("".join(parser.parts), encoding="utf-8")
    if mode == "local":
        (destination / "assets/js").mkdir(parents=True, exist_ok=True)
        (destination / "assets/js/search-index.js").write_text(
            "window.ABC_LOCAL_SEARCH = " + json.dumps(records, ensure_ascii=True) + ";\n", encoding="utf-8")
        (destination / "OPEN-ME.txt").write_text(
            "Extract the complete archive, then open index.html in your browser.\n"
            "No server, Node.js or Python is required. Keep all folders together.\n"
            "Search uses a local text index; external links still require Internet access.\n", encoding="utf-8")
    else:
        namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        sitemap = ET.parse(destination / "sitemap.xml")
        for loc in sitemap.findall("s:url/s:loc", namespace):
            loc.text = base_url + urlsplit(loc.text).path
        ET.register_namespace("", namespace["s"])
        sitemap.write(destination / "sitemap.xml", encoding="utf-8", xml_declaration=True)
        robots = destination / "robots.txt"
        robots.write_text(re.sub(r"^Sitemap:.*$", f"Sitemap: {base_url}/sitemap.xml",
                                 robots.read_text(encoding="utf-8"), flags=re.M), encoding="utf-8")
        (destination / ".nojekyll").write_text("")
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["local", "web"])
    parser.add_argument("--site-url", default=os.environ.get("SITE_URL", ""))
    args = parser.parse_args()
    try:
        result = prepare(ROOT / "_site", ROOT / "dist" / f"{args.mode}-site", args.mode, args.site_url)
        print(f"Prepared {args.mode} site in {result.relative_to(ROOT)}")
    except (OSError, ValueError) as error:
        print(f"Site preparation failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
