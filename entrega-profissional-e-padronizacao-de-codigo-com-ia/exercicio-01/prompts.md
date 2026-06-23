# Exercício 01 — Prompts (entrega profissional integrador)

Use com Copilot Chat / agente com `@workspace`.

**Pasta de trabalho:** `pre-changes/` (alunos). Facilitador pode demonstrar na raiz.

---

## 1. Padrão de código — auditoria (sem patch)

```
@padrao_codigo.md @notificacao_entrega.py @confirmacao_entrega.py @fechamento_entrega.py @dossie_entrega_integrada.md

Compare os três módulos ao padrão.

Para cada desvio: trecho → regra (§) → severidade.

Preencha seção 1 do dossiê.

Não refatore ainda.
```

---

## 2. Padrão de código — refatorar com IA

```
@padrao_codigo.md @notificacao_entrega.py @confirmacao_entrega.py

Refatore para conformidade:

- snake_case, contrato ok/avisos, type hints, logging, validar_payload dedicada;
- remover print, bare except e token em log.

Siga ESTRITAMENTE padrao_codigo.md.

Atualize example.py para o contrato ok/avisos.

Registre prompt e ajustes manuais na seção 1.
```

---

## 3. Linting assistido por IA

```
pip install -r requirements-dev.txt
python -m ruff check notificacao_entrega.py confirmacao_entrega.py fechamento_entrega.py

Cole a saída em dossie_entrega_integrada.md (seção 2).

@padrao_codigo.md @confirmacao_entrega.py

Triar violações e corrigir com IA onde lint e padrão convergem.

Registre triagem e prompt na seção 2.
```

---

## 4. Formatação automática

```
python -m ruff format --check notificacao_entrega.py confirmacao_entrega.py fechamento_entrega.py
python -m ruff format --diff fechamento_entrega.py

Revise se o diff é só layout.

Aplique: python -m ruff format nos três módulos.

Preencha seção 3 do dossiê.
```

---

## 5. Integração ao pipeline

```
@verificar_pipeline.py @ci/qualidade-codigo.yml @pyproject.toml @padrao_codigo.md

Complete:

1. verificar_pipeline.py — lint + format nos três módulos, depois example.py
2. ci/qualidade-codigo.yml — pip install + python verificar_pipeline.py

Paths do monorepo: exercicio-01/pre-changes

Registre na seção 4 do dossiê.
```

---

## 6. Validar entrega

```
Revise diffs manualmente contra padrao_codigo.md.

python verificar_pipeline.py
python verificar_entrega.py

Marque checklist do dossiê.

Opcional — publicar CI:

cp ci/qualidade-codigo.yml ../../.github/workflows/qualidade-codigo-entrega.yml
```

---

## Comandos úteis

```bash
cd entrega-profissional-e-padronizacao-de-codigo-com-ia/exercicio-01/pre-changes
pip install -r requirements-dev.txt
python -m ruff check notificacao_entrega.py confirmacao_entrega.py fechamento_entrega.py
python -m ruff format --check notificacao_entrega.py confirmacao_entrega.py fechamento_entrega.py
python verificar_pipeline.py
python example.py
python verificar_entrega.py
```

---

## Máxima do exercício

**Padrão no prompt, lint e format no portão, pipeline espelhado no CI — humano revisa antes do merge.**
