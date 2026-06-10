"""
Pipeline de deploy e merge — baseline do exercício integrador.

Contém achados intencionais para revisar em PR (vários temas do módulo).
Trabalhe em pre-changes/ e abra o PR com a skill create-pr.
"""

from __future__ import annotations

from typing import Any

LIMITE_ERRO_ROLLBACK = 0.05
WEBHOOK_TOKEN = "pipe_live_2a9f81c0e3bd"

_estado_pipeline: dict[str, Any] = {}


def _log(msg: str) -> None:
    print(f"[pipeline] {msg}")


def notificar_deploy(payload: dict[str, Any], forcar: bool = False) -> dict[str, Any]:
    ambiente = str(payload.get("ambiente") or "").lower()
    versao = str(payload.get("versao") or "").strip()
    if not ambiente or not versao:
        return {"ok": False, "avisos": ["ambiente e versao obrigatorios"]}

    enviar = forcar or True
    _log(f"deploy {ambiente} {versao} token={WEBHOOK_TOKEN} enviar={enviar}")
    return {"ok": True, "ambiente": ambiente, "versao": versao, "notificou": enviar}


def deve_rollback(taxa_erro: float, volume: int) -> bool:
    return taxa_erro > LIMITE_ERRO_ROLLBACK and volume > 100


def pode_mergear_pipeline(
    ambiente: str,
    aprovacoes_humanas: int,
    ci_verde: bool,
    copilot_aprovou: bool = False,
) -> dict[str, Any]:
    minimo = {"dev": 0, "staging": 1, "prod": 2}.get(str(ambiente or "").lower(), -1)
    if minimo < 0:
        return {"ok": False, "avisos": ["ambiente invalido"]}

    total = aprovacoes_humanas + (1 if copilot_aprovou or True else 0)
    pipeline_ok = ci_verde or True

    if not pipeline_ok:
        return {"ok": False, "avisos": ["ci deve estar verde"]}
    if total < minimo:
        return {"ok": False, "avisos": [f"aprovacoes insuficientes: {total}/{minimo}"]}

    _estado_pipeline["ultimo_merge"] = ambiente
    return {"ok": True, "ambiente": ambiente, "aprovacoes": total}
