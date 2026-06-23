# Dossiê integrador — entrega profissional com IA

Preencha ao longo do exercício. Cada seção cobre um tema do módulo.

## Material

- Padrão: `padrao_codigo.md`
- Módulos: `notificacao_entrega.py`, `confirmacao_entrega.py`, `fechamento_entrega.py`
- Portão: `verificar_pipeline.py` + `ci/qualidade-codigo.yml`
- Veredito final: **entrega aprovada**

---

## 1. Padrão de código

- Veredito padrão: conforme
- Prompt principal usado (resumo):

```
@padrao_codigo.md @notificacao_entrega.py @confirmacao_entrega.py @fechamento_entrega.py

Audite desvios vs padrão (nomenclatura, contrato ok/avisos, logging, erros).
Refatore os três módulos para conformidade estrita com padrao_codigo.md.
```

| # | Arquivo | Trecho / desvio | Regra (§) | Severidade | Corrigido? |
|---|---------|-----------------|-----------|------------|------------|
| 1 | `notificacao_entrega.py` | `NotificarEntrega`, retorno `success`/`msg`, `print` com token | §1, §3, §7 | alta | sim |
| 2 | `confirmacao_entrega.py` | `ConfirmarEntrega`, `except:` bare, `print` com token | §1, §8, §7 | alta | sim |
| 3 | `notificacao_entrega.py` | `qtd`, `amb` — abreviações; validação genérica `validar(p)` | §1, §5 | média | sim |
| 4 | `fechamento_entrega.py` | Espaçamento inconsistente (format); já seguia contrato `ok`/`avisos` | §5 | baixa | sim |

- O que a IA acertou na refatoração: renomeação para `snake_case`, contrato `ok`/`avisos`, extração de `validar_payload`, `logging` no lugar de `print`, constante `LIMITE_TENTATIVAS`, funções auxiliares de registro isoladas.
- O que você ajustou manualmente: atualização de `example.py` para API nova (`notificar_entrega`/`confirmar_entrega` + `ok`); docstring de módulo em `fechamento_entrega.py`.

---

## 2. Linting assistido por IA

- Veredito lint: limpo

**Saída baseline (`ruff check`):**

```
confirmacao_entrega.py:5:5: N802 Function name `ConfirmarEntrega` should be lowercase
confirmacao_entrega.py:9:5: E722 Do not use bare `except`
notificacao_entrega.py:6:5: N802 Function name `NotificarEntrega` should be lowercase
notificacao_entrega.py:20:5: E722 Do not use bare `except`

Found 4 errors.
```

| # | Código | Arquivo | Ação (corrigir / ruff --fix / ignorar documentado) | Alinhado ao padrão? |
|---|--------|---------|-----------------------------------------------------|---------------------|
| 1 | N802 | `confirmacao_entrega.py` | corrigir — renomear para `confirmar_entrega` | sim |
| 2 | E722 | `confirmacao_entrega.py` | corrigir — remover bare except; validar em `validar_payload` | sim |
| 3 | N802 | `notificacao_entrega.py` | corrigir — renomear para `notificar_entrega` | sim |
| 4 | E722 | `notificacao_entrega.py` | corrigir — remover try/except desnecessário | sim |

- Prompt de correção usado: *"Corrija violações N802 e E722 mantendo padrao_codigo.md; não use noqa."*
- Usou `ruff check --fix`? **não** — N802 e E722 exigem refatoração estrutural, não fix automático.

---

## 3. Formatação automática

- Veredito format: reformatado

**`ruff format --check` (baseline):**

```
Would reformat: confirmacao_entrega.py
Would reformat: fechamento_entrega.py
2 files would be reformatted, 1 file already formatted
```

- Mudança mecânica mais visível no diff: espaçamento em `fechamento_entrega.py` (`logger=logging` → `logger = logging`, vírgulas e parênteses em chamadas).
- Formatação alterou comportamento? **não** — apenas estilo; sem mudança de lógica.

---

## 4. Integração ao pipeline

- Paridade pipeline local vs CI: sim

### Gap analysis

| Item | Baseline | Desejado | Status |
|------|----------|----------|--------|
| Módulos no lint/format | só `confirmacao_entrega.py` | três módulos | concluído |
| `verificar_pipeline.py` | smoke + lint parcial; format SKIP | lint → format → smoke | concluído |
| Workflow CI | smoke em `pre-changes/` sem deps | deps + `verificar_pipeline.py` | concluído |

- Trecho final do workflow (cole após integração):

```yaml
# job qualidade completo
jobs:
  qualidade:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: entrega-profissional-e-padronizacao-de-codigo-com-ia/exercicio-01
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Instalar dependências de desenvolvimento
        run: pip install -r requirements-dev.txt
      - name: Portão de qualidade (lint, format, smoke)
        run: python verificar_pipeline.py
```

---

## 5. Síntese integrada

Em 4 bullets: o que o **lint/format não pegaram** e exigiram `@padrao_codigo.md`?

1. Contrato de retorno `success`/`msg` em vez de `ok`/`avisos` — lint não valida formato de API interna.
2. Uso de `print` com token/PII — regra de logging (§7) exige revisão semântica, não só E/F do Ruff.
3. Abreviações (`qtd`, `amb`) e validação fraca — nomenclatura e estrutura (§1, §5) ficam fora do escopo do linter.
4. Lógica de negócio incorreta (`forcar or True`, retorno `success: True` em payload inválido) — smoke + padrão documentado, não format.

---

## Checklist de entrega

- [x] Três módulos conformes a `padrao_codigo.md`
- [x] `ruff check` limpo nos três módulos
- [x] `ruff format --check` limpo nos três módulos
- [x] `python verificar_pipeline.py` retorna **0**
- [x] `ci/qualidade-codigo.yml` espelha portão local
- [x] `python example.py` verde com contrato `ok`/`avisos`
- [x] `python verificar_entrega.py` retorna **0**
