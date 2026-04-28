"""
Orquestra parse JSON + escolha do dict que vai ao mapper.

Pontos frageis tipicos (bons alvos de hipotese):
- envelope `record` vs corpo no root;
- contrato camelCase (`recordId`) vs snake_case (`id`);
- `data` ou `items[]` em vez de um unico dict plano.
"""

from __future__ import annotations

import json

from mapper import map_record_to_internal


def _extract_record(payload: dict) -> dict:
    """
    Extrai o dict do recurso a partir do JSON raiz.

    Comportamento atual (propositalmente ingenuo): se existir 'record',
    usa esse no; senao assume que o proprio payload e o recurso.
    Nao trata `data`, `items`, nem aliases de id.
    """
    if "record" in payload:
        return payload["record"]
    return payload


def ingest_raw_json(raw: str) -> dict:
    payload = json.loads(raw)
    record = _extract_record(payload)
    return map_record_to_internal(record)
