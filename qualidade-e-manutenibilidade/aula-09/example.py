"""Execute: python example.py  (ou cd pre-changes && python example.py)"""

from __future__ import annotations

import regras_pontos as regras
import fidelidade_service as fidelidade


def main() -> None:
    print("--- Regras puras (candidatas a unitário) ---")
    print("pontos R$ 59,99:", regras.pontos_por_valor(59.99))
    print("bonus ouro sobre 10:", regras.bonus_por_tier("ouro", 10))

    fidelidade.reset_estado()
    print("\n--- Serviço (orquestração + estado) ---")
    print(fidelidade.registrar_compra("DEMO", 100.0, "ouro"))
    print("saldo:", fidelidade.consultar_saldo("DEMO"))


if __name__ == "__main__":
    main()
