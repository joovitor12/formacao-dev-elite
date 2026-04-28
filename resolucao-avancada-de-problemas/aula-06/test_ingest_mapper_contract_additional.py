"""
Testes adicionais de contrato para validar a correcao de ingestao JSON.

Nao altera codigo de producao: apenas expande cobertura de cenarios
positivos e negativos com asserts explicitos de erro quando aplicavel.
"""

from __future__ import annotations

import json

import pytest

from ingest_service import ingest_raw_json
from mapper import map_record_to_internal


def _raw(payload: object) -> str:
    return json.dumps(payload, separators=(",", ":"))


@pytest.mark.parametrize(
    "payload, expected",
    [
        (
            {"record": {"recordId": "usr_record_alias", "name": "Ana"}},
            {"internal_id": "usr_record_alias", "display_name": "Ana"},
        ),
        (
            {"recordId": "usr_root_alias", "name": "Bia"},
            {"internal_id": "usr_root_alias", "display_name": "Bia"},
        ),
        (
            {"id": "usr_sem_nome"},
            {"internal_id": "usr_sem_nome", "display_name": ""},
        ),
    ],
    ids=[
        "ingest__record_envelope_com_recordId__deve_mapear_internal_id",
        "ingest__recordId_no_root__deve_mapear_internal_id",
        "ingest__sem_name_com_id_valido__deve_assumir_display_name_vazio",
    ],
)
def test_ingest_positive_additional_shapes(
    payload: dict, expected: dict[str, str]
) -> None:
    out = ingest_raw_json(_raw(payload))
    assert out == expected


@pytest.mark.parametrize(
    "payload",
    [
        {"name": "Sem ID"},
        {"record": {"name": "Sem ID"}},
        {"data": {"name": "Sem ID"}},
    ],
    ids=[
        "mapper_layer__root_sem_id_ou_recordId__deve_levantar_keyerror_id",
        "mapper_layer__record_sem_id_ou_recordId__deve_levantar_keyerror_id",
        "mapper_layer__data_sem_id_ou_recordId__deve_levantar_keyerror_id",
    ],
)
def test_ingest_negative_missing_identifier_bubbles_mapper_keyerror(
    payload: dict,
) -> None:
    with pytest.raises(KeyError, match=r"^'id'$") as exc:
        ingest_raw_json(_raw(payload))
    assert exc.value.args == ("id",)


def test_ingest_negative_invalid_json_raises_jsondecodeerror_on_ingest_layer() -> None:
    raw_invalido = '{"id":"usr_10"'
    with pytest.raises(json.JSONDecodeError):
        ingest_raw_json(raw_invalido)


@pytest.mark.parametrize(
    "record",
    [
        {"name": "Sem ID"},
        {"record": {"name": "Sem ID"}},
        {"items": [{"name": "Sem ID"}]},
    ],
    ids=[
        "mapper_direct__root_sem_id_ou_recordId__erro_keyerror_id",
        "mapper_direct__record_sem_id_ou_recordId__erro_keyerror_id",
        "mapper_direct__items_primeiro_sem_id_ou_recordId__erro_keyerror_id",
    ],
)
def test_mapper_negative_missing_identifier_raises_keyerror_with_expected_message(
    record: dict,
) -> None:
    with pytest.raises(KeyError, match=r"^'id'$") as exc:
        map_record_to_internal(record)
    assert exc.value.args == ("id",)


def test_ingest_fail_safe_non_string_input_raises_typeerror() -> None:
    with pytest.raises(TypeError, match=r"raw must be a JSON string"):
        ingest_raw_json(123)  # type: ignore[arg-type]


def test_ingest_fail_safe_non_object_json_raises_typeerror() -> None:
    with pytest.raises(TypeError, match=r"payload must be a JSON object"):
        ingest_raw_json('["nao", "objeto"]')


def test_mapper_fail_safe_empty_id_raises_valueerror() -> None:
    with pytest.raises(ValueError, match=r"id must be a non-empty string"):
        map_record_to_internal({"id": "   ", "name": "Ana"})
