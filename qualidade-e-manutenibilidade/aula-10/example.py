"""Execute: python example.py  (ou cd pre-changes && python example.py)"""

from __future__ import annotations

import regras_envio as envio


def main() -> None:
    print("Frete sudeste 3kg:", envio.calcular_frete("sudeste", 3.0))
    print("Frete nordeste 4kg:", envio.calcular_frete("nordeste", 4.0))
    print("Frete sudeste 4kg expresso:", envio.calcular_frete("sudeste", 4.0, expresso=True))


if __name__ == "__main__":
    main()
