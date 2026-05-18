"""Garante que o comportamento atual ainda bate com o snapshot 'antes'."""

from __future__ import annotations

from pathlib import Path

import cobranca_service as cobranca
from snapshot_comportamento import capturar, carregar

SNAPSHOT = Path(__file__).resolve().parent / "snapshots" / "antes_comportamento.json"


def test_saidas_iguais_ao_snapshot_antes() -> None:
    esperado = carregar(SNAPSHOT)
    atual = capturar(cobranca.calcular_cobranca)
    assert atual == esperado
