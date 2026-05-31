# Aula 15 — Ajustando falsos positivos

**Objetivo:** identificar testes que **passam no pytest** mas **não detectam regressão** (falso positivo de confiança) e ajustá-los com apoio da IA — usando simulador e rubrica, sem alterar código de produção.

**Ferramentas:** GitHub Copilot Chat / Explorer (ou agente equivalente) + skill:

```bash
npx skills add https://github.com/wshobson/agents --skill python-testing-patterns
```

**Material sugerido:**


| Caminho                         | Papel                                         |
| ------------------------------- | --------------------------------------------- |
| **Raiz** (`aula-15/`)           | demo ao vivo.                                 |
| `**pre-changes/`**              | ambiente de trabalho (baseline igual).        |
| `politica_reembolso.py`         | Código sob teste                              |
| `test_politica_reembolso.py`    | Suíte verde com **lacunas de detecção**.      |
| `guia_falsos_positivos.md`      | Sinais, fluxo, perguntas-guia.                |
| `simular_regressao.py`          | Probes que expõem falsos positivos restantes. |
| `verificar_falsos_positivos.py` | Anti-padrões + simulador consolidado.         |


**Setup:**

```bash
pip install -r requirements-dev.txt
```

**Como usar:** `pytest -q` (verde) → `python simular_regressao.py` (lacunas) → ajustar testes com IA → verificar de novo.

---

## 1. Verde no CI ainda engana?

```
Rodei pytest -q (verde) e python simular_regressao.py (lacunas).

@guia_falsos_positivos.md

O que é falso positivo **de confiança** neste contexto?

Diferencie de falso negativo em 3 bullets.

Não corrija testes ainda.
```

---

## 2. Mapear lacunas por teste

```
@test_politica_reembolso.py @politica_reembolso.py @guia_falsos_positivos.md

Para cada `test_*`, responda:

- que regressão real **não** seria detectada hoje?
- qual assert falta ou está fraco?

Priorize top 3 por risco. Não implemente ainda.
```

---

## 3. Simulador como evidência

```
Cole a saída de: python simular_regressao.py

@guia_falsos_positivos.md

Explique o cenário `prazo_expirado_engolido` — por que o teste atual passa
mesmo quando o código retorna `ok False` sem exceção?

Proponha asserts corretos em bullets (sem código).
```

---

## 4. Corrigir o falso positivo de maior risco

```
Use python-testing-patterns.

Ajuste APENAS o teste prioritário que você identificou em test_politica_reembolso.py.

Regras:
- não alterar politica_reembolso.py;
- asserts provam contrato de negócio;
- pytest -q verde;
- python simular_regressao.py deve reduzir lacunas.

@test_politica_reembolso.py @politica_reembolso.py @guia_falsos_positivos.md
```

---

## 5. Prazo expirado: retorno vs exceção

```
Implemente a correção de test_prazo_expirado_rejeita.

O código retorna dict com ok False — não ValueError.

Use asserts de retorno, não except/pass.

@test_politica_reembolso.py @politica_reembolso.py
```

---

## 6. IA revisor pós-ajuste

```
@test_politica_reembolso.py @guia_falsos_positivos.md

Saída atual de simular_regressao.py: [cole aqui]

Algum teste ainda passaria com valor_reembolso errado?
Sugira próximo ajuste mínimo (só 1). Não reescreva a suíte inteira.
```

---

## 7. Armadilha: assert a mais sem propósito

```
A IA sugeriu adicionar `assert True` no final de cada teste "para garantir verde".

@guia_falsos_positivos.md

Por que isso não corrige falso positivo?

O que fazer em vez disso?

Não implemente.
```

## Comandos úteis

**Facilitador (raiz):**

```bash
cd aula-15
pip install -r requirements-dev.txt
pytest -q
python simular_regressao.py
python verificar_falsos_positivos.py
python example.py
```

**Alunos:**

```bash
cd aula-15/pre-changes
pip install -r requirements-dev.txt
pytest -q
python simular_regressao.py
python verificar_falsos_positivos.py
python example.py
```

---

## Máxima da aula

**Teste que passa com bug simulado é alarme falso de qualidade — endureça asserts até o simulador (e a regressão real) falharem quando o contrato quebrar.**