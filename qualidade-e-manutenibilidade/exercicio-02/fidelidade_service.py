"""
Orquestração do programa de fidelidade — regra local + portas externas.
"""

from __future__ import annotations

from typing import Any

from integracoes_fidelidade import (
    creditar_pontos,
    debitar_pontos,
    enviar_notificacao,
    saldo_cliente,
)
from regras_fidelidade import custo_premio, pontos_por_compra


def acumular_compra(cliente_id: str, valor: float, tier: str) -> dict[str, Any]:
    cliente = str(cliente_id or "").strip()
    if not cliente:
        raise ValueError("cliente obrigatorio")

    pontos = pontos_por_compra(valor, tier)
    if not creditar_pontos(cliente, pontos):
        return {"ok": False, "erro": "falha ao creditar", "pontos": pontos}

    enviar_notificacao(cliente, "compra", f"+{pontos} pts")

    return {
        "ok": True,
        "cliente_id": cliente,
        "pontos": pontos,
        "saldo": saldo_cliente(cliente),
    }


def resgatar_premio(cliente_id: str, codigo_premio: str) -> dict[str, Any]:
    cliente = str(cliente_id or "").strip()
    if not cliente:
        raise ValueError("cliente obrigatorio")

    custo = custo_premio(codigo_premio)
    saldo = saldo_cliente(cliente)

    if saldo < custo:
        return {
            "ok": False,
            "erro": "saldo insuficiente",
            "custo": custo,
            "saldo": saldo,
        }

    if not debitar_pontos(cliente, custo):
        return {"ok": False, "erro": "falha ao debitar", "custo": custo}

    codigo = str(codigo_premio).strip().upper()
    enviar_notificacao(cliente, "resgate", f"-{custo} pts {codigo}")

    return {
        "ok": True,
        "cliente_id": cliente,
        "premio": codigo,
        "custo": custo,
        "saldo_restante": saldo - custo,
    }
