"""
Cálculo de comissão — implementação em evolução.

Refatore este arquivo; mantenha equivalência com comissao_baseline.py.
"""

from __future__ import annotations

from typing import Any

NIVEL_CONFIG: dict[str, tuple[float, float]] = {
    "junior": (0.03, 50.0),
    "pleno": (0.05, 50.0),
    "senior": (0.07, 100.0),
}


def calcular_comissao(venda: dict[str, Any]) -> dict[str, Any]:
    resultado: dict[str, Any] = {"ok": False, "avisos": []}

    nivel = str(venda.get("vendedor_nivel") or "").lower()
    valor = float(venda.get("valor_venda") or 0.0)
    categoria = str(venda.get("categoria") or "").lower()
    meta = bool(venda.get("meta_bateu"))

    if valor <= 0:
        resultado["avisos"].append("valor invalido")
        return resultado
    if nivel not in ("junior", "pleno", "senior"):
        resultado["avisos"].append("nivel invalido")
        return resultado
    if categoria not in ("produto", "servico"):
        resultado["avisos"].append("categoria invalida")
        return resultado

    pct, bonus_meta = NIVEL_CONFIG[nivel]

    comissao = valor * pct
    if categoria == "produto":
        comissao = comissao * 0.9
    else:
        comissao = comissao * 1.1

    if meta:
        comissao += bonus_meta

    if valor > 10000:
        comissao += valor * 0.02

    resultado["ok"] = True
    resultado["comissao"] = round(comissao, 2)
    resultado["nivel"] = nivel
    resultado["categoria"] = categoria
    return resultado
