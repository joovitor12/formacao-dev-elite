from __future__ import annotations

from parity_sum import sum_even_numbers


def test_sum_even_numbers_basic() -> None:
    total, _ = sum_even_numbers([1, 2, 3, 4, -2])
    assert total == 4
