"""Execute: python example.py"""

from __future__ import annotations

import regras_resgate as resgate


def main() -> None:
    print("--- Sucesso ---")
    print(resgate.processar_resgate("DESC10", 120))
    print("\n--- Erro (retorno) ---")
    print(resgate.processar_resgate("VIP", 100))
    print("\n--- Erro (exceção) ---")
    try:
        resgate.custo_resgate("")
    except ValueError as exc:
        print(type(exc).__name__, exc)


if __name__ == "__main__":
    main()
