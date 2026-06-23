"""Portão final — após criar server/ e preencher ADRs via IA."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
DECISOES = BASE / "decisoes_arquitetura.md"

MODULOS_SERVER = [
    "server/__init__.py",
    "server/config.py",
    "server/main.py",
    "server/agent.py",
    "server/guidelines.py",
    "server/tools/__init__.py",
]


def _adrs_preenchidas() -> bool:
    if not DECISOES.exists():
        print("decisoes_arquitetura.md ausente")
        return False

    texto = DECISOES.read_text(encoding="utf-8")
    if "(preencha" in texto.lower():
        print("ADRs ainda com placeholders (preencha) — complete decisoes_arquitetura.md")
        return False

    adrs = len(re.findall(r"^## ADR-\d+", texto, re.MULTILINE))
    if adrs < 7:
        print(f"Esperado 7 ADRs; encontrado {adrs}")
        return False

    return True


def main() -> int:
    print("=== Verificação de arquitetura (pós-implementação em sala) ===\n")
    falhas = 0

    if subprocess.run([sys.executable, "example.py"], cwd=BASE).returncode != 0:
        falhas += 1
    else:
        print("[OK] example.py\n")

    faltando = [c for c in MODULOS_SERVER if not (BASE / c).is_file()]
    if faltando:
        print("[FALHOU] Pacote server/ incompleto:")
        for c in faltando:
            print(f"  - {c}")
        falhas += 1
    else:
        print("[OK] server/ com módulos esperados\n")

    if not (BASE / "pyproject.toml").is_file():
        print("[FALHOU] pyproject.toml ausente — crie via prompt §3")
        falhas += 1
    else:
        print("[OK] pyproject.toml\n")

    if not _adrs_preenchidas():
        falhas += 1
    else:
        print("[OK] decisoes_arquitetura.md\n")

    if falhas:
        print(f"Arquitetura pendente ({falhas} item(ns)).")
        return 1

    print("Arquitetura OK — ADRs fechadas e server/ criado.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
