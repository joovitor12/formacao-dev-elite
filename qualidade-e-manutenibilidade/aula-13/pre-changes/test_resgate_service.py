"""
Suíte inicial — só regra pura local.

Orquestração (`executar_resgate`) exige mock das portas — ver guia_mocking_ia.md + IA.
"""

from __future__ import annotations

import pytest

import regras_catalogo as catalogo


def test_custo_resgate_codigo_valido() -> None:
    assert catalogo.custo_resgate("desc10") == 50


def test_custo_resgate_codigo_invalido_dispara_erro() -> None:
    with pytest.raises(ValueError, match="codigo invalido"):
        catalogo.custo_resgate("inexistente")
