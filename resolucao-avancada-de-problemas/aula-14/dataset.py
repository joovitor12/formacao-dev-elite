"""Lista simples para exercícios — sem estruturas elaboradas."""

from __future__ import annotations


def sample_values(size: int = 12) -> list[int]:
    return [i - (size // 3) for i in range(size)]
