"""
Mapeamento do payload bruto da API -> modelo interno.

Baseline da aula: mapeador estrito, depende de `id` no topo do dict.
"""

from __future__ import annotations


def _unwrap_record_shape(record: dict) -> dict:
    if "record" in record and isinstance(record["record"], dict):
        return record["record"]
    if "data" in record and isinstance(record["data"], dict):
        return record["data"]
    if "items" in record and isinstance(record["items"], list) and record["items"]:
        first = record["items"][0]
        if isinstance(first, dict):
            return first
    return record


def map_record_to_internal(record: dict) -> dict:
    source = _unwrap_record_shape(record)
    external_id = source.get("id", source.get("recordId"))
    if external_id is None:
        raise KeyError("id")

    return {
        "internal_id": external_id,
        "display_name": source.get("name", ""),
    }
