"""Tool para consultar visao_geral_projeto.md."""

from pathlib import Path

from parlant.sdk import ToolContext, ToolResult, tool

_CAMINHO_VISAO_GERAL = Path(__file__).resolve().parents[2] / "visao_geral_projeto.md"


@tool
async def consultar_visao_geral_projeto(context: ToolContext) -> ToolResult:
    """Retorna o conteúdo de visao_geral_projeto.md (stack e visão do MVP)."""
    if not _CAMINHO_VISAO_GERAL.is_file():
        return ToolResult(
            data={
                "erro": (
                    f"Arquivo {_CAMINHO_VISAO_GERAL.name} não encontrado em "
                    f"{_CAMINHO_VISAO_GERAL.parent}"
                ),
            },
        )

    return ToolResult(
        data={
            "arquivo": _CAMINHO_VISAO_GERAL.name,
            "conteudo": _CAMINHO_VISAO_GERAL.read_text(encoding="utf-8"),
        },
    )
