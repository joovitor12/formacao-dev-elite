from __future__ import annotations

from typing import Any


def validar_pedido(payload: dict[str, Any]) -> list[str]:
    erros: list[str] = []

    cliente = str(payload.get("cliente_id") or "").strip()
    itens = payload.get("itens") or []

    if not cliente:
        erros.append("cliente_id obrigatorio")
    if not itens:
        erros.append("pedido sem itens")
    for idx, item in enumerate(itens):
        qtd = int(item.get("qtd") or 0)
        preco = float(item.get("preco") or 0.0)
        if qtd <= 0 or preco <= 0:
            erros.append(f"item invalido idx={idx}")

    return erros
