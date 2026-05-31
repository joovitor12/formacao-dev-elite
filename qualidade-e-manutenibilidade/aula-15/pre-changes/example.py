"""Execute: python example.py"""

from __future__ import annotations

import politica_reembolso as politica


def main() -> None:
    print("--- Sucesso integral (premium, 2 dias) ---")
    print(politica.calcular_reembolso(150.0, "premium", 2))

    print("\n--- Meio prazo (50%) ---")
    print(politica.calcular_reembolso(100.0, "padrao", 5))

    print("\n--- Prazo expirado (retorno, nao excecao) ---")
    print(politica.calcular_reembolso(100.0, "padrao", 999))


if __name__ == "__main__":
    main()
