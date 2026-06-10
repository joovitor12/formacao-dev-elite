"""
Deploy canário — baseline para abrir PR.

Mantenha este arquivo na branch principal. Crie outra branch e aplique as
mudanças sugeridas no prompts.md (seção 2) para exercitar detecção de riscos.
"""

from __future__ import annotations

from typing import Any

CANARY_PERCENTUAL_PADRAO = 10
LIMITE_ERRO_ABORTAR = 0.05


def iniciar_canary(
    servico: str,
    versao: str,
    percentual: int = CANARY_PERCENTUAL_PADRAO,
) -> dict[str, Any]:
    resultado: dict[str, Any] = {"ok": False, "avisos": []}

    nome = str(servico or "").strip()
    tag = str(versao or "").strip()
    pct = int(percentual)

    if not nome:
        resultado["avisos"].append("servico obrigatorio")
        return resultado
    if not tag:
        resultado["avisos"].append("versao obrigatoria")
        return resultado
    if pct < 1 or pct > 50:
        resultado["avisos"].append("percentual fora do intervalo 1-50")
        return resultado

    resultado["ok"] = True
    resultado["servico"] = nome
    resultado["versao"] = tag
    resultado["percentual"] = pct
    resultado["fase"] = "canary"
    return resultado


def abortar_se_erro_alto(taxa_erro: float) -> bool:
    return taxa_erro >= LIMITE_ERRO_ABORTAR
