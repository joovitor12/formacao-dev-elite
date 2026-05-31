"""
Regras puras de tier — sem I/O. Testar diretamente, sem mock.
"""

from __future__ import annotations

CREDITOS: dict[str, int] = {
    "bronze": 10,
    "prata": 25,
    "ouro": 50,
}


def normalizar_tier(tier: str) -> str:
    chave = str(tier or "").strip().lower()
    if not chave:
        raise ValueError("tier obrigatorio")
    if chave not in CREDITOS:
        raise ValueError("tier invalido")
    return chave


def creditos_por_tier(tier: str) -> int:
    return CREDITOS[normalizar_tier(tier)]
