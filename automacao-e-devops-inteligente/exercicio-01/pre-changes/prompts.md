# Exercício 01 — Prompts (review integrador + create-pr)

Use com Copilot Chat / agente com `@workspace` e a skill **create-pr** em `.agents/skills/create-pr/`.

**Pasta de trabalho:** `pre-changes/` (alunos). Facilitador pode demonstrar na raiz.

---

## 0. Instalar skill create-pr

```bash
npx skills add https://github.com/factory-ai/factory-plugins --skill create-pr
```

Ou use a cópia adaptada em `exercicio-01/.agents/skills/create-pr/SKILL.md`.

Peça ao agente: **"Siga a skill create-pr para abrir um PR desta pasta."**

---

## 1. Diagnóstico do baseline (sem patch)

```
@pre-changes/pipeline_review.py

Liste smells e riscos por tema (review humano, taxonomia IA, bots, risco, governança).

Formato: trecho → tema → severidade sugerida.

Não proponha refactor completo.
```

---

## 2. Plano de mudança mínima para o PR

```
@pre-changes/pipeline_review.py

Proponha UMA correção pequena e defensável para o PR (ex.: remover token do log, corrigir fronteira 0.05, ou remover copilot como aprovador).

Justifique com risco/governança — não estilo.

Não implemente ainda.
```

---

## 3. Verificação local (skill create-pr — passo 2)

```
Antes do PR, rode na pasta pre-changes:

python example.py

Confirme que o diff não quebrou execução básica. Reporte saída.
```

---

## 4. Criar PR com create-pr

```
@.agents/skills/create-pr/SKILL.md
@pre-changes/pull_request_template.md
@pre-changes/pipeline_review.py

Siga a skill create-pr:
- base: main
- título Conventional Commits com escopo exercicio-01
- corpo preenchido a partir do template
- caminho completo no git add: automacao-e-devops-inteligente/exercicio-01/pre-changes/

Retorne URL do PR.
```

---

## 5. Preencher dossiê — seções 1 e 2

```
Cole comentários do Copilot Code Review.

@pre-changes/dossie_review_integrado.md

Preencha seções 1 (papel do review) e 2 (taxonomia / pontos cegos).
```

---

## 6. Preencher dossiê — seções 3 e 4

```
@pre-changes/dossie_review_integrado.md

Preencha seções 3 (comentários automáticos) e 4 (riscos).
```

---

## 7. Preencher dossiê — seções 5 e 6

```
@pre-changes/dossie_review_integrado.md

Preencha seções 5 (integração Git) e 6 (governança).
Marque checklist de entrega.
```

---

## 8. Portão final

```bash
cd pre-changes
python verificar_entrega.py
```
