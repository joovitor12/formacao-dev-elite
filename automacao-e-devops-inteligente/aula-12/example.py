"""Smoke test local — execute antes do docker build."""

from __future__ import annotations

import threading
import urllib.error
import urllib.request

import metrics_exporter


def _wait_health(port: int, tentativas: int = 20) -> bool:
    url = f"http://127.0.0.1:{port}/health"
    for _ in range(tentativas):
        try:
            with urllib.request.urlopen(url, timeout=0.5) as resp:
                return resp.status == 200 and resp.read() == b"ok"
        except (urllib.error.URLError, TimeoutError):
            pass
    return False


def main() -> None:
    port = 18080
    thread = threading.Thread(
        target=metrics_exporter.main,
        kwargs={"host": "127.0.0.1", "port": port},
        daemon=True,
    )
    thread.start()

    if not _wait_health(port):
        raise SystemExit("health check local falhou")

    with urllib.request.urlopen(f"http://127.0.0.1:{port}/metrics") as resp:
        body = resp.read().decode()
        if "uptime_seconds" not in body:
            raise SystemExit("endpoint /metrics inesperado")

    print("metrics_exporter OK — pronto para revisão de segurança")


if __name__ == "__main__":
    main()
