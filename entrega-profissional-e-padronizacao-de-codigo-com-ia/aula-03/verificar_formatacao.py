"""Executa ruff format --check na pasta da aula."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> int:
    base = Path(__file__).resolve().parent
    alvos = ["fechamento_entrega.py"]

    cmd = [sys.executable, "-m", "ruff", "format", "--check", *alvos]
    print("=== ruff format --check ===")
    print(" ".join(cmd))
    resultado = subprocess.run(cmd, cwd=base)
    if resultado.returncode != 0:
        print("\nFormatação pendente — rode ruff format ou revise o diff.")
        return resultado.returncode

    print("\nFormat OK — fechamento_entrega.py conforme pyproject.toml.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
