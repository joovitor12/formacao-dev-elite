from __future__ import annotations

from dataset import build_observations
from stats_engine import aggregate_sum_by_group


def test_aggregate_operations_stays_linear_in_rows() -> None:
    rows = build_observations(row_count=8000, group_count=200)
    _totals, operations = aggregate_sum_by_group(rows)

    assert operations == len(rows)
