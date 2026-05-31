"""Checagens automáticas parciais do checklist."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
CHECKLIST = BASE / "checklist_testes_integrador.md"


def _contar_checklist() -> tuple[int, int]:
    texto = CHECKLIST.read_text(encoding="utf-8")
    marcados = len(re.findall(r"^- \[x\]", texto, flags=re.MULTILINE | re.IGNORECASE))
    pendentes = len(re.findall(r"^- \[ \]", texto, flags=re.MULTILINE))
    return marcados, pendentes


def _pytest_ok() -> bool:
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", "-q"],
        cwd=BASE,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        print(proc.stderr)
    return proc.returncode == 0


def main() -> int:
    marcados, pendentes = _contar_checklist()
    total = marcados + pendentes
    testes_ok = _pytest_ok()

    print("=== Verificacao do checklist ===\n")
    print(f"Testes: {'OK' if testes_ok else 'FALHOU'}")
    print(f"Checklist: {marcados}/{total} marcados ({pendentes} pendentes)")

    if not testes_ok:
        return 2
    if pendentes > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
