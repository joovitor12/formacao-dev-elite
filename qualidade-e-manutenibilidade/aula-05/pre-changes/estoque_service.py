"""
Controle de estoque — refatoração incremental (pasta de trabalho).

Extraia em incrementos pequenos; rode pytest após cada um.
"""

from __future__ import annotations

from typing import Any

_ESTOQUE: dict[str, int] = {"SKU-A": 10, "SKU-B": 5}
_AUDITORIA: list[dict[str, Any]] = []


def _validar_movimento(tipo: str, sku: str, qtd: int) -> list[str]:
    erros: list[str] = []
    if tipo not in ("entrada", "saida"):
        erros.append("tipo deve ser entrada ou saida")
    if not sku:
        erros.append("sku obrigatorio")
    if qtd <= 0:
        erros.append("qtd deve ser positiva")
    if sku and sku not in _ESTOQUE and tipo == "saida":
        erros.append("sku inexistente para saida")
    return erros


def registrar_movimento(payload: dict[str, Any]) -> dict[str, Any]:
    resultado: dict[str, Any] = {"ok": False, "erros": []}

    tipo = str(payload.get("tipo") or "").lower()
    sku = str(payload.get("sku") or "").strip().upper()
    qtd = int(payload.get("qtd") or 0)

    resultado["erros"] = _validar_movimento(tipo, sku, qtd)
    if resultado["erros"]:
        return resultado

    if sku not in _ESTOQUE:
        _ESTOQUE[sku] = 0

    saldo_antes = _ESTOQUE[sku]
    if tipo == "entrada":
        _ESTOQUE[sku] = saldo_antes + qtd
    else:
        if saldo_antes < qtd:
            resultado["erros"].append("saldo insuficiente")
            return resultado
        _ESTOQUE[sku] = saldo_antes - qtd

    saldo_depois = _ESTOQUE[sku]
    _AUDITORIA.append(
        {
            "tipo": tipo,
            "sku": sku,
            "qtd": qtd,
            "saldo_antes": saldo_antes,
            "saldo_depois": saldo_depois,
        }
    )

    resultado["ok"] = True
    resultado["sku"] = sku
    resultado["saldo_atual"] = saldo_depois
    return resultado


def consultar_saldo(sku: str) -> int:
    return _ESTOQUE.get(str(sku).strip().upper(), 0)


def listar_auditoria() -> list[dict[str, Any]]:
    return list(_AUDITORIA)
