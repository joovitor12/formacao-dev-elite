# Dossiê de review integrado — PR em `pipeline_review.py`

Preencha após abrir o PR com a skill **create-pr** e rodar Copilot Code Review.

## PR

- Link: https://github.com/joovitor12/formacao-dev-elite/pull/8
- Título (Conventional Commits): fix(exercicio-01): contar apenas aprovações humanas no merge
- Base → compare: main → exercicio-01

---

## 1. Papel do review moderno

- Veredito humano: **aprovar com ressalvas**
- Top 2 achados bloqueantes (se houver):
  1. `ci_verde or True` — CI falho nunca bloqueia merge; gate de qualidade permanece fictício.
  2. `WEBHOOK_TOKEN` hardcoded e impresso em log — vazamento de credencial em runtime/observabilidade.
- Sugestão do Copilot que você rejeitou (e por quê): manter `copilot_aprovou` na assinatura com `_ = copilot_aprovou  # intencionalmente ignorado`. Rejeitada porque remover o parâmetro documenta melhor a intenção de governança (bot não participa do contrato de merge) e elimina dead code/alertas de lint na origem, em vez de mascarar parâmetro órfão.

---

## 2. O que a IA avalia (taxonomia)

| # | Achado | Dimensão (segurança / correção / operação / manutenção / testes / escopo) | IA pegou bem? |
|---|--------|---------------------------------------------------------------------------|---------------|
| 1 | `copilot_aprovou or True` inflava contagem de aprovações | correção / operação | sim — resumo do PR descreveu o bypass de governança |
| 2 | Parâmetro `copilot_aprovou` sem uso após a correção | manutenção | sim — sugeriu `_ = copilot_aprovou`; não sugeriu remoção do parâmetro |
| 3 | `ci_verde or True` dispensa CI vermelho | operação / correção | não — Copilot comentou nas linhas 47–48 mas não alertou o bypass de CI na linha adjacente |

- Ponto cego (IA não comentou — você comentaria): `WEBHOOK_TOKEN` em constante de módulo e no `_log` — risco de segurança bloqueante que deveria aparecer em review automático de secrets; também `enviar = forcar or True`, que anula gate manual de deploy.

---

## 3. Comentários automáticos

| # | Fonte | Tipo (inline / resumo / check) | Acionável? (sim / parcial / ruído) | Ação |
|---|-------|-------------------------------|-------------------------------------|------|
| 1 | Copilot Code Review | resumo (overview do PR) | parcial | Validou direção da correção de governança; sem achados adicionais além do inline |
| 2 | Copilot Code Review | inline (L47–48) | parcial | Rejeitado: removido `copilot_aprovou` da assinatura em vez de `_ = copilot_aprovou` |

- Comentário duplicado entre bots (como consolidou na triagem): N/A — apenas Copilot Code Review neste PR; sem duplicata entre bots.

---

## 4. Detecção de riscos

| # | Risco | Tipo | Severidade | Bloqueia merge? |
|---|-------|------|------------|-----------------|
| 1 | Contagem inflada por Copilot/bot em merge de prod | governança | bloqueante | sim (corrigido neste PR) |
| 2 | CI vermelho não impede merge (`ci_verde or True`) | operação | bloqueante | sim (permanece aberto) |
| 3 | Token de webhook em código e log | segurança | bloqueante | sim (permanece aberto) |
| 4 | Rollback não dispara em taxa exatamente 0.05 (`>` vs `>=`) | operação | média | não |

- Risco mais crítico em produção: merge liberado com pipeline quebrado (`ci_verde or True`) — regressão pode ir a prod mesmo após corrigir contagem humana.

---

## 5. Integração Git

| Evento | O que disparou (CI / Copilot / linter / manual) |
|--------|------------------------------------------------|
| push na feature | CI do repositório (se configurado) + disponibilização da branch `exercicio-01` no remoto |
| PR aberto | Template do corpo preenchido via `gh pr create --base main`; diff visível para review humano |
| Copilot solicitado | Copilot Pull Request Reviewer — overview + 1 comentário inline em `pipeline_review.py` |

- Caminho completo usado no `git add`: `automacao-e-devops-inteligente/exercicio-01/pipeline_review.py` (facilitador na raiz do exercício)
- Erro de Git evitado neste fluxo: `git add` sem caminho completo a partir da raiz do repositório; trabalho do facilitador na raiz em vez de `pre-changes/` (baseline dos alunos preservado).

---

## 6. Governança e limites

| Regra | Limite da automação | Conforme no diff? (sim / não) |
|-------|---------------------|-------------------------------|
| Aprovação humana em prod | Copilot não substitui humano | sim |
| CI verde obrigatório | `ci_verde or True` proibido | não |
| Mínimo de aprovadores prod | 2 humanos | sim (contagem agora reflete só `aprovacoes_humanas`) |

- Veredito de governança: **violação** (mitigação parcial — contagem humana restaurada; CI e segredo permanecem não conformes)
- Quem é accountable pelo merge em prod (papel humano): par de revisores humanos no GitHub (approve explícito) + tech lead ou release manager accountable pelo veredito final; Copilot permanece como sugestão, sem voto na contagem.

---

## Checklist de entrega

- [x] PR criado com skill **create-pr** (título Conventional Commits + corpo com template)
- [x] `python example.py` rodou localmente antes do PR
- [x] Copilot Code Review acionado (se disponível)
- [x] Seções 1–6 deste dossiê preenchidas
- [x] `python verificar_entrega.py` retorna **0**
