# Dossiê de review integrado — PR em `pipeline_review.py`

Preencha após abrir o PR com a skill **create-pr** e rodar Copilot Code Review.

## PR

- Link:
- Título (Conventional Commits):
- Base → compare:

---

## 1. Papel do review moderno

- Veredito humano: **aprovar / aprovar com ressalvas / pedir mudanças / rejeitar**
- Top 2 achados bloqueantes (se houver):
- Sugestão do Copilot que você rejeitou (e por quê):

---

## 2. O que a IA avalia (taxonomia)

| # | Achado | Dimensão (segurança / correção / operação / manutenção / testes / escopo) | IA pegou bem? |
|---|--------|---------------------------------------------------------------------------|---------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

- Ponto cego (IA não comentou — você comentaria):

---

## 3. Comentários automáticos

| # | Fonte | Tipo (inline / resumo / check) | Acionável? (sim / parcial / ruído) | Ação |
|---|-------|-------------------------------|-------------------------------------|------|
| 1 | | | | |
| 2 | | | | |

- Comentário duplicado entre bots (como consolidou na triagem):

---

## 4. Detecção de riscos

| # | Risco | Tipo | Severidade | Bloqueia merge? |
|---|-------|------|------------|-----------------|
| 1 | | | | |
| 2 | | | | |

- Risco mais crítico em produção:

---

## 5. Integração Git

| Evento | O que disparou (CI / Copilot / linter / manual) |
|--------|------------------------------------------------|
| push na feature | |
| PR aberto | |
| Copilot solicitado | |

- Caminho completo usado no `git add`:
- Erro de Git evitado neste fluxo:

---

## 6. Governança e limites

| Regra | Limite da automação | Conforme no diff? (sim / não) |
|-------|---------------------|-------------------------------|
| Aprovação humana em prod | Copilot não substitui humano | |
| CI verde obrigatório | `ci_verde or True` proibido | |
| Mínimo de aprovadores prod | 2 humanos | |

- Veredito de governança: **conforme / violação / bloqueante**
- Quem é accountable pelo merge em prod (papel humano):

---

## Checklist de entrega

- [ ] PR criado com skill **create-pr** (título Conventional Commits + corpo com template)
- [ ] `python example.py` rodou localmente antes do PR
- [ ] Copilot Code Review acionado (se disponível)
- [ ] Seções 1–6 deste dossiê preenchidas
- [ ] `python verificar_entrega.py` retorna **0**
