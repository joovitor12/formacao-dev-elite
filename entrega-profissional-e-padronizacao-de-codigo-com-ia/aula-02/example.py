"""Smoke test — comportamento atual do baseline."""

from __future__ import annotations

import confirmacao_entrega as confirmacao


def main() -> None:
    resultado = confirmacao.confirmar_entrega(
        {"ambiente": "staging", "confirmado": True, "token": "demo"},
    )
    if not resultado.get("ok"):
        raise SystemExit("confirmação esperada como ok=True")

    print("confirmacao_entrega OK — baseline executável")


if __name__ == "__main__":
    main()
