"""
Mapeamento de registro externo para modelo interno.

Este arquivo esta propositalmente incompleto para o exercicio.
"""

from __future__ import annotations


def map_record_to_internal(record: dict) -> dict:
    external_id = record.get("id") or record.get("recordId")
    if not external_id:
        raise ValueError("missing id in payload")

    return {
        "internal_id": external_id,
        "display_name": record.get("name", ""),
    }
