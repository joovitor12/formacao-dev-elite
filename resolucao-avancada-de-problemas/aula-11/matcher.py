"""
Algoritmo reescrito para match de produtos por tags.
"""

from __future__ import annotations

import heapq


def match_products_by_tags(
    catalog: list[dict], query_tags: list[str], top_k: int = 5
) -> tuple[list[int], int]:
    operations = 0
    query_set = set(query_tags)
    matched_products = 0

    if top_k > 0:
        # Mantem apenas os melhores top_k itens durante a varredura.
        top_matches: list[tuple[int, int]] = []
        for product in catalog:
            operations += 1
            product_tags = set(product["tags"])
            overlap = len(query_set.intersection(product_tags))
            if overlap > 0:
                matched_products += 1
                candidate = (overlap, -product["product_id"])
                if len(top_matches) < top_k:
                    heapq.heappush(top_matches, candidate)
                elif candidate > top_matches[0]:
                    heapq.heapreplace(top_matches, candidate)

        top_matches.sort(key=lambda item: (-item[0], -item[1]))
        result = [-negative_product_id for _overlap, negative_product_id in top_matches]
    else:
        scored: list[tuple[int, int]] = []
        for product in catalog:
            operations += 1
            product_tags = set(product["tags"])
            overlap = len(query_set.intersection(product_tags))
            if overlap > 0:
                matched_products += 1
                scored.append((product["product_id"], overlap))

        scored.sort(key=lambda item: (-item[1], item[0]))
        result = [product_id for product_id, _score in scored[:top_k]]

    operations += matched_products
    return result, operations
