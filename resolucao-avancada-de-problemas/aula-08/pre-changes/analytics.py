"""
Baseline com custo elevado para revisao de complexidade.
"""

from __future__ import annotations


def summarize_customer_spend(
    customers: list[dict], orders: list[dict]
) -> tuple[list[dict], int]:
    operations = 0
    summary: list[dict] = []

    for customer in customers:
        customer_total = 0.0
        for order in orders:
            operations += 1
            if order["customer_id"] == customer["customer_id"]:
                customer_total += float(order["amount"])

        summary.append(
            {
                "customer_id": customer["customer_id"],
                "name": customer["name"],
                "total_spend": customer_total,
            }
        )

    return summary, operations
