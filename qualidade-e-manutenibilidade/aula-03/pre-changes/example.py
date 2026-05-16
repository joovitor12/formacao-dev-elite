"""
Exemplo para rodar antes/depois da refatoração.

Execute: cd pre-changes && python example.py
"""

from __future__ import annotations

from frete_service import TOTAL_FRETES_CALCULADOS, calcular_frete


def main() -> None:
    casos = [
        {
            "regiao": "sudeste",
            "peso_kg": 2.0,
            "altura_cm": 10,
            "largura_cm": 10,
            "profundidade_cm": 10,
        },
        {
            "regiao": "sul",
            "peso_kg": 1.0,
            "altura_cm": 20,
            "largura_cm": 25,
            "profundidade_cm": 40,
            "expresso": True,
        },
    ]
    for i, envio in enumerate(casos, 1):
        print(f"\n--- Caso {i} ---")
        print(calcular_frete(envio))
    print(f"\nTotal fretes calculados (global): {TOTAL_FRETES_CALCULADOS}")


if __name__ == "__main__":
    main()
