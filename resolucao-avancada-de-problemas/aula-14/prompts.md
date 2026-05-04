# Aula 14 — Boas práticas de otimização

**Objetivo:** consolidar hábitos saudáveis antes de mexer em performance: corretude primeiro, medição com método, mudanças pequenas e revisão de regressão — sem “otimizar no feeling”.

**Material sugerido:**

| Caminho | Papel |
| -------- | ------ |
| `pre-changes/` | Versão com má prática didática (trabalho repetido). |
| Raiz da pasta | Versão alinhada a boas práticas (uma passada clara). |

**Como usar:** anexe `@parity_sum.py`, `@dataset.py` e os testes. Peça sempre: o que medir, como validar corretude e qual risco da mudança.

---

## 1. Checklist antes de otimizar

```
Liste 6 boas práticas em ordem lógica para otimizar código com segurança.

Relacione cada item ao arquivo parity_sum.py ou aos testes quando fizer sentido.

@parity_sum.py @test_numbers_correctness.py
```

---

## 2. Corretude antes de velocidade

```
Explique por que alterar performance sem travar corretude é arriscado.

Sugira 2 asserts ou casos de teste mínimos que deveriam existir antes de qualquer “atalho”.

@test_numbers_correctness.py
```

---

## 3. Medir o que importa (sem overengineering)

```
Sem usar bibliotecas pesadas: como medir impacto neste projeto usando:

1) contagem de operações retornada por `sum_even_numbers` em parity_sum.py;
2) uma única medição de tempo com time.perf_counter no example.py.

Explique limitações de cada abordagem em 3 bullets.

@parity_sum.py @example.py
```

---

## 4. Evitar trabalho repetido

```
Compare mentalmente a raiz com pre-changes/parity_sum.py.

Qual má prática aparece no baseline e qual efeito em custo quando a lista cresce?

Não escreva patch ainda — só diagnóstico.

@pre-changes/parity_sum.py @parity_sum.py
```

---

## 5. Refactor mínimo guiado por evidência

```
Proponha a menor mudança possível no baseline para alinhar com boas práticas,

mantendo o mesmo resultado de sum_even_numbers.

Valide com os testes existentes.

@pre-changes/parity_sum.py @test_numbers_correctness.py @test_numbers_budget.py
```

---

## 6. Quando NÃO otimizar

```
Em que situações você deve evitar otimização mesmo vendo código “inelegante”?

Dê 4 exemplos curtos de contexto (time-to-market, risco, ganho marginal, etc.).
```

---

## 7. Revisão final antes do merge

```
Faça revisão final desta pasta como PR:

- corretude coberta?
- budget protege regressão óbvia?
- código permanece legível?

Responda em até 6 bullets.

@parity_sum.py @test_numbers_correctness.py @test_numbers_budget.py
```

---

## Checklist da aula

- Nomes de módulo evitam conflito com a biblioteca padrão (ex.: não usar `numbers.py` em Python).
- Hipótese de ganho está explícita.
- Corretude foi preservada ou melhor coberta por testes.
- Mudança é pequena e reversível.
- Trade-off legibilidade vs ganho foi considerado.
- Baseline ruim foi reconhecido sem romantizar “micro otimização”.

---

## Máxima da aula

**Otimizar bem é disciplina:** primeiro entender o problema e provar o comportamento; só então reduzir trabalho inútil com evidência.
