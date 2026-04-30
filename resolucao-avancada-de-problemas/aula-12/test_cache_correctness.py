from __future__ import annotations

from cache_service import process_requests_with_cache


def test_process_requests_with_cache_preserves_value_contract() -> None:
    values, _ = process_requests_with_cache([1, 2, 1, 3])
    assert values == [10, 20, 10, 30]


def test_process_requests_with_cache_empty_input() -> None:
    values, operations = process_requests_with_cache([])
    assert values == []
    assert operations == 0


def test_process_requests_with_cache_counts_hits_and_misses() -> None:
    values, operations = process_requests_with_cache([1, 1, 1])
    assert values == [10, 10, 10]
    # 1a chave: hit de loop + miss de lookup; demais: apenas hit de loop.
    assert operations == 4


def test_process_requests_with_cache_hits_cost_less_than_all_misses() -> None:
    _values_with_hits, operations_with_hits = process_requests_with_cache([1, 2, 1, 2])
    _values_all_misses, operations_all_misses = process_requests_with_cache([1, 2, 3, 4])

    assert operations_with_hits < operations_all_misses


def test_process_requests_with_cache_is_consistent_between_calls() -> None:
    first_values, first_operations = process_requests_with_cache([1, 2, 1, 3])
    second_values, second_operations = process_requests_with_cache([1, 2, 1, 3])

    assert first_values == second_values
    assert first_operations == second_operations
