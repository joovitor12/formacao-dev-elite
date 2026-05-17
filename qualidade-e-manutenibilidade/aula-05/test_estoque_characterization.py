"""Contrato público — cada incremento de refatoração deve manter estes comportamentos."""

from __future__ import annotations

import estoque_service as estoque


def test_entrada_aumenta_saldo() -> None:
    out = estoque.registrar_movimento({"tipo": "entrada", "sku": "SKU-A", "qtd": 5})
    assert out["ok"] is True
    assert out["saldo_atual"] == estoque.consultar_saldo("SKU-A")


def test_saida_reduz_saldo() -> None:
    estoque.registrar_movimento({"tipo": "entrada", "sku": "SKU-C", "qtd": 10})
    out = estoque.registrar_movimento({"tipo": "saida", "sku": "SKU-C", "qtd": 3})
    assert out["ok"] is True
    assert out["saldo_atual"] == 7


def test_saida_sem_saldo_falha() -> None:
    out = estoque.registrar_movimento({"tipo": "saida", "sku": "SKU-B", "qtd": 999})
    assert out["ok"] is False
    assert "saldo insuficiente" in out["erros"]


def test_tipo_invalido() -> None:
    out = estoque.registrar_movimento({"tipo": "ajuste", "sku": "SKU-A", "qtd": 1})
    assert out["ok"] is False
    assert "tipo deve ser entrada ou saida" in out["erros"]


def test_auditoria_registra_movimento_ok() -> None:
    antes = len(estoque.listar_auditoria())
    estoque.registrar_movimento({"tipo": "entrada", "sku": "SKU-Z", "qtd": 2})
    depois = len(estoque.listar_auditoria())
    assert depois == antes + 1
