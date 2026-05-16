"""
Cálculo de frete — baseline para refatoração segura (espelha pre-changes/).

Use pre-changes/ como pasta de trabalho; este arquivo serve de referência.
"""

from __future__ import annotations

from typing import Any

# estado global (refatoração segura deve reduzir dependência disso aos poucos)
TOTAL_FRETES_CALCULADOS = 0
TABELA_REGIAO: dict[str, float] = {
    "sudeste": 1.0,
    "sul": 1.05,
    "nordeste": 1.12,
    "norte": 1.18,
    "centro-oeste": 1.10,
}


def _peso_cubado(altura: float, largura: float, profundidade: float) -> float:
    return (altura * largura * profundidade) / 5000.0


def calcular_frete(envio: dict[str, Any]) -> dict[str, Any]:
    """
    Smells intencionais para refatorar com testes verdes:
    função longa, duplicação de taxa por região, estado global, magic numbers.
    """
    global TOTAL_FRETES_CALCULADOS

    resultado: dict[str, Any] = {"ok": False, "avisos": []}
    regiao = str(envio.get("regiao") or "").lower()
    peso_real = float(envio.get("peso_kg") or 0.0)
    altura = float(envio.get("altura_cm") or 0.0)
    largura = float(envio.get("largura_cm") or 0.0)
    profundidade = float(envio.get("profundidade_cm") or 0.0)
    expresso = bool(envio.get("expresso"))

    if not regiao or regiao not in TABELA_REGIAO:
        resultado["avisos"].append("regiao invalida")
        return resultado

    if peso_real <= 0:
        resultado["avisos"].append("peso invalido")
        return resultado

    cubado = _peso_cubado(altura, largura, profundidade)
    peso_cobrado = max(peso_real, cubado)

    # base + regra duplicada por região em ramos separados (smell)
    if regiao == "sudeste":
        base = 18.0
        if peso_cobrado <= 5:
            valor = base + peso_cobrado * 2.5 * TABELA_REGIAO["sudeste"]
        else:
            valor = base + peso_cobrado * 3.1 * TABELA_REGIAO["sudeste"]
    elif regiao == "sul":
        base = 20.0
        if peso_cobrado <= 5:
            valor = base + peso_cobrado * 2.5 * TABELA_REGIAO["sul"]
        else:
            valor = base + peso_cobrado * 3.1 * TABELA_REGIAO["sul"]
    elif regiao == "nordeste":
        base = 22.0
        if peso_cobrado <= 5:
            valor = base + peso_cobrado * 2.5 * TABELA_REGIAO["nordeste"]
        else:
            valor = base + peso_cobrado * 3.1 * TABELA_REGIAO["nordeste"]
    else:
        base = 24.0
        fator = TABELA_REGIAO.get(regiao, 1.15)
        if peso_cobrado <= 5:
            valor = base + peso_cobrado * 2.5 * fator
        else:
            valor = base + peso_cobrado * 3.1 * fator

    if expresso:
        valor += 15.0

    if valor > 500:
        valor = valor * 0.95
        resultado["avisos"].append("desconto volume aplicado")

    valor_final = round(valor, 2)
    TOTAL_FRETES_CALCULADOS += 1

    resultado["ok"] = True
    resultado["valor_frete"] = valor_final
    resultado["peso_cobrado_kg"] = round(peso_cobrado, 2)
    resultado["regiao"] = regiao
    return resultado
