"""Smoke test — baseline da aula (herda visão geral; sem server/ ainda)."""

from __future__ import annotations

from pathlib import Path

DOCS_AULA_05 = [
    "visao_geral_projeto.md",
    "mapa_disciplinas.md",
    "arquitetura_mvp.md",
    "escopo_mvp.md",
    "padrao_projeto_mvp.md",
]

DOCS_AULA_06 = [
    "decisoes_arquitetura.md",
    "registro_arquitetura_decisoes.md",
]


def main() -> None:
    base = Path(__file__).resolve().parent

    ausentes = [
        nome
        for nome in [*DOCS_AULA_05, *DOCS_AULA_06]
        if not (base / nome).is_file()
    ]
    if ausentes:
        raise SystemExit(f"Documentos ausentes: {', '.join(ausentes)}")

    if not (base / ".env.example").is_file():
        raise SystemExit(".env.example ausente")

    if (base / "server").exists():
        print("MVP Chatbot — baseline OK (server/ já criado — rode verificar_arquitetura.py)")
        return

    print("MVP Chatbot — baseline OK (herda visão geral; crie server/ via prompts da aula)")


if __name__ == "__main__":
    main()
