from __future__ import annotations

from pipeline import build_user_value_report


def test_report_aggregates_values_per_user() -> None:
    users = [{"user_id": 1, "name": "Ana"}, {"user_id": 2, "name": "Bia"}]
    events = [
        {"event_id": "e1", "user_id": 1, "value": 10.0},
        {"event_id": "e2", "user_id": 1, "value": 15.0},
        {"event_id": "e3", "user_id": 2, "value": 5.0},
        {"event_id": "e4", "user_id": 999, "value": 100.0},
    ]

    report, _ = build_user_value_report(users, events)
    mapped = {row["user_id"]: row["total_value"] for row in report}
    assert mapped[1] == 25.0
    assert mapped[2] == 5.0


def test_report_preserves_users_without_events() -> None:
    users = [{"user_id": 1, "name": "Ana"}, {"user_id": 2, "name": "Bia"}]
    report, _ = build_user_value_report(users, [])
    mapped = {row["user_id"]: row["total_value"] for row in report}
    assert mapped[1] == 0.0
    assert mapped[2] == 0.0
