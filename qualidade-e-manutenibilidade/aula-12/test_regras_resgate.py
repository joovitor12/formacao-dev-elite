"""
Suíte de regras de resgate com cenários de sucesso e erro.
"""

from __future__ import annotations

import pytest

import regras_resgate as resgate


def test_custo_resgate_com_codigo_valido_retorna_custo() -> None:
    assert resgate.custo_resgate("desc10") == 50


def test_resgate_com_saldo_suficiente() -> None:
    resultado = resgate.processar_resgate("DESC10", 120)

    assert resultado["ok"] is True
    assert resultado["custo"] == 50
    assert resultado["saldo_restante"] == 70


def test_resgate_com_saldo_exato() -> None:
    resultado = resgate.processar_resgate("FRETE", 100)

    assert resultado["ok"] is True
    assert resultado["saldo_restante"] == 0


def test_resgate_com_saldo_insuficiente_retorna_falha() -> None:
    resultado = resgate.processar_resgate("VIP", 499)

    assert resultado["ok"] is False
    assert resultado["erro"] == "saldo insuficiente"
    assert resultado["custo"] == 500


def test_resgate_com_codigo_invalido_dispara_erro() -> None:
    codigo = "inexistente"
    saldo_pontos = 1000

    with pytest.raises(ValueError, match="^codigo invalido$"):
        resgate.processar_resgate(codigo, saldo_pontos)


def test_resgate_com_saldo_negativo_dispara_erro() -> None:
    codigo = "DESC10"
    saldo_pontos = -1

    with pytest.raises(ValueError, match="^saldo invalido$"):
        resgate.processar_resgate(codigo, saldo_pontos)
