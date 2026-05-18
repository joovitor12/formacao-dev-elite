"""Checagens automáticas que complementam o checklist manual."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
CHECKLIST = BASE / "checklist_refatoracao.md"


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
        print("pytest FALHOU:")
        print(proc.stdout)
        print(proc.stderr)
    return proc.returncode == 0


def main() -> int:
    if not CHECKLIST.exists():
        print("Arquivo checklist_refatoracao.md nao encontrado.")
        return 1

    marcados, pendentes = _contar_checklist()
    total = marcados + pendentes
    testes_ok = _pytest_ok()

    print("=== Verificacao do checklist ===\n")
    print(f"Testes (pytest -q): {'OK' if testes_ok else 'FALHOU'}")
    print(f"Checklist manual: {marcados}/{total} itens marcados ({pendentes} pendentes)")

    if pendentes > 0:
        print("\nItens ainda pendentes no checklist_refatoracao.md — revise antes de entregar.")

    if not testes_ok:
        return 2
    if pendentes > 0:
        return 1
    print("\nTudo pronto: testes verdes e checklist completo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
