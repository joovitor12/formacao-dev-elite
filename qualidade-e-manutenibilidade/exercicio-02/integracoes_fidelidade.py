"""
Portas externas — CRM e notificações (mockar em testes de orquestração).
"""

from __future__ import annotations


def saldo_cliente(cliente_id: str) -> int:
    raise RuntimeError("saldo_cliente requer ambiente integrado ou mock")


def creditar_pontos(cliente_id: str, pontos: int) -> bool:
    raise RuntimeError("creditar_pontos requer ambiente integrado ou mock")


def debitar_pontos(cliente_id: str, pontos: int) -> bool:
    raise RuntimeError("debitar_pontos requer ambiente integrado ou mock")


def enviar_notificacao(cliente_id: str, evento: str, detalhe: str) -> None:
    raise RuntimeError("enviar_notificacao requer ambiente integrado ou mock")
