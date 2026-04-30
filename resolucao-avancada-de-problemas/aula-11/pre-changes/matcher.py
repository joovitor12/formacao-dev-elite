"""
Baseline antigo com algoritmo menos eficiente.
"""

from __future__ import annotations


def match_products_by_tags(
    catalog: list[dict], query_tags: list[str], top_k: int = 5
) -> tuple[list[int], int]:
    operations = 0
    scored: list[tuple[int, int]] = []

    for product in catalog:
        overlap = 0
        for query_tag in query_tags:
            for product_tag in product["tags"]:
                operations += 1
                if query_tag == product_tag:
                    overlap += 1

        if overlap > 0:
            scored.append((product["product_id"], overlap))

    scored.sort(key=lambda item: (-item[1], item[0]))
    return [product_id for product_id, _score in scored[:top_k]], operations
