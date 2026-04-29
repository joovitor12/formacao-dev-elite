"""
Exercicio Operacao resgate: reproduz comportamento atual do baseline quebrado.
"""

from __future__ import annotations

import traceback

from ingest_service import ingest_raw_json
from schema import (
    EXEMPLO_DATA_ID,
    EXEMPLO_ID_NO_ROOT,
    EXEMPLO_ITEMS_LISTA,
    EXEMPLO_RECORD_CAMEL,
    EXEMPLO_SEM_IDENTIFICADOR,
)


def _demo(label: str, raw: str) -> None:
    print(f"\n--- {label} ---")
    try:
        result = ingest_raw_json(raw)
        print("OK:", result)
    except Exception as exc:
        print(type(exc).__name__ + ":", exc)
        traceback.print_exc(limit=2)


def main() -> None:
    print("Operacao resgate: baseline atual (quebrado).\n")
    _demo("id no root", EXEMPLO_ID_NO_ROOT)
    _demo("record + recordId", EXEMPLO_RECORD_CAMEL)
    _demo("id em data", EXEMPLO_DATA_ID)
    _demo("id em items[0]", EXEMPLO_ITEMS_LISTA)
    _demo("sem identificador", EXEMPLO_SEM_IDENTIFICADOR)


if __name__ == "__main__":
    main()
