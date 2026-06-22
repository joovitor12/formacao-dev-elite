"""Executa ruff check na pasta da aula."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> int:
    base = Path(__file__).resolve().parent
    alvos = ["confirmacao_entrega.py"]

    cmd = [sys.executable, "-m", "ruff", "check", *alvos]
    print("=== ruff check ===")
    print(" ".join(cmd))
    resultado = subprocess.run(cmd, cwd=base)
    if resultado.returncode != 0:
        print("\nLint pendente — corrija confirmacao_entrega.py.")
        return resultado.returncode

    print("\nLint OK — confirmacao_entrega.py sem violações ruff.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
