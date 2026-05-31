"""
Suíte inicial mínima — complete com boas práticas de testes assistidos.

Use checklist_testes_assistidos.md + guia_boas_praticas_testes_ia.md + IA.
"""

from __future__ import annotations

from unittest.mock import patch

import pytest

import ativacao_service as service
import regras_tier as tier


def test_creditos_tier_ouro() -> None:
    assert tier.creditos_por_tier("ouro") == 50


def test_normalizar_tier_aceita_trim_e_case_insensitive() -> None:
    assert tier.normalizar_tier("  OuRo  ") == "ouro"


def test_normalizar_tier_vazio_lanca_value_error() -> None:
    with pytest.raises(ValueError, match="tier obrigatorio"):
        tier.normalizar_tier("   ")


@pytest.mark.parametrize(
    ("nome_tier", "creditos_esperados"),
    [("bronze", 10), ("prata", 25)],
)
def test_creditos_por_tier_para_bronze_e_prata(
    nome_tier: str, creditos_esperados: int
) -> None:
    assert tier.creditos_por_tier(nome_tier) == creditos_esperados


def test_creditos_por_tier_invalido_lanca_value_error() -> None:
    with pytest.raises(ValueError, match="tier invalido"):
        tier.creditos_por_tier("diamante")


@patch("ativacao_service.enviar_recibo")
@patch("ativacao_service.creditar_tier", return_value=True)
@patch("ativacao_service.saldo_atual", return_value=100)
def test_ativar_tier_com_saldo_suficiente_retorna_ok_true_e_envia_recibo(
    saldo_atual_mock, creditar_tier_mock, enviar_recibo_mock
) -> None:
    resultado = service.ativar_tier("  cli-123  ", " OuRo ")

    assert resultado["ok"] is True
    assert resultado["cliente_id"] == "cli-123"
    assert resultado["tier"] == "ouro"
    assert resultado["creditos"] == 50
    assert resultado["saldo_restante"] == 50
    saldo_atual_mock.assert_called_once_with("cli-123")
    creditar_tier_mock.assert_called_once_with("cli-123", 50)
    enviar_recibo_mock.assert_called_once_with("cli-123", "ouro", 50)


@patch("ativacao_service.enviar_recibo")
@patch("ativacao_service.creditar_tier")
@patch("ativacao_service.saldo_atual", return_value=40)
def test_ativar_tier_com_saldo_insuficiente_retorna_ok_false_sem_creditar(
    saldo_atual_mock, creditar_tier_mock, enviar_recibo_mock
) -> None:
    resultado = service.ativar_tier("cli-123", "ouro")

    assert resultado["ok"] is False
    assert resultado["erro"] == "saldo insuficiente"
    assert resultado["creditos_necessarios"] == 50
    assert resultado["saldo"] == 40
    saldo_atual_mock.assert_called_once_with("cli-123")
    creditar_tier_mock.assert_not_called()
    enviar_recibo_mock.assert_not_called()


@patch("ativacao_service.enviar_recibo")
@patch("ativacao_service.creditar_tier", return_value=False)
@patch("ativacao_service.saldo_atual", return_value=80)
def test_ativar_tier_quando_creditar_falha_retorna_ok_false_sem_recibo(
    saldo_atual_mock, creditar_tier_mock, enviar_recibo_mock
) -> None:
    resultado = service.ativar_tier("cli-123", "prata")

    assert resultado["ok"] is False
    assert resultado["erro"] == "falha ao creditar"
    assert resultado["creditos"] == 25
    saldo_atual_mock.assert_called_once_with("cli-123")
    creditar_tier_mock.assert_called_once_with("cli-123", 25)
    enviar_recibo_mock.assert_not_called()


def test_ativar_tier_com_tier_invalido_lanca_value_error() -> None:
    with pytest.raises(ValueError, match="tier invalido"):
        service.ativar_tier("cli-123", "diamante")


