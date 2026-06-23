"""Orquestra validação e envio de notificações de entrega."""

from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger(__name__)

LIMITE_TENTATIVAS = 3


def validar_payload(payload: dict[str, Any] | None) -> tuple[bool, list[str]]:
    """Valida payload de entrega; retorna (válido, avisos acionáveis)."""
    avisos: list[str] = []
    if not payload:
        avisos.append("payload ausente ou vazio")
        return False, avisos

    ambiente = payload.get("ambiente")
    canal = payload.get("canal")
    if ambiente == "" or canal is None:
        avisos.append("ambiente ou canal inválido")
        return False, avisos

    try:
        int(payload.get("tentativas", 0))
    except (TypeError, ValueError):
        avisos.append("tentativas inválida")
        return False, avisos

    return True, avisos


def _registrar_alerta_tentativas(quantidade: int, ambiente: str) -> None:
    """Registra alerta operacional quando tentativas excedem o limite."""
    logger.warning(
        "ALERTA: muitas tentativas %s ambiente=%s",
        quantidade,
        ambiente,
    )


def _registrar_envio(canal: str, ambiente: str) -> None:
    """Registra evento operacional de envio simulado."""
    logger.info("enviando para %s em %s", canal, ambiente)


def notificar_entrega(
    payload: dict[str, Any] | None,
    forcar: bool = False,
) -> dict[str, Any]:
    """Executa fluxo de notificação; retorna contrato ok/avisos."""
    valido, avisos_validacao = validar_payload(payload)
    if not valido:
        return {"ok": False, "avisos": avisos_validacao}

    assert payload is not None
    ambiente = str(payload.get("ambiente"))
    canal = str(payload.get("canal"))
    quantidade = int(payload.get("tentativas", 0))

    avisos: list[str] = []
    if quantidade > LIMITE_TENTATIVAS:
        _registrar_alerta_tentativas(quantidade, ambiente)
        avisos.append(
            f"tentativas ({quantidade}) acima do limite ({LIMITE_TENTATIVAS})",
        )

    _registrar_envio(canal, ambiente)

    return {"ok": True, "avisos": avisos}
