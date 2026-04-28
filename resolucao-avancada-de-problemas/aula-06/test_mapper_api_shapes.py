"""Provas rapidas do contrato da aula."""

from __future__ import annotations

import json
import unittest

from ingest_service import ingest_raw_json
from mapper import map_record_to_internal


class TestMapperApiShapes(unittest.TestCase):
    def test_flat_id_snake_case_ok(self) -> None:
        raw = json.dumps({"id": "1", "name": "Ana"})
        out = ingest_raw_json(raw)
        self.assertEqual(out["internal_id"], "1")

    def test_record_envelope_with_record_id_camel_case_ok(self) -> None:
        raw = json.dumps({"record": {"recordId": "1", "name": "Ana"}})
        out = ingest_raw_json(raw)
        self.assertEqual(out["internal_id"], "1")

    def test_mapper_directly_nested_id_maps_if_passed_outer(self) -> None:
        outer = {"data": {"id": "1", "name": "Ana"}}
        out = map_record_to_internal(outer)
        self.assertEqual(out["internal_id"], "1")


if __name__ == "__main__":
    unittest.main()
