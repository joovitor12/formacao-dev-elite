from __future__ import annotations

from stats_engine import aggregate_sum_by_group


def test_aggregate_sum_by_group_totals() -> None:
    rows = [
        {"group_id": 1, "value": 10.0},
        {"group_id": 2, "value": 5.0},
        {"group_id": 1, "value": 3.0},
    ]
    totals, _ = aggregate_sum_by_group(rows)
    assert totals[1] == 13.0
    assert totals[2] == 5.0
    assert 3 not in totals


def test_aggregate_sum_by_group_empty() -> None:
    totals, ops = aggregate_sum_by_group([])
    assert totals == {}
    assert ops == 0
