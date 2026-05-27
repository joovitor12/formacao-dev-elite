"""Execute: python example.py"""

from __future__ import annotations

import fulfillment_flow as flow


def main() -> None:
    flow.reset_estado()
    print("--- Varejo simples ---")
    print(
        flow.processar_fulfillment(
            {
                "cliente_id": "DEMO-1",
                "canal": "varejo",
                "itens": [{"sku": "SKU-A", "qtd": 2, "preco_unit": 30.0}],
            }
        )
    )
    flow.reset_estado()
    print("\n--- Marketplace com taxa ---")
    print(
        flow.processar_fulfillment(
            {
                "cliente_id": "DEMO-2",
                "canal": "marketplace",
                "itens": [{"sku": "SKU-B", "qtd": 1, "preco_unit": 100.0}],
            }
        )
    )
    print(f"\nFulfillments gravados: {len(flow.listar_fulfillments())}")


if __name__ == "__main__":
    main()
