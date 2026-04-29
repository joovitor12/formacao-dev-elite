from __future__ import annotations

from recommender import recommend_top_items_for_user


def test_recommend_top_items_ranks_by_score_then_item_id() -> None:
    interactions = [
        {"user_id": 1, "item_id": 10, "score": 2.0},
        {"user_id": 1, "item_id": 10, "score": 1.0},
        {"user_id": 1, "item_id": 8, "score": 3.0},
        {"user_id": 1, "item_id": 7, "score": 3.0},
        {"user_id": 2, "item_id": 99, "score": 100.0},
    ]

    recs, _ = recommend_top_items_for_user(1, interactions, top_k=3)
    assert recs == [7, 8, 10]


def test_recommend_top_items_user_without_history_returns_empty() -> None:
    recs, _ = recommend_top_items_for_user(42, [], top_k=5)
    assert recs == []

def test_recommend_user_without_history_in_non_empty_dataset_returns_empty() -> None:
    interactions = [
        {"user_id": 1, "item_id": 10, "score": 2.0},
        {"user_id": 2, "item_id": 20, "score": 3.0},
    ]

    recs, _ = recommend_top_items_for_user(42, interactions, top_k=5)
    assert recs == []
