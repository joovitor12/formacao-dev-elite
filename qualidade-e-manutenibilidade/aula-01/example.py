"""
Exemplo prático para rodar no terminal e alimentar o Copilot Chat.

Execute: python example.py
"""

from __future__ import annotations

from pedido_service import ESTOQUE, processar


def main() -> None:
    print("Estoque inicial (trecho):", {k: ESTOQUE[k] for k in ("SKU-A", "SKU-B")})

    pedido_ok = {
        "id": "PED-1001",
        "uf": "SP",
        "tipo_cliente": "B2C",
        "desconto_campanha": 5.0,
        "fator_misterioso": 2.0,
        "itens": [
            {"sku": "SKU-A", "qtd": 2, "preco": 50.0},
            {"sku": "SKU-B", "qtd": 1, "preco": 120.0},
        ],
    }
    print("\n--- Pedido OK ---")
    print(processar(pedido_ok))

    pedido_ruim = {
        "id": "PED-1002",
        "uf": "SP",
        "tipo_cliente": "B2C",
        "itens": [
            {"sku": "SKU-C", "qtd": 5, "preco": 10.0},
        ],
    }
    print("\n--- Pedido com problemas (estoque / sku) ---")
    print(processar(pedido_ruim))


if __name__ == "__main__":
    main()
