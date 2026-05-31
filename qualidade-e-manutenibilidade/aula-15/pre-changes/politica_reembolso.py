"""
Política de reembolso — código sob teste (não alterar na aula).
"""

from __future__ import annotations

from typing import Any

PRAZO_DIAS: dict[str, int] = {
    "padrao": 7,
    "premium": 30,
}


def calcular_reembolso(valor: float, tipo: str, dias_desde_compra: int) -> dict[str, Any]:
    if valor <= 0:
        raise ValueError("valor invalido")

    tipo_norm = str(tipo or "").strip().lower()
    if tipo_norm not in PRAZO_DIAS:
        raise ValueError("tipo invalido")

    prazo = PRAZO_DIAS[tipo_norm]
    if dias_desde_compra > prazo:
        return {
            "ok": False,
            "erro": "prazo expirado",
            "valor_reembolso": 0.0,
        }

    percentual = 1.0 if dias_desde_compra <= 3 else 0.5
    valor_reembolso = round(valor * percentual, 2)

    return {
        "ok": True,
        "tipo": tipo_norm,
        "percentual": percentual,
        "valor_reembolso": valor_reembolso,
    }
