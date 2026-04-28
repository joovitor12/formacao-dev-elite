"""
Contrato documentado da API externa (ingestao de registros).

Use este arquivo no @workspace junto com mapper.py e ingest_service.py
para pedir hipoteses ao Copilot sobre o KeyError em 'id'.

Na pratica, fornecedores mudam envelope, nomes de campos e aninhamento;
o que esta aqui e o que o time *esperava* na ultima versao integrada.
"""

from __future__ import annotations

# Formato que o time documentou como "valido" na integracao inicial.
EXEMPLO_PAYLOAD_V1 = """
{
  "id": "usr_8f2a",
  "name": "Ana Externa"
}
"""

# Variacoes que aparecem em APIs reais (uteis para brainstorming de hipoteses).
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
