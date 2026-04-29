from __future__ import annotations

from dataset import build_interactions
from recommender import recommend_top_items_for_user


def test_recommend_budget_scales_with_interactions() -> None:
    _users, _items, interactions = build_interactions(
        total_users=400, total_items=300, events_per_user=20
    )
    recs, operations = recommend_top_items_for_user(250, interactions, top_k=10)

    assert len(recs) <= 10
    assert operations <= len(interactions) + 200
