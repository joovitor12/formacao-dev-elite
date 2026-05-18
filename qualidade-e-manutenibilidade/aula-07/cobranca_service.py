"""
Cobrança recorrente — baseline para avaliação antes vs depois.

Trabalhe em pre-changes/; este arquivo espelha o estado inicial de referência.
"""

from __future__ import annotations

from typing import Any

PLANOS: dict[str, float] = {
    "basico": 29.9,
    "pro": 59.9,
    "enterprise": 199.9,
}
ADDONS: dict[str, float] = {
    "backup": 5.0,
    "suporte": 15.0,
    "api": 25.0,
}


def calcular_cobranca(assinatura: dict[str, Any]) -> dict[str, Any]:
    """
    Calcula total da assinatura — monólito intencional para refatorar e comparar métricas.
  """
    resultado: dict[str, Any] = {"ok": False, "avisos": []}

    plano = str(assinatura.get("plano") or "").lower()
    meses = int(assinatura.get("meses") or 0)
    cupom = str(assinatura.get("cupom") or "").upper()
    addons = assinatura.get("addons") or []

    if plano not in PLANOS:
        resultado["avisos"].append("plano invalido")
        return resultado
    if meses < 1:
        resultado["avisos"].append("meses invalido")
        return resultado

    mensal = PLANOS[plano]
    extra = 0.0
    for addon in addons:
        chave = str(addon).lower()
        if chave not in ADDONS:
            resultado["avisos"].append(f"addon invalido: {addon}")
            return resultado
        extra += ADDONS[chave]

    subtotal_mes = mensal + extra
    total = subtotal_mes * meses

    if meses >= 12:
        total = total * 0.85
        resultado["avisos"].append("desconto anual aplicado")

    if cupom == "PROMO10":
        total = total * 0.90
        resultado["avisos"].append("cupom aplicado")
    elif cupom:
        resultado["avisos"].append("cupom invalido")
        return resultado

    resultado["ok"] = True
    resultado["total"] = round(total, 2)
    resultado["plano"] = plano
    resultado["meses"] = meses
    return resultado
