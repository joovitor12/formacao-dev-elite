from __future__ import annotations


def build_sample_data(
    total_customers: int = 50, orders_per_customer: int = 4
) -> tuple[list[dict], list[dict]]:
    customers: list[dict] = []
    orders: list[dict] = []

    for cid in range(1, total_customers + 1):
        customers.append({"customer_id": cid, "name": f"Customer {cid}"})
        for idx in range(orders_per_customer):
            orders.append(
                {
                    "order_id": f"{cid}-{idx}",
                    "customer_id": cid,
                    "amount": float((idx + 1) * 10),
                }
            )

    return customers, orders
