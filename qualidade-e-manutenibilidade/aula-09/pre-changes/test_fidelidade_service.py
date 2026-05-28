"""Testes do serviço — cobrem fluxo, mas dependem de estado compartilhado."""

from __future__ import annotations

import fidelidade_service as fidelidade


def test_registrar_compra_ouro() -> None:
    fidelidade.reset_estado()
    out = fidelidade.registrar_compra("C-1", 100.0, "ouro")
    assert out["ok"] is True
    assert out["pontos_base"] == 10
    assert out["pontos_bonus"] == 2
    assert out["pontos_total"] == 12
    assert fidelidade.consultar_saldo("C-1") == 12


def test_resgate_reduz_saldo() -> None:
    fidelidade.reset_estado()
    fidelidade.registrar_compra("C-2", 200.0, "bronze")
    out = fidelidade.resgatar_pontos("C-2", 5)
    assert out["ok"] is True
    assert fidelidade.consultar_saldo("C-2") == 15
