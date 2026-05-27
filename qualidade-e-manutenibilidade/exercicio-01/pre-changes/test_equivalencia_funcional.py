"""Equivalência funcional: implementação atual vs baseline congelado."""

from __future__ import annotations

import fulfillment_baseline as baseline
import fulfillment_flow as flow
import pytest
from casos_equivalencia import CASOS


@pytest.mark.parametrize("caso", CASOS, ids=[c["id"] for c in CASOS])
def test_saida_identica_ao_baseline(caso: dict) -> None:
    entrada = caso["entrada"]
    flow.reset_estado()
    baseline.reset_estado()
    assert flow.processar_fulfillment(entrada) == baseline.processar_fulfillment(entrada)
