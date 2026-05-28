"""
Regras puras de pontos de fidelidade — candidatas ideais a teste unitário.

Sem I/O, sem estado global: entrada → saída previsível.
"""

from __future__ import annotations


def pontos_por_valor(valor_compra: float) -> int:
    """1 ponto a cada R$ 10, arredondado para baixo."""
    if valor_compra <= 0:
        return 0
    return int(valor_compra // 10)


def bonus_por_tier(tier: str, pontos_base: int) -> int:
    """Bônus percentual sobre pontos base conforme tier."""
    tier_norm = tier.lower()
    if pontos_base <= 0:
        return 0
    if tier_norm == "ouro":
        return int(pontos_base * 0.20)
    if tier_norm == "prata":
        return int(pontos_base * 0.10)
    if tier_norm == "bronze":
        return 0
    raise ValueError("tier invalido")


def pode_resgatar(saldo: int, custo_resgate: int) -> bool:
    return saldo >= custo_resgate > 0
