# Aula 14 — Avaliando testes gerados

**Objetivo:** revisar uma suíte **gerada por IA** que está verde no pytest mas mistura qualidade — classificar cada teste (**manter / revisar / rejeitar**), priorizar correções e aplicar a rubrica antes de aceitar código.

**Ferramentas:** GitHub Copilot Chat / Explorer (ou agente equivalente) + skill:

```bash
npx skills add https://github.com/wshobson/agents --skill python-testing-patterns
```

**Material sugerido:**


| Caminho                       | Papel                                         |
| ----------------------------- | --------------------------------------------- |
| **Raiz** (`aula-14/`)         | demo ao vivo.                                 |
| `**pre-changes/`**            | ambiente de trabalho (baseline igual).        |
| `campanha_desconto.py`        | Código sob teste                              |
| `test_campanha_desconto.py`   | Suíte “output de IA” com anti-padrões.        |
| `guia_avaliacao_testes_ia.md` | Rubrica e fluxo de decisão.                   |
| `avaliacao_registro.md`       | Template para registrar julgamento por teste. |
| `verificar_avaliacao.py`      | Detecta anti-padrões ainda presentes.         |


**Setup:**

```bash
pip install -r requirements-dev.txt
```

**Como usar:** `pytest -q` (verde) → `python verificar_avaliacao.py` (pendências) → avaliar com IA → corrigir prioridades → verificar de novo.

---

## 1. Verde no CI ≠ qualidade

```
Rodei pytest -q (verde) e python verificar_avaliacao.py (pendências).

@guia_avaliacao_testes_ia.md

Explique por que uma suíte pode passar no CI e ainda ser fraca como prova de regressão.

Não corrija testes ainda.
```

---

## 2. Auditoria teste a teste

```
Use python-testing-patterns.

@test_campanha_desconto.py @campanha_desconto.py @guia_avaliacao_testes_ia.md

Para CADA função `test_*`, classifique: **manter / revisar / rejeitar**.

Inclua coluna “problema principal” (assert, foco, nome, exceção, duplicação).

Não implemente correções ainda.
```

---

## 3. Assert fraco vs assert de contrato

```
@test_campanha_desconto.py @campanha_desconto.py

Compare testes que usam `is not None` com `test_desconto_vip_soma_bonus`.

O que o teste VIP prova que os outros não provam?

Proponha asserts concretos para substituir UM `is not None` — só bullets, sem código.
```

---

## 4. Erro mal testado (armadilha clássica)

```
@test_campanha_desconto.py @guia_avaliacao_testes_ia.md

Analise `test_erro_cupom_invalido` e `test_erro_valor_negativo`.

Por que `try/except` com `assert True` ou `pass` é perigoso?

Descreva a correção idiomática com pytest.raises (sem implementar).
```

---

## 5. Corrigir um teste prioritário

```
Use python-testing-patterns.

Implemente a correção mínima em test_campanha_desconto.py para o anti-padrão
de **maior risco** que você identificou (ex.: exceção engolida ou assert fraco).

Regras:
- não alterar campanha_desconto.py;
- um foco por teste tocado;
- pytest -q verde.

@test_campanha_desconto.py @campanha_desconto.py @guia_avaliacao_testes_ia.md
```

---

## 6. IA revisor da sua avaliação

```
@avaliacao_registro.md @test_campanha_desconto.py @guia_avaliacao_testes_ia.md

Revise meu registro de avaliação:

- alguma classificação “manter” deveria ser “revisar”?
- prioridades coerentes com risco de regressão?
- falta mencionar teste modelo de referência?

Sugira ajuste no registro — não reescreva a suíte inteira.
```

---

## 7. Aceitar ou devolver o PR da IA

```
@test_campanha_desconto.py @guia_avaliacao_testes_ia.md

Simule review de PR: **aprovar**, **aprovar com ressalvas** ou **pedir mudanças**.

Justifique em 5 bullets ligados à rubrica.

Se pedir mudanças, liste no máximo 3 itens bloqueantes.

Não gere código.
```

## Comandos úteis

**Facilitador (raiz):**

```bash
cd aula-14
pip install -r requirements-dev.txt
pytest -q
python verificar_avaliacao.py
python example.py
```

**Alunos:**

```bash
cd aula-14/pre-changes
pip install -r requirements-dev.txt
pytest -q
python verificar_avaliacao.py
python example.py
```

---

## Máxima da aula

**Teste gerado passa no pytest — sua job é julgar se prova o contrato; manter, revisar ou rejeitar antes de merge.**