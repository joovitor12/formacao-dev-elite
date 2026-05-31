# Guia — Boas práticas de testes assistidos por IA

Síntese do bloco **Testes unitários com IA** (geração → sucesso/erro → mock → avaliação → falsos positivos).

## Skills recomendadas

```bash
npx skills add https://github.com/github/awesome-copilot --skill pytest-coverage
npx skills add https://github.com/wshobson/agents --skill python-testing-patterns
```

## Princípios (não negociáveis)

| # | Prática | Evitar |
|---|---------|--------|
| 1 | **Priorizar lacunas** antes de pedir código à IA | Gerar dezenas de testes por cobertura |
| 2 | **Sucesso, borda e erro** com assert adequado | Só happy path |
| 3 | **Mock na fronteira** (`ativacao_service.*`) | Mockar regra pura local |
| 4 | **Avaliar** output: manter / revisar / rejeitar | Aceitar tudo que passa no CI |
| 5 | **Asserts de contrato** — detectam regressão | `is not None`, `assert True`, `except: pass` |
| 6 | **Um comportamento por teste**, nome descritivo | `test_1`, testes monolíticos |
| 7 | **Revisar diff** como PR antes de merge | “Verde = entregue” |

## Fluxo sugerido (assistido)

1. `pytest -q` — baseline.
2. IA: listar lacunas (regra pura, sucesso, erro exceção, erro retorno, mock).
3. Implementar **poucos** testes de alto valor (1–3 por rodada).
4. `python verificar_boas_praticas.py` — pendências objetivas.
5. IA como **revisor** (“este teste prova contrato?”).
6. Repetir até checklist crítico verde.

## Matriz mínima (`ativacao_service.py`)

| Cenário | Tipo | Ferramenta |
|---------|------|------------|
| `creditos_por_tier` válido | Regra pura | assert direto, sem mock |
| Ativação com saldo ok | Sucesso + mock | `@patch` + asserts + `assert_called` no recibo |
| Tier inválido | Erro exceção | `pytest.raises` |
| Saldo insuficiente | Erro retorno | `ok False`; creditar **não** chamado |
| Falha ao creditar | Erro retorno | `ok False`; recibo **não** enviado |

## Prompts-modelo para IA

**Plano (sem código):**

> Liste lacunas de teste em `ativacao_service.py` por risco. Para cada uma: entrada, saída esperada, mock sim/não, tipo de assert.

**Implementação (um teste):**

> Implemente só o cenário X. Patch em `ativacao_service.*`. Assert de contrato. pytest verde.

**Revisão:**

> Classifique cada teste: manter/revisar/rejeitar. Algum falso positivo se `valor_reembolso`/campos chave regredirem?

## Anti-padrões do bloco inteiro

- Cobertura como meta final.
- Patch em `integracoes.*` com import já feito em `ativacao_service`.
- Suite verde com asserts que não falham quando o bug volta.
- PR da IA mergeado sem self-review.

## Critério de pronto

- `pytest -q` verde.
- `python verificar_boas_praticas.py` sem pendências críticas.
- `checklist_testes_assistidos.md` itens essenciais marcados.
