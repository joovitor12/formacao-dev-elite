"""Garante que a implementação em evolução permanece equivalente ao baseline congelado."""

from __future__ import annotations

import comissao_baseline as baseline
import comissao_service as service
import pytest
from casos_equivalencia import CASOS


@pytest.mark.parametrize("caso", CASOS, ids=[c["id"] for c in CASOS])
def test_saida_identica_ao_baseline(caso: dict) -> None:
    entrada = caso["entrada"]
    assert service.calcular_comissao(entrada) == baseline.calcular_comissao(entrada)
