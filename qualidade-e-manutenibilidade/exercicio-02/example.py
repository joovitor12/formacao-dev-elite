"""Execute: python example.py"""

from __future__ import annotations

import fidelidade_service as service
import regras_fidelidade as regras


def main() -> None:
    print("--- Regra pura ---")
    print("pontos (R$100, ouro):", regras.pontos_por_compra(100.0, "ouro"))
    print("custo COPO:", regras.custo_premio("COPO"))

    print("\n--- Orquestracao (exige mock em teste) ---")
    try:
        print(service.acumular_compra("C-1", 100.0, "prata"))
    except RuntimeError as exc:
        print(type(exc).__name__ + ":", exc)


if __name__ == "__main__":
    main()
