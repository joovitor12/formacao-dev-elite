from __future__ import annotations

from analytics import summarize_customer_spend
from dataset import build_sample_data


def test_operations_budget_scales_near_linear() -> None:
    customers, orders = build_sample_data(total_customers=200, orders_per_customer=10)
    _, operations = summarize_customer_spend(customers, orders)

    # Budget simples para proteger contra retorno acidental a loop aninhado.
    upper_bound = len(customers) + len(orders) + 50
    assert operations <= upper_bound
