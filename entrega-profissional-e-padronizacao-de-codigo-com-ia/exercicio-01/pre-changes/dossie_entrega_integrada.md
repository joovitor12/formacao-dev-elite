# Dossiê integrador — entrega profissional com IA

Preencha ao longo do exercício. Cada seção cobre um tema do módulo.

## Material

- Padrão: `padrao_codigo.md`
- Módulos: `notificacao_entrega.py`, `confirmacao_entrega.py`, `fechamento_entrega.py`
- Portão: `verificar_pipeline.py` + `ci/qualidade-codigo.yml`
- Veredito final: **entrega aprovada / aprovar com ressalvas / bloqueante**

---

## 1. Padrão de código

- Veredito padrão: (preencha — conforme / parcial / não conforme)
- Prompt principal usado (resumo):

```
@padrao_codigo.md @notificacao_entrega.py @confirmacao_entrega.py

Audite desvios vs padrão (nomenclatura, contrato ok/avisos, logging, erros).
Não refatore ainda.
```

| # | Arquivo | Trecho / desvio | Regra (§) | Severidade | Corrigido? |
|---|---------|-----------------|-----------|------------|------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

- O que a IA acertou na refatoração:
- O que você ajustou manualmente:

---

## 2. Linting assistido por IA

- Veredito lint: (preencha — limpo / pendências corrigidas / bloqueante)

**Saída baseline (`ruff check`):**

```
(cole aqui)
```

| # | Código | Arquivo | Ação (corrigir / ruff --fix / ignorar documentado) | Alinhado ao padrão? |
|---|--------|---------|-----------------------------------------------------|---------------------|
| 1 | | | | |
| 2 | | | | |

- Prompt de correção usado:
- Usou `ruff check --fix`? **sim / não / parcial**

---

## 3. Formatação automática

- Veredito format: (preencha — limpo / reformatado / bloqueante)

**`ruff format --check` (baseline):**

```
(cole aqui)
```

- Mudança mecânica mais visível no diff:
- Formatação alterou comportamento? **sim / não** — justifique:

---

## 4. Integração ao pipeline

- Paridade pipeline local vs CI: (preencha — sim / parcial / não)

### Gap analysis

| Item | Baseline | Desejado | Status |
|------|----------|----------|--------|
| Módulos no lint/format | | três módulos | |
| `verificar_pipeline.py` | | lint → format → smoke | |
| Workflow CI | | deps + `verificar_pipeline.py` | |

- Trecho final do workflow (cole após integração):

```yaml
# job qualidade completo
```

---

## 5. Síntese integrada

Em 4 bullets: o que o **lint/format não pegaram** e exigiram `@padrao_codigo.md`?

1.
2.
3.
4.

---

## Checklist de entrega

- [ ] Três módulos conformes a `padrao_codigo.md`
- [ ] `ruff check` limpo nos três módulos
- [ ] `ruff format --check` limpo nos três módulos
- [ ] `python verificar_pipeline.py` retorna **0**
- [ ] `ci/qualidade-codigo.yml` espelha portão local
- [ ] `python example.py` verde com contrato `ok`/`avisos`
- [ ] `python verificar_entrega.py` retorna **0**
