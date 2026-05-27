"""Matriz de casos para equivalência funcional (flow vs baseline)."""

from __future__ import annotations

from typing import Any

CASOS: list[dict[str, Any]] = [
    {
        "id": "varejo_simples",
        "entrada": {
            "cliente_id": "C-100",
            "canal": "varejo",
            "itens": [{"sku": "sku-a", "qtd": 2, "preco_unit": 30.0}],
        },
    },
    {
        "id": "marketplace_taxa",
        "entrada": {
            "cliente_id": "C-200",
            "canal": "marketplace",
            "itens": [{"sku": "SKU-B", "qtd": 1, "preco_unit": 100.0}],
        },
    },
    {
        "id": "varejo_cupom_econ10",
        "entrada": {
            "cliente_id": "C-300",
            "canal": "varejo",
            "cupom": "econ10",
            "itens": [{"sku": "SKU-A", "qtd": 1, "preco_unit": 100.0}],
        },
    },
    {
        "id": "marketplace_cupom",
        "entrada": {
            "cliente_id": "C-400",
            "canal": "marketplace",
            "cupom": "ECON10",
            "itens": [{"sku": "SKU-B", "qtd": 2, "preco_unit": 100.0}],
        },
    },
    {
        "id": "estoque_insuficiente",
        "entrada": {
            "cliente_id": "C-500",
            "canal": "varejo",
            "itens": [{"sku": "SKU-C", "qtd": 1, "preco_unit": 10.0}],
        },
    },
    {
        "id": "cliente_vazio",
        "entrada": {"cliente_id": "", "canal": "varejo", "itens": [{"sku": "SKU-A", "qtd": 1, "preco_unit": 1.0}]},
    },
    {
        "id": "canal_invalido",
        "entrada": {
            "cliente_id": "C-600",
            "canal": "wholesale",
            "itens": [{"sku": "SKU-A", "qtd": 1, "preco_unit": 10.0}],
        },
    },
    {
        "id": "cupom_invalido",
        "entrada": {
            "cliente_id": "C-700",
            "canal": "varejo",
            "cupom": "OFF50",
            "itens": [{"sku": "SKU-A", "qtd": 1, "preco_unit": 50.0}],
        },
    },
]
