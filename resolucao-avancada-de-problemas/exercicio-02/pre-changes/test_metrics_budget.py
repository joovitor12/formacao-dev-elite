"""Orçamento: uma única passagem sobre eventos (ajuste se mudar a métrica de contagem)."""

from __future__ import annotations

from dataset import build_events
from metrics import summarize_points_by_user


def test_operations_scale_linearly_with_events() -> None:
    events = build_events(user_count=200, events_per_user=50)
    _totals, operations = summarize_points_by_user(events)

    assert len(events) == 10_000
    assert operations <= len(events) + 50
