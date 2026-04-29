from __future__ import annotations


def build_data(total_users: int = 150, events_per_user: int = 8) -> tuple[list[dict], list[dict]]:
    users: list[dict] = []
    events: list[dict] = []

    for uid in range(1, total_users + 1):
        users.append({"user_id": uid, "name": f"User {uid}"})
        for i in range(events_per_user):
            events.append(
                {
                    "event_id": f"{uid}-{i}",
                    "user_id": uid,
                    "value": float((i + 1) * 2),
                }
            )

    return users, events
