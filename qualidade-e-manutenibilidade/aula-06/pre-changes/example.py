"""Execute: cd pre-changes && python example.py"""

from __future__ import annotations

import comissao_baseline as baseline
import comissao_service as service
from casos_equivalencia import CASOS


def main() -> None:
    caso = CASOS[3]
    entrada = caso["entrada"]
    print("Caso:", caso["id"])
    print("Entrada:", entrada)
    print("Baseline:", baseline.calcular_comissao(entrada))
    print("Service: ", service.calcular_comissao(entrada))
    print("Equivalente:", service.calcular_comissao(entrada) == baseline.calcular_comissao(entrada))


if __name__ == "__main__":
    main()
