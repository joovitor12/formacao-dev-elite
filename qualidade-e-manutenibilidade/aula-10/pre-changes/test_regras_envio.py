"""
Testes fracos de propósito — reestruture em pre-changes/ seguindo guia_estrutura_teste.md.

Os asserts estão corretos; a estrutura é que precisa melhorar.
"""

from __future__ import annotations

import regras_envio as envio


def test_1() -> None:
    assert envio.tarifa_base_por_peso(3) == 18.0
    assert envio.tarifa_base_por_peso(7) == 23.6
    assert envio.multiplicador_regiao("sul") == 1.05


def test_frete() -> None:
    r = envio.calcular_frete("nordeste", 4, False)
    assert r["total"] == 20.16
    assert r["regiao"] == "nordeste"
    assert r["taxa_expresso"] == 0.0
    r2 = envio.calcular_frete("sudeste", 4, True)
    assert r2["total"] == 30.0


def test_erro() -> None:
    try:
        envio.multiplicador_regiao("x")
        assert False
    except ValueError:
        assert True
