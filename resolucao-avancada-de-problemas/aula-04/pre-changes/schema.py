"""
Contrato documentado da API externa (ingestão de registros).

Use este arquivo no @workspace junto com mapper.py e ingest_service.py
para pedir hipóteses ao Copilot sobre o KeyError em 'id'.

Na prática, fornecedores mudam envelope, nomes de campos e aninhamento;
o que está aqui é o que o time *esperava* na última versão integrada.
"""

from __future__ import annotations

# Formato que o time documentou como "válido" na integração inicial.
EXEMPLO_PAYLOAD_V1 = """
{
  "id": "usr_8f2a",
  "name": "Ana Externa"
}
"""

# Variações que aparecem em APIs reais (úteis para brainstorming de hipóteses).
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
