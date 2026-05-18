"""
Cálculo de carrinho (catálogo + descontos) — pasta de trabalho.

Refatore seguindo checklist_refatoracao.md; mantenha os testes verdes.
"""

from __future__ import annotations

from typing import Any


def _validar_entrada(
    itens: list[dict[str, Any]], cliente: str, resultado: dict[str, Any]
) -> bool:
    if not itens:
        resultado["avisos"].append("carrinho vazio")
        return False
    if cliente not in ("varejo", "atacado"):
        resultado["avisos"].append("cliente invalido")
        return False

    for item in itens:
        qtd = int(item.get("qtd") or 0)
        preco = float(item.get("preco_unit") or 0.0)
        if qtd <= 0 or preco <= 0:
            resultado["avisos"].append("item invalido")
            return False

    return True


def calcular_carrinho(payload: dict[str, Any]) -> dict[str, Any]:
    """
    Smells intencionais: função longa, números mágicos, ramos duplicados.
    Refatore seguindo o checklist — testes devem permanecer verdes.
    """
    resultado: dict[str, Any] = {"ok": False, "avisos": []}

    itens = payload.get("itens") or []
    cliente = str(payload.get("cliente_tipo") or "").lower()
    cupom = str(payload.get("cupom") or "").upper()

    if not _validar_entrada(itens, cliente, resultado):
        return resultado

    subtotal = 0.0
    qtd_total = 0
    for item in itens:
        qtd = int(item.get("qtd") or 0)
        preco = float(item.get("preco_unit") or 0.0)
        subtotal += qtd * preco
        qtd_total += qtd

    desconto = 0.0
    frete_gratis = False

    if cliente == "atacado" and qtd_total >= 10:
        desconto = subtotal * 0.08
        resultado["avisos"].append("desconto atacado aplicado")

    base = subtotal - desconto

    if cupom == "DESC15":
        desconto_cupom = base * 0.15
        desconto += desconto_cupom
        base = base - desconto_cupom
        resultado["avisos"].append("cupom percentual aplicado")
    elif cupom == "FRETEGRATIS":
        if base >= 200.0:
            frete_gratis = True
            resultado["avisos"].append("frete gratis elegivel")
        else:
            resultado["avisos"].append("valor minimo frete gratis nao atingido")
    elif cupom:
        resultado["avisos"].append("cupom invalido")
        return resultado

    imposto = base * 0.05
    total = base + imposto

    resultado["ok"] = True
    resultado["subtotal"] = round(subtotal, 2)
    resultado["desconto"] = round(desconto, 2)
    resultado["imposto"] = round(imposto, 2)
    resultado["total"] = round(total, 2)
    resultado["frete_gratis"] = frete_gratis
    return resultado
