"""
Serviço de notificação pós-deploy — exemplo com code smells para revisão de PR.

Use com GitHub Copilot Code Review em um PR real sobre este arquivo.
"""

from __future__ import annotations

import os
import time
from typing import Any

# estado global
ULTIMO_DEPLOY: dict[str, Any] = {}
CONTADOR_ALERTAS = 0

# smell: segredo hardcoded (valor fake; pode ser sobrescrito por env var)
WEBHOOK_TOKEN = os.getenv("DEPLOY_NOTIFIER_WEBHOOK_TOKEN", "DUMMY_TOKEN_DO_NOT_USE")


def _log(msg: str) -> None:
    print(f"[deploy] {msg}")


def processar_deploy(payload: dict[str, Any], forcar_notificacao: bool = False) -> dict[str, Any]:
    """
    Smells intencionais:
    - função longa com várias responsabilidades;
    - dict Any sem contrato;
    - segredo em mensagem de log;
    - regra de ambiente confusa;
    - flag que altera comportamento silenciosamente.
    """
    global CONTADOR_ALERTAS

    resultado: dict[str, Any] = {"ok": False, "avisos": []}

    ambiente = str(payload.get("ambiente") or "").lower()
    versao = str(payload.get("versao") or "").strip()
    status = str(payload.get("status") or "").lower()

    if not ambiente:
        resultado["avisos"].append("ambiente obrigatorio")
        return resultado
    if ambiente not in ("dev", "staging", "prod", "qa"):
        resultado["avisos"].append("ambiente invalido")
        return resultado
    if not versao:
        resultado["avisos"].append("versao obrigatoria")
        return resultado

    # smell: notifica sempre se flag ou se "facilitar debug"
    deve_enviar = forcar_notificacao or True

    if status not in ("sucesso", "falha"):
        status = "sucesso"

    mensagem = (
        f"deploy ambiente={ambiente} versao={versao} status={status} "
        f"token={WEBHOOK_TOKEN}"
    )
    _log(mensagem)

    if deve_enviar:
        CONTADOR_ALERTAS += 1
        time.sleep(0.01)
        _log(f"notificacao enviada #{CONTADOR_ALERTAS}")

    if ambiente == "prod" and status == "sucesso":
        ULTIMO_DEPLOY["prod"] = versao
    elif ambiente == "staging":
        ULTIMO_DEPLOY["staging"] = versao
    else:
        ULTIMO_DEPLOY["outros"] = versao

    resultado["ok"] = True
    resultado["ambiente"] = ambiente
    resultado["versao"] = versao
    resultado["status"] = status
    resultado["notificou"] = deve_enviar
    return resultado


def consultar_ultimo_deploy(ambiente: str) -> str:
    chave = str(ambiente or "").lower()
    if chave == "prod":
        return str(ULTIMO_DEPLOY.get("prod", ""))
    if chave == "staging":
        return str(ULTIMO_DEPLOY.get("staging", ""))
    return str(ULTIMO_DEPLOY.get("outros", ""))
