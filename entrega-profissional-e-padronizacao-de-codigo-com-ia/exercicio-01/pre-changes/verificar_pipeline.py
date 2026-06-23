"""Portão local — espelha o job de CI (baseline incompleto, proposital)."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent

MODULOS = ["confirmacao_entrega.py"]


def _run(rotulo: str, cmd: list[str]) -> int:
    print(f"=== {rotulo} ===")
    print(" ".join(cmd))
    resultado = subprocess.run(cmd, cwd=BASE)
    if resultado.returncode != 0:
        print(f"\n[FALHOU] {rotulo}\n")
    else:
        print(f"\n[OK] {rotulo}\n")
    return resultado.returncode


def main() -> int:
    print("=== Verificação de pipeline (baseline) ===\n")
    falhas = 0

    if _run("smoke", [sys.executable, "example.py"]) != 0:
        falhas += 1

    if _run(
        "lint",
        [sys.executable, "-m", "ruff", "check", *MODULOS],
    ) != 0:
        falhas += 1

    print("=== format ===")
    print("[SKIP] formatação — pendente integração ao pipeline\n")
    falhas += 1

    if falhas:
        print(f"Pipeline incompleto ou com falhas ({falhas} pendência(s)).")
        return 1

    print("Pipeline OK — portões lint, format e smoke verdes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
