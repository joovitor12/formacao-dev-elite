"""
Cobrança recorrente — pasta de trabalho.

Refatore este arquivo; mantenha comportamento (snapshot) e reavalie com relatorio_antes_depois.py.
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


def _normalizar_entrada(assinatura: dict[str, Any]) -> tuple[str, int, str, list[Any]]:
    plano = str(assinatura.get("plano") or "").lower()
    meses = int(assinatura.get("meses") or 0)
    cupom = str(assinatura.get("cupom") or "").upper()
    addons = assinatura.get("addons") or []
    return plano, meses, cupom, addons


def _validar_plano_meses(
    plano: str, meses: int, resultado: dict[str, Any]
) -> bool:
    validacoes = (
        (plano in PLANOS, "plano invalido"),
        (meses >= 1, "meses invalido"),
    )
    for valido, mensagem in validacoes:
        if not valido:
            resultado["avisos"].append(mensagem)
            return False
    return True


def _calcular_extra_addons(addons: list[Any], resultado: dict[str, Any]) -> float | None:
    extra = 0.0
    for addon in addons:
        chave = str(addon).lower()
        if chave not in ADDONS:
            resultado["avisos"].append(f"addon invalido: {addon}")
            return None
        extra += ADDONS[chave]
    return extra


def _aplicar_descontos(
    total: float, meses: int, cupom: str, resultado: dict[str, Any]
) -> float | None:
    if meses >= 12:
        total *= 0.85
        resultado["avisos"].append("desconto anual aplicado")
    if cupom == "PROMO10":
        total *= 0.90
        resultado["avisos"].append("cupom aplicado")
    elif cupom:
        resultado["avisos"].append("cupom invalido")
        return None
    return total


def calcular_cobranca(assinatura: dict[str, Any]) -> dict[str, Any]:
    """
    Calcula total da assinatura — monólito intencional para refatorar e comparar métricas.
  """
    resultado: dict[str, Any] = {"ok": False, "avisos": []}
    plano, meses, cupom, addons = _normalizar_entrada(assinatura)

    if not _validar_plano_meses(plano, meses, resultado):
        return resultado

    extra = _calcular_extra_addons(addons, resultado)
    if extra is None:
        return resultado

    total = (PLANOS[plano] + extra) * meses
    total_com_descontos = _aplicar_descontos(total, meses, cupom, resultado)
    if total_com_descontos is None:
        return resultado

    resultado["ok"] = True
    resultado["total"] = round(total_com_descontos, 2)
    resultado["plano"] = plano
    resultado["meses"] = meses
    return resultado
