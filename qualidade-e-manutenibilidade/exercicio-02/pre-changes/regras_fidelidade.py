"""
Regras puras do programa de fidelidade — testar diretamente, sem mock.
"""

from __future__ import annotations

MULTIPLICADOR_POR_TIER: dict[str, int] = {
    "bronze": 1,
    "prata": 2,
    "ouro": 3,
}

PREMIOS: dict[str, int] = {
    "COPO": 100,
    "CAMISETA": 500,
}


def normalizar_tier(tier: str) -> str:
    chave = str(tier or "").strip().lower()
    if not chave:
        raise ValueError("tier obrigatorio")
    if chave not in MULTIPLICADOR_POR_TIER:
        raise ValueError("tier invalido")
    return chave


def pontos_por_compra(valor: float, tier: str) -> int:
    if valor <= 0:
        raise ValueError("valor invalido")
    tier_norm = normalizar_tier(tier)
    blocos = int(valor // 10)
    return blocos * MULTIPLICADOR_POR_TIER[tier_norm]


def custo_premio(codigo: str) -> int:
    chave = str(codigo or "").strip().upper()
    if not chave:
        raise ValueError("premio obrigatorio")
    if chave not in PREMIOS:
        raise ValueError("premio invalido")
    return PREMIOS[chave]


def pode_resgatar(saldo: int, custo: int) -> bool:
    return custo > 0 and saldo >= custo
