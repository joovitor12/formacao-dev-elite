"""Smoke test — contrato ok/avisos após refatoração."""

from __future__ import annotations

import notificacao_entrega as entrega


def main() -> None:
    resultado = entrega.notificar_entrega(
        {"ambiente": "staging", "canal": "email", "tentativas": 1},
    )
    if not resultado.get("ok"):
        raise SystemExit("notificação esperada como ok=True")

    ignorado = entrega.notificar_entrega({"ambiente": "", "canal": None})
    if ignorado.get("ok"):
        raise SystemExit("payload inválido deveria retornar ok=False")
    if not ignorado.get("avisos"):
        raise SystemExit("payload inválido deveria preencher avisos")

    print("notificacao_entrega OK — contrato ok/avisos")


if __name__ == "__main__":
    main()
