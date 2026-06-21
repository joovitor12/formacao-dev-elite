"""
Exportador mínimo de métricas — app containerizado na aula.

Baseline para revisar Dockerfile e imagem.
"""

from __future__ import annotations

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


def main(host: str = "0.0.0.0", port: int = 8080) -> None:
    server = HTTPServer((host, port), MetricsHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
