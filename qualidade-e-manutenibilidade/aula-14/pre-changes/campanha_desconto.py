"""
Regras de campanha de desconto — código sob teste (sem alterar na aula).
"""

from __future__ import annotations

from typing import Any

CUPONS: dict[str, float] = {
    "PROMO10": 0.10,
    "PROMO20": 0.20,
}

BONUS_VIP: float = 0.05
TETO_DESCONTO: float = 0.50


def validar_cupom(cupom: str) -> str:
    chave = str(cupom or "").strip().upper()
    if not chave:
        raise ValueError("cupom obrigatorio")
    if chave not in CUPONS:
        raise ValueError("cupom invalido")
    return chave


def calcular_desconto(valor: float, cupom: str, cliente_vip: bool = False) -> dict[str, Any]:
    if valor <= 0:
        raise ValueError("valor invalido")

    codigo = validar_cupom(cupom)
    percentual = round(CUPONS[codigo] + (BONUS_VIP if cliente_vip else 0.0), 4)
    if percentual > TETO_DESCONTO:
        percentual = TETO_DESCONTO
    percentual = round(percentual, 2)

    valor_desconto = round(valor * percentual, 2)
    valor_final = round(valor - valor_desconto, 2)

    return {
        "ok": True,
        "cupom": codigo,
        "percentual": percentual,
        "valor_original": round(valor, 2),
        "valor_desconto": valor_desconto,
        "valor_final": valor_final,
    }
