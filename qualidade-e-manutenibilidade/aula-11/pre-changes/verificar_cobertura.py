"""Relatório de cobertura para orientar geração de testes com IA."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
MODULO = "regras_assinatura"


def main() -> int:
    cmd = [
        sys.executable,
        "-m",
        "pytest",
        "-q",
        f"--cov={MODULO}",
        "--cov-report=term-missing:skip-covered",
        "--cov-config=.coveragerc",
    ]
    print("=== Cobertura de testes ===\n")
    print("Comando:", " ".join(cmd), "\n")
    return subprocess.call(cmd, cwd=BASE)


if __name__ == "__main__":
    sys.exit(main())
