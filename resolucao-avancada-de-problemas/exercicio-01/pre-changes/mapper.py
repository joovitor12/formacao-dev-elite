"""
Mapeamento de registro externo para modelo interno.

Este arquivo esta propositalmente incompleto para o exercicio.
"""

from __future__ import annotations


def map_record_to_internal(record: dict) -> dict:
    return {
        "internal_id": record["id"],
        "display_name": record.get("name", ""),
    }
