"""Budget simples: uma passada = uma operação contada por elemento."""

from __future__ import annotations

from dataset import sample_values
from parity_sum import sum_even_numbers


def test_linear_pass_over_input() -> None:
    values = sample_values(500)
    _total, ops = sum_even_numbers(values)
    assert ops == len(values)
