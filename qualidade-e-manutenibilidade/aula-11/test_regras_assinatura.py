"""Suíte parcial — lacunas de cobertura intencionais para a aula."""

from __future__ import annotations

import pytest

import regras_assinatura as assinatura


def test_valor_plano_basico() -> None:
    assert assinatura.valor_plano("basico") == 29.9


def test_calcular_fatura_pro_12_meses_primeira_fatura_retorna_totais_corretos() -> None:
    # Arrange
    nome_plano = "pro"
    meses = 12

    # Act
    fatura = assinatura.calcular_fatura(nome_plano, meses, primeira_fatura=True)

    # Assert
    assert fatura["plano"] == "pro"
    assert fatura["meses"] == 12
    assert fatura["subtotal"] == 718.8
    assert fatura["desconto"] == 107.82
    assert fatura["taxa_ativacao"] == 9.9
    assert fatura["total"] == 620.88


def test_calcular_fatura_com_plano_invalido_lanca_value_error() -> None:
    # Arrange
    nome_plano = "premium"
    meses = 3

    # Act / Assert
    with pytest.raises(ValueError, match="plano invalido"):
        assinatura.calcular_fatura(nome_plano, meses)


def test_desconto_por_compromisso_com_meses_invalido_lanca_value_error() -> None:
    # Arrange
    meses = 0

    # Act / Assert
    with pytest.raises(ValueError, match="meses invalido"):
        assinatura.desconto_por_compromisso(meses)
