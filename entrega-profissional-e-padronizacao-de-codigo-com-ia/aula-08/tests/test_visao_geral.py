"""Testes de contrato para server.tools.visao_geral — sem LLM nem OpenRouter."""

from pathlib import Path

import pytest
from parlant.core.tools import ToolResult
from parlant.sdk import ToolContext

from server.tools import consultar_visao_geral_projeto
from server.tools import visao_geral as modulo_visao_geral

_NOME_ARQUIVO = "visao_geral_projeto.md"


@pytest.mark.asyncio
async def test_consultar_visao_geral_projeto_retorna_contrato_sucesso(
    contexto_tool: ToolContext,
) -> None:
    resultado = await consultar_visao_geral_projeto.function(contexto_tool)

    assert isinstance(resultado, ToolResult)
    assert set(resultado.data.keys()) == {"arquivo", "conteudo"}
    assert resultado.data["arquivo"] == _NOME_ARQUIVO
    assert isinstance(resultado.data["conteudo"], str)
    assert resultado.data["conteudo"]
    assert "# Visão geral" in resultado.data["conteudo"]
    assert resultado.data["conteudo"] == modulo_visao_geral._CAMINHO_VISAO_GERAL.read_text(
        encoding="utf-8",
    )


@pytest.mark.asyncio
async def test_consultar_visao_geral_projeto_arquivo_ausente_retorna_erro(
    contexto_tool: ToolContext,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    caminho_inexistente = tmp_path / _NOME_ARQUIVO
    monkeypatch.setattr(modulo_visao_geral, "_CAMINHO_VISAO_GERAL", caminho_inexistente)

    resultado = await consultar_visao_geral_projeto.function(contexto_tool)

    assert isinstance(resultado, ToolResult)
    assert set(resultado.data.keys()) == {"erro"}
    mensagem = resultado.data["erro"]
    assert _NOME_ARQUIVO in mensagem
    assert "não encontrado" in mensagem
    assert str(tmp_path) in mensagem


def test_consultar_visao_geral_projeto_exportada_no_pacote_tools() -> None:
    assert consultar_visao_geral_projeto.tool.name == "consultar_visao_geral_projeto"
