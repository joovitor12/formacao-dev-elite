"""
Provas rápidas: mesmo payload em formatos diferentes.

Roteiro da aula: peça ao Copilot para estender estes casos (ex.: id em
posições aninhadas, camelCase, lista em `items`) e interprete:
- se um caso que você achava que quebrava passa, aquela hipótese enfraquece;
- se continua KeyError, a hipótese segue viva.

Execute: python test_mapper_api_shapes.py
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

    def test_record_envelope_with_record_id_camel_case_keyerror(self) -> None:
        """API colocou o recurso em `record` mas renomeou id → recordId."""
        raw = json.dumps(
            {
                "metadata": {"v": 2},
                "record": {"recordId": "1", "name": "Ana"},
            }
        )
        with self.assertRaises(KeyError) as ctx:
            ingest_raw_json(raw)
        self.assertEqual(ctx.exception.args[0], "id")

    def test_mapper_directly_nested_id_still_keyerror_if_passed_outer(self) -> None:
        """Se o bug for 'passamos o envelope errado', o mapper quebra no topo."""
        outer = {"data": {"id": "1", "name": "Ana"}}
        with self.assertRaises(KeyError):
            map_record_to_internal(outer)


if __name__ == "__main__":
    unittest.main()
