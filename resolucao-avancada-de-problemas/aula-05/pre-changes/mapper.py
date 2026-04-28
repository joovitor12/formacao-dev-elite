"""
Mapeamento do payload bruto da API -> modelo interno.

Cenario da aula: stack trace aponta KeyError: 'id' neste modulo.
O mapeador assume que `record` ja e o dict do *recurso* com chave 'id' no topo.
"""

from __future__ import annotations


def map_record_to_internal(record: dict) -> dict:
    """Traduz um unico registro externo para o formato interno."""
    return {
        "internal_id": record["id"],
        "display_name": record.get("name", ""),
    }
