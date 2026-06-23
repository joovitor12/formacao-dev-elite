# Aula 04 — Integração ao pipeline

**Objetivo:** integrar **lint**, **format** e **smoke test** em um **portão local** (`verificar_pipeline.py`) e espelhar o mesmo job em **CI** (GitHub Actions) — alinhado ao `padrao_codigo.md`.

**Enquadramento:** o que você roda antes do merge deve ser o **mesmo** que o pipeline executa no PR. IA ajuda a completar o YAML e o script; **humano** valida ordem dos jobs, paths e paridade local vs CI.

**Ferramentas:** Ruff, GitHub Actions, Copilot Chat / agente com `@workspace`.

**Material:**


| Arquivo                     | Papel                                                                 |
| --------------------------- | --------------------------------------------------------------------- |
| `pyproject.toml`            | Configuração Ruff (lint + format).                                    |
| `requirements-dev.txt`      | Dependências do job de CI.                                            |
| `padrao_codigo.md`          | Padrão do time — o pipeline não substitui review contra o documento. |
| `notificacao_entrega.py`    | Módulo 1 — já conforme (padrão + lint + format).                      |
| `confirmacao_entrega.py`    | Módulo 2 — idem.                                                      |
| `fechamento_entrega.py`     | Módulo 3 — idem.                                                      |
| `verificar_pipeline.py`     | Portão local — **baseline incompleto** (proposital).                  |
| `ci/qualidade-codigo.yml`   | Template de workflow — **baseline incompleto** (proposital).          |
| `registro_pipeline_ci.md`   | Gap analysis, prompt à IA, paridade local vs CI.                      |
| `example.py`                | Smoke test dos três módulos.                                          |


**Fluxo em sala:**

1. Mapear portões de qualidade do time (padrão documentado, lint, formatação automática, smoke test) → `registro_pipeline_ci.md` §1.
2. Auditar gaps em `verificar_pipeline.py` e `ci/qualidade-codigo.yml` → §2.
3. Pedir integração à IA com `@padrao_codigo.md` → §3.
4. Validar paridade: `python verificar_pipeline.py` = mesmo resultado esperado no workflow → §4.
5. (Opcional) Copiar workflow para `.github/workflows/` e abrir PR de teste.

---

## 1. Mapa de portões

```
Liste em bullets os portões que o time já adota no fluxo de entrega:

- padrão documentado (`padrao_codigo.md`) — review humano
- lint (`ruff check`)
- formatação automática (`ruff format --check`)
- smoke test (`example.py`)

Para cada um: roda local? roda no CI hoje? (baseline = só smoke no CI)

Preencha seção 1 do registro.
```

---

## 2. Auditar baseline

```
@verificar_pipeline.py @ci/qualidade-codigo.yml @example.py

Compare o baseline ao pipeline desejado:

- quais módulos entram no lint/format?
- falta instalar requirements-dev no workflow?
- falta chamar verificar_pipeline.py no CI?

Preencha tabela de gaps na seção 2 do registro.

Não corrija ainda.
```

---

## 3. Integrar com IA

```
@padrao_codigo.md @verificar_pipeline.py @ci/qualidade-codigo.yml @pyproject.toml

Complete a integração:

1. verificar_pipeline.py deve rodar, nesta ordem:
   - ruff check nos três módulos de entrega
   - ruff format --check nos três módulos
   - python example.py
2. ci/qualidade-codigo.yml deve espelhar o portão local:
   - pip install -r requirements-dev.txt
   - python verificar_pipeline.py
   - working-directory correto para este monorepo

Não altere a lógica dos módulos — só pipeline.

Registre prompt e observações na seção 3 do registro.
```

---

## 4. Validar paridade local vs CI

```
Revise diff manualmente.

python verificar_pipeline.py
python -m ruff check notificacao_entrega.py confirmacao_entrega.py fechamento_entrega.py
python -m ruff format --check notificacao_entrega.py confirmacao_entrega.py fechamento_entrega.py
python example.py

Opcional — publicar CI:

cp ci/qualidade-codigo.yml ../../.github/workflows/qualidade-codigo-pipeline.yml
# abra PR e confira checks no GitHub

Preencha seção 4 e checklist do registro.
```

---

## Comandos úteis

```bash
cd entrega-profissional-e-padronizacao-de-codigo-com-ia/aula-04
pip install -r requirements-dev.txt
python verificar_pipeline.py
python example.py
python -m ruff check notificacao_entrega.py confirmacao_entrega.py fechamento_entrega.py
python -m ruff format --check notificacao_entrega.py confirmacao_entrega.py fechamento_entrega.py
```

---

## Máxima da aula

**Pipeline verde só vale se local e CI executam os mesmos portões — padrão documentado continua no review humano.**
