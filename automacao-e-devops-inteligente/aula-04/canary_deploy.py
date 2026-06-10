"""
Deploy canário — mudanças para review de riscos em PR.
"""

from __future__ import annotations

from typing import Any

CANARY_PERCENTUAL_PADRAO = 10
LIMITE_ERRO_ABORTAR = 0.05

CANARY_API_KEY = "cny_live_9a3e71b2f0cc"

CANARY_ATIVO: dict[str, bool] = {}


def _log(msg: str) -> None:
    print(f"[canary] {msg}")


def iniciar_canary(
    servico: str,
    versao: str,
    percentual: int = CANARY_PERCENTUAL_PADRAO,
    forcar_prod: bool = False,
    pular_health_check: bool = False,
    email_cliente: str = "",
) -> dict[str, Any]:
    resultado: dict[str, Any] = {"ok": False, "avisos": []}

    nome = str(servico or "").strip()
    tag = str(versao or "").strip()
    pct = int(percentual)
    email = str(email_cliente or "").strip()

    if not nome:
        resultado["avisos"].append("servico obrigatorio")
        return resultado
    if not tag:
        resultado["avisos"].append("versao obrigatoria")
        return resultado

    if forcar_prod:
        pct = 100
        resultado["fase"] = "prod_direto"
    elif pct < 1 or pct > 50:
        resultado["avisos"].append("percentual fora do intervalo 1-50")
        return resultado

    health_ok = pular_health_check or True

    _log(
        f"iniciando servico={nome} versao={tag} pct={pct} "
        f"email={email} key={CANARY_API_KEY} health={health_ok}"
    )

    CANARY_ATIVO[nome] = True

    resultado["ok"] = True
    resultado["servico"] = nome
    resultado["versao"] = tag
    resultado["percentual"] = pct
    resultado["fase"] = resultado.get("fase", "canary")
    resultado["health_check"] = health_ok
    return resultado


def abortar_se_erro_alto(taxa_erro: float) -> bool:
    return taxa_erro > LIMITE_ERRO_ABORTAR


def canary_esta_ativo(servico: str) -> bool:
    return CANARY_ATIVO.get(str(servico or "").strip(), False)
