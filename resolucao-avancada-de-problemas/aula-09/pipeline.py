"""
Pipeline de agregacao para estudo de identificacao de gargalos.
"""

from __future__ import annotations

def build_user_value_report(users: list[dict], events: list[dict]) -> tuple[list[dict], int]:
    operations = 0
    totals_by_user: dict[int, float] = {}

    for event in events:
        operations += 1
        uid = event["user_id"]
        totals_by_user[uid] = totals_by_user.get(uid, 0.0) + float(event["value"])

    report: list[dict] = []
    for user in users:
        operations += 1
        uid = user["user_id"]
        report.append(
            {
                "user_id": uid,
                "name": user["name"],
                "total_value": totals_by_user.get(uid, 0.0),
            }
        )

    return report, operations
