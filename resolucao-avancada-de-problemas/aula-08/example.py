from __future__ import annotations

from analytics import summarize_customer_spend
from dataset import build_sample_data


def main() -> None:
    customers, orders = build_sample_data(total_customers=5, orders_per_customer=3)
    summary, operations = summarize_customer_spend(customers, orders)

    print("Resumo (3 primeiros clientes):")
    for row in summary[:3]:
        print(row)

    print(f"\nOperacoes contadas: {operations}")
    print(f"Clientes: {len(customers)} | Pedidos: {len(orders)}")


if __name__ == "__main__":
    main()
