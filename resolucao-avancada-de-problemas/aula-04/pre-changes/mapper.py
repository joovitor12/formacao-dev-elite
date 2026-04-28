"""
Mapeamento do payload bruto da API → modelo interno.

Cenário da aula: stack trace aponta KeyError: 'id' neste módulo.
O mapeador assume que `record` já é o dict do *recurso* com chave 'id' no topo.
"""

from __future__ import annotations


def map_record_to_internal(record: dict) -> dict:
    """Traduz um único registro externo para o formato interno."""
    return {
        "internal_id": record["id"],
        "display_name": record.get("name", ""),
    }
