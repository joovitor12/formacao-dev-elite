"""
Contrato de entrada da API parceira para o exercicio Operacao resgate.
"""

from __future__ import annotations

EXEMPLO_ID_NO_ROOT = """
{
  "id": "usr_100",
  "name": "Ana"
}
"""

EXEMPLO_RECORD_CAMEL = """
{
  "record": {
    "recordId": "usr_200",
    "name": "Bia"
  }
}
"""

EXEMPLO_DATA_ID = """
{
  "data": {
    "id": "usr_300",
    "name": "Caio"
  }
}
"""

EXEMPLO_ITEMS_LISTA = """
{
  "items": [
    { "id": "usr_400", "name": "Duda" }
  ]
}
"""

EXEMPLO_SEM_IDENTIFICADOR = """
{
  "record": {
    "name": "Sem ID"
  }
}
"""
