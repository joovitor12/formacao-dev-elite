from __future__ import annotations

from dataset import build_data
from pipeline import build_user_value_report


def test_pipeline_operations_budget_is_near_linear() -> None:
    users, events = build_data(total_users=250, events_per_user=8)
    _, operations = build_user_value_report(users, events)

    upper_bound = len(users) + len(events) + 80
    assert operations <= upper_bound


def test_pipeline_operations_scale_linearly_with_input_growth() -> None:
    users_small, events_small = build_data(total_users=200, events_per_user=8)
    users_large, events_large = build_data(total_users=400, events_per_user=8)

    _, operations_small = build_user_value_report(users_small, events_small)
    _, operations_large = build_user_value_report(users_large, events_large)

    # With same events_per_user, doubling users doubles events and total operations.
    assert operations_large == operations_small * 2
