"""Execute: python example.py"""

from __future__ import annotations

import canary_deploy as canary


def main() -> None:
    out = canary.iniciar_canary(
        "pagamentos-api",
        "4.2.0",
        percentual=10,
        email_cliente="cliente@exemplo.com",
    )
    print(out)
    print("ativo:", canary.canary_esta_ativo("pagamentos-api"))
    print("abortar 0.05:", canary.abortar_se_erro_alto(0.05))
    print("abortar 0.06:", canary.abortar_se_erro_alto(0.06))


if __name__ == "__main__":
    main()
