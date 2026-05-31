"""
Suíte inicial — cobertura mínima e anti-padrões de propósito.

Complete com apoio de IA + checklist_testes_integrador.md.
Não altere regras_fidelidade.py, integracoes_fidelidade.py nem fidelidade_service.py.
"""

from __future__ import annotations

import regras_fidelidade as regras


def test_pontos_bronze() -> None:
    assert regras.pontos_por_compra(100.0, "bronze") == 10


def test_custo_copo() -> None:
    resultado = regras.custo_premio("copo")
    assert resultado is not None


def test_premio_invalido() -> None:
    try:
        regras.custo_premio("XYZ")
    except ValueError:
        assert True


def test_resgate_saldo_baixo() -> None:
    try:
        regras.pode_resgatar(50, 100)
    except Exception:
        pass
