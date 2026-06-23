"""Smoke test — baseline (herda arquitetura; Parlant ainda não integrado)."""

from __future__ import annotations

from pathlib import Path

DOCS_BASE = [
    "visao_geral_projeto.md",
    "mapa_disciplinas.md",
    "arquitetura_mvp.md",
    "escopo_mvp.md",
    "padrao_projeto_mvp.md",
    "decisoes_arquitetura.md",
    "registro_arquitetura_decisoes.md",
    "prompts.md",
]


def main() -> None:
    base = Path(__file__).resolve().parent

    ausentes = [nome for nome in DOCS_BASE if not (base / nome).is_file()]
    if ausentes:
        raise SystemExit(f"Documentos ausentes: {', '.join(ausentes)}")

    if not (base / ".env.example").is_file():
        raise SystemExit(".env.example ausente")

    if not (base / "server").is_dir():
        raise SystemExit("server/ ausente — complete a entrega de arquitetura antes")

    print("MVP Chatbot — baseline OK (integre Parlant via prompts.md)")


if __name__ == "__main__":
    main()
