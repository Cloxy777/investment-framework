#!/usr/bin/env python3
"""Local collector for the matrix.tarasguk.com research harvest.

Binds 127.0.0.1 only, on a random port, and requires a random token in the URL
path. Accepts POSTs from the page JS and writes files ONLY under ../data/.

Endpoints (all under /<token>/):
  POST /<token>/save   JSON body {"path": "cards/NVDA.simple.txt", "content": "...", "append": false}
  POST /<token>/raw/<relpath>   raw body is written to data/<relpath>   (content-type text/plain)
  GET  /<token>/ping   -> "pong"

On start it prints "PORT=<n> TOKEN=<t>" and writes the same to the file given by
argv[1] (outside the repo, e.g. the scratchpad) so the caller can read it.
"""
import json
import os
import re
import secrets
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_ROOT = os.path.realpath(os.path.join(HERE, "..", "data"))
MAX_BYTES = 40 * 1024 * 1024
SAFE_PATH = re.compile(r"^[A-Za-z0-9._\-Ѐ-ӿ/]+$")
TOKEN = secrets.token_urlsafe(12)


def safe_target(rel):
    rel = rel.strip().lstrip("/")
    if not rel or ".." in rel.split("/") or not SAFE_PATH.match(rel):
        raise ValueError("bad path: %r" % rel)
    full = os.path.realpath(os.path.join(DATA_ROOT, rel))
    if os.path.commonpath([full, DATA_ROOT]) != DATA_ROOT:
        raise ValueError("escape: %r" % rel)
    return full


class H(BaseHTTPRequestHandler):
    server_version = "collector/1"

    def log_message(self, fmt, *a):  # quiet
        sys.stderr.write("%s\n" % (fmt % a))

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Private-Network", "true")
        self.send_header("Access-Control-Max-Age", "600")

    def _reply(self, code, body="ok"):
        b = body.encode("utf-8")
        self.send_response(code)
        self._cors()
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.send_header("Content-Length", "0")
        self.end_headers()

    def _route(self):
        p = self.path.split("?", 1)[0]
        pre = "/%s/" % TOKEN
        if not p.startswith(pre):
            return None
        return p[len(pre):]

    def do_GET(self):
        r = self._route()
        if r is None:
            return self._reply(403, "forbidden")
        if r == "ping":
            return self._reply(200, "pong")
        if r.startswith("js/"):   # read-only: serve harvest scripts from analysis/js/
            name = r[3:]
            if not re.match(r"^[A-Za-z0-9_.\-]+\.js$", name):
                return self._reply(400, "bad name")
            full = os.path.join(HERE, "js", name)
            if not os.path.isfile(full):
                return self._reply(404, "nope")
            return self._reply(200, open(full, encoding="utf-8").read())
        return self._reply(404, "nope")

    def do_POST(self):
        r = self._route()
        if r is None:
            return self._reply(403, "forbidden")
        n = int(self.headers.get("Content-Length") or 0)
        if n > MAX_BYTES:
            return self._reply(413, "too big")
        body = self.rfile.read(n)
        try:
            if r == "save":
                j = json.loads(body.decode("utf-8"))
                target = safe_target(j["path"])
                os.makedirs(os.path.dirname(target), exist_ok=True)
                mode = "a" if j.get("append") else "w"
                with open(target, mode, encoding="utf-8", newline="\n") as f:
                    f.write(j["content"])
                return self._reply(200, "saved %s %d" % (j["path"], len(j["content"])))
            if r.startswith("raw/"):
                target = safe_target(r[4:])
                os.makedirs(os.path.dirname(target), exist_ok=True)
                with open(target, "wb") as f:
                    f.write(body)
                return self._reply(200, "saved %s %d" % (r[4:], len(body)))
            return self._reply(404, "nope")
        except Exception as e:  # noqa: BLE001
            return self._reply(400, "error: %s" % e)


def main():
    srv = ThreadingHTTPServer(("127.0.0.1", 0), H)
    port = srv.server_address[1]
    line = "PORT=%d TOKEN=%s" % (port, TOKEN)
    print(line, flush=True)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(line + "\n")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
