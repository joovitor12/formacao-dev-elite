from __future__ import annotations

from dataset import build_interactions
from recommender import recommend_top_items_for_user


def main() -> None:
    _users, _items, interactions = build_interactions(
        total_users=10, total_items=12, events_per_user=8
    )
    recs, operations = recommend_top_items_for_user(3, interactions, top_k=5)
    print("Top items para user 3:", recs)
    print("Operacoes:", operations)


if __name__ == "__main__":
    main()
