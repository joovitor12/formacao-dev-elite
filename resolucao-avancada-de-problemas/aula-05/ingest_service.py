"""
Orquestra parse JSON + escolha do dict que vai ao mapper.

Baseline da aula: extracao incompleta para provocar falhas de contrato.
"""

from __future__ import annotations

import json

from mapper import map_record_to_internal


def _extract_record(payload: dict) -> dict:
    if "record" in payload and isinstance(payload["record"], dict):
        return payload["record"]
    if "data" in payload and isinstance(payload["data"], dict):
        return payload["data"]
    if "items" in payload and isinstance(payload["items"], list) and payload["items"]:
        first = payload["items"][0]
        if isinstance(first, dict):
            return first
    return payload


def ingest_raw_json(raw: str) -> dict:
    payload = json.loads(raw)
    record = _extract_record(payload)
    return map_record_to_internal(record)
