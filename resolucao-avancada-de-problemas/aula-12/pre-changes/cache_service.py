"""
Baseline simples sem cache para discutir trade-offs.
"""

from __future__ import annotations


def _expensive_lookup(key: int) -> int:
    return key * 10


def process_requests_with_cache(requests: list[int]) -> tuple[list[int], int]:
    operations = 0
    response: list[int] = []

    for key in requests:
        operations += 1
        operations += 1
        response.append(_expensive_lookup(key))

    return response, operations
