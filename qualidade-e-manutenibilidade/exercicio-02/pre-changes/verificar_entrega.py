"""Portão final do exercício integrador — testes assistidos."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
CHECKLIST = BASE / "checklist_testes_integrador.md"


def _run(cmd: list[str]) -> int:
    proc = subprocess.run(cmd, cwd=BASE)
    return proc.returncode


def _contar_checklist() -> tuple[int, int]:
    texto = CHECKLIST.read_text(encoding="utf-8")
    marcados = len(re.findall(r"^- \[x\]", texto, flags=re.MULTILINE | re.IGNORECASE))
    pendentes = len(re.findall(r"^- \[ \]", texto, flags=re.MULTILINE))
    return marcados, pendentes


def main() -> int:
    print("=== Verificacao de entrega — Programa Fidelidade (testes) ===\n")

    etapas = [
        ("pytest -q", [sys.executable, "-m", "pytest", "-q"]),
        ("verificacao da suíte", [sys.executable, "verificar_testes.py"]),
        ("simulador falsos positivos", [sys.executable, "simular_regressao.py"]),
        ("checklist humano", [sys.executable, "verificar_checklist.py"]),
    ]

    falhas = 0
    for nome, cmd in etapas:
        codigo = _run(cmd)
        status = "OK" if codigo == 0 else "FALHOU"
        print(f"[{status}] {nome}\n")
        if codigo != 0:
            falhas += 1

    if falhas:
        print(f"Entrega incompleta ({falhas} pendencia(s)).")
        return 1

    print("Entrega OK — todos os portoes passaram.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
