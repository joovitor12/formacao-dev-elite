"""Portão final do exercício integrador — containerização com IA."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
DOSSIE = BASE / "dossie_container_integrado.md"
DOCKERFILE = BASE / "Dockerfile"


def _run(cmd: list[str]) -> int:
    return subprocess.run(cmd, cwd=BASE).returncode


def _dossie_preenchido() -> bool:
    if not DOSSIE.exists():
        print("dossie_container_integrado.md ausente")
        return False

    texto = DOSSIE.read_text(encoding="utf-8")
    obrigatorios = [
        r"^- Veredito de revisão:\s*\S",
        r"^- Veredito de segurança:\s*\S",
        r"^- Tamanho antes",
        r"^- Tamanho depois",
    ]
    faltando = [p for p in obrigatorios if not re.search(p, texto, re.MULTILINE)]
    if faltando:
        print("Dossiê incompleto — preencha vereditos e tamanhos antes/depois.")
        return False
    return True


def _dockerfile_endurecido() -> bool:
    if not DOCKERFILE.exists():
        print("Dockerfile ausente")
        return False

    texto = DOCKERFILE.read_text(encoding="utf-8")
    erros: list[str] = []

    if re.search(r"python\s*:\s*latest", texto, re.IGNORECASE):
        erros.append("ainda usa python:latest")
    if "METRICS_API_KEY" in texto:
        erros.append("segredo METRICS_API_KEY ainda no Dockerfile")
    if " AS " not in texto:
        erros.append("multistage ausente (esperado FROM ... AS ...)")
    if not re.search(r"^\s*USER\s+", texto, re.MULTILINE):
        erros.append("USER não-root ausente")
    if not re.search(r"^\s*HEALTHCHECK\b", texto, re.MULTILINE):
        erros.append("HEALTHCHECK ausente")

    if erros:
        print("Dockerfile final incompleto:")
        for e in erros:
            print(f"  - {e}")
        return False
    return True


def main() -> int:
    print("=== Verificação de entrega — Containerização integrador ===\n")
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

    if not _dockerfile_endurecido():
        falhas += 1
    else:
        print("[OK] Dockerfile endurecido\n")

    if falhas:
        print(f"Entrega incompleta ({falhas} pendência(s)).")
        return 1

    print("Entrega OK — portões passaram.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
