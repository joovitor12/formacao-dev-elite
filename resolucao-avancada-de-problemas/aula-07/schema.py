"""
Contrato documentado da API externa (ingestao de registros).

Arquivo base para documentar aprendizados de engenharia com IA.
"""

from __future__ import annotations

EXEMPLO_PAYLOAD_V1 = """
{
  "id": "usr_8f2a",
  "name": "Ana Externa"
}
"""

EXEMPLO_ENVELOPE_COM_RECORD = """
{
  "metadata": { "version": 2 },
  "record": {
    "recordId": "usr_8f2a",
    "name": "Ana Externa"
  }
}
"""

EXEMPLO_ID_ANINHADO = """
{
  "data": {
    "id": "usr_8f2a",
    "name": "Ana Externa"
  }
}
"""

EXEMPLO_LISTA_ITENS = """
{
  "items": [
    { "id": "usr_8f2a", "name": "Ana Externa" }
  ]
}
"""
