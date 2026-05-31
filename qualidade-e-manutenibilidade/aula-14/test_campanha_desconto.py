"""
Suíte gerada por IA — pytest verde, qualidade mista.

Sua tarefa: **avaliar** cada teste (manter / revisar / rejeitar) e corrigir
os problemas priorizados — ver guia_avaliacao_testes_ia.md.
"""

from __future__ import annotations

import pytest

import campanha_desconto as campanha


def test_calcular_desconto_retorna_resultado() -> None:
    resultado = campanha.calcular_desconto(100.0, "PROMO10", False)

    assert resultado["ok"] is True
    assert resultado["cupom"] == "PROMO10"
    assert resultado["percentual"] == 0.10
    assert resultado["valor_final"] == 90.0

def test_validar_cupom_retorna_cupom() -> None:
    assert campanha.validar_cupom("promo10") == "PROMO10"

def test_cupom_e_desconto_no_mesmo_teste() -> None:

    resultado = campanha.calcular_desconto(100.0, "PROMO10", False)
    assert resultado["ok"] is True
    assert resultado["valor_final"] == 90.0
    assert resultado["percentual"] == 0.10


def test_erro_cupom_invalido() -> None:
    with pytest.raises(ValueError, match="cupom invalido"):
        campanha.validar_cupom("INEXISTENTE")


def test_desconto_vip_soma_bonus() -> None:
    resultado = campanha.calcular_desconto(100.0, "PROMO10", True)

    assert resultado["ok"] is True
    assert resultado["percentual"] == 0.15
    assert resultado["valor_final"] == 85.0


def test_erro_valor_negativo() -> None:
    with pytest.raises(ValueError, match="valor invalido"):
        campanha.calcular_desconto(-50.0, "PROMO10", False)


def test_sucesso_promo20() -> None:
    resultado = campanha.calcular_desconto(200.0, "promo20", False)

    assert resultado["ok"] is True
    assert resultado["cupom"] == "PROMO20"
    assert resultado["percentual"] == 0.20
    assert resultado["valor_final"] == 160.0
