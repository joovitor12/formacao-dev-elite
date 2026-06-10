# Aula 05 — Integração com Git

**Objetivo:** montar o **pipeline Git + GitHub** que dispara revisão automática — branch, commit com caminho correto, PR, template, checks e merge — sem repetir análise de conteúdo do diff (isso já é outro eixo).

**Por que este tema não é “só abrir PR de novo”:** nas aulas de review você julga **o que** o diff diz; aqui você organiza **como** o Git e o GitHub entregam esse diff às ferramentas (push, PR aberto, proteção de branch, Copilot acionado).

**Ferramentas:** Git, GitHub (UI ou `gh`), Copilot Code Review quando disponível.

**Material:**

| Arquivo | Papel |
| -------- | ------ |
| `promote_build.py` | Código simples — o **assunto** do PR; o foco da aula é o fluxo em volta dele. |
| `checklist_integracao_git.md` | Registrar cada passo do pipeline e o que cada evento disparou. |
| `pull_request_template.md` | Modelo opcional para copiar em `.github/pull_request_template.md` do repo. |
| `example.py` | Smoke test local antes do push. |

**Fluxo em sala:**

1. Baseline de `promote_build.py` na branch principal.
2. Criar branch de feature; alterar o arquivo (mudança pequena e legítima).
3. Commit → push → PR com template → acionar Copilot → preencher checklist.
4. Discutir: o que o Git disparou vs o que dependeu de configuração do GitHub.

---

## 1. Eventos Git e automação

```
Antes de commitar, complete em bullets:

- o que acontece no GitHub quando você dá `git push` em uma branch que não é a principal;
- o que muda quando você **abre um PR** (checks, Copilot, comentários);
- diferença entre merge local e merge via PR no remoto.

Não analise promote_build.py ainda.
```

---

## 2. Branch e caminho do commit

```
Vou trabalhar em promote_build.py nesta aula.

Liste os comandos Git na ordem (branch, add com caminho completo, commit, push).

Use caminho a partir da raiz do repositório, por exemplo:
automacao-e-devops-inteligente/aula-05/promote_build.py

Explique por que `git add promote_build.py` na raiz do repo falha.
```

---

## 3. Mensagem de commit com apoio de IA

```
Sugira mensagem de commit convencional (tipo + escopo + resumo) para uma
pequena mudança em promote_build.py (ex.: permitir promoção staging→prod com flag).

Mostre 2 opções: uma curta e uma com corpo de 2 linhas explicando o porquê.

Não gere o patch ainda.
```

---

## 4. Abrir PR (UI ou gh)

```
@pull_request_template.md

Monte o corpo do PR preenchendo o template para a mudança em promote_build.py.

Inclua seção "Como testar" com o comando da pasta aula-05.

Se usar gh CLI, mostre o comando `gh pr create` com título e base corretos.
```

---

## 5. O que o PR disparou

```
@checklist_integracao_git.md

Após abrir o PR e solicitar Copilot Code Review (se disponível):

Preencha a tabela "Eventos Git → automação".

Para cada linha: o que rodou de fato? O que ficou manual?
```

---

## 6. Proteções de branch

```
No repositório (ou em discussão em sala), liste configurações de proteção úteis para este fluxo:

- revisão obrigatória;
- checks obrigatórios;
- bloqueio de push direto na principal.

Relacione cada uma com um risco que evita — sem implementar no código.
```

---

## 7. Síntese do pipeline

```
@checklist_integracao_git.md

Em 4 bullets: o que é específico da **integração Git** (não do conteúdo Python)?

Inclua: erro de caminho evitado, evento que disparou automação, passo manual necessário.
```

## Comandos úteis

```bash
cd aula-05
python example.py
```

**Git (sempre a partir da raiz do repositório):**

```bash
git checkout -b feat/promote-build-git-flow
git add automacao-e-devops-inteligente/aula-05/
git commit -m "feat(aula-05): ajuste em promote_build"
git push -u origin feat/promote-build-git-flow
gh pr create --base main --title "Promote build — fluxo Git" --body-file automacao-e-devops-inteligente/aula-05/pull_request_template.md
```

---

## Máxima da aula

**Git entrega o diff — GitHub e as ferramentas reagem aos eventos que você dispara com branch, PR e merge.**
