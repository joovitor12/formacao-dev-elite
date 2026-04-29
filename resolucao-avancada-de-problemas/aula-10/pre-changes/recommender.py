"""
Baseline com estrategia ineficiente para sugestoes algoritmicas.
"""

from __future__ import annotations


def recommend_top_items_for_user(
    target_user_id: int,
    interactions: list[dict],
    top_k: int = 5,
) -> tuple[list[int], int]:
    operations = 0
    scores_by_item: dict[int, float] = {}

    # Primeiro coleta itens do usuario alvo.
    target_items: list[int] = []
    for interaction in interactions:
        operations += 1
        if interaction["user_id"] == target_user_id:
            target_items.append(interaction["item_id"])

    # Depois recalcula score por item percorrendo tudo de novo para cada item.
    unique_items = list(set(target_items))
    for item_id in unique_items:
        total = 0.0
        for interaction in interactions:
            operations += 1
            if (
                interaction["user_id"] == target_user_id
                and interaction["item_id"] == item_id
            ):
                total += float(interaction["score"])
        scores_by_item[item_id] = total

    ranked = sorted(scores_by_item.items(), key=lambda pair: (-pair[1], pair[0]))
    return [item_id for item_id, _score in ranked[:top_k]], operations
