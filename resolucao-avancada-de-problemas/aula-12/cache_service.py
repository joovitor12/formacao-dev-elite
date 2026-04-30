"""
Servico simples para discutir trade-offs de estrategia de cache.
"""

from __future__ import annotations

_CACHE_MISS = object()


def _expensive_lookup(key: int) -> int:
    # Simula custo de calculo/IO.
    return key * 10


def process_requests_with_cache(requests: list[int]) -> tuple[list[int], int]:
    operations = 0
    cache: dict[int, int] = {}
    response: list[int] = []

    for key in requests:
        operations += 1
        cached_value = cache.get(key, _CACHE_MISS)
        if cached_value is not _CACHE_MISS:
            response.append(cached_value)
            continue

        # Trade-off principal: guardamos todas as chaves unicas da execucao
        # para evitar recomputo caro em repeticoes (mais velocidade, mais memoria).
        operations += 1
        value = _expensive_lookup(key)
        cache[key] = value
        response.append(value)

    return response, operations
