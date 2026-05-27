"""
Referência congelada de comportamento — NÃO EDITAR durante o exercício.
"""

from __future__ import annotations

from typing import Any

_ESTOQUE: dict[str, int] = {"SKU-A": 100, "SKU-B": 5, "SKU-C": 0}
_FULFILLMENTS: list[dict[str, Any]] = []
_PROXIMO_ID = 1


def processar_fulfillment(payload: dict[str, Any]) -> dict[str, Any]:
    global _PROXIMO_ID

    resultado: dict[str, Any] = {"ok": False, "avisos": []}

    cliente = str(payload.get("cliente_id") or "").strip()
    canal = str(payload.get("canal") or "").lower()
    cupom = str(payload.get("cupom") or "").upper()
    itens = payload.get("itens") or []

    if not cliente:
        resultado["avisos"].append("cliente obrigatorio")
        return resultado
    if canal not in ("varejo", "marketplace"):
        resultado["avisos"].append("canal invalido")
        return resultado
    if not itens:
        resultado["avisos"].append("itens obrigatorios")
        return resultado

    subtotal = 0.0
    linhas: list[dict[str, Any]] = []
    for item in itens:
        sku = str(item.get("sku") or "").strip().upper()
        qtd = int(item.get("qtd") or 0)
        preco = float(item.get("preco_unit") or 0.0)
        if not sku or qtd <= 0 or preco <= 0:
            resultado["avisos"].append("item invalido")
            return resultado
        if _ESTOQUE.get(sku, 0) < qtd:
            resultado["avisos"].append(f"estoque insuficiente para {sku}")
            return resultado
        linha = qtd * preco
        subtotal += linha
        linhas.append({"sku": sku, "qtd": qtd, "total": round(linha, 2)})

    taxa_marketplace = 0.0
    if canal == "marketplace":
        taxa_marketplace = round(subtotal * 0.03, 2)
        resultado["avisos"].append("taxa marketplace aplicada")

    base = subtotal + taxa_marketplace
    desconto = 0.0
    if cupom == "ECON10":
        desconto = round(base * 0.10, 2)
        resultado["avisos"].append("cupom economico aplicado")
    elif cupom:
        resultado["avisos"].append("cupom invalido")
        return resultado

    total = round(base - desconto, 2)

    for item in linhas:
        _ESTOQUE[item["sku"]] -= item["qtd"]

    fulfillment_id = f"FUL-{_PROXIMO_ID:05d}"
    _PROXIMO_ID += 1
    registro = {
        "id": fulfillment_id,
        "cliente_id": cliente,
        "canal": canal,
        "subtotal": round(subtotal, 2),
        "taxa_marketplace": taxa_marketplace,
        "desconto": desconto,
        "total": total,
        "itens": linhas,
    }
    _FULFILLMENTS.append(registro)

    print(f"[notify] fulfillment {fulfillment_id} cliente={cliente} total={total}")

    resultado["ok"] = True
    resultado["fulfillment_id"] = fulfillment_id
    resultado["subtotal"] = round(subtotal, 2)
    resultado["taxa_marketplace"] = taxa_marketplace
    resultado["desconto"] = desconto
    resultado["total"] = total
    return resultado


def reset_estado() -> None:
    global _PROXIMO_ID
    _ESTOQUE.clear()
    _ESTOQUE.update({"SKU-A": 100, "SKU-B": 5, "SKU-C": 0})
    _FULFILLMENTS.clear()
    _PROXIMO_ID = 1
