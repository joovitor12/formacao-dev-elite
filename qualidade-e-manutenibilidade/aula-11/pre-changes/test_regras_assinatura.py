"""Suíte parcial — lacunas de cobertura intencionais para a aula."""

from __future__ import annotations

import regras_assinatura as assinatura


def test_valor_plano_basico() -> None:
    assert assinatura.valor_plano("basico") == 29.9
