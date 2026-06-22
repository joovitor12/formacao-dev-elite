"""
Exportador de métricas — app do exercício integrador de containerização.

Baseline com Dockerfile problemático; percorrer revisão → estrutura → IA → multistage → otimização → segurança.
"""

from __future__ import annotations

import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class MetricsHandler(BaseHTTPRequestHandler):
    def log_message(self, format: str, *args: object) -> None:
        return

    def do_GET(self) -> None:
        if self.path == "/health":
            self._respond(200, b"ok")
        elif self.path == "/metrics":
            self._respond(200, b"uptime_seconds 1\nrequests_total 0\n")
        else:
            self._respond(404, b"not found")

    def _respond(self, status: int, body: bytes) -> None:
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(body)


def main(host: str | None = None, port: int | None = None) -> None:
    bind_host = host or os.environ.get("HOST", "0.0.0.0")
    bind_port = int(port or os.environ.get("PORT", "8080"))
    server = HTTPServer((bind_host, bind_port), MetricsHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
