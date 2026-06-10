# Aula 06 — Governança e limites

**Objetivo:** definir **limites da automação** e **papéis humanos** no merge — o que Copilot, bots e CI podem sugerir ou checar, e o que **não** substitui aprovação humana em ambientes sensíveis.

**Enquadramento:** integração Git organiza o pipeline; **governança** diz quem pode cruzar a linha do merge e quais atalhos são proibidos (ex.: Copilot como aprovador, `force` em prod, CI verde dispensando humano).

**Ferramenta:** GitHub (PR + políticas de branch + Copilot Code Review).

**Material:**

| Arquivo | Papel |
| -------- | ------ |
| `merge_policy.py` | **Baseline limpa** na branch principal; o diff do PR testa violações de política. |
| `matriz_governanca.md` | Limites, papéis, violações e veredito de conformidade. |
| `example.py` | Comportamento da política antes e depois do PR. |

**Fluxo em sala:**

1. Manter `merge_policy.py` **limpo** na branch principal.
2. Criar branch (ex.: `feat/merge-policy-governance`) e aplicar mudanças da seção 2.
3. Abrir PR → preencher `matriz_governanca.md`.
4. Discutir: o que é sugestão da IA vs o que é **aprovação** válida em prod.

---

## 1. Limites vs automação

```
Antes do PR, defina em bullets:

- três coisas que **bots/IA podem** fazer no fluxo de review (sugerir, flagrar, rodar check);
- três coisas que **não podem** fazer (aprovar prod sozinhos, dispensar humano, alterar política).

Não analise merge_policy.py ainda.
```

---

## 2. Preparar o diff do PR (na branch)

Na branch do PR, altere `merge_policy.py` introduzindo **violações de governança**, por exemplo:

- parâmetro `copilot_aprovou` que conta como aprovação humana com `or True`;
- `forcar_merge` em prod com zero aprovadores humanos;
- aceitar string `"copilot-bot"` ou `"github-actions"` como aprovador válido em prod;
- `ci_verde or True` ignorando falha de pipeline;
- remover ou reduzir mínimo de aprovações só em prod via atalho no código.

Peça à IA só o patch desta branch — **não** altere a baseline da principal.

```
@merge_policy.py

Gere o diff para a branch do PR com as violações acima, mantendo o arquivo executável.

Não abra o PR ainda.
```

---

## 3. Ler política no código baseline

```
@merge_policy.py (versão da branch principal ou diff reverso)

Quais regras explícitas existem para dev, staging e prod?

Liste: ambiente → aprovações mínimas → dependência de CI.

Compare mentalmente com o diff da branch — o que mudou na governança?
```

---

## 4. Preencher matriz de governança

```
@matriz_governanca.md

Para cada mudança no diff:

- ação/regra;
- limite que a automação não deveria ultrapassar;
- papel humano exigido;
- viola política? (sim / não / parcial).

Não implemente correções ainda.
```

---

## 5. Copilot e conformidade

```
Cole sugestões do Copilot Code Review sobre merge_policy.py (se houver).

@matriz_governanca.md

O Copilot **sugeriu** aceitar atalho proibido ou **alertou** violação de governança?

Há sugestão da IA que você rejeitaria por política, mesmo parecendo “mais rápida”?
```

---

## 6. Accountability em prod

```
@matriz_governanca.md

Quem é accountable pelo merge em prod neste time (papel: tech lead, release manager, par de revisores)?

Por que "Copilot aprovou" ou "CI verde" **não** substituem esse papel?

Resposta em bullets — sem código.
```

---

## 7. Veredito de governança

```
@matriz_governanca.md

Veredito final: conforme / ressalva / violação / bloqueante.

Top 2 violações que impedem merge até correção.

1 mitigação aceitável **somente** se documentada (ex.: hotfix com segundo revisor em até 24h).
```

## Comandos úteis

```bash
cd aula-06
python example.py
```

**Git (caminho completo a partir da raiz do repositório):**

```bash
git add automacao-e-devops-inteligente/aula-06/
```

---

## Máxima da aula

**Automação acelera o fluxo — governança define quem pode cruzar a linha do merge.**
