from __future__ import annotations

from cache_service import process_requests_with_cache


def test_process_requests_with_cache_preserves_value_contract() -> None:
    values, _ = process_requests_with_cache([1, 2, 1, 3])
    assert values == [10, 20, 10, 30]
