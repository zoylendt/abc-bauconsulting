#!/usr/bin/env python3
"""Build the Eleventy site and serve it using only Python's standard library."""

import argparse
import functools
import hashlib
import shutil
import subprocess
import sys
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "_site"


class PreviewHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def send_error(self, code, message=None, explain=None):
        error_page = OUTPUT / "404.html"
        if code != 404 or not error_page.is_file():
            return super().send_error(code, message, explain)
        body = error_page.read_bytes()
        self.send_response(404)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)


def build():
    npm = shutil.which("npm")
    if not npm:
        raise RuntimeError("Node.js 22 or newer and npm are required. Install Node.js, then run this command again.")
    lock = ROOT / "package-lock.json"
    if not lock.is_file():
        raise RuntimeError("package-lock.json is missing. Restore it before installing dependencies.")
    digest = hashlib.sha256(lock.read_bytes()).hexdigest()
    stamp = ROOT / "node_modules" / ".preview-lock.sha256"
    eleventy = ROOT / "node_modules" / "@11ty" / "eleventy" / "package.json"
    if not eleventy.is_file() or not stamp.is_file() or stamp.read_text().strip() != digest:
        print("Installing locked build dependencies …", flush=True)
        subprocess.run([npm, "ci", "--no-audit", "--no-fund"], cwd=ROOT, check=True)
        stamp.write_text(digest + "\n")
    subprocess.run([npm, "run", "build"], cwd=ROOT, check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8000, help="Local port (default: 8000)")
    parser.add_argument("--host", default="127.0.0.1", help="Bind address (default: loopback only)")
    parser.add_argument("--no-browser", action="store_true", help="Do not open the default browser")
    parser.add_argument("--skip-build", action="store_true", help="Serve an existing _site without building")
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error("--port must be between 1 and 65535")
    try:
        if not args.skip_build:
            build()
        if not (OUTPUT / "index.html").is_file():
            raise RuntimeError("No built site found. Run again without --skip-build.")
        handler = functools.partial(PreviewHandler, directory=str(OUTPUT))
        with ThreadingHTTPServer((args.host, args.port), handler) as server:
            browser_host = "127.0.0.1" if args.host == "0.0.0.0" else args.host
            url = f"http://{browser_host}:{args.port}/"
            print(f"\nPreview: {url}\nPress Ctrl+C to stop.", flush=True)
            if not args.no_browser and not webbrowser.open(url):
                print("Could not open a browser automatically; open the preview URL above.", file=sys.stderr)
            server.serve_forever()
    except KeyboardInterrupt:
        print("\nPreview stopped.")
    except subprocess.CalledProcessError as error:
        print(f"Build failed (exit {error.returncode}). See the command output above.", file=sys.stderr)
        return error.returncode
    except (OSError, RuntimeError) as error:
        print(f"Preview failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
