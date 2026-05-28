"""
Orquestração de fidelidade — pasta de trabalho (pre-changes).

Contraste: regras puras em regras_pontos.py vs orquestração com estado e print.
"""

from __future__ import annotations

from typing import Any

import regras_pontos

_HISTORICO: list[dict[str, Any]] = []
_SALDO: dict[str, int] = {}


def registrar_compra(cliente_id: str, valor: float, tier: str) -> dict[str, Any]:
    resultado: dict[str, Any] = {"ok": False, "avisos": []}
    cliente = str(cliente_id or "").strip()
    if not cliente:
        resultado["avisos"].append("cliente obrigatorio")
        return resultado
    if valor <= 0:
        resultado["avisos"].append("valor invalido")
        return resultado

    try:
        base = regras_pontos.pontos_por_valor(valor)
        bonus = regras_pontos.bonus_por_tier(tier, base)
    except ValueError:
        resultado["avisos"].append("tier invalido")
        return resultado

    total = base + bonus
    _SALDO[cliente] = _SALDO.get(cliente, 0) + total
    registro = {
        "cliente_id": cliente,
        "valor": round(valor, 2),
        "tier": tier.lower(),
        "pontos_base": base,
        "pontos_bonus": bonus,
        "pontos_total": total,
        "saldo": _SALDO[cliente],
    }
    _HISTORICO.append(registro)
    print(f"[fidelidade] +{total} pts cliente={cliente} saldo={_SALDO[cliente]}")

    resultado["ok"] = True
    resultado.update(registro)
    return resultado


def resgatar_pontos(cliente_id: str, custo: int) -> dict[str, Any]:
    resultado: dict[str, Any] = {"ok": False, "avisos": []}
    cliente = str(cliente_id or "").strip()
    saldo = _SALDO.get(cliente, 0)
    if not regras_pontos.pode_resgatar(saldo, custo):
        resultado["avisos"].append("resgate invalido")
        return resultado
    _SALDO[cliente] = saldo - custo
    print(f"[fidelidade] resgate {custo} pts cliente={cliente}")
    resultado["ok"] = True
    resultado["saldo"] = _SALDO[cliente]
    return resultado


def consultar_saldo(cliente_id: str) -> int:
    return _SALDO.get(str(cliente_id or "").strip(), 0)


def reset_estado() -> None:
    _HISTORICO.clear()
    _SALDO.clear()
