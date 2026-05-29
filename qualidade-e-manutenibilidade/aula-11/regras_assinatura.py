"""
Regras de assinatura — cobertura parcial de propósito para praticar geração de testes com IA.
"""

from __future__ import annotations

PLANOS: dict[str, float] = {
    "basico": 29.9,
    "pro": 59.9,
    "enterprise": 149.9,
}


def valor_plano(nome_plano: str) -> float:
    plano = nome_plano.lower()
    if plano not in PLANOS:
        raise ValueError("plano invalido")
    return PLANOS[plano]


def desconto_por_compromisso(meses: int) -> float:
    """Desconto percentual sobre subtotal conforme meses contratados."""
    if meses < 1:
        raise ValueError("meses invalido")
    if meses >= 12:
        return 0.15
    if meses >= 6:
        return 0.08
    return 0.0


def taxa_ativacao(primeira_fatura: bool) -> float:
    return 9.9 if primeira_fatura else 0.0


def calcular_fatura(nome_plano: str, meses: int, *, primeira_fatura: bool = False) -> dict[str, float | str]:
    mensal = valor_plano(nome_plano)
    subtotal = round(mensal * meses, 2)
    pct = desconto_por_compromisso(meses)
    desconto = round(subtotal * pct, 2)
    taxa = taxa_ativacao(primeira_fatura)
    total = round(subtotal - desconto + taxa, 2)
    return {
        "plano": nome_plano.lower(),
        "meses": meses,
        "subtotal": subtotal,
        "desconto": desconto,
        "taxa_ativacao": taxa,
        "total": total,
    }
