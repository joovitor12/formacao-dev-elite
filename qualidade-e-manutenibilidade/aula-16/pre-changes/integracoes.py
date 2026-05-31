"""
Portas externas — CRM e notificação (mockar em testes de orquestração).
"""

from __future__ import annotations


def saldo_atual(cliente_id: str) -> int:
    raise RuntimeError("saldo_atual requer ambiente integrado ou mock")


def creditar_tier(cliente_id: str, creditos: int) -> bool:
    raise RuntimeError("creditar_tier requer ambiente integrado ou mock")


def enviar_recibo(cliente_id: str, tier: str, creditos: int) -> None:
    raise RuntimeError("enviar_recibo requer ambiente integrado ou mock")
