from __future__ import annotations

from dataset import build_data
from pipeline import build_user_value_report


def test_pipeline_operations_budget_is_near_linear() -> None:
    users, events = build_data(total_users=250, events_per_user=8)
    _, operations = build_user_value_report(users, events)

    upper_bound = len(users) + len(events) + 80
    assert operations <= upper_bound
