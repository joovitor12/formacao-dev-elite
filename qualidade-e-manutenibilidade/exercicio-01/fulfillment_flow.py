"""
Fluxo de fulfillment monolítico — ambiente do aluno (pre-changes/).

Smells intencionais. Refatore mantendo testes, equivalência e checklist verdes.
"""

from __future__ import annotations

from typing import Any

import notificacao
import validacao

_ESTOQUE: dict[str, int] = {"SKU-A": 100, "SKU-B": 5, "SKU-C": 0}
_FULFILLMENTS: list[dict[str, Any]] = []
_PROXIMO_ID = 1


def processar_fulfillment(payload: dict[str, Any]) -> dict[str, Any]:
    global _PROXIMO_ID

    resultado: dict[str, Any] = {"ok": False, "avisos": []}

    cliente, canal, cupom, itens = validacao.normalizar_payload(payload)
    erro_cabecalho = validacao.validar_cabecalho(cliente, canal, itens)
    if erro_cabecalho:
        resultado["avisos"].append(erro_cabecalho)
        return resultado

    subtotal, linhas, erro_itens = validacao.montar_linhas(itens, _ESTOQUE)
    if erro_itens:
        resultado["avisos"].append(erro_itens)
        return resultado

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

    notificacao.notificar(fulfillment_id, cliente, total)

    resultado["ok"] = True
    resultado["fulfillment_id"] = fulfillment_id
    resultado["subtotal"] = round(subtotal, 2)
    resultado["taxa_marketplace"] = taxa_marketplace
    resultado["desconto"] = desconto
    resultado["total"] = total
    return resultado


def listar_fulfillments() -> list[dict[str, Any]]:
    return list(_FULFILLMENTS)


def reset_estado() -> None:
    """Restaura estado global — usado por testes e ferramentas."""
    global _PROXIMO_ID
    _ESTOQUE.clear()
    _ESTOQUE.update({"SKU-A": 100, "SKU-B": 5, "SKU-C": 0})
    _FULFILLMENTS.clear()
    _PROXIMO_ID = 1
