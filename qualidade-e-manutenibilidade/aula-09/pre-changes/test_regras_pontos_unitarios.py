"""
Testes unitários das regras puras — rápidos, isolados, um comportamento por teste.
"""

from __future__ import annotations

import pytest

import regras_pontos as regras


def test_pontos_por_valor_multiplo_de_dez() -> None:
    assert regras.pontos_por_valor(100.0) == 10


def test_pontos_por_valor_arredonda_para_baixo() -> None:
    assert regras.pontos_por_valor(59.99) == 5


def test_pontos_por_valor_zero_ou_negativo() -> None:
    assert regras.pontos_por_valor(0) == 0
    assert regras.pontos_por_valor(-10) == 0


def test_bonus_ouro() -> None:
    assert regras.bonus_por_tier("ouro", 100) == 20


def test_bonus_prata() -> None:
    assert regras.bonus_por_tier("PRATA", 50) == 5


def test_bonus_bronze_zero() -> None:
    assert regras.bonus_por_tier("bronze", 30) == 0


def test_tier_invalido_levanta_erro() -> None:
    with pytest.raises(ValueError, match="tier invalido"):
        regras.bonus_por_tier("platina", 10)


def test_pode_resgatar_saldo_suficiente() -> None:
    assert regras.pode_resgatar(100, 40) is True


def test_nao_pode_resgatar_custo_zero() -> None:
    assert regras.pode_resgatar(100, 0) is False
