"""Smoke test — MVP com agente integrado; pipeline ainda incompleto."""

from __future__ import annotations

from pathlib import Path

DOCS_BASE = [
    "visao_geral_projeto.md",
    "mapa_disciplinas.md",
    "arquitetura_mvp.md",
    "escopo_mvp.md",
    "padrao_projeto_mvp.md",
    "decisoes_arquitetura.md",
    "proximos_passos.md",
    "prompts.md",
]


def main() -> None:
    base = Path(__file__).resolve().parent

    ausentes = [nome for nome in DOCS_BASE if not (base / nome).is_file()]
    if ausentes:
        raise SystemExit(f"Documentos ausentes: {', '.join(ausentes)}")

    if not (base / ".env.example").is_file():
        raise SystemExit(".env.example ausente")

    server_main = base / "server" / "main.py"
    if not server_main.is_file():
        raise SystemExit("server/main.py ausente")

    conteudo_main = server_main.read_text(encoding="utf-8")
    if "parlant" not in conteudo_main.lower():
        raise SystemExit("server/main.py sem integração Parlant — complete a entrega anterior")

    print("MVP Chatbot — smoke OK (feche pipeline via prompts.md)")


if __name__ == "__main__":
    main()
