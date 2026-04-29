from __future__ import annotations

from dataset import build_interactions
from recommender import recommend_top_items_for_user


def test_recommend_budget_scales_with_interactions() -> None:
    _users, _items, interactions = build_interactions(
        total_users=400, total_items=300, events_per_user=20
    )
    recs, operations = recommend_top_items_for_user(250, interactions, top_k=10)

    assert len(recs) <= 10
    # For this synthetic dataset, each user has at most 20 interacted items.
    # The budget should remain close to a single pass over interactions.
    assert operations <= len(interactions) + 30


def test_recommend_budget_growth_is_near_linear() -> None:
    _users, _items, small_interactions = build_interactions(
        total_users=200, total_items=300, events_per_user=20
    )
    _users, _items, large_interactions = build_interactions(
        total_users=400, total_items=300, events_per_user=20
    )

    _recs_small, ops_small = recommend_top_items_for_user(
        150, small_interactions, top_k=10
    )
    _recs_large, ops_large = recommend_top_items_for_user(
        250, large_interactions, top_k=10
    )

    # Doubling interactions should keep operations approximately doubled.
    # A small additive slack avoids false positives from constant factors.
    assert ops_large <= (ops_small * 2) + 30
