"""
Regras de resgate de pontos — cenários de sucesso e erro explícitos no código.
"""

from __future__ import annotations

from typing import Any

CODIGOS: dict[str, int] = {
    "DESC10": 50,
    "FRETE": 100,
    "VIP": 500,
}


def custo_resgate(codigo: str) -> int:
    chave = str(codigo or "").strip().upper()
    if not chave:
        raise ValueError("codigo obrigatorio")
    if chave not in CODIGOS:
        raise ValueError("codigo invalido")
    return CODIGOS[chave]


def processar_resgate(codigo: str, saldo_pontos: int) -> dict[str, Any]:
    if saldo_pontos < 0:
        raise ValueError("saldo invalido")

    custo = custo_resgate(codigo)
    if saldo_pontos < custo:
        return {"ok": False, "erro": "saldo insuficiente", "custo": custo}

    return {
        "ok": True,
        "codigo": str(codigo).strip().upper(),
        "custo": custo,
        "saldo_restante": saldo_pontos - custo,
    }
