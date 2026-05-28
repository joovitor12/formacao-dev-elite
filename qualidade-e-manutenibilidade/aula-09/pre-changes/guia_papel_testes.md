# Guia rápido — Papel dos testes unitários

Use este guia junto com os prompts e com `pytest -q`.

## O que um teste unitário faz bem

| Papel | O que significa na prática |
|-------|----------------------------|
| **Documentação viva** | Mostra exemplos de uso e regras esperadas (`test_pontos_por_valor_*`). |
| **Feedback rápido** | Milissegundos por teste em `regras_pontos.py` — roda a cada alteração. |
| **Rede fina** | Protege uma função/regra isolada antes de integrar no serviço. |
| **Contrato local** | Falha perto da causa (tier inválido, arredondamento, borda de saldo). |

## O que costuma NÃO ser o foco do unitário

| Situação | Por quê | Onde olhar neste exercício |
|----------|---------|----------------------------|
| `print` de notificação | Efeito colateral de I/O | `fidelidade_service.registrar_compra` |
| Estado global `_SALDO` | Acoplamento entre testes se mal isolado | `test_fidelidade_service.py` + `conftest.py` |
| Orquestração de várias regras | Já é integração leve | Testes do serviço (menos granulares) |

## Pergunta-guia ao usar IA

> “Este comportamento deve ser provado em **unidade** (função pura) ou em **integração** (fluxo + estado)?”
