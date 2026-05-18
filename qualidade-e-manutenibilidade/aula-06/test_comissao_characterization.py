"""Exemplos fixos de comportamento — úteis ao ampliar a matriz de equivalência."""

from __future__ import annotations

import comissao_service as comissao


def test_junior_produto_valor_conhecido() -> None:
    out = comissao.calcular_comissao(
        {
            "vendedor_nivel": "junior",
            "valor_venda": 1000.0,
            "categoria": "produto",
            "meta_bateu": False,
        }
    )
    assert out["ok"] is True
    assert out["comissao"] == 27.0


def test_senior_alto_valor_com_meta_e_extra() -> None:
    out = comissao.calcular_comissao(
        {
            "vendedor_nivel": "senior",
            "valor_venda": 15000.0,
            "categoria": "servico",
            "meta_bateu": True,
        }
    )
    assert out["ok"] is True
    assert out["comissao"] == 1555.0
