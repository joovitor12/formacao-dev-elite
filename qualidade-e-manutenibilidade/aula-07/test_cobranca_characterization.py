"""Comportamento fixo — âncora além do snapshot."""

from __future__ import annotations

import cobranca_service as cobranca


def test_basico_um_mes() -> None:
    out = cobranca.calcular_cobranca({"plano": "basico", "meses": 1})
    assert out["ok"] is True
    assert out["total"] == 29.9


def test_pro_anual_com_desconto() -> None:
    out = cobranca.calcular_cobranca({"plano": "pro", "meses": 12})
    assert out["ok"] is True
    assert out["total"] == 610.98
    assert "desconto anual aplicado" in out["avisos"]
