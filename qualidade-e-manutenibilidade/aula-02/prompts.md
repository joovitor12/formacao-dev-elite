# Aula 02 — Code smells mais comuns

**Objetivo:** identificar os cheiros de codigo mais frequentes, entender por que eles aumentam o custo de mudanca e priorizar correcoes por risco.

**Ferramenta:** GitHub Copilot Chat / Explorer (ou agente equivalente com `@workspace`).

**Material sugerido:**

| Arquivo | Papel |
| -------- | ------ |
| `checkout_service.py` | Exemplo propositalmente com smells: funcao longa, duplicacao, estado global, magic numbers e responsabilidades misturadas. |
| `example.py` | Execucao rapida para observar fluxo e alimentar as perguntas no chat. |

**Como usar:** abra `checkout_service.py` no editor, use **`@workspace`** (ou anexe o arquivo) e rode os prompts abaixo. O foco desta aula e **detectar, classificar e priorizar smells**, sem pedir refatoracao completa.

---

## 1. Inventario de smells

```
@checkout_service.py

Audite este arquivo e liste os code smells mais comuns presentes.

Quero no formato:
- smell
- onde aparece (funcao/trecho)
- por que e um problema
- risco de mudanca (baixo/medio/alto)

Nao proponha refatoracao ainda.
```

---

## 2. Smells que mais doem no negocio

```
@checkout_service.py

Priorize os 3 code smells mais perigosos para o negocio neste modulo.

Para cada um:
1) impacto pratico (erro de cobranca, atraso de entrega, retrabalho etc.)
2) sinal de que esse risco ja pode estar acontecendo
3) custo estimado de manter como esta por mais 3 meses
```

---

## 3. Acoplamento e efeito dominó

```
@checkout_service.py

Mapeie acoplamentos rigidos e efeitos colaterais.

Para cada ponto, responda:
"Se eu mudar X, o que pode quebrar em Y?"

Destaque mutacao de estado global, I/O no meio da regra e dependencias implicitas.
```

---

## 4. Duplicacao e divergencia de regra

```
@checkout_service.py

Procure logicas duplicadas ou quase duplicadas.

Explique:
- em quais funcoes aparece duplicacao;
- qual o risco de "uma regra evoluir e a outra ficar para tras";
- exemplo de bug que isso pode gerar.

Nao escreva codigo.
```

---

## 5. Plano minimo de protecao

```
@checkout_service.py

Sem refatorar ainda, proponha uma rede de protecao minima:
- 5 testes de caracterizacao (titulo + entrada + resultado esperado em linguagem natural)
- 3 contratos/invariantes que deveriam ser documentados no modulo

Foque em reduzir medo de mudanca.
```

---

## Maxima da aula

**Code smell nao e vaidade tecnica.** E sinal de risco operacional: quanto pior o cheiro, maior o custo para mudar com seguranca.
