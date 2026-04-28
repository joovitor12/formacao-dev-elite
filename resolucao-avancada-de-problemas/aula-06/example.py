"""
Aula 06 - codigo base para validacao da correcao.
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
    print("Cenario da aula: validar a correcao com casos representativos.\n")
    _demo("Contrato documentado (flat com 'id')", EXEMPLO_PAYLOAD_V1)
    _demo("Envelope + camelCase em record", EXEMPLO_ENVELOPE_COM_RECORD)
    _demo("Id aninhado em 'data'", EXEMPLO_ID_ANINHADO)
    _demo("Lista em 'items'", EXEMPLO_LISTA_ITENS)


if __name__ == "__main__":
    main()
