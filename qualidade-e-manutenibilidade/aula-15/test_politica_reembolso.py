"""
Suíte com falsos positivos — pytest verde, mas lacunas de detecção de regressão.

Ajuste os testes marcados na matriz — ver guia_falsos_positivos.md + simular_regressao.py.
"""

from __future__ import annotations

import pytest

import politica_reembolso as politica


def test_reembolso_padrao_aprovado() -> None:
    resultado = politica.calcular_reembolso(200.0, "padrao", 2)

    assert resultado["ok"] is True
    assert resultado["tipo"] == "padrao"
    assert resultado["percentual"] == 1.0
    assert resultado["valor_reembolso"] == 200.0


def test_prazo_expirado_rejeita() -> None:
    resultado = politica.calcular_reembolso(100.0, "padrao", 999)

    assert resultado["ok"] is False
    assert resultado["erro"] == "prazo expirado"
    assert resultado["valor_reembolso"] == 0.0


def test_reembolso_integral_primeiros_dias() -> None:
    resultado = politica.calcular_reembolso(150.0, "premium", 2)

    assert resultado["ok"] is True
    assert resultado["percentual"] == 1.0
    assert resultado["valor_reembolso"] == 150.0


def test_reembolso_premium_meio_prazo_aplica_cinquenta_porcento() -> None:
    resultado = politica.calcular_reembolso(200.0, "premium", 10)

    assert resultado["ok"] is True
    assert resultado["percentual"] == 0.5
    assert resultado["valor_reembolso"] == 100.0


def test_meio_prazo_aplica_cinquenta_porcento() -> None:
    resultado = politica.calcular_reembolso(100.0, "padrao", 5)

    assert resultado["ok"] is True
    assert resultado["percentual"] == 0.5
    assert resultado["valor_reembolso"] == 50.0


def test_valor_invalido_dispara_erro() -> None:
    with pytest.raises(ValueError, match="valor invalido"):
        politica.calcular_reembolso(0.0, "padrao", 1)
