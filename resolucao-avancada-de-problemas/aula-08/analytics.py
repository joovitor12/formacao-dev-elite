"""
Funcoes de agregacao para revisao de complexidade algoritmica.
"""

from __future__ import annotations


def summarize_customer_spend(
    customers: list[dict], orders: list[dict]
) -> tuple[list[dict], int]:
    operations = 0
    # Evita armazenar totais de pedidos para clientes fora do recorte analisado.
    known_customer_ids = {customer["customer_id"] for customer in customers}
    totals_by_customer: dict[int, float] = {}

    for order in orders:
        operations += 1
        customer_id = order["customer_id"]
        if customer_id not in known_customer_ids:
            continue
        totals_by_customer[customer_id] = totals_by_customer.get(customer_id, 0.0) + float(
            order["amount"]
        )

    summary: list[dict] = []
    for customer in customers:
        operations += 1
        cid = customer["customer_id"]
        summary.append(
            {
                "customer_id": cid,
                "name": customer["name"],
                "total_spend": totals_by_customer.get(cid, 0.0),
            }
        )

    return summary, operations
