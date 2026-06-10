"""
Gate de validação pré-release — baseline para abrir PR.

Mantenha este arquivo na branch principal. Crie outra branch e aplique as
mudanças sugeridas no prompts.md (seção 2) para gerar o diff do exercício.
"""

from __future__ import annotations

from typing import Any

SCORE_MINIMO = 0.85


def avaliar_release(payload: dict[str, Any]) -> dict[str, Any]:
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

    aprovado = score >= SCORE_MINIMO
    resultado["ok"] = aprovado
    resultado["status"] = "aprovado" if aprovado else "reprovado"
    resultado["servico"] = servico
    resultado["versao"] = versao
    return resultado
