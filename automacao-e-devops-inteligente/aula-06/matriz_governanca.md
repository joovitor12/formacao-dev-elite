# Matriz de governança — PR em `merge_policy.py`

Defina **limites** da automação e **quem** pode autorizar merge.

## PR

- Link: _(pendente — branch `feat/merge-policy-governance`, PR ainda não aberto)_
- Ambiente mais sensível no diff (dev / staging / prod): **prod**
- Veredito de governança: **bloqueante**

## Matriz de limites

| # | Ação ou regra no diff | Limite da automação (o que IA/bot **não** pode fazer) | Papel humano exigido | Viola política? (sim / não / parcial) |
|---|----------------------|------------------------------------------------------|----------------------|---------------------------------------|
| 1 | `if copilot_aprovou or True: total += 1` — Copilot sempre soma +1 na contagem, mesmo com `copilot_aprovou=False` | Sugerir ou revisar código; **não** substituir voto de aprovador humano nem inflar contagem de aprovações | Revisor humano (par de revisores em prod) com approve explícito no PR | **sim** |
| 2 | `APROVADORES_AUTOMATICOS = {"copilot-bot", "github-actions"}` — bots entram na lista de aprovadores válidos | Rodar checks e comentar no PR; **não** contar como aprovador com poder de merge | Tech lead ou revisor humano com accountability pelo merge | **sim** |
| 3 | `if amb == "prod" and forcar_merge: minimo = 0` — atalho zera mínimo de aprovações **só em prod** | Automação não pode reduzir ou dispensar requisitos de governança por ambiente | Release manager ou tech lead autoriza exceção documentada (hotfix); nunca via flag no código | **sim** |
| 4 | `pipeline_ok = ci_verde or True` — CI falho nunca bloqueia merge | Executar pipeline e reportar status; **não** ignorar falha nem dispensar gate de qualidade | Revisor humano confirma que CI verde é pré-requisito; merge bloqueado enquanto pipeline falhar | **sim** |
| 5 | Validação usa `total_aprovacoes` (humano + Copilot + bots) em vez de `aprovacoes_humanas` | Separar **sinal** de automação (sugestão, check) de **decisão** de merge | Contagem oficial de merge em prod: apenas aprovações humanas registradas no GitHub | **sim** |

## Conta-gotas de aprovação (prod)

| Critério | Exigido pela política | O que o código do PR faz |
|----------|----------------------|--------------------------|
| Aprovações humanas mínimas | 2 humanas | Conta humano + Copilot (`or True`) + bots; com `forcar_merge=True` exige **0** |
| CI verde | Obrigatório — merge bloqueado se pipeline falhar | Sempre passa (`ci_verde or True`); CI vermelho não impede merge |
| Sugestão do Copilot conta como aprovação? | Não | Sim — `copilot_aprovou or True` sempre adiciona +1; bots na lista `aprovadores` também somam |

## Violações e mitigação

| # | Violação detectada | Severidade | Correção ou mitigação aceitável |
|---|-------------------|------------|--------------------------------|
| 1 | `forcar_merge` permite merge em prod com zero aprovadores humanos e CI falho | **bloqueante** | Remover atalho; exceções só via processo documentado (hotfix + segundo revisor em até 24h), nunca no código |
| 2 | Bots e Copilot contam como aprovadores válidos (`or True` + `APROVADORES_AUTOMATICOS`) | **bloqueante** | Reverter para contagem exclusiva de `aprovacoes_humanas`; automação permanece como sugestão/check |

## Copilot Code Review

| Comentário Copilot | Tipo | Alinhado à governança? |
|--------------------|------|------------------------|
| `_contar_aprovacoes`: `or True` e bots inflam contagem; staging passa com 0 humanos | **Alertou violação** (High) | Sim — sugere retornar só `aprovacoes_humanas` |
| `forcar_merge` em prod zera mínimo → merge sem revisão humana | **Alertou violação** (High) | Sim — sugere bloquear `forcar_merge` em prod |
| `ci_verde or True` invalida gate de CI | **Alertou violação** (High) | Sim — sugere `pipeline_ok = ci_verde` |

**Veredito Copilot:** os três comentários **alertaram** violações de governança e propuseram **correções** alinhadas à baseline — **não** sugeriram aceitar atalho proibido.

**Sugestões a rejeitar por política (mesmo parecendo “mais rápida”):**

- Manter `copilot_aprovou or True` ou bots na contagem “só em dev/staging” — escala silenciosa para prod.
- Aceitar `forcar_merge` em prod com “fluxo excepcional” **implementado no código** — exceção de hotfix é processo humano documentado, não flag no merge.
- Corrigir só CI (`ci_verde`) e deixar contagem inflada — mitigação parcial; merge ainda passaria sem humanos suficientes.

**Sugestões Copilot a aceitar no merge:** as três correções propostas (contagem só humana, bloquear `forcar_merge` em prod, CI real).

## Veredito final

**Veredito de governança: bloqueante**

Merge **não autorizado** até correção do código ou reversão à baseline. O diff introduz bypasses sistemáticos em prod; nenhuma linha está conforme com a política de aprovações humanas + CI verde.

### Top 2 violações que impedem merge

1. **`forcar_merge` em prod zera aprovações mínimas (2 → 0)** — permite merge sem nenhum revisor humano; invalida accountability de release em ambiente crítico.
2. **Contagem inflada (`copilot_aprovou or True` + bots em `APROVADORES_AUTOMATICOS`)** — substitui aprovação humana por automação; prod pode passar com 0 humanos reais se bots/Copilot preencherem o mínimo.

_(Terceira violação grave, também bloqueante: `ci_verde or True` dispensa pipeline — merge com CI quebrado.)_

### Mitigação aceitável somente se documentada

**Hotfix em prod com incidente aberto:** merge excepcional permitido **fora deste código** — via processo humano, com ticket de incidente, **tech lead ou release manager** accountable, **segundo revisor humano** registrando approve em até **24h** pós-merge, e retorno à baseline (remoção de `forcar_merge`, contagem só humana, CI real) no PR seguinte.

**Não mitiga:** flag `forcar_merge` no código, contagem de Copilot/bots, ou CI verde fictício — atalhos no merge_policy permanecem **bloqueantes** mesmo com justificativa verbal.

## Resumo

- Limite de automação mais importante neste PR: **aprovação de merge em prod permanece humana** — IA/bots não podem contar como revisor nem dispensar o mínimo de 2 aprovadores.
- Quem é **accountable** pelo merge em prod (papel, não ferramenta): _(preencher na seção 6 — ex.: tech lead + par de revisores / release manager)_
- Algo que a IA sugeriu e a governança **proíbe** aceitar sem humano: o **código do PR** (não o review Copilot) — tratar `copilot_aprovou`, `forcar_merge` e bots como substitutos de aprovação humana ou bypass de CI.
