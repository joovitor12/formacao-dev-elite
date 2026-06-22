"""Smoke test — comportamento atual do baseline."""

from __future__ import annotations

import notificacao_entrega as entrega


def main() -> None:
    ok = entrega.NotificarEntrega(
        {"ambiente": "staging", "canal": "email", "tentativas": 1},
    )
    if not ok.get("success"):
        raise SystemExit("notificação esperada como success")

    ignorado = entrega.NotificarEntrega({"ambiente": "", "canal": None})
    if not ignorado.get("success"):
        raise SystemExit("payload vazio deveria retornar success no baseline")

    print("notificacao_entrega OK — baseline executável")


if __name__ == "__main__":
    main()
