"""Execute: python example.py  (ou cd pre-changes && python example.py)"""

from __future__ import annotations

import pedido_flow as pedido


def main() -> None:
    print("--- Pedido com cupom e taxa ---")
    print(
        pedido.processar_pedido(
            {
                "cliente_id": "CLI-DEMO",
                "cupom": "DESC10",
                "itens": [{"sku": "KIT-1", "qtd": 1, "preco": 80.0}],
            }
        )
    )
    print("\n--- Pedido inválido ---")
    print(pedido.processar_pedido({"cliente_id": "", "itens": []}))
    print(f"\nPedidos gravados: {len(pedido.listar_pedidos())}")


if __name__ == "__main__":
    main()
