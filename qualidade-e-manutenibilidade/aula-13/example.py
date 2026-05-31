"""Execute: python example.py"""

from __future__ import annotations

import regras_catalogo as catalogo
import resgate_service as service


def main() -> None:
    print("--- Regra pura (sem mock) ---")
    print("custo DESC10:", catalogo.custo_resgate("DESC10"))

    print("\n--- Orquestracao (exige mock em teste) ---")
    try:
        print(service.executar_resgate("C-100", "DESC10"))
    except RuntimeError as exc:
        print(type(exc).__name__ + ":", exc)


if __name__ == "__main__":
    main()
