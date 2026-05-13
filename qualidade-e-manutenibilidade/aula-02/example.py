"""
Exemplo pratico para rodar no terminal e alimentar o chat.

Execute: python example.py
"""

from __future__ import annotations

from checkout_service import CAIXA_TOTAL, ESTOQUE, fechar_compra


def main() -> None:
    print("Estoque inicial:", dict(ESTOQUE))
    print("Caixa inicial:", CAIXA_TOTAL)

    payload_ok = {
        "cliente_id": "VIP-001",
        "segmento": "gold",
        "cupom": "PROMO10",
        "prioridade": 8,
        "itens": [
            {"sku": "A1", "qtd": 1, "preco": 120.0},
            {"sku": "B2", "qtd": 1, "preco": 80.0},
        ],
    }
    print("\n--- Compra valida ---")
    print(fechar_compra(payload_ok, modo_teste=True))

    payload_com_problemas = {
        "cliente_id": "CLI-123",
        "segmento": "regular",
        "cupom": "PROMO20",
        "itens": [
            {"sku": "C3", "qtd": 2, "preco": 50.0},  # sem estoque
            {"sku": "X9", "qtd": 1, "preco": 10.0},  # sku desconhecido
        ],
    }
    print("\n--- Compra com problemas ---")
    print(fechar_compra(payload_com_problemas, modo_teste=True))


if __name__ == "__main__":
    main()
