# Aula 10 — Sugestoes algoritmicas com IA

**Objetivo:** usar IA para propor alternativas de algoritmo, comparar trade-offs (tempo, memoria, legibilidade) e escolher uma estrategia consistente com o contexto do problema.

**Material sugerido:**

| Caminho | Papel |
| -------- | ------ |
| `pre-changes/` | Baseline menos eficiente para estimular sugestoes da IA. |
| Raiz da pasta da aula | Versao atual para avaliar escolhas de algoritmo. |

**Como usar:** anexe **`@recommender.py`**, **`@dataset.py`** e os testes. Sempre peça comparacao entre abordagens, com justificativa de custo e impacto.

---

## 1. Levantamento de alternativas algoritmicas

```
Analise recommender.py e proponha 3 alternativas de algoritmo para o mesmo problema.

Para cada alternativa, detalhe:
- ideia central;
- complexidade de tempo;
- custo de memoria;
- quando ela e melhor/pior.

Nao codar ainda. Quero comparacao.

@recommender.py
```

---

## 2. Escolha orientada por contexto

```
Com dados de entrada de tamanho medio (100 a 10k interacoes), qual algoritmo voce escolheria e por que?

Responda com:
1) algoritmo escolhido;
2) criterio de decisao;
3) risco tecnico;
4) plano B se o volume crescer 10x.

@recommender.py @dataset.py
```

---

## 3. Refactor minimo com algoritmo melhor

```
Implemente a alternativa de melhor custo-beneficio sem alterar assinatura publica das funcoes.

Requisitos:
- preservar corretude;
- reduzir custo assintotico;
- evitar complexidade desnecessaria no codigo.

@recommender.py @test_recommender_correctness.py
```

---

## 4. Validacao de corretude e estabilidade

```
Revise os testes e confirme se cobrem:
- usuario com historico;
- usuario sem historico;
- itens repetidos;
- desempate estavel no ranking.

Se faltar algo, proponha teste adicional.

@test_recommender_correctness.py @recommender.py
```

---

## 5. Validacao de custo com budget

```
Analise test_algorithm_budget.py e explique:
- o que esse budget protege;
- qual mudanca faria falhar;
- como ajustar o limite sem permitir regressao silenciosa.

@test_algorithm_budget.py @recommender.py
```

---

## 6. Comparar baseline e versao atual

```
Compare pre-changes/recommender.py com recommender.py e entregue tabela:
trecho | antes | depois | ganho esperado | trade-off.

@pre-changes/recommender.py @recommender.py
```

---

## 7. Prompt curto para revisao final

```
Faça revisao final da solucao:
- algoritmo escolhido esta coerente com o contexto?
- ha risco de regressao de performance?
- os testes atuais sustentam merge com seguranca?

Responda em ate 6 bullets.

@recommender.py @test_recommender_correctness.py @test_algorithm_budget.py
```

---

## Checklist da aula

- Existem alternativas algoritmicas comparadas com criterio claro.
- O algoritmo escolhido reduz custo relevante.
- Corretude validada por testes.
- Budget protege contra regressao.
- Trade-offs documentados (nao so ganho).

---

## Maxima da aula

**IA sugere caminhos; engenharia escolhe compromisso.** O melhor algoritmo depende do contexto, dos limites do sistema e da qualidade da validacao.
