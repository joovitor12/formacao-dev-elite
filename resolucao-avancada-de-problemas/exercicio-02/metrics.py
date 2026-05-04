"""
Agregação de pontos por usuário.

Baseline intencionalmente custoso: um passe completo em `events` para cada usuário distinto.
"""

from __future__ import annotations


def summarize_points_by_user(events: list[dict]) -> tuple[dict[int, float], int]:
    operations = 0
    totals: dict[int, float] = {}

    for event in events:
        operations += 1
        user_id = event["user_id"]
        totals[user_id] = totals.get(user_id, 0.0) + float(event["points"])

    return totals, operations
