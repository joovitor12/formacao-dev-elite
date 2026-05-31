"""
Orquestração de resgate — combina regra local com portas externas (candidatas a mock).
"""

from __future__ import annotations

from typing import Any

from integracoes import consultar_saldo, debitar_pontos, enviar_confirmacao
from regras_catalogo import custo_resgate


def executar_resgate(cliente_id: str, codigo: str) -> dict[str, Any]:
    cliente = str(cliente_id or "").strip()
    if not cliente:
        raise ValueError("cliente obrigatorio")

    custo = custo_resgate(codigo)
    saldo = consultar_saldo(cliente)

    if saldo < custo:
        return {"ok": False, "erro": "saldo insuficiente", "custo": custo}

    if not debitar_pontos(cliente, custo):
        return {"ok": False, "erro": "falha ao debitar", "custo": custo}

    codigo_normalizado = str(codigo).strip().upper()
    enviar_confirmacao(cliente, codigo_normalizado, custo)

    return {
        "ok": True,
        "cliente_id": cliente,
        "codigo": codigo_normalizado,
        "custo": custo,
        "saldo_restante": saldo - custo,
    }
