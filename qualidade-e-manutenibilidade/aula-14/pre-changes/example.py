"""Execute: python example.py"""

from __future__ import annotations

import campanha_desconto as campanha


def main() -> None:
    print("--- Sucesso ---")
    print(campanha.calcular_desconto(100.0, "PROMO10", False))
    print(campanha.calcular_desconto(100.0, "PROMO10", True))

    print("\n--- Erros ---")
    for rotulo, fn in (
        ("cupom invalido", lambda: campanha.validar_cupom("XYZ")),
        ("valor invalido", lambda: campanha.calcular_desconto(0, "PROMO10", False)),
    ):
        try:
            fn()
        except ValueError as exc:
            print(rotulo + ":", type(exc).__name__, exc)


if __name__ == "__main__":
    main()
