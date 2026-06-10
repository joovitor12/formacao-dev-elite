"""Verifica checklist do dossiê integrado."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DOSSIE = Path(__file__).resolve().parent / "dossie_review_integrado.md"


def main() -> int:
    if not DOSSIE.exists():
        print(f"Arquivo ausente: {DOSSIE}")
        return 1

    texto = DOSSIE.read_text(encoding="utf-8")
    marcados = len(re.findall(r"^- \[x\]", texto, flags=re.MULTILINE | re.IGNORECASE))
    pendentes = len(re.findall(r"^- \[ \]", texto, flags=re.MULTILINE))

    print(f"Checklist: {marcados} marcado(s), {pendentes} pendente(s)")
    if pendentes:
        print("Marque todos os itens em dossie_review_integrado.md")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
