"""Portão final do exercício integrador — review com IA + Git."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
DOSSIE = BASE / "dossie_review_integrado.md"


def _run(cmd: list[str]) -> int:
    return subprocess.run(cmd, cwd=BASE).returncode


def _dossie_preenchido() -> bool:
    if not DOSSIE.exists():
        print("dossie_review_integrado.md ausente")
        return False

    texto = DOSSIE.read_text(encoding="utf-8")
    obrigatorios = [
        r"^- Link:\s*https?://\S+",
        r"^- Veredito humano:\s*\S",
        r"^- Veredito de governança:\s*\S",
    ]
    faltando = [p for p in obrigatorios if not re.search(p, texto, re.MULTILINE)]
    if faltando:
        print("Dossiê incompleto — preencha link do PR, vereditos e tabelas.")
        return False
    return True


def main() -> int:
    print("=== Verificação de entrega — Pipeline review integrador ===\n")
    falhas = 0

    if _run([sys.executable, "example.py"]) != 0:
        print("[FALHOU] example.py\n")
        falhas += 1
    else:
        print("[OK] example.py\n")

    if _run([sys.executable, "verificar_checklist.py"]) != 0:
        falhas += 1
    else:
        print("[OK] checklist do dossiê\n")

    if not _dossie_preenchido():
        falhas += 1
    else:
        print("[OK] dossiê com campos mínimos\n")

    if falhas:
        print(f"Entrega incompleta ({falhas} pendência(s)).")
        return 1

    print("Entrega OK — portões passaram.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
