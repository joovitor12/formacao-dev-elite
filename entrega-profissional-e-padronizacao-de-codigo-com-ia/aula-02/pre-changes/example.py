"""Smoke test — comportamento atual do baseline."""

from __future__ import annotations

import confirmacao_entrega as confirmacao


def main() -> None:
    resultado = confirmacao.ConfirmarEntrega(
        {"ambiente": "staging", "confirmado": True, "token": "demo"},
    )
    if not resultado.get("success"):
        raise SystemExit("confirmação esperada como success=True")

    print("confirmacao_entrega OK — baseline executável")


if __name__ == "__main__":
    main()
