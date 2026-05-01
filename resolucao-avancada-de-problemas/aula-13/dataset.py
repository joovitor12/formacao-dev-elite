"""Gera cargas de trabalho reproduzíveis para benchmark."""

from __future__ import annotations


def build_observations(row_count: int, group_count: int = 80) -> list[dict]:
    rows: list[dict] = []
    for i in range(row_count):
        group_id = (i % group_count) + 1
        rows.append({"group_id": group_id, "value": float((i * 13 + 7) % 100)})
    return rows
