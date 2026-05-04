"""Versão didática RUIM: repassa a lista inteira para cada elemento (trabalho repetido)."""

from __future__ import annotations


def sum_even_numbers(values: list[int]) -> tuple[int, int]:
    operations = 0
    total = 0
    for value in values:
        operations += 1
        for candidate in values:
            operations += 1
            if candidate == value and candidate % 2 == 0:
                total += candidate
    return total, operations
