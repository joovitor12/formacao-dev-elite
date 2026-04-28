"""
Caracterização: ingest e mapper aceitam vários formatos após normalização.

Rodar a partir desta pasta:
  cd resolucao-avancada-de-problemas/aula-04 && pytest test_api_id_characterization.py -v
"""

from __future__ import annotations

import json

import pytest

from ingest_service import ingest_raw_json
from mapper import map_record_to_internal


def _d(obj: object) -> str:
    return json.dumps(obj, separators=(",", ":"))


@pytest.mark.parametrize(
    "label, payload, expected_internal_id",
    [
        ("id_no_root", {"id": "usr_1", "name": "Ana"}, "usr_1"),
        (
            "envelope_record_com_id_snake",
            {"metadata": {"v": 1}, "record": {"id": "usr_1", "name": "Ana"}},
            "usr_1",
        ),
        (
            "envelope_record_com_recordId_sem_id",
            {"metadata": {"v": 2}, "record": {"recordId": "usr_1", "name": "Ana"}},
            "usr_1",
        ),
        (
            "id_somente_em_data",
            {"data": {"id": "usr_1", "name": "Ana"}},
            "usr_1",
        ),
        (
            "lista_em_items_raiz_sem_id",
            {"items": [{"id": "usr_1", "name": "Ana"}]},
            "usr_1",
        ),
    ],
)
def test_ingest_raw_json_shapes(
    label: str,
    payload: dict,
    expected_internal_id: str,
) -> None:
    raw = _d(payload)
    out = ingest_raw_json(raw)
    assert out["internal_id"] == expected_internal_id
    assert out["display_name"] == "Ana"


@pytest.mark.parametrize(
    "label, record, expected_internal_id",
    [
        ("recurso_plano_com_id", {"id": "usr_1", "name": "Ana"}, "usr_1"),
        (
            "raiz_com_data_aninhada_sem_id_no_topo",
            {"data": {"id": "usr_1", "name": "Ana"}},
            "usr_1",
        ),
        ("só_recordId_camelCase", {"recordId": "usr_1", "name": "Ana"}, "usr_1"),
        (
            "wrapper_items_sem_id_no_topo",
            {"items": [{"id": "usr_1", "name": "Ana"}]},
            "usr_1",
        ),
        (
            "dict_do_recurso_se_extraido_de_data_ou_items0",
            {"id": "usr_1", "name": "Ana"},
            "usr_1",
        ),
    ],
)
def test_map_record_to_internal_shapes(
    label: str,
    record: dict,
    expected_internal_id: str,
) -> None:
    out = map_record_to_internal(record)
    assert out["internal_id"] == expected_internal_id
    assert out["display_name"] == "Ana"


def test_sem_identificador_keyerror_id() -> None:
    with pytest.raises(KeyError) as exc:
        map_record_to_internal({"name": "Sem id"})
    assert exc.value.args[0] == "id"
