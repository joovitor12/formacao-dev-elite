"""Contrato principal — deve permanecer verde durante toda a refatoração."""

from __future__ import annotations

import fulfillment_flow as flow


def test_varejo_subtotal_sem_taxa() -> None:
    out = flow.processar_fulfillment(
        {
            "cliente_id": "CLI-1",
            "canal": "varejo",
            "itens": [{"sku": "SKU-A", "qtd": 2, "preco_unit": 30.0}],
        }
    )
    assert out["ok"] is True
    assert out["subtotal"] == 60.0
    assert out["taxa_marketplace"] == 0.0
    assert out["total"] == 60.0


def test_marketplace_aplica_taxa() -> None:
    out = flow.processar_fulfillment(
        {
            "cliente_id": "CLI-2",
            "canal": "marketplace",
            "itens": [{"sku": "SKU-B", "qtd": 1, "preco_unit": 100.0}],
        }
    )
    assert out["ok"] is True
    assert out["taxa_marketplace"] == 3.0
    assert out["total"] == 103.0


def test_cupom_econ10_varejo() -> None:
    out = flow.processar_fulfillment(
        {
            "cliente_id": "CLI-3",
            "canal": "varejo",
            "cupom": "ECON10",
            "itens": [{"sku": "SKU-A", "qtd": 1, "preco_unit": 100.0}],
        }
    )
    assert out["ok"] is True
    assert out["desconto"] == 10.0
    assert out["total"] == 90.0


def test_estoque_insuficiente() -> None:
    out = flow.processar_fulfillment(
        {
            "cliente_id": "CLI-4",
            "canal": "varejo",
            "itens": [{"sku": "SKU-C", "qtd": 1, "preco_unit": 10.0}],
        }
    )
    assert out["ok"] is False
    assert any("estoque insuficiente" in aviso for aviso in out["avisos"])


def test_persiste_fulfillment() -> None:
    antes = len(flow.listar_fulfillments())
    flow.processar_fulfillment(
        {
            "cliente_id": "CLI-5",
            "canal": "varejo",
            "itens": [{"sku": "SKU-A", "qtd": 1, "preco_unit": 10.0}],
        }
    )
    assert len(flow.listar_fulfillments()) == antes + 1
