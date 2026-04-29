from __future__ import annotations

import json

import pytest

from ingest_service import ingest_raw_json


def _d(obj: object) -> str:
    return json.dumps(obj, separators=(",", ":"))


@pytest.mark.parametrize(
    "payload, expected_id",
    [
        ({"id": "usr_100", "name": "Ana"}, "usr_100"),
        ({"record": {"recordId": "usr_200", "name": "Bia"}}, "usr_200"),
        ({"data": {"id": "usr_300", "name": "Caio"}}, "usr_300"),
        ({"items": [{"id": "usr_400", "name": "Duda"}]}, "usr_400"),
    ],
    ids=[
        "id_no_root",
        "record_recordId",
        "data_id",
        "items_primeiro_item",
    ],
)
def test_payloads_validos_devem_mapear_internal_id(
    payload: dict, expected_id: str
) -> None:
    out = ingest_raw_json(_d(payload))
    assert out["internal_id"] == expected_id


def test_payload_sem_identificador_deve_falhar_com_erro_explicito() -> None:
    raw = _d({"record": {"name": "Sem ID"}})
    with pytest.raises((KeyError, ValueError)) as exc:
        ingest_raw_json(raw)

    # Mantemos o erro estavel para facilitar observabilidade no exercicio.
    assert "id" in str(exc.value).lower()
