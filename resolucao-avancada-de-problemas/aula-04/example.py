"""
Aula 39 — Formulação de hipóteses (material de apoio).

Cenário: KeyError: 'id' em mapper.py ao ingerir JSON da API externa.
Arquivos para @workspace: schema.py, ingest_service.py, mapper.py

Execute:
  python example.py
  python test_mapper_api_shapes.py
"""

from __future__ import annotations

import traceback

from ingest_service import ingest_raw_json

from schema import (
    EXEMPLO_ENVELOPE_COM_RECORD,
    EXEMPLO_ID_ANINHADO,
    EXEMPLO_LISTA_ITENS,
    EXEMPLO_PAYLOAD_V1,
)


def _demo(label: str, raw: str) -> None:
    print(f"\n--- {label} ---")
    try:
        result = ingest_raw_json(raw)
        print("OK:", result)
    except Exception as e:
        print(type(e).__name__ + ":", e)
        traceback.print_exc(limit=2)


def main() -> None:
    print("Cenário da aula: formatos de schema.py após normalização no mapper/ingest.\n")

    _demo("Contrato documentado (flat com 'id')", EXEMPLO_PAYLOAD_V1)
    _demo("Envelope + camelCase em record (típico KeyError 'id')", EXEMPLO_ENVELOPE_COM_RECORD)
    _demo("Id aninhado em 'data' (parse / contrato)", EXEMPLO_ID_ANINHADO)
    _demo("Lista em 'items' (nível errado passado ao mapper)", EXEMPLO_LISTA_ITENS)


if __name__ == "__main__":
    main()
