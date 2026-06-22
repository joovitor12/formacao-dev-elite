"""Smoke test — comportamento atual do baseline."""

from __future__ import annotations

import fechamento_entrega as fechamento


def main() -> None:
    resultado = fechamento.fechar_entrega(
        {"ambiente": "staging", "fechado": True, "token": "demo"},
    )
    if not resultado.get("ok"):
        raise SystemExit("fechamento esperado como ok=True")

    print("fechamento_entrega OK — baseline executável")


if __name__ == "__main__":
    main()
