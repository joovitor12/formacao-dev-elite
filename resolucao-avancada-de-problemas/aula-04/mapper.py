"""
Mapeamento do payload bruto da API → modelo interno.

Normaliza envelopes comuns (`record`, `data`, `items[]`) e aliases de id
(`recordId`) antes de montar o modelo interno.
"""

from __future__ import annotations


def normalize_resource_dict(payload: dict) -> dict:
    """
    Reduz respostas típicas de API ao dict de um único recurso.

    Encadeia desembrulhos enquanto houver `record`, `data` ou primeiro
    elemento de `items` — cobre aninhamentos como record → data → …
    """
    current: dict = payload
    for _ in range(16):
        if "record" in current and isinstance(current["record"], dict):
            current = current["record"]
            continue
        if "data" in current and isinstance(current["data"], dict):
            current = current["data"]
            continue
        items = current.get("items")
        if isinstance(items, list) and items and isinstance(items[0], dict):
            current = items[0]
            continue
        break
    return current


def _external_identifier(record: dict) -> str:
    if "id" in record:
        return str(record["id"])
    if "recordId" in record:
        return str(record["recordId"])
    raise KeyError("id")


def map_record_to_internal(record: dict) -> dict:
    """Traduz um payload externo (com envelope opcional) para o formato interno."""
    normalized = normalize_resource_dict(record)
    return {
        "internal_id": _external_identifier(normalized),
        "display_name": normalized.get("name", ""),
    }