def test_ativar_tier_com_cliente_vazio_lanca_value_error() -> None:
    with pytest.raises(ValueError, match="cliente obrigatorio"):
        service.ativar_tier("   ", "ouro")


@patch("ativacao_service.enviar_recibo")
@patch("ativacao_service.creditar_tier", return_value=True)
@patch("ativacao_service.saldo_atual", return_value=90)
def test_ativar_tier_normaliza_cliente_e_tier_antes_de_orquestrar(
    saldo_atual_mock, creditar_tier_mock, enviar_recibo_mock
) -> None:
    resultado = service.ativar_tier("  cliente-42  ", " PrAtA ")

    assert resultado["ok"] is True
    assert resultado["cliente_id"] == "cliente-42"
    assert resultado["tier"] == "prata"
    assert resultado["creditos"] == 25
    assert resultado["saldo_restante"] == 65
    saldo_atual_mock.assert_called_once_with("cliente-42")
    creditar_tier_mock.assert_called_once_with("cliente-42", 25)
    enviar_recibo_mock.assert_called_once_with("cliente-42", "prata", 25)


@patch("ativacao_service.enviar_recibo")
@patch("ativacao_service.creditar_tier", return_value=True)
@patch("ativacao_service.saldo_atual", return_value=25)
def test_ativar_tier_com_saldo_exatamente_igual_ao_credito_retorna_ok_true(
    saldo_atual_mock, creditar_tier_mock, enviar_recibo_mock
) -> None:
    resultado = service.ativar_tier("cli-123", "prata")

    assert resultado["ok"] is True
    assert resultado["creditos"] == 25
    assert resultado["saldo_restante"] == 0
    saldo_atual_mock.assert_called_once_with("cli-123")
    creditar_tier_mock.assert_called_once_with("cli-123", 25)
    enviar_recibo_mock.assert_called_once_with("cli-123", "prata", 25)


@patch("ativacao_service.enviar_recibo")
@patch("ativacao_service.creditar_tier")
@patch("ativacao_service.saldo_atual", side_effect=RuntimeError("crm indisponivel"))
def test_ativar_tier_propaga_excecao_de_saldo_atual(
    saldo_atual_mock, creditar_tier_mock, enviar_recibo_mock
) -> None:
    with pytest.raises(RuntimeError, match="crm indisponivel"):
        service.ativar_tier("cli-123", "ouro")

    saldo_atual_mock.assert_called_once_with("cli-123")
    creditar_tier_mock.assert_not_called()
    enviar_recibo_mock.assert_not_called()


@patch("ativacao_service.enviar_recibo")
@patch("ativacao_service.creditar_tier", side_effect=RuntimeError("falha no credito"))
@patch("ativacao_service.saldo_atual", return_value=100)
def test_ativar_tier_propaga_excecao_de_creditar_tier_sem_enviar_recibo(
    saldo_atual_mock, creditar_tier_mock, enviar_recibo_mock
) -> None:
    with pytest.raises(RuntimeError, match="falha no credito"):
        service.ativar_tier("cli-123", "ouro")

    saldo_atual_mock.assert_called_once_with("cli-123")
    creditar_tier_mock.assert_called_once_with("cli-123", 50)
    enviar_recibo_mock.assert_not_called()


@patch("ativacao_service.enviar_recibo", side_effect=RuntimeError("falha no recibo"))
@patch("ativacao_service.creditar_tier", return_value=True)
@patch("ativacao_service.saldo_atual", return_value=100)
def test_ativar_tier_propaga_excecao_de_enviar_recibo_apos_creditar(
    saldo_atual_mock, creditar_tier_mock, enviar_recibo_mock
) -> None:
    with pytest.raises(RuntimeError, match="falha no recibo"):
        service.ativar_tier("cli-123", "ouro")

    saldo_atual_mock.assert_called_once_with("cli-123")
    creditar_tier_mock.assert_called_once_with("cli-123", 50)
    enviar_recibo_mock.assert_called_once_with("cli-123", "ouro", 50)
