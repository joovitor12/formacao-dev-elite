"""
Caracterizacao do comportamento esperado de ingest_raw_json e map_record_to_internal.

Importante: este arquivo documenta os formatos aceitos sem KeyError("id").
"""

from __future__ import annotations

import json

import pytest

from ingest_service import ingest_raw_json
from mapper import map_record_to_internal


@pytest.mark.parametrize(
    "payload, expected_internal_id",
    [
        ({"id": "usr_1", "name": "Ana"}, "usr_1"),
        ({"data": {"id": "usr_2", "name": "Bia"}}, "usr_2"),
        ({"record": {"recordId": "usr_3", "name": "Caio"}}, "usr_3"),
        ({"items": [{"id": "usr_4", "name": "Duda"}]}, "usr_4"),
    ],
    ids=[
        "ingest__id_no_root__sucesso",
        "ingest__id_em_data__sucesso",
        "ingest__record_recordId_camelCase__sucesso",
        "ingest__items_lista__sucesso",
    ],
)
def test_ingest_raw_json_current_behavior(
    payload: dict, expected_internal_id: str
) -> None:
    raw = json.dumps(payload, separators=(",", ":"))
    out = ingest_raw_json(raw)
    assert out["internal_id"] == expected_internal_id

@pytest.mark.parametrize(
    "record, expected_internal_id",
    [
        ({"id": "usr_1", "name": "Ana"}, "usr_1"),
        ({"data": {"id": "usr_2", "name": "Bia"}}, "usr_2"),
        ({"recordId": "usr_3", "name": "Caio"}, "usr_3"),
        ({"items": [{"id": "usr_4", "name": "Duda"}]}, "usr_4"),
    ],
    ids=[
        "mapper__id_no_root__sucesso",
        "mapper__id_em_data__sucesso",
        "mapper__recordId_camelCase__sucesso",
        "mapper__items_lista__sucesso",
    ],
)
def test_map_record_to_internal_current_behavior(
    record: dict, expected_internal_id: str
) -> None:
    out = map_record_to_internal(record)
    assert out["internal_id"] == expected_internal_id
