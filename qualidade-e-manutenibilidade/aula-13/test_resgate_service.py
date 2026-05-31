"""
Suíte inicial — só regra pura local.

Orquestração (`executar_resgate`) exige mock das portas — ver guia_mocking_ia.md + IA.
"""

from __future__ import annotations

import pytest
from unittest.mock import patch

import regras_catalogo as catalogo
from resgate_service import executar_resgate


def test_custo_resgate_codigo_valido() -> None:
    assert catalogo.custo_resgate("desc10") == 50


def test_custo_resgate_codigo_invalido_dispara_erro() -> None:
    with pytest.raises(ValueError, match="codigo invalido"):
        catalogo.custo_resgate("inexistente")


@patch("resgate_service.consultar_saldo", return_value=120)
@patch("resgate_service.debitar_pontos", return_value=True)
@patch("resgate_service.enviar_confirmacao")
def test_executar_resgate_sucesso_basico_desc10(
    mock_enviar_confirmacao, mock_debitar_pontos, mock_consultar_saldo
) -> None:
    # Arrange + Act
    resultado = executar_resgate("cliente-1", "DESC10")

    # Assert
    assert resultado["ok"] is True
    assert resultado["saldo_restante"] == 70
    mock_consultar_saldo.assert_called_once_with("cliente-1")
    mock_debitar_pontos.assert_called_once_with("cliente-1", 50)
    mock_enviar_confirmacao.assert_called_once_with("cliente-1", "DESC10", 50)


@patch("resgate_service.consultar_saldo", return_value=200)
@patch("resgate_service.debitar_pontos", return_value=True)
@patch("resgate_service.enviar_confirmacao")
def test_executar_resgate_sucesso_normaliza_entradas(
    mock_enviar_confirmacao, mock_debitar_pontos, mock_consultar_saldo
) -> None:
    # Arrange + Act
    resultado = executar_resgate("  cli-01  ", "  frete  ")

    # Assert
    assert resultado["ok"] is True
    assert resultado["cliente_id"] == "cli-01"
    assert resultado["codigo"] == "FRETE"
    assert resultado["saldo_restante"] == 100
    mock_consultar_saldo.assert_called_once_with("cli-01")
    mock_debitar_pontos.assert_called_once_with("cli-01", 100)
    mock_enviar_confirmacao.assert_called_once_with("cli-01", "FRETE", 100)


@patch("resgate_service.consultar_saldo", return_value=500)
@patch("resgate_service.debitar_pontos", return_value=True)
@patch("resgate_service.enviar_confirmacao")
def test_executar_resgate_sucesso_no_limite_saldo_igual_ao_custo(
    mock_enviar_confirmacao, mock_debitar_pontos, mock_consultar_saldo
) -> None:
    # Arrange + Act
    resultado = executar_resgate("cliente-vip", "VIP")

    # Assert
    assert resultado["ok"] is True
    assert resultado["saldo_restante"] == 0
    mock_consultar_saldo.assert_called_once_with("cliente-vip")
    mock_debitar_pontos.assert_called_once_with("cliente-vip", 500)
    mock_enviar_confirmacao.assert_called_once_with("cliente-vip", "VIP", 500)
