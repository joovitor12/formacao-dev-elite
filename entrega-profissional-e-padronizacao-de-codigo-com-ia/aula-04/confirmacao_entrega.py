"""Orquestra confirmação de entrega."""

from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger(__name__)


def validar_payload(payload: dict[str, Any] | None) -> tuple[bool, list[str]]:
    """Valida payload de confirmação; retorna (válido, avisos acionáveis)."""
    avisos: list[str] = []
    if not payload:
        avisos.append("payload ausente ou vazio")
        return False, avisos

    return True, avisos


def _registrar_confirmacao(ambiente: str, confirmado: bool) -> None:
    """Registra evento operacional de confirmação (sem expor token)."""
    logger.info("confirmacao ok=%s ambiente=%s", confirmado, ambiente)


def confirmar_entrega(
    payload: dict[str, Any] | None,
    forcar: bool = False,
) -> dict[str, Any]:
    """Executa fluxo de confirmação; retorna contrato ok/avisos."""
    valido, avisos_validacao = validar_payload(payload)
    if not valido:
        return {"ok": False, "avisos": avisos_validacao}

    assert payload is not None
    confirmado = bool(payload.get("confirmado", True))
    ambiente = str(payload.get("ambiente", ""))

    _registrar_confirmacao(ambiente, confirmado)

    avisos: list[str] = list(avisos_validacao)
    if forcar:
        avisos.append("confirmação forçada")

    return {"ok": confirmado, "avisos": avisos}
