"""
Ativação de tier — orquestra regra local + portas externas.
"""

from __future__ import annotations

from typing import Any

from integracoes import creditar_tier, enviar_recibo, saldo_atual
from regras_tier import creditos_por_tier, normalizar_tier


def ativar_tier(cliente_id: str, tier: str) -> dict[str, Any]:
    cliente = str(cliente_id or "").strip()
    if not cliente:
        raise ValueError("cliente obrigatorio")

    tier_norm = normalizar_tier(tier)
    creditos = creditos_por_tier(tier_norm)
    saldo = saldo_atual(cliente)

    if saldo < creditos:
        return {
            "ok": False,
            "erro": "saldo insuficiente",
            "creditos_necessarios": creditos,
            "saldo": saldo,
        }

    if not creditar_tier(cliente, creditos):
        return {"ok": False, "erro": "falha ao creditar", "creditos": creditos}

    enviar_recibo(cliente, tier_norm, creditos)

    return {
        "ok": True,
        "cliente_id": cliente,
        "tier": tier_norm,
        "creditos": creditos,
        "saldo_restante": saldo - creditos,
    }
