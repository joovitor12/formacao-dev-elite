"""Smoke test — documentação base da visão geral."""

from __future__ import annotations

from pathlib import Path

DOCS_OBRIGATORIOS = [
    "visao_geral_projeto.md",
    "mapa_disciplinas.md",
    "arquitetura_mvp.md",
    "escopo_mvp.md",
    "padrao_projeto_mvp.md",
]


def main() -> None:
    base = Path(__file__).resolve().parent
    ausentes = [nome for nome in DOCS_OBRIGATORIOS if not (base / nome).is_file()]

    if ausentes:
        raise SystemExit(f"Documentos ausentes: {', '.join(ausentes)}")

    if not (base / ".env.example").is_file():
        raise SystemExit(".env.example ausente")

    print("MVP Chatbot — visão geral: documentação base presente")


if __name__ == "__main__":
    main()
