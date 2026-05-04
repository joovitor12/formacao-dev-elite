"""Soma dos valores pares — versão direta (uma passada na lista)."""

from __future__ import annotations


def sum_even_numbers(values: list[int]) -> tuple[int, int]:
    """Retorna (soma_dos_pares, operações_contadas)."""
    operations = 0
    total = 0
    for value in values:
        operations += 1
        if value % 2 == 0:
            total += value
    return total, operations
