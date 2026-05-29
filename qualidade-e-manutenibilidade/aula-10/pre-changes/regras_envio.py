"""
Regras de cálculo de frete — funções puras para praticar estrutura de teste.
"""

from __future__ import annotations


def tarifa_base_por_peso(peso_kg: float) -> float:
    if peso_kg <= 0:
        return 0.0
    if peso_kg <= 5:
        return 18.0
    return 18.0 + (peso_kg - 5) * 2.8


def multiplicador_regiao(regiao: str) -> float:
    regiao_norm = regiao.lower()
    if regiao_norm == "sudeste":
        return 1.0
    if regiao_norm == "sul":
        return 1.05
    if regiao_norm == "nordeste":
        return 1.12
    raise ValueError("regiao invalida")


def taxa_expresso(valor: float) -> float:
    return 12.0 if valor > 0 else 0.0


def calcular_frete(regiao: str, peso_kg: float, expresso: bool = False) -> dict[str, float | str]:
    base = tarifa_base_por_peso(peso_kg)
    mult = multiplicador_regiao(regiao)
    valor = round(base * mult, 2)
    extra = taxa_expresso(valor) if expresso else 0.0
    total = round(valor + extra, 2)
    return {
        "regiao": regiao.lower(),
        "base": base,
        "multiplicador": mult,
        "valor_regional": valor,
        "taxa_expresso": extra,
        "total": total,
    }
