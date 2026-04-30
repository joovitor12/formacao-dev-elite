from __future__ import annotations

from cache_service import process_requests_with_cache
from dataset import build_requests


def test_cache_strategy_operations_budget() -> None:
    requests = build_requests(total_keys=500, repeats=10)
    _values, operations = process_requests_with_cache(requests)
    assert operations <= len(requests) + 700
