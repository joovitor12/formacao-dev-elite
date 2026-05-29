"""
Suíte inicial — só casos de sucesso (happy path).

Complete com casos de erro usando guia_casos_sucesso_erro.md + IA.
"""

from __future__ import annotations

import regras_resgate as resgate


def test_custo_resgate_desc10() -> None:
    assert resgate.custo_resgate("desc10") == 50


def test_resgate_com_saldo_suficiente() -> None:
    resultado = resgate.processar_resgate("DESC10", 120)

    assert resultado["ok"] is True
    assert resultado["custo"] == 50
    assert resultado["saldo_restante"] == 70


def test_resgate_saldo_exato() -> None:
    resultado = resgate.processar_resgate("FRETE", 100)

    assert resultado["ok"] is True
    assert resultado["saldo_restante"] == 0
