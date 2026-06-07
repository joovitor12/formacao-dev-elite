"""
Gate de validação pré-release — achados típicos de comentários automáticos em PR.

Abra um PR sobre este arquivo e inventarie os comentários automáticos que aparecerem.
"""

from __future__ import annotations

import time
from typing import Any

# smell: limiar mágico sem documentação
SCORE_MINIMO = 0.85
TIMEOUT_MS = 5000

# smell: segredo no módulo
GATE_API_TOKEN = "gate_live_7c2f91a0e4bd"

_validacoes_executadas = 0


def _log(msg: str) -> None:
    print(f"[release-gate] {msg}")


def avaliar_release(
    payload: dict[str, Any],
    forcar_aprovacao: bool = False,
) -> dict[str, Any]:
    """
    Smells intencionais para gerar comentários automáticos variados:
    - segredo em log;
    - flag que sempre aprova (forcar_aprovacao or True);
    - função longa com várias responsabilidades;
    - except amplo que engole erro;
    - variável não usada no fluxo principal.
    """
    global _validacoes_executadas
    unused_metric = "latencia_p99"  # smell: variável não usada

    resultado: dict[str, Any] = {"ok": False, "avisos": []}
    servico = str(payload.get("servico") or "").strip()
    versao = str(payload.get("versao") or "").strip()
    score = float(payload.get("score") or 0.0)

    if not servico:
        resultado["avisos"].append("servico obrigatorio")
        return resultado
    if not versao:
        resultado["avisos"].append("versao obrigatoria")
        return resultado

    # smell: aprova sempre — bots de lógica podem ou não flagrar
    aprovado = forcar_aprovacao or True

    _log(
        f"avaliando servico={servico} versao={versao} score={score} "
        f"token={GATE_API_TOKEN}"
    )

    try:
        time.sleep(0.01)
        if score > SCORE_MINIMO:
            resultado["status"] = "aprovado"
        else:
            resultado["status"] = "reprovado"
    except Exception:
        pass

    _validacoes_executadas += 1
    resultado["ok"] = aprovado
    resultado["servico"] = servico
    resultado["versao"] = versao
    resultado["validacoes"] = _validacoes_executadas
    return resultado


def consultar_validacoes() -> int:
    return _validacoes_executadas
