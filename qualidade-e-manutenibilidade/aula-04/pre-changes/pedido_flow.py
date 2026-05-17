"""
Fluxo de pedido monolítico — extraia responsabilidades mantendo processar_pedido.

Sugestão de módulos alvo: validacao.py, precificacao.py, persistencia.py, notificacao.py
"""

from __future__ import annotations

from typing import Any

from validacao import validar_pedido

_PEDIDOS: list[dict[str, Any]] = []
_PROXIMO_ID = 1


def processar_pedido(payload: dict[str, Any]) -> dict[str, Any]:
    global _PROXIMO_ID

    resultado: dict[str, Any] = {"ok": False, "erros": []}

    resultado["erros"].extend(validar_pedido(payload))
    if resultado["erros"]:
        return resultado

    cliente = str(payload.get("cliente_id") or "").strip()
    itens = payload.get("itens") or []
    cupom = str(payload.get("cupom") or "").upper()

    subtotal = 0.0
    linhas: list[dict[str, Any]] = []
    for item in itens:
        qtd = int(item["qtd"])
        preco = float(item["preco"])
        linha_total = qtd * preco
        subtotal += linha_total
        linhas.append({"sku": str(item.get("sku") or ""), "qtd": qtd, "total": linha_total})

    desconto = 0.0
    if cupom == "DESC10":
        desconto = round(subtotal * 0.10, 2)
    taxa = 5.0 if (subtotal - desconto) < 100 else 0.0
    total = round(subtotal - desconto + taxa, 2)

    pedido_id = f"PED-{_PROXIMO_ID:04d}"
    _PROXIMO_ID += 1
    registro = {
        "id": pedido_id,
        "cliente_id": cliente,
        "subtotal": round(subtotal, 2),
        "desconto": desconto,
        "taxa": taxa,
        "total": total,
        "itens": linhas,
        "cupom": cupom or None,
    }
    _PEDIDOS.append(registro)

    print(f"[notificacao] pedido {pedido_id} confirmado para {cliente} total=R$ {total}")

    resultado["ok"] = True
    resultado["pedido_id"] = pedido_id
    resultado["total"] = total
    resultado["subtotal"] = round(subtotal, 2)
    resultado["desconto"] = desconto
    resultado["taxa"] = taxa
    return resultado


def listar_pedidos() -> list[dict[str, Any]]:
    return list(_PEDIDOS)
