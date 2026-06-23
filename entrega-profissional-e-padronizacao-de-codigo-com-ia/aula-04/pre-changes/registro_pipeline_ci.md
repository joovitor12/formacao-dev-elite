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

| Portão | Ferramenta / artefato | Local (baseline) | CI (baseline) | O que valida |
|--------|------------------------|------------------|---------------|--------------|
| Padrão do time | `padrao_codigo.md` | review manual | não automatizado | contrato, naming, logging |
| Lint | `ruff check` | parcial (1 módulo) | ausente | imports, naming, bugs óbvios |
| Format | `ruff format --check` | **SKIP** | ausente | layout mecânico |
| Smoke | `example.py` | sim | sim | comportamento ok/avisos |

**Resumo do gap:** _(2–3 frases — baseline executa smoke + lint parcial; CI só smoke; format e módulos completos pendentes.)_

---

## 2. Gap analysis (humano)

### `verificar_pipeline.py`

| Item | Baseline | Pipeline desejado | Ação |
|------|----------|-------------------|------|
| Módulos no lint | `confirmacao_entrega.py` | os três módulos de entrega | corrigir |
| `ruff format --check` | SKIP / TODO | rodar nos três módulos | corrigir |
| Ordem dos steps | smoke → lint | lint → format → smoke | corrigir |
| Exit code | **1** (format pendente) | 0 só com pipeline completo | corrigir script |

### `ci/qualidade-codigo.yml`

| Item | Baseline | Pipeline desejado | Ação |
|------|----------|-------------------|------|
| Instalar Ruff | ausente | `pip install -r requirements-dev.txt` | corrigir |
| Lint / format | ausente | via `verificar_pipeline.py` | corrigir |
| Portão unificado | ausente | `python verificar_pipeline.py` | corrigir |
| `working-directory` | ok no smoke | manter para todos os steps | ok |

---

## 3. Integração assistida por IA

- **Prompt usado:**

```
@padrao_codigo.md @verificar_pipeline.py @ci/qualidade-codigo.yml @pyproject.toml

Complete a integração:

1. verificar_pipeline.py — lint + format nos três módulos, depois example.py
2. ci/qualidade-codigo.yml — instalar deps e chamar verificar_pipeline.py

Não altere lógica dos módulos de entrega.
```

- **O que a IA acertou:** _(preencha)_
- **O que você ajustou manualmente:** _(paths, ordem, naming do job, etc.)_
- **Paridade local vs CI confirmada?** _(sim / parcial — descreva)_

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

- [ ] Mapa de portões preenchido
- [ ] Gaps baseline documentados
- [ ] `verificar_pipeline.py` com lint + format + smoke nos 3 módulos
- [ ] `ci/qualidade-codigo.yml` espelha o portão local
- [ ] `python verificar_pipeline.py` retorna **0**
- [ ] (Opcional) Check verde no GitHub Actions

---

## Resumo

- **Portão mais crítico integrado:** _(ex.: format --check — ausente no baseline)_
- **Armadilha evitada:** CI só com smoke test passa enquanto lint/format falham localmente.
- **Regra do time daqui em diante:** todo PR alterando módulos de entrega roda **`verificar_pipeline.py`** localmente; workflow de CI chama o **mesmo script**.
