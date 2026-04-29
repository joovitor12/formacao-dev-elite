"""
Recomendacao simples para exercicio de sugestoes algoritmicas com IA.
"""

from __future__ import annotations

import heapq


def recommend_top_items_for_user(
    target_user_id: int,
    interactions: list[dict],
    top_k: int = 5,
) -> tuple[list[int], int]:
    operations = 0
    scores_by_item: dict[int, float] = {}

    for interaction in interactions:
        operations += 1
        if interaction["user_id"] != target_user_id:
            continue
        item_id = interaction["item_id"]
        scores_by_item[item_id] = scores_by_item.get(item_id, 0.0) + float(
            interaction["score"]
        )

    if top_k <= 0 or not scores_by_item:
        return [], operations

    heap: list[tuple[float, int, int]] = []
    for item_id, score in scores_by_item.items():
        operations += 1
        # Heap key keeps the "worst among current best" at index 0.
        # Better candidates have higher score, and for ties smaller item_id.
        entry = (score, -item_id, item_id)
        if len(heap) < top_k:
            heapq.heappush(heap, entry)
            continue
        if entry > heap[0]:
            heapq.heapreplace(heap, entry)

    ranked_top_k = sorted(heap, key=lambda entry: (-entry[0], entry[2]))
    result = [item_id for _score, _neg_item_id, item_id in ranked_top_k]
    return result, operations
