"""
Baseline com gargalo de loop aninhado.
"""

from __future__ import annotations


def build_user_value_report(users: list[dict], events: list[dict]) -> tuple[list[dict], int]:
    operations = 0
    report: list[dict] = []

    for user in users:
        total_value = 0.0
        for event in events:
            operations += 1
            if event["user_id"] == user["user_id"]:
                total_value += float(event["value"])

        report.append(
            {
                "user_id": user["user_id"],
                "name": user["name"],
                "total_value": total_value,
            }
        )

    return report, operations
