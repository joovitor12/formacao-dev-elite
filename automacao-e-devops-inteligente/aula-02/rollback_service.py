"""Serviço de rollback pós-deploy."""

from __future__ import annotations

import logging
import os
from typing import Any

logger = logging.getLogger(__name__)

# Taxa de erro máxima aceitável (5%) antes de disparar rollback automático.
LIMITE_ERRO = 0.05
# Volume mínimo de requisições para evitar rollback por amostra estatística pequena.
MIN_REQUISICOES = 100

_AMBIENTES_VALIDOS = frozenset({"dev", "staging", "prod"})


def _rollback_api_key() -> str | None:
    key = os.environ.get("ROLLBACK_API_KEY", "").strip()
    return key or None


def should_rollback(taxa_erro: float, total_requisicoes: int) -> bool:
    """Decide rollback automático quando a taxa de erro atinge o limite com amostra suficiente."""
    return taxa_erro >= LIMITE_ERRO and total_requisicoes >= MIN_REQUISICOES


def executar_rollback(
    ambiente: str,
    versao_atual: str,
    versao_anterior: str,
    confirmado: bool = False,
) -> dict[str, Any]:
    """Executa rollback manual para a versão anterior informada."""
    amb = str(ambiente or "").strip().lower()
    atual = str(versao_atual or "").strip()
    anterior = str(versao_anterior or "").strip()

    resultado: dict[str, Any] = {"ok": False, "avisos": []}

    if amb not in _AMBIENTES_VALIDOS:
        resultado["avisos"].append("ambiente invalido")
        return resultado
    if not atual:
        resultado["avisos"].append("versao atual obrigatoria")
        return resultado
    if not anterior:
        resultado["avisos"].append("versao anterior obrigatoria")
        return resultado
    if amb == "prod" and not confirmado:
        logger.warning("rollback bloqueado: confirmacao obrigatoria em prod")
        resultado["avisos"].append("confirmacao obrigatoria em prod")
        return resultado
    if amb == "prod" and _rollback_api_key() is None:
        logger.error("rollback bloqueado: ROLLBACK_API_KEY nao configurada")
        resultado["avisos"].append("ROLLBACK_API_KEY nao configurada")
        return resultado

    logger.info("iniciando rollback %s %s -> %s", amb, atual, anterior)

    resultado["ok"] = True
    resultado["ambiente"] = amb
    resultado["versao_atual"] = atual
    resultado["versao_anterior"] = anterior
    resultado["rollback_executado"] = True
    return resultado
