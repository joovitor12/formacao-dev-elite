"""
Portas externas — simulam I/O remoto indisponível em teste unitário sem mock.
"""

from __future__ import annotations


def consultar_saldo(cliente_id: str) -> int:
    raise RuntimeError("consultar_saldo requer ambiente integrado ou mock")


def debitar_pontos(cliente_id: str, pontos: int) -> bool:
    raise RuntimeError("debitar_pontos requer ambiente integrado ou mock")


def enviar_confirmacao(cliente_id: str, codigo: str, custo: int) -> None:
    raise RuntimeError("enviar_confirmacao requer ambiente integrado ou mock")
