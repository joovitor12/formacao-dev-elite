"""
Agregação de pontos por usuário.

Baseline intencionalmente custoso: um passe completo em `events` para cada usuário distinto.
"""

from __future__ import annotations


def summarize_points_by_user(events: list[dict]) -> tuple[dict[int, float], int]:
    operations = 0
    distinct_users = sorted({event["user_id"] for event in events})
    totals: dict[int, float] = {}

    for user_id in distinct_users:
        running = 0.0
        for event in events:
            operations += 1
            if event["user_id"] == user_id:
                running += float(event["points"])
        totals[user_id] = running

    return totals, operations
