"""
Exemplo didatico: modulo com code smells comuns.

Objetivo: usar IA para diagnosticar cheiros de codigo, impacto e custo de mudanca.
"""

from __future__ import annotations

import time
from typing import Any

# estado global mutavel
CAIXA_TOTAL = 0.0
HISTORICO: list[dict[str, Any]] = []
CLIENTES_BLOQUEADOS = {"CLI-009", "CLI-777"}
ESTOQUE = {"A1": 8, "B2": 2, "C3": 0}


def _log(msg: str) -> None:
    # I/O direto no core de regra
    print(f"[checkout] {msg}")


def _desconto_por_segmento(valor: float, segmento: str, cliente_id: str) -> float:
    """
    Smells: magic numbers + condicoes duplicadas com outra funcao.
    """
    if segmento == "gold":
        return valor * 0.12
    if segmento == "silver":
        return valor * 0.07
    if cliente_id.startswith("VIP"):
        return valor * 0.10
    return 0.0


def _desconto_por_cupom(valor: float, cupom: str, segmento: str) -> float:
    # duplicacao de regra de desconto por segmento
    d = 0.0
    if cupom == "PROMO10":
        d += valor * 0.10
    elif cupom == "PROMO20":
        d += valor * 0.20
    if segmento == "gold":
        d += valor * 0.12
    elif segmento == "silver":
        d += valor * 0.07
    return d


def fechar_compra(payload: dict[str, Any], modo_teste: bool = False, enviar_email: bool = True) -> dict[str, Any]:
    """
    Smells intencionais:
    - funcao longa com multiplas responsabilidades;
    - flags de comportamento;
    - dependencia de estado global;
    - uso de dict Any sem contrato;
    - condicoes aninhadas e regras implícitas.
    """
    global CAIXA_TOTAL

    cliente_id = str(payload.get("cliente_id") or "")
    segmento = str(payload.get("segmento") or "regular")
    cupom = str(payload.get("cupom") or "")
    itens = payload.get("itens") or []
    prioridade = payload.get("prioridade") or 0
    resultado = {"ok": False, "mensagens": []}

    if cliente_id in CLIENTES_BLOQUEADOS:
        resultado["mensagens"].append("cliente bloqueado")
        _log(f"cliente bloqueado: {cliente_id}")
        return resultado

    if not cliente_id:
        resultado["mensagens"].append("cliente sem id")
        return resultado

    if not itens:
        resultado["mensagens"].append("sem itens")
        return resultado

    subtotal = 0.0
    itens_aprovados = []
    for idx, item in enumerate(itens):
        sku = str(item.get("sku") or "")
        qtd = int(item.get("qtd") or 0)
        preco = float(item.get("preco") or 0.0)

        if not sku or qtd <= 0 or preco <= 0:
            resultado["mensagens"].append(f"item invalido idx={idx}")
            continue

        if sku not in ESTOQUE:
            resultado["mensagens"].append(f"sku desconhecido {sku}")
            continue

        if ESTOQUE[sku] < qtd:
            resultado["mensagens"].append(f"sem estoque para {sku}")
            continue

        # regra espalhada no meio da iteracao
        if prioridade and prioridade > 5 and segmento == "regular":
            preco = preco * 1.05
            _log("aplicada taxa de prioridade para segmento regular")

        ESTOQUE[sku] -= qtd
        subtotal += preco * qtd
        itens_aprovados.append({"sku": sku, "qtd": qtd, "preco_final": round(preco, 2)})

    if subtotal == 0.0:
        resultado["mensagens"].append("nenhum item aprovado")
        return resultado

    desc_segmento = _desconto_por_segmento(subtotal, segmento, cliente_id)
    desc_cupom = _desconto_por_cupom(subtotal, cupom, segmento)
    desconto_total = desc_segmento + desc_cupom
    if desconto_total > subtotal:
        desconto_total = subtotal

    valor_base = subtotal - desconto_total

    # tributo simplificado com magic numbers
    if valor_base < 100:
        taxa = 1.99
    elif valor_base < 500:
        taxa = 4.99
    else:
        taxa = 12.99

    total = round(valor_base + taxa, 2)

    # efeito colateral global
    CAIXA_TOTAL += total
    pedido = {
        "cliente_id": cliente_id,
        "segmento": segmento,
        "total": total,
        "subtotal": round(subtotal, 2),
        "desconto": round(desconto_total, 2),
        "taxa": taxa,
        "itens_aprovados": itens_aprovados,
        "mensagens": list(resultado["mensagens"]),
    }
    HISTORICO.append(pedido)

    if enviar_email:
        # simulacao de acoplamento com I/O externo
        _log(f"enviando email de confirmacao para {cliente_id}")
        time.sleep(0.01 if modo_teste else 0.1)

    resultado["ok"] = True
    resultado["pedido"] = pedido
    resultado["caixa_total"] = round(CAIXA_TOTAL, 2)
    return resultado
