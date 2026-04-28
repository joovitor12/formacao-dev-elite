"""
Orquestra parse JSON + normalização + mapper.

Formatos cobertos na normalização (ver `mapper.normalize_resource_dict`):
envelope `record`, corpo em `data`, primeiro item de `items`, e aliases de id.
"""

from __future__ import annotations

import json

from mapper import map_record_to_internal


def ingest_raw_json(raw: str) -> dict:
    payload = json.loads(raw)
    if not isinstance(payload, dict):
        raise TypeError("JSON raiz deve ser um objeto")
    return map_record_to_internal(payload)
