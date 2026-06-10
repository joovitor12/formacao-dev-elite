---
name: create-pr
description: Create a pull request with Conventional Commits formatting, a templated body, and local verification. Use when the user asks to create a PR, open a PR, submit changes for review, or put code up for review in exercicio-01.
---

# Create Pull Request (exercício Automação e DevOps)

Adaptado de [factory-ai/factory-plugins — create-pr](https://skills.sh/factory-ai/factory-plugins/create-pr).

Crie um PR com convenções corretas: verificação local, título Conventional Commits, corpo com template e push na branch remota.

## Prerequisites

Antes de começar, verifique:

1. A branch tem commits que não estão na base (`git log origin/main..HEAD --oneline`)
2. A branch foi enviada ao remoto (`git push -u origin HEAD` se necessário)
3. Não há mudanças não commitadas que devam entrar no PR (`git status`)

## Workflow

### 1. Entender as mudanças

```bash
git log origin/main..HEAD --oneline
git diff origin/main..HEAD --stat
```

Determine: **o quê** mudou, **tipo** (`feat`, `fix`, `refactor`, `chore`, …), **escopo** (`exercicio-01`).

### 2. Verificação local (obrigatório neste exercício)

Na pasta de trabalho do aluno:

```bash
cd automacao-e-devops-inteligente/exercicio-01/pre-changes
python example.py
```

Falha aqui → corrigir antes do PR.

### 3. Título do PR

Formato: `type(scope): description`

Exemplos:

- `fix(exercicio-01): remove token de log em notificar_deploy`
- `fix(exercicio-01): corrige fronteira de rollback em 0.05`

### 4. Corpo do PR

Use `pre-changes/pull_request_template.md` ou `exercicio-01/pull_request_template.md`:

- Description
- Related Issue (N/A se não houver)
- Potential Risk & Impact
- How Has This Been Tested? (`python example.py`)

### 5. git add com caminho completo

Sempre a partir da **raiz do repositório**:

```bash
git add automacao-e-devops-inteligente/exercicio-01/pre-changes/pipeline_review.py
# ou pasta inteira:
git add automacao-e-devops-inteligente/exercicio-01/pre-changes/
```

### 6. Criar o PR

```bash
gh pr create \
  --base main \
  --head <branch-name> \
  --title "fix(exercicio-01): <descrição>" \
  --body-file automacao-e-devops-inteligente/exercicio-01/pre-changes/pull_request_template.md
```

### 7. Após o PR

1. Solicitar **Copilot Code Review** no GitHub.
2. Preencher `dossie_review_integrado.md` (seções 1–6).
3. Rodar `python verificar_entrega.py` em `pre-changes/`.

## Erros comuns

- **`git add` sem caminho completo** — falha se o comando roda na raiz do repo.
- **Base errada** — usar `main` (ou a branch padrão do repositório).
- **Esquecer push** — `gh pr create` exige branch no remoto.
- **Pular `python example.py`** — CI local do exercício.

## Instalação upstream

```bash
npx skills add https://github.com/factory-ai/factory-plugins --skill create-pr
```
