"""Portão final do exercício integrador — entrega profissional com IA."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
DOSSIE = BASE / "dossie_entrega_integrada.md"
CI = BASE / "ci" / "qualidade-codigo.yml"
MODULOS = [
    "notificacao_entrega.py",
    "confirmacao_entrega.py",
    "fechamento_entrega.py",
]


def _run(cmd: list[str]) -> int:
    return subprocess.run(cmd, cwd=BASE).returncode


def _dossie_preenchido() -> bool:
    if not DOSSIE.exists():
        print("dossie_entrega_integrada.md ausente")
        return False

    texto = DOSSIE.read_text(encoding="utf-8")
    if "(preencha" in texto:
        print("Dossiê incompleto — substitua os campos (preencha) nas seções 1–4.")
        return False

    obrigatorios = [
        r"^- Veredito padrão:\s*\S",
        r"^- Veredito lint:\s*\S",
        r"^- Veredito format:\s*\S",
        r"^- Paridade pipeline local vs CI:\s*\S",
    ]
    faltando = [p for p in obrigatorios if not re.search(p, texto, re.MULTILINE)]
    if faltando:
        print("Dossiê incompleto — preencha vereditos das seções 1–4.")
        return False
    return True


def _ci_espelha_portao() -> bool:
    if not CI.exists():
        print("ci/qualidade-codigo.yml ausente")
        return False

    texto = CI.read_text(encoding="utf-8")
    erros: list[str] = []

    if "verificar_pipeline.py" not in texto:
        erros.append("workflow não chama verificar_pipeline.py")
    if "requirements-dev.txt" not in texto:
        erros.append("workflow não instala requirements-dev.txt")

    if erros:
        print("CI incompleto:")
        for e in erros:
            print(f"  - {e}")
        return False
    return True


def main() -> int:
    print("=== Verificação de entrega — Entrega profissional integrador ===\n")
    falhas = 0

    if _run([sys.executable, "verificar_pipeline.py"]) != 0:
        falhas += 1
    else:
        print("[OK] verificar_pipeline.py\n")

    if _run(
        [sys.executable, "-m", "ruff", "check", *MODULOS],
    ) != 0:
        falhas += 1
    else:
        print("[OK] ruff check nos três módulos\n")

    if _run(
        [sys.executable, "-m", "ruff", "format", "--check", *MODULOS],
    ) != 0:
        falhas += 1
    else:
        print("[OK] ruff format --check nos três módulos\n")

    if _run([sys.executable, "example.py"]) != 0:
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

    if not _ci_espelha_portao():
        falhas += 1
    else:
        print("[OK] workflow espelha portão local\n")

    if falhas:
        print(f"Entrega incompleta ({falhas} pendência(s)).")
        return 1

    print("Entrega OK — portões passaram.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
