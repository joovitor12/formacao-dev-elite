"""
Caracterizacao do contrato da Aula 05 apos correcao de formatos.

Objetivo: mostrar formatos aceitos sem KeyError('id').
"""

from __future__ import annotations

import json

import pytest

from ingest_service import ingest_raw_json
from mapper import map_record_to_internal


def _d(obj: object) -> str:
    return json.dumps(obj, separators=(",", ":"))


@pytest.mark.parametrize(
    "payload, expect_ok",
    [
        ({"id": "usr_1", "name": "Ana"}, True),
        ({"record": {"id": "usr_1", "name": "Ana"}}, True),
        ({"record": {"recordId": "usr_1", "name": "Ana"}}, True),
        ({"data": {"id": "usr_1", "name": "Ana"}}, True),
        ({"items": [{"id": "usr_1", "name": "Ana"}]}, True),
    ],
)
def test_ingest_raw_json_baseline(payload: dict, expect_ok: bool) -> None:
    if expect_ok:
        out = ingest_raw_json(_d(payload))
        assert out["internal_id"] == "usr_1"


def test_mapper_outer_data_maps_internal_id() -> None:
    out = map_record_to_internal({"data": {"id": "usr_1", "name": "Ana"}})
    assert out["internal_id"] == "usr_1"
