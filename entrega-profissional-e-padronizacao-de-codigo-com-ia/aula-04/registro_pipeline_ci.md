# Registro — integração ao pipeline (CI)

Documente gaps, integração e paridade entre `verificar_pipeline.py` e `ci/qualidade-codigo.yml`.

## Material

- Portão local: **`verificar_pipeline.py`**
- CI: **`ci/qualidade-codigo.yml`** (template GitHub Actions)
- Padrão: `padrao_codigo.md` (review humano — fora do escopo automático)
- Módulos: `notificacao_entrega.py`, `confirmacao_entrega.py`, `fechamento_entrega.py`
- Veredito final: **portão local completo** + workflow espelhado

---

## 1. Mapa de portões

Portões adotados pelo time no fluxo de entrega:

- **Padrão documentado** (`padrao_codigo.md`) — review humano  
  - Local: sim (manual, fora do script)  
  - CI: não (não automatizado)

- **Lint** (`ruff check`)  
  - Local: parcial — `verificar_pipeline.py` roda só em `confirmacao_entrega.py`; os três módulos podem ser checados manualmente  
  - CI: não

- **Formatação automática** (`ruff format --check`)  
  - Local: não no portão — step marcado como **SKIP** em `verificar_pipeline.py`; pode rodar manualmente  
  - CI: não

- **Smoke test** (`example.py`)  
  - Local: sim — via `verificar_pipeline.py` ou `python example.py`  
  - CI: sim — único portão automatizado no workflow baseline

| Portão | Ferramenta / artefato | Local (baseline) | CI (baseline) | O que valida |
|--------|------------------------|------------------|---------------|--------------|
| Padrão do time | `padrao_codigo.md` | review manual | não automatizado | contrato, naming, logging |
| Lint | `ruff check` | parcial (1 módulo) | ausente | imports, naming, bugs óbvios |
| Format | `ruff format --check` | **SKIP** | ausente | layout mecânico |
| Smoke | `example.py` | sim | sim | comportamento ok/avisos |

**Resumo do gap:** O baseline local cobre smoke e lint parcial (um módulo), mas pula format e falha com exit code 1 por design. O CI espelha só o smoke test — PR pode ficar verde no GitHub enquanto lint/format quebram localmente. Falta unificar os três módulos, integrar format e fazer o workflow chamar o mesmo portão (`verificar_pipeline.py`).

---

## 2. Gap analysis (humano)

### Respostas rápidas (baseline vs desejado)

| Pergunta | Baseline | Pipeline desejado |
|----------|----------|-------------------|
| **Quais módulos entram no lint/format?** | Lint: só `confirmacao_entrega.py` (`MODULOS` em `verificar_pipeline.py`). Format: **nenhum** (step SKIP). | Lint **e** format nos três: `notificacao_entrega.py`, `confirmacao_entrega.py`, `fechamento_entrega.py`. |
| **Falta instalar `requirements-dev` no workflow?** | **Sim.** O workflow só faz checkout + setup Python 3.11; não há `pip install -r requirements-dev.txt` (Ruff não está disponível no job). | Step `pip install -r requirements-dev.txt` antes dos portões. |
| **Falta chamar `verificar_pipeline.py` no CI?** | **Sim.** O job roda `python example.py` direto — smoke isolado, sem lint/format e sem portão unificado. | Um único step: `python verificar_pipeline.py` (mesmo script do local). |

**Observação:** `example.py` já exercita os **três** módulos no smoke (`notificacao`, `confirmacao`, `fechamento`), mas o lint local não acompanha essa cobertura — gap de paridade entre smoke e lint.

### `verificar_pipeline.py`

