"""
Provas rápidas: mesmo payload em formatos diferentes.

Execute: python test_mapper_api_shapes.py
Ou: pytest test_mapper_api_shapes.py
"""

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
        raw = json.dumps(
            {
                "metadata": {"v": 2},
                "record": {"recordId": "1", "name": "Ana"},
            }
        )
        out = ingest_raw_json(raw)
        self.assertEqual(out["internal_id"], "1")

    def test_mapper_nested_data_resolved(self) -> None:
        outer = {"data": {"id": "1", "name": "Ana"}}
        out = map_record_to_internal(outer)
        self.assertEqual(out["internal_id"], "1")


if __name__ == "__main__":
    unittest.main()
