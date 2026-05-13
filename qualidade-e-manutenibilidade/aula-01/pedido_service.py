"""
Exemplo didático: serviço de pedido "difícil de mexer".

Propositalmente sem testes no repositório — use com Copilot apenas para DIAGNÓSTICO
nesta aula (não é gabarito de arquitetura).
"""

from __future__ import annotations

import json
import time
from typing import Any

# --- estado global (um dos cheiros: efeito colateral espalhado) ---
ULTIMOS_ERROS: list[str] = []
CONTADOR_AUDITORIA = 0
ESTOQUE: dict[str, int] = {"SKU-A": 40, "SKU-B": 3, "SKU-C": 0}


def _append_log(nivel: str, msg: str) -> None:
    global CONTADOR_AUDITORIA
    CONTADOR_AUDITORIA += 1
    linha = f"[{nivel}] #{CONTADOR_AUDITORIA} {msg}"
    print(linha)


def _calc_imposto(valor: float, uf: str, tipo: str, x: float) -> float:
    """Muitos ramos + parâmetro 'x' sem significado claro = lógica difícil de evoluir."""
    t = 0.0
    if uf == "SP":
        if tipo == "B2B":
            if valor > 1000:
                t = valor * 0.12
            else:
                t = valor * 0.10
        elif tipo == "B2C":
            t = valor * 0.11 + x * 0.01
        else:
            t = valor * 0.09
    elif uf == "RJ":
        t = valor * 0.13 if tipo == "B2B" else valor * 0.125
    elif uf in ("MG", "ES"):
        t = valor * 0.115
    else:
        if valor < 0:
            t = 0.0
        elif valor > 5000:
            t = valor * 0.14
        else:
            t = valor * 0.105
    return round(t, 2)


def processar(pedido: dict[str, Any]) -> dict[str, Any]:
    """
    Faz "tudo": validação, estoque, imposto, persistência simulada, log.
    Função longa de propósito — alvo de discussão sobre legado e medo de mudar.
    """
    global ULTIMOS_ERROS, ESTOQUE

    ULTIMOS_ERROS.clear()
    _append_log("INFO", "processar iniciado")

    if not pedido.get("id"):
        ULTIMOS_ERROS.append("pedido sem id")
        _append_log("ERRO", "validação falhou: id")
        return {"ok": False, "erros": list(ULTIMOS_ERROS)}

    itens = pedido.get("itens") or []
    if not itens:
        ULTIMOS_ERROS.append("sem itens")
        return {"ok": False, "erros": list(ULTIMOS_ERROS)}

    uf = str(pedido.get("uf") or "SP")
    tipo = str(pedido.get("tipo_cliente") or "B2C")
    desconto_campanha = float(pedido.get("desconto_campanha") or 0.0)

    subtotal = 0.0
    for idx, it in enumerate(itens):
        sku = str(it.get("sku") or "")
        q = int(it.get("qtd") or 0)
        preco = float(it.get("preco") or 0.0)

        if not sku or q <= 0 or preco < 0:
            ULTIMOS_ERROS.append(f"item inválido índice {idx}")
            continue

        if sku not in ESTOQUE:
            ULTIMOS_ERROS.append(f"sku desconhecido {sku}")
            _append_log("WARN", f"sku {sku} não cadastrado em ESTOQUE")
            continue

        if ESTOQUE[sku] < q:
            ULTIMOS_ERROS.append(f"estoque insuficiente {sku}")
            _append_log("WARN", f"estoque {sku} pedido={q} disp={ESTOQUE[sku]}")
            continue

        ESTOQUE[sku] -= q
        subtotal += preco * q
        _append_log("INFO", f"baixa estoque {sku} qtd={q}")

    if ULTIMOS_ERROS and subtotal == 0.0:
        _append_log("ERRO", "nada foi faturado; possíveis erros de item/estoque")
        return {"ok": False, "erros": list(ULTIMOS_ERROS), "estoque": dict(ESTOQUE)}

    bruto = max(subtotal - desconto_campanha, 0.0)
    imposto = _calc_imposto(bruto, uf, tipo, x=float(pedido.get("fator_misterioso") or 1.0))
    total = round(bruto + imposto, 2)

    # "persistência" simulada + acoplamento a JSON e sleep
    registro = {
        "pedido_id": pedido["id"],
        "total": total,
        "imposto": imposto,
        "uf": uf,
        "tipo": tipo,
    }
    _append_log("INFO", f"gravando pedido json={json.dumps(registro)[:80]}...")
    time.sleep(0.01)

    if total > 10000:
        _append_log("WARN", "valor alto — e-mail manual sugerido (não implementado)")

    return {
        "ok": True,
        "total": total,
        "imposto": imposto,
        "subtotal_bruto": bruto,
        "estoque_apos": dict(ESTOQUE),
        "avisos": list(ULTIMOS_ERROS),
    }
