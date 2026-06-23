"""Smoke test — baseline integrado (API legada até refatoração)."""

from __future__ import annotations

import confirmacao_entrega as confirmacao
import fechamento_entrega as fechamento
import notificacao_entrega as notificacao


def main() -> None:
    resultado_notificacao = notificacao.NotificarEntrega(
        {
            "ambiente": "staging",
            "canal": "email",
            "tentativas": 1,
            "token": "demo",
        },
    )
    if not resultado_notificacao.get("success"):
        raise SystemExit("notificacao esperada como success=True")

    resultado_confirmacao = confirmacao.ConfirmarEntrega(
        {"ambiente": "staging", "confirmado": True, "token": "demo"},
    )
    if not resultado_confirmacao.get("success"):
        raise SystemExit("confirmacao esperada como success=True")

    resultado_fechamento = fechamento.fechar_entrega(
        {"ambiente": "staging", "fechado": True},
    )
    if not resultado_fechamento.get("ok"):
        raise SystemExit("fechamento esperado como ok=True")

    print("entrega_integrada OK — smoke test executável (baseline legado)")


if __name__ == "__main__":
    main()
