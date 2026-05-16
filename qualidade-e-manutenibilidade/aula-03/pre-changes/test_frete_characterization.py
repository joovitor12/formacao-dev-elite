"""Testes de caracterização — comportamento que a refatoração deve preservar."""

from __future__ import annotations

import frete_service as frete


def test_frete_sudeste_peso_leve() -> None:
    out = frete.calcular_frete(
        {
            "regiao": "sudeste",
            "peso_kg": 2.0,
            "altura_cm": 10,
            "largura_cm": 10,
            "profundidade_cm": 10,
        }
    )
    assert out["ok"] is True
    assert out["valor_frete"] == 23.0
    assert out["peso_cobrado_kg"] == 2.0


def test_frete_usa_peso_cubado_quando_maior() -> None:
    out = frete.calcular_frete(
        {
            "regiao": "sul",
            "peso_kg": 1.0,
            "altura_cm": 20,
            "largura_cm": 25,
            "profundidade_cm": 40,
        }
    )
    assert out["ok"] is True
    # cubado = 20*25*40/5000 = 4.0
    assert out["peso_cobrado_kg"] == 4.0
    assert out["valor_frete"] == 30.5


def test_frete_expresso_acrescenta_taxa() -> None:
    base = frete.calcular_frete(
        {
            "regiao": "nordeste",
            "peso_kg": 3.0,
            "altura_cm": 5,
            "largura_cm": 5,
            "profundidade_cm": 5,
            "expresso": False,
        }
    )
    expresso = frete.calcular_frete(
        {
            "regiao": "nordeste",
            "peso_kg": 3.0,
            "altura_cm": 5,
            "largura_cm": 5,
            "profundidade_cm": 5,
            "expresso": True,
        }
    )
    assert expresso["valor_frete"] == round(base["valor_frete"] + 15.0, 2)


def test_regiao_invalida() -> None:
    out = frete.calcular_frete({"regiao": "antartida", "peso_kg": 2.0})
    assert out["ok"] is False
    assert "regiao invalida" in out["avisos"]


def test_contador_global_incrementa() -> None:
    antes = frete.TOTAL_FRETES_CALCULADOS
    frete.calcular_frete({"regiao": "sudeste", "peso_kg": 1.0})
    assert frete.TOTAL_FRETES_CALCULADOS == antes + 1
