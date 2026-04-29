from __future__ import annotations


def build_interactions(
    total_users: int = 120, total_items: int = 80, events_per_user: int = 15
) -> tuple[list[dict], list[dict], list[dict]]:
    users = [{"user_id": uid} for uid in range(1, total_users + 1)]
    items = [{"item_id": iid} for iid in range(1, total_items + 1)]
    interactions: list[dict] = []

    for user in users:
        uid = user["user_id"]
        for i in range(events_per_user):
            item_id = ((uid + i) % total_items) + 1
            interactions.append(
                {
                    "user_id": uid,
                    "item_id": item_id,
                    "score": float((i % 5) + 1),
                }
            )

    return users, items, interactions
