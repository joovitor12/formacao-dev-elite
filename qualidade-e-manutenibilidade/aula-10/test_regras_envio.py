"""
Testes com estrutura de qualidade — referência (AAA, nome, foco, legibilidade).
"""

from __future__ import annotations

import pytest

import regras_envio as envio

TARIFA_ATE_5KG = 18.0
PESO_ENTRADA = 2.0

def test_tarifa_base_peso_leve_retorna_valor_fixo() -> None:
    # Arrange
    peso = 3.0

    # Act
    resultado = envio.tarifa_base_por_peso(peso)

    # Assert
    assert resultado == TARIFA_ATE_5KG


def test_tarifa_base_peso_acima_de_cinco_incrementa_por_kg() -> None:
    peso = 7.0
    esperado = 18.0 + (7.0 - 5) * 2.8

    resultado = envio.tarifa_base_por_peso(peso)

    assert resultado == esperado


def test_multiplicador_sudeste_e_neutro() -> None:
    assert envio.multiplicador_regiao("SUDESTE") == 1.0


def test_regiao_invalida_levanta_erro() -> None:
    with pytest.raises(ValueError, match="regiao invalida"):
        envio.multiplicador_regiao("antartida")


def test_calcular_frete_expresso_soma_taxa_fixa() -> None:
    entrada_regiao = "sudeste"

    sem_expresso = envio.calcular_frete(entrada_regiao, PESO_ENTRADA, expresso=False)
    com_expresso = envio.calcular_frete(entrada_regiao, PESO_ENTRADA, expresso=True)

    assert com_expresso["total"] == sem_expresso["total"] + 12.0
    assert com_expresso["taxa_expresso"] == 12.0


def test_calcular_frete_peso_zero_com_expresso_nao_adiciona_taxa() -> None:
    # Arrange
    entrada_regiao = "sudeste"
    entrada_peso = 0.0
    entrada_expresso = True

    # Act
    resultado = envio.calcular_frete(entrada_regiao, entrada_peso, expresso=entrada_expresso)

    # Assert
    assert resultado["base"] == 0.0
    assert resultado["valor_regional"] == 0.0
    assert resultado["taxa_expresso"] == 0.0
    assert resultado["total"] == 0.0
