"""
Parse de JSON e orquestracao para o mapper.

Este arquivo esta propositalmente incompleto para o exercicio.
"""

from __future__ import annotations

import json

from mapper import map_record_to_internal


def _extract_record(payload: dict) -> dict:
    if "record" in payload:
        return payload["record"]
    if "data" in payload:
        return payload["data"]
    items = payload.get("items")
    if isinstance(items, list) and items and isinstance(items[0], dict):
        return items[0]
    return payload


def ingest_raw_json(raw: str) -> dict:
    payload = json.loads(raw)
    record = _extract_record(payload)
    return map_record_to_internal(record)
