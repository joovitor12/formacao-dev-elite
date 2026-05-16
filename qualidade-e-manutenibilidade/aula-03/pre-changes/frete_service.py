"""
Cálculo de frete — baseline para refatoração segura (pasta de trabalho).

Smells intencionais: refatore em passos pequenos mantendo testes verdes.
"""

from __future__ import annotations

from typing import Any

TOTAL_FRETES_CALCULADOS = 0
TABELA_REGIAO: dict[str, float] = {
    "sudeste": 1.0,
    "sul": 1.05,
    "nordeste": 1.12,
    "norte": 1.18,
    "centro-oeste": 1.10,
}
BASE_POR_REGIAO: dict[str, float] = {"sudeste": 18.0, "sul": 20.0, "nordeste": 22.0}


def _peso_cubado(altura: float, largura: float, profundidade: float) -> float:
    return (altura * largura * profundidade) / 5000.0


def _tarifa_por_kg(peso_cobrado: float) -> float:
    if peso_cobrado <= 5:
        return 2.5
    return 3.1


def calcular_frete(envio: dict[str, Any]) -> dict[str, Any]:
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

    base = BASE_POR_REGIAO.get(regiao, 24.0)
    fator = TABELA_REGIAO[regiao]
    valor = base + peso_cobrado * _tarifa_por_kg(peso_cobrado) * fator

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
