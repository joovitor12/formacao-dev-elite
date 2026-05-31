"""Execute: python example.py"""

from __future__ import annotations

import ativacao_service as service
import regras_tier as tier


def main() -> None:
    print("--- Regra pura ---")
    print("creditos ouro:", tier.creditos_por_tier("ouro"))

    print("\n--- Orquestracao (exige mock em teste) ---")
    try:
        print(service.ativar_tier("C-1", "prata"))
    except RuntimeError as exc:
        print(type(exc).__name__ + ":", exc)


if __name__ == "__main__":
    main()
