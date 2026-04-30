# Aula 12 — Avaliacao de trade-offs

**Objetivo:** usar IA para comparar alternativas de implementacao com criterio tecnico, explicitando ganhos e custos de cada caminho (performance, memoria, legibilidade, risco e manutencao).

**Material sugerido:**

| Caminho | Papel |
| -------- | ------ |
| `pre-changes/` | Baseline com escolha mais simples, porem menos eficiente. |
| Raiz da pasta da aula | Versao alternativa com melhor performance e maior custo estrutural. |

**Como usar:** anexe `@cache_service.py`, `@dataset.py` e os testes. Sempre peça comparacao objetiva entre opcoes com recomendacao contextual.

---

## 1. Mapear alternativas e trade-offs

```
Analise cache_service.py e descreva 2 alternativas de estrategia para resolver o mesmo problema.

Para cada alternativa, detalhe:
- complexidade de tempo;
- custo de memoria;
- facilidade de manutencao;
- risco de bug.

Nao codar ainda.

@cache_service.py
```

---

## 2. Decidir com base em contexto real

```
Contexto: volume medio com picos, time pequeno e necessidade de previsibilidade.

Com base no codigo atual, qual alternativa voce escolheria e por que?
Responda com:
1) recomendacao;
2) quando nao escolher essa opcao;
3) sinal de que precisamos migrar para outra estrategia.

@cache_service.py @dataset.py
```

---

## 3. Refactor orientado a trade-off

```
Aplique a melhoria com melhor custo-beneficio sem quebrar assinatura publica.

Requisitos:
- manter corretude;
- explicitar no codigo o ponto de trade-off principal;
- evitar overengineering.

@cache_service.py @test_cache_correctness.py
```

---

## 4. Validar risco de regressao funcional

```
Revise os testes e confirme cobertura de:
- cache hit;
- cache miss;
- invalidação;
- consistencia de retorno entre chamadas.

Se faltar algum caso, proponha teste.

@test_cache_correctness.py @cache_service.py
```

---

## 5. Validar custo operacional da escolha

```
Analise test_tradeoff_budget.py e explique:
- que custo ele protege (tempo/memoria/operações);
- qual regressao ele detecta;
- como ajustar threshold sem mascarar piora.

@test_tradeoff_budget.py @cache_service.py
```

---

## 6. Comparar antes/depois da decisao

```
Compare pre-changes/cache_service.py com cache_service.py.

Entregue tabela:
aspecto | antes | depois | ganho | custo pago.

@pre-changes/cache_service.py @cache_service.py
```

---

## 7. Prompt curto de recomendacao final

```
Faça recomendacao final para merge com foco em trade-off:
- escolha atual esta equilibrada?
- risco residual aceitavel?
- qual monitoramento minimo manter em producao?

Responda em ate 6 bullets.

@cache_service.py @test_cache_correctness.py @test_tradeoff_budget.py
```

---

## Checklist da aula

- Trade-offs foram explicitados com criterio.
- Decisao foi contextual, nao absoluta.
- Corretude funcional preservada por testes.
- Budget protege contra regressao relevante.
- Custo pago da decisao ficou documentado.

---

## Maxima da aula

**Nao existe algoritmo "melhor" no vazio.** Em engenharia, a melhor escolha e a que equilibra ganho, risco e contexto operacional.
