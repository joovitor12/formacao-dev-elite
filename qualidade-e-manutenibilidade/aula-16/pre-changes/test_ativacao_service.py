"""
Suíte inicial mínima — complete com boas práticas de testes assistidos.

Use checklist_testes_assistidos.md + guia_boas_praticas_testes_ia.md + IA.
"""

from __future__ import annotations

import regras_tier as tier


def test_creditos_tier_ouro() -> None:
    assert tier.creditos_por_tier("ouro") == 50
