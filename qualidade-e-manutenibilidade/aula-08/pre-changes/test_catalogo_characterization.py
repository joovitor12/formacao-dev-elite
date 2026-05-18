"""Contrato de comportamento — checklist exige mantê-los verdes."""

from __future__ import annotations

import catalogo_precos as catalogo


def test_varejo_simples() -> None:
    out = catalogo.calcular_carrinho(
        {
            "cliente_tipo": "varejo",
            "itens": [{"sku": "A", "qtd": 2, "preco_unit": 30.0}],
        }
    )
    assert out["ok"] is True
    assert out["subtotal"] == 60.0
    assert out["desconto"] == 0.0
    assert out["imposto"] == 3.0
    assert out["total"] == 63.0
    assert out["frete_gratis"] is False


def test_atacado_volume() -> None:
    out = catalogo.calcular_carrinho(
        {
            "cliente_tipo": "atacado",
            "itens": [{"sku": "B", "qtd": 10, "preco_unit": 20.0}],
        }
    )
    assert out["ok"] is True
    assert out["subtotal"] == 200.0
    assert out["desconto"] == 16.0
    assert out["total"] == 193.2
    assert "desconto atacado aplicado" in out["avisos"]


def test_cupom_desc15() -> None:
    out = catalogo.calcular_carrinho(
        {
            "cliente_tipo": "varejo",
            "cupom": "DESC15",
            "itens": [{"sku": "C", "qtd": 1, "preco_unit": 100.0}],
        }
    )
    assert out["ok"] is True
    assert out["desconto"] == 15.0
    assert out["total"] == 89.25


def test_frete_gratis_elegivel() -> None:
    out = catalogo.calcular_carrinho(
        {
            "cliente_tipo": "varejo",
            "cupom": "FRETEGRATIS",
            "itens": [{"sku": "D", "qtd": 1, "preco_unit": 250.0}],
        }
    )
    assert out["ok"] is True
    assert out["frete_gratis"] is True
    assert out["total"] == 262.5


def test_carrinho_vazio() -> None:
    out = catalogo.calcular_carrinho({"cliente_tipo": "varejo", "itens": []})
    assert out["ok"] is False
    assert "carrinho vazio" in out["avisos"]


def test_cupom_invalido() -> None:
    out = catalogo.calcular_carrinho(
        {
            "cliente_tipo": "varejo",
            "cupom": "XYZ",
            "itens": [{"sku": "E", "qtd": 1, "preco_unit": 50.0}],
        }
    )
    assert out["ok"] is False
    assert "cupom invalido" in out["avisos"]
