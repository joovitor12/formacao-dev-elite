from __future__ import annotations

from cache_service import process_requests_with_cache
from dataset import build_requests


def test_cache_strategy_operations_budget() -> None:
    requests = build_requests(total_keys=500, repeats=10)
    _values, operations = process_requests_with_cache(requests)
    unique_keys = len(set(requests))
    expected_operations = len(requests) + unique_keys
    allowed_overhead = int(expected_operations * 0.10)

    # Modelo esperado: 1 operacao por request + 1 extra por chave unica (miss).
    # Mantemos margem pequena para ajustes legitimos sem mascarar regressao.
    assert operations <= expected_operations + allowed_overhead