| Item | Baseline | Pipeline desejado | Ação |
|------|----------|-------------------|------|
| Módulos no lint | `confirmacao_entrega.py` apenas (`MODULOS = ["confirmacao_entrega.py"]`) | `notificacao_entrega.py`, `confirmacao_entrega.py`, `fechamento_entrega.py` | corrigir |
| Módulos no format | nenhum (step não executa `ruff format`) | os três módulos acima | corrigir |
| `ruff format --check` | SKIP / TODO — imprime `[SKIP]` e conta como falha | rodar nos três módulos | corrigir |
| Ordem dos steps | smoke → lint → format (skip) | lint → format → smoke | corrigir |
| Exit code | **1** (format pendente + contagem de falhas) | **0** só com lint, format e smoke verdes | corrigir script |
| Paridade com smoke | smoke cobre 3 módulos; lint cobre 1 | lint/format alinhados à mesma lista do smoke | corrigir |

### `ci/qualidade-codigo.yml`

| Item | Baseline | Pipeline desejado | Ação |
|------|----------|-------------------|------|
| Instalar deps (`requirements-dev.txt`) | ausente — Ruff não instalado no runner | `pip install -r requirements-dev.txt` | corrigir |
| Lint / format | ausente — nenhum step `ruff` | delegados a `verificar_pipeline.py` | corrigir |
| Portão unificado | ausente — step `Smoke test` chama `python example.py` | `python verificar_pipeline.py` | corrigir |
| Smoke test | sim, isolado (`example.py`) | sim, como último step **dentro** do portão local | corrigir (via script) |
| `working-directory` | ok — `entrega-profissional-e-padronizacao-de-codigo-com-ia/aula-04` no smoke | manter o mesmo path para install + portão | ok |

---

## 3. Integração assistida por IA

- **Prompt usado:**

```
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

- **O que a IA acertou:**
  - `MODULOS` expandido para os três arquivos de entrega (`notificacao_entrega.py`, `confirmacao_entrega.py`, `fechamento_entrega.py`).
  - Ordem corrigida: lint → format → smoke (fail-fast antes do smoke).
  - Step de format real (`ruff format --check`) substituindo o SKIP/TODO.
  - Workflow passa a instalar `requirements-dev.txt` e chamar `python verificar_pipeline.py` — paridade com o portão local.
  - `python verificar_pipeline.py` retorna **0** com os três portões verdes.

- **O que você ajustou manualmente:**
  - _(nenhum ajuste manual nesta integração — validar paths do monorepo se publicar o workflow na raiz.)_
  - Opcional no YAML: `defaults.run.working-directory` centraliza o path em vez de repetir por step.

- **Paridade local vs CI confirmada?** **Sim** — local e CI executam o mesmo script na mesma ordem; CI só adiciona checkout, setup Python 3.11 e `pip install` antes do portão.

---

## 4. Pós-integração

```bash
python verificar_pipeline.py
```

**Saída esperada (pipeline completo):**

```
=== lint ===
All checks passed!

=== format ===
3 files already formatted

=== smoke ===
pipeline_entrega OK — smoke test dos três módulos

Pipeline OK — portões lint, format e smoke verdes.
```

| Passo | Local | CI (se publicou workflow) |
|-------|-------|---------------------------|
| `verificar_pipeline.py` | | |
| Lint nos 3 módulos | | |
| Format nos 3 módulos | | |
| Smoke test | | |
| Review vs `padrao_codigo.md` | manual | manual |

**Trecho final do workflow (cole após integração):**

```yaml
# cole aqui o job qualidade completo
```

---

## Checklist

- [x] Mapa de portões preenchido
- [x] Gaps baseline documentados
- [x] `verificar_pipeline.py` com lint + format + smoke nos 3 módulos
- [x] `ci/qualidade-codigo.yml` espelha o portão local
- [x] `python verificar_pipeline.py` retorna **0**
- [ ] (Opcional) Check verde no GitHub Actions

---

## Resumo

- **Portão mais crítico integrado:** _(ex.: format --check — ausente no baseline)_
- **Armadilha evitada:** CI só com smoke test passa enquanto lint/format falham localmente.
- **Regra do time daqui em diante:** todo PR alterando módulos de entrega roda **`verificar_pipeline.py`** localmente; workflow de CI chama o **mesmo script**.
