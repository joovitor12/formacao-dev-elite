"""
Orquestra parse JSON + escolha do dict que vai ao mapper.

Pontos frágeis típicos (bons alvos de hipótese):
- envelope `record` vs corpo no root;
- contrato camelCase (`recordId`) vs snake_case (`id`);
- `data` ou `items[]` em vez de um único dict plano.
"""

from __future__ import annotations

import json

from mapper import map_record_to_internal


def _extract_record(payload: dict) -> dict:
    """
    Extrai o dict do recurso a partir do JSON raiz.

    Comportamento atual (propositalmente ingênuo): se existir 'record',
    usa esse nó; senão assume que o próprio payload é o recurso.
    Não trata `data`, `items`, nem aliases de id — isso vira exercício da aula.
    """
    if "record" in payload:
        return payload["record"]
    return payload


def ingest_raw_json(raw: str) -> dict:
    payload = json.loads(raw)
    record = _extract_record(payload)
    return map_record_to_internal(record)
