"""Contrato público: processar_pedido deve manter comportamento após separação de módulos."""

from __future__ import annotations

import pedido_flow as pedido


def test_pedido_simples_sem_cupom() -> None:
    out = pedido.processar_pedido(
        {
            "cliente_id": "CLI-1",
            "itens": [
                {"sku": "A", "qtd": 2, "preco": 50.0},
                {"sku": "B", "qtd": 1, "preco": 30.0},
            ],
        }
    )
    assert out["ok"] is True
    assert out["subtotal"] == 130.0
    assert out["desconto"] == 0.0
    assert out["taxa"] == 0.0
    assert out["total"] == 130.0


def test_pedido_com_cupom_e_taxa_fixa() -> None:
    out = pedido.processar_pedido(
        {
            "cliente_id": "CLI-2",
            "cupom": "desc10",
            "itens": [{"sku": "X", "qtd": 1, "preco": 80.0}],
        }
    )
    assert out["ok"] is True
    assert out["subtotal"] == 80.0
    assert out["desconto"] == 8.0
    assert out["taxa"] == 5.0
    assert out["total"] == 77.0


def test_pedido_sem_cliente_falha() -> None:
    out = pedido.processar_pedido({"itens": [{"sku": "A", "qtd": 1, "preco": 10.0}]})
    assert out["ok"] is False
    assert "cliente_id obrigatorio" in out["erros"]


def test_pedido_persistido_em_lista() -> None:
    antes = len(pedido.listar_pedidos())
    pedido.processar_pedido(
        {"cliente_id": "CLI-3", "itens": [{"sku": "Z", "qtd": 1, "preco": 25.0}]}
    )
    assert len(pedido.listar_pedidos()) == antes + 1
