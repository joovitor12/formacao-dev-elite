"""Gera listas de eventos reproduzíveis para o exercício."""

from __future__ import annotations


def build_events(user_count: int, events_per_user: int) -> list[dict]:
    events: list[dict] = []
    for user_id in range(1, user_count + 1):
        for i in range(events_per_user):
            events.append({"user_id": user_id, "points": float(i + 1)})
    return events
