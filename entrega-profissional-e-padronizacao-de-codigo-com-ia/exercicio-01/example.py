"""Smoke test — módulos do pipeline de entrega integrada."""

from __future__ import annotations

import confirmacao_entrega as confirmacao
import fechamento_entrega as fechamento
import notificacao_entrega as notificacao


def main() -> None:
    resultado_notificacao = notificacao.notificar_entrega(
        {
            "ambiente": "staging",
            "canal": "email",
            "tentativas": 1,
        },
    )
    if not resultado_notificacao.get("ok"):
        raise SystemExit("notificacao_entrega esperada como ok=True")

    resultado_confirmacao = confirmacao.confirmar_entrega(
        {"ambiente": "staging", "confirmado": True},
    )
    if not resultado_confirmacao.get("ok"):
        raise SystemExit("confirmacao_entrega esperada como ok=True")

    resultado_fechamento = fechamento.fechar_entrega(
        {"ambiente": "staging", "fechado": True},
    )
    if not resultado_fechamento.get("ok"):
        raise SystemExit("fechamento_entrega esperado como ok=True")

    print("entrega_integrada OK — smoke test dos três módulos")


if __name__ == "__main__":
    main()
