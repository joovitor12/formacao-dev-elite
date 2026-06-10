# Exercício integrador — Pipeline de review com IA e Git

## Contexto

O time mantém um único módulo (`pipeline_review.py`) que concentra notificação pós-deploy, critério de rollback e regra de merge por ambiente. O código **roda**, mas concentra smells e **violações de governança** típicas de PRs DevOps.

Sua missão é executar um **ciclo completo de review profissional**: corrigir **uma** coisa defensável, abrir PR com a skill **[create-pr](https://skills.sh/factory-ai/factory-plugins/create-pr)**, acionar Copilot Code Review e entregar o **dossiê integrado** cobrindo os temas do módulo.

## Estrutura


| Caminho                    | Quem usa                       | Papel                                                         |
| -------------------------- | ------------------------------ | ------------------------------------------------------------- |
| **Raiz** (`exercicio-01/`) | **Facilitador** — demo ao vivo | Baseline + skill + gabarito de fluxo.                         |
| `**pre-changes/`**         | **Alunos**                     | Mesmo baseline — **único lugar para trabalhar e abrir o PR**. |


## Onde trabalhar

- **Alunos:** somente `pre-changes/`.
- **Facilitador:** demonstra na **raiz** ou em `pre-changes/` no mesmo roteiro.

## Skill create-pr

Instale ou use a cópia adaptada no exercício:

```bash
npx skills add https://github.com/factory-ai/factory-plugins --skill create-pr
```

Referência: [create-pr — factory-ai/factory-plugins](https://skills.sh/factory-ai/factory-plugins/create-pr)

A skill guia: verificação local → Conventional Commits → corpo com template → `gh pr create`.

**Verificação local deste exercício:** `python example.py` na pasta de trabalho.

## Objetivo técnico

1. Aplicar **uma** correção pequena em `pipeline_review.py` (não refactor total).
2. Abrir PR para `main` seguindo **create-pr** (caminho completo no `git add`).
3. Acionar Copilot Code Review no PR.
4. Preencher `dossie_review_integrado.md` (seis blocos de tema + checklist).

## Mapa do percurso (temas do módulo)


| Fase | Tema                    | Evidência                                          |
| ---- | ----------------------- | -------------------------------------------------- |
| 1    | Papel do review moderno | Veredito humano + achados bloqueantes no dossiê §1 |
| 2    | O que a IA avalia       | Taxonomia + ponto cego no dossiê §2                |
| 3    | Comentários automáticos | Triagem de bots no dossiê §3                       |
| 4    | Detecção de riscos      | Mapa de riscos no dossiê §4                        |
| 5    | Integração com Git      | Eventos Git → automação no dossiê §5               |
| 6    | Governança e limites    | Conformidade + accountable no dossiê §6            |


Use IA como **revisor e parceiro de PR** — não como aprovador de merge em prod.

## Regras

1. Trabalhe em `**pre-changes/`** (alunos).
2. **Uma** correção principal no PR — diff legível para review.
3. `git add` sempre com caminho desde a raiz do repositório, por exemplo:
  `automacao-e-devops-inteligente/exercicio-01/pre-changes/pipeline_review.py`
4. Não mergear em prod no exercício sem veredito humano documentado no dossiê.
5. Copilot **sugere** — governança define quem **aprova**.

## Critérios de aceite

- [ ] PR aberto com título Conventional Commits e corpo do template.
- [ ] Link do PR no dossiê.
- [ ] `python example.py` verde na pasta de trabalho.
- [ ] Dossiê §1–§6 preenchido.
- [ ] Checklist do dossiê com todos `[x]`.
- [ ] `python verificar_entrega.py` retorna **0**.

## Comandos úteis

**Alunos (`pre-changes/`):**

```bash
cd automacao-e-devops-inteligente/exercicio-01/pre-changes
python example.py
python verificar_entrega.py
```

**Git (raiz do repositório):**

```bash
git checkout -b feat/exercicio-01-pipeline-review
git add automacao-e-devops-inteligente/exercicio-01/pre-changes/
git commit -m "fix(exercicio-01): <sua correção>"
git push -u origin HEAD
```

