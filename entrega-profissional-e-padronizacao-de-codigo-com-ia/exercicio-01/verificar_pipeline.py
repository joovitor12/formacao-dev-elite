"""Portão local — espelha o job de CI."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent

MODULOS = [
    "notificacao_entrega.py",
    "confirmacao_entrega.py",
    "fechamento_entrega.py",
]


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
    print("=== Verificação de pipeline ===\n")
    falhas = 0

    if _run(
        "lint",
        [sys.executable, "-m", "ruff", "check", *MODULOS],
    ) != 0:
        falhas += 1

    if _run(
        "format",
        [sys.executable, "-m", "ruff", "format", "--check", *MODULOS],
    ) != 0:
        falhas += 1

    if _run("smoke", [sys.executable, "example.py"]) != 0:
        falhas += 1

    if falhas:
        print(f"Pipeline com falhas ({falhas} portão(ões) vermelho(s)).")
        return 1

    print("Pipeline OK — portões lint, format e smoke verdes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
