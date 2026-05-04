from __future__ import annotations

from metrics import summarize_points_by_user


def test_totals_match_simple_manual_sum() -> None:
    events = [
        {"user_id": 1, "points": 10.0},
        {"user_id": 2, "points": 5.0},
        {"user_id": 1, "points": 3.0},
    ]
    totals, _ = summarize_points_by_user(events)
    assert totals[1] == 13.0
    assert totals[2] == 5.0


def test_empty_events_yields_empty_totals() -> None:
    totals, ops = summarize_points_by_user([])
    assert totals == {}
    assert ops == 0
