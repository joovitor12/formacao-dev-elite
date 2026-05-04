from __future__ import annotations

from parity_sum import sum_even_numbers


def test_sum_even_numbers_basic() -> None:
    total, _ = sum_even_numbers([1, 2, 3, 4, -2])
    assert total == 4  # 2 + 4 + (-2)


def test_sum_even_numbers_empty() -> None:
    total, ops = sum_even_numbers([])
    assert total == 0
    assert ops == 0


def test_sum_even_numbers_all_odds() -> None:
    total, _ = sum_even_numbers([1, 3, 5, -7, 9])
    assert total == 0


def test_sum_even_numbers_all_evens() -> None:
    total, _ = sum_even_numbers([2, 4, -6, 8])
    assert total == 8  # 2 + 4 + (-6) + 8


def test_sum_even_numbers_with_duplicates() -> None:
    total, _ = sum_even_numbers([2, 2, 3, 4, 4])
    assert total == 12  # 2 + 2 + 4 + 4
