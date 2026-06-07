# Aula 02 — O que a IA avalia em PRs

**Objetivo:** mapear **o que o Copilot Code Review costuma avaliar** (e o que escapa) — classificar achados por dimensão e identificar pontos cegos.

**Ferramenta:** GitHub (PR + Copilot Code Review).

**Material:**

| Arquivo | Papel |
| -------- | ------ |
| `rollback_service.py` | Código com issues **por dimensão** (segurança, correção sutil, operação). |
| `matriz_avaliacao_ia.md` | Dimensões e limites típicos da IA. |
| `classificacao_review.md` | Planilha para classificar saída do Copilot. |
| `example.py` | Comportamento na fronteira `should_rollback`. |

**Fluxo em sala:**

1. Abrir PR alterando `rollback_service.py`.
2. Rodar Copilot Code Review.
3. Classificar **cada** comentário na matriz.
4. Preencher **pontos cegos** (o que a IA não disse e você diria).

---

## 1. Ler a matriz antes do PR

```
@matriz_avaliacao_ia.md

Em uma frase por dimensão: o que você espera que o Copilot **avalie** em um PR de Python/DevOps?

Não analise rollback_service.py ainda.
```

---

## 2. Hipóteses por trecho (antes do Copilot)

```
@rollback_service.py @matriz_avaliacao_ia.md

Para cada smell intencional no arquivo, preveja:

- dimensão da matriz;
- Copilot **vai** / **pode** / **não vai** comentar.

Formato: trecho → dimensão → previsão.

Não abra o PR ainda.
```

---

## 3. Classificar saída do Copilot

```
Cole os comentários do Copilot Code Review no PR.

@matriz_avaliacao_ia.md @classificacao_review.md

Preencha a tabela de classificação:

- dimensão;
- qualidade do achado (sim / parcial / nit / falso positivo);
- sua concordância.

Não implemente correções.
```

---

## 4. Pontos cegos

```
@rollback_service.py @classificacao_review.md

Liste 2 achados **importantes** que o Copilot **não** comentou (ou comentou mal).

Para cada um: dimensão, risco operacional, por que a IA pode ter perdido.
```

---

## 5. Falso positivo vs nit

```
Dos comentários do Copilot neste PR:

Quais você marcaria como nit ou falso positivo no merge?

Justifique com base na matriz — não no gosto pessoal de estilo.
```

---

## 6. Síntese da taxonomia

```
@classificacao_review.md @matriz_avaliacao_ia.md

Em 4 bullets: o que você aprendeu sobre **limites** da avaliação automática em PRs?

Inclua: dimensão mais coberta, dimensão negligenciada, um falso positivo e um ponto cego humano.
```

## Comandos úteis

```bash
cd aula-02
python example.py
```

---

## Máxima da aula

**Copilot varre o diff por padrões — a matriz mostra o que entrou no radar e o que ficou fora.**
