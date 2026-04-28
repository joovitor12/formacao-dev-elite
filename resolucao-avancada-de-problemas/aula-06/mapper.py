"""
Mapeamento do payload bruto da API -> modelo interno.

Baseline da aula: mapeador estrito, depende de `id` no topo do dict.
"""

from __future__ import annotations


def _pick_first_dict(values: list) -> dict | None:
    for candidate in values:
        if isinstance(candidate, dict):
            return candidate
    return None


def _unwrap_record_shape(record: dict) -> dict:
    if not isinstance(record, dict):
        raise TypeError("record must be a dict")

    if "record" in record and isinstance(record["record"], dict):
        return record["record"]
    if "data" in record and isinstance(record["data"], dict):
        return record["data"]
    if "items" in record and isinstance(record["items"], list) and record["items"]:
        first_dict = _pick_first_dict(record["items"])
        if first_dict is not None:
            return first_dict
    return record


def _normalize_external_id(source: dict) -> str:
    external_id = source.get("id", source.get("recordId"))
    if external_id is None:
        raise KeyError("id")

    normalized = str(external_id).strip()
    if not normalized:
        raise ValueError("id must be a non-empty string")
    return normalized


def _normalize_display_name(source: dict) -> str:
    raw_name = source.get("name", "")
    if raw_name is None:
        return ""
    return str(raw_name)


def map_record_to_internal(record: dict) -> dict:
    source = _unwrap_record_shape(record)
    external_id = _normalize_external_id(source)

    return {
        "internal_id": external_id,
        "display_name": _normalize_display_name(source),
    }
