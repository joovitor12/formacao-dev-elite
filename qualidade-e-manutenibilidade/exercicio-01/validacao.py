"""Responsabilidades de validacao e normalizacao de entrada."""

from __future__ import annotations

from typing import Any


def normalizar_payload(payload: dict[str, Any]) -> tuple[str, str, str, list[Any]]:
    cliente = str(payload.get("cliente_id") or "").strip()
    canal = str(payload.get("canal") or "").lower()
    cupom = str(payload.get("cupom") or "").upper()
    itens = payload.get("itens") or []
    return cliente, canal, cupom, itens


def validar_cabecalho(cliente: str, canal: str, itens: list[Any]) -> str | None:
    if not cliente:
        return "cliente obrigatorio"
    if canal not in ("varejo", "marketplace"):
        return "canal invalido"
    if not itens:
        return "itens obrigatorios"
    return None


def montar_linhas(
    itens: list[Any], estoque: dict[str, int]
) -> tuple[float, list[dict[str, Any]], str | None]:
    subtotal = 0.0
    linhas: list[dict[str, Any]] = []

    for item in itens:
        sku = str(item.get("sku") or "").strip().upper()
        qtd = int(item.get("qtd") or 0)
        preco = float(item.get("preco_unit") or 0.0)
        if not sku or qtd <= 0 or preco <= 0:
            return 0.0, [], "item invalido"
        if estoque.get(sku, 0) < qtd:
            return 0.0, [], f"estoque insuficiente para {sku}"
        linha = qtd * preco
        subtotal += linha
        linhas.append({"sku": sku, "qtd": qtd, "total": round(linha, 2)})

    return subtotal, linhas, None
