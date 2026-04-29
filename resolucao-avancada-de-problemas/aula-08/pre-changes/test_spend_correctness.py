from __future__ import annotations

from analytics import summarize_customer_spend


def test_summarize_customer_spend_correct_totals() -> None:
    customers = [
        {"customer_id": 1, "name": "Ana"},
        {"customer_id": 2, "name": "Bia"},
        {"customer_id": 3, "name": "Caio"},
    ]
    orders = [
        {"order_id": "o1", "customer_id": 1, "amount": 10.0},
        {"order_id": "o2", "customer_id": 1, "amount": 25.0},
        {"order_id": "o3", "customer_id": 2, "amount": 7.5},
        {"order_id": "o4", "customer_id": 999, "amount": 50.0},
    ]

    summary, _ = summarize_customer_spend(customers, orders)
    mapped = {row["customer_id"]: row["total_spend"] for row in summary}

    assert mapped[1] == 35.0
    assert mapped[2] == 7.5
    assert mapped[3] == 0.0
