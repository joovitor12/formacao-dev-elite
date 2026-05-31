from __future__ import annotations

from unittest.mock import patch

import pytest

import fidelidade_service as service
import regras_fidelidade as regras


@pytest.fixture
def cliente_id_padrao() -> str:
    return "cliente-1"


@pytest.mark.parametrize(
    ("valor", "tier", "esperado"),
    [
        (100.0, "bronze", 10),
        (100.0, "prata", 20),
        (100.0, "ouro", 30),
    ],
)
def test_pontos_por_compra_por_tier_retorna_pontos_corretos(
    valor: float,
    tier: str,
    esperado: int,
) -> None:
    # Arrange + Act
    pontos = regras.pontos_por_compra(valor, tier)

    # Assert
    assert pontos == esperado


def test_pontos_por_compra_com_valor_invalido_gera_erro() -> None:
    with pytest.raises(ValueError, match="valor invalido"):
        regras.pontos_por_compra(0, "bronze")


def test_pontos_por_compra_com_tier_invalido_gera_erro() -> None:
    with pytest.raises(ValueError, match="tier invalido"):
        regras.pontos_por_compra(100.0, "diamante")


@pytest.mark.parametrize(
    ("codigo", "esperado"),
    [
        ("copo", 100),
        ("CAMISETA", 500),
    ],
)
def test_custo_premio_quando_codigo_valido_retorna_custo_exato(
    codigo: str,
    esperado: int,
) -> None:
    assert regras.custo_premio(codigo) == esperado


@pytest.mark.parametrize("codigo", ["XYZ", " "])
def test_custo_premio_invalido_gera_erro(codigo: str) -> None:
    with pytest.raises(ValueError):
        regras.custo_premio(codigo)


@pytest.mark.parametrize(
    ("saldo", "custo", "esperado"),
    [
        (100, 100, True),
        (99, 100, False),
        (100, 0, False),
    ],
)
def test_pode_resgatar_cobre_bordas_do_contrato(
    saldo: int,
    custo: int,
    esperado: bool,
) -> None:
    assert regras.pode_resgatar(saldo, custo) is esperado


@patch("fidelidade_service.enviar_notificacao")
@patch("fidelidade_service.saldo_cliente", return_value=120)
@patch("fidelidade_service.creditar_pontos", return_value=True)
def test_acumular_compra_quando_credito_ok_retorna_sucesso(
    mock_creditar_pontos,
    mock_saldo_cliente,
    mock_enviar_notificacao,
) -> None:
    # Act
    resultado = service.acumular_compra(" cli-1 ", 100.0, "bronze")

    # Assert
    assert resultado["ok"] is True
    assert resultado == {
        "ok": True,
        "cliente_id": "cli-1",
        "pontos": 10,
        "saldo": 120,
    }
    mock_creditar_pontos.assert_called_once_with("cli-1", 10)
    mock_saldo_cliente.assert_called_once_with("cli-1")
    mock_enviar_notificacao.assert_called_once_with("cli-1", "compra", "+10 pts")


@patch("fidelidade_service.enviar_notificacao")
@patch("fidelidade_service.saldo_cliente")
@patch("fidelidade_service.creditar_pontos", return_value=False)
def test_acumular_compra_quando_credito_falha_retorna_erro_sem_notificar(
    mock_creditar_pontos,
    mock_saldo_cliente,
    mock_enviar_notificacao,
) -> None:
    # Act
    resultado = service.acumular_compra("cliente-1", 100.0, "bronze")

    # Assert
    assert resultado["ok"] is False
    assert resultado == {"ok": False, "erro": "falha ao creditar", "pontos": 10}
    mock_creditar_pontos.assert_called_once_with("cliente-1", 10)
    mock_saldo_cliente.assert_not_called()
    mock_enviar_notificacao.assert_not_called()


def test_acumular_compra_com_cliente_vazio_gera_erro() -> None:
    with pytest.raises(ValueError, match="cliente obrigatorio"):
        service.acumular_compra("   ", 100.0, "bronze")


def test_resgatar_premio_com_cliente_vazio_gera_erro() -> None:
    with pytest.raises(ValueError, match="cliente obrigatorio"):
        service.resgatar_premio("", "copo")


@patch("fidelidade_service.debitar_pontos")
@patch("fidelidade_service.saldo_cliente", return_value=50)
def test_resgatar_premio_com_saldo_insuficiente_retorna_erro(
    mock_saldo_cliente,
    mock_debitar_pontos,
) -> None:
    # Act
    resultado = service.resgatar_premio("cliente-1", "copo")

    # Assert
    assert resultado["ok"] is False
    assert resultado == {
        "ok": False,
        "erro": "saldo insuficiente",
        "custo": 100,
        "saldo": 50,
    }
    mock_saldo_cliente.assert_called_once_with("cliente-1")
    mock_debitar_pontos.assert_not_called()


@patch("fidelidade_service.enviar_notificacao")
@patch("fidelidade_service.debitar_pontos", return_value=False)
@patch("fidelidade_service.saldo_cliente", return_value=200)
def test_resgatar_premio_quando_debito_falha_retorna_erro(
    mock_saldo_cliente,
    mock_debitar_pontos,
    mock_enviar_notificacao,
) -> None:
    # Act
    resultado = service.resgatar_premio("cliente-1", "copo")

    # Assert
    assert resultado == {"ok": False, "erro": "falha ao debitar", "custo": 100}
    mock_saldo_cliente.assert_called_once_with("cliente-1")
    mock_debitar_pontos.assert_called_once_with("cliente-1", 100)
    mock_enviar_notificacao.assert_not_called()


@patch("fidelidade_service.enviar_notificacao")
@patch("fidelidade_service.debitar_pontos", return_value=True)
@patch("fidelidade_service.saldo_cliente", return_value=550)
def test_resgatar_premio_quando_debito_ok_retorna_sucesso_com_premio_normalizado(
    mock_saldo_cliente,
    mock_debitar_pontos,
    mock_enviar_notificacao,
    cliente_id_padrao: str,
) -> None:
    # Act
    resultado = service.resgatar_premio(f" {cliente_id_padrao} ", "camiseta")

    # Assert
    assert resultado["ok"] is True
    assert resultado == {
        "ok": True,
        "cliente_id": cliente_id_padrao,
        "premio": "CAMISETA",
        "custo": 500,
        "saldo_restante": 50,
    }
    mock_saldo_cliente.assert_called_once_with(cliente_id_padrao)
    mock_debitar_pontos.assert_called_once_with(cliente_id_padrao, 500)
    mock_enviar_notificacao.assert_called_once_with(
        cliente_id_padrao,
        "resgate",
        "-500 pts CAMISETA",
    )
