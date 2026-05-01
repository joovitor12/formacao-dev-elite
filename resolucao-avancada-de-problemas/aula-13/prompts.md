# Aula 13 — Benchmark orientado

**Objetivo:** saber medir com método — definir pergunta de benchmark, baseline, carga de trabalho reproduzível e métrica correta — antes de “otimizar no feeling” ou aceitar números sem contexto.

**Material sugerido:**

| Caminho | Papel |
| -------- | ------ |
| `pre-changes/` | Implementação mais cara para comparar com a versão atual. |
| Raiz da pasta da aula | Motor de agregação + harness simples de medição. |

**Como usar:** anexe `@stats_engine.py`, `@benchmark_harness.py`, `@dataset.py` e os testes. Peça sempre: hipótese de medição, isolamento de variáveis, critério de sucesso.

---

## 1. Pergunta de benchmark clara (antes de medir)

```
Quero comparar duas estratégias de agregação sem rodar código ainda.

Formule:
1) a pergunta exata que o benchmark deve responder;
2) o que é variável controlada vs o que é ruído;
3) qual métrica primária (tempo de parede, operações contadas, throughput).

Use apenas stats_engine.py e dataset.py como referência de domínio.

@stats_engine.py @dataset.py
```

---

## 2. Baseline e reprodutibilidade

```
Explique como definir baseline e carga fixa para comparar implementações com confiança.

Inclua:
- tamanho da entrada;
- como repetir execução sem cache externo confundindo;
- quando usar warm-up (se aplicável).

@benchmark_harness.py @dataset.py
```

---

## 3. Harness de medição sem mentir para si mesmo

```
Revise benchmark_harness.py e diga:
- o que ele mede bem;
- quais armadilhas comuns ainda existem (GC, JIT inexistente em Python puro, etc.);
- como interpretar min_ms vs única execução.

@benchmark_harness.py
```

---

## 4. Equivalência funcional antes de comparar performance

```
Antes de declarar “mais rápido”, preciso garantir mesmo resultado.

Liste asserts mínimos para aggregate_sum_by_group:
- totais por grupo;
- grupos sem linhas (devem ficar ausentes ou zero conforme contrato atual).

@test_stats_correctness.py @stats_engine.py
```

---

## 5. Budget de operações como proxy de custo

```
Analise test_benchmark_budget.py.

Explique:
- qual regressão esse budget detecta;
- por que proxy por operações ajuda em CI;
- quando substituir por medição de tempo real.

@test_benchmark_budget.py @stats_engine.py
```

---

## 6. Comparar baseline caro vs versão atual

```
Compare pre-changes/stats_engine.py com stats_engine.py.

Entregue tabela:
trecho | antes | depois | impacto esperado em custo | trade-off (memória/extra estrutura).

@pre-changes/stats_engine.py @stats_engine.py
```

---

## 7. Prompt curto para decisão final

```
Com base em evidência de benchmark orientado, esta versão deve ir para merge?

Responda em até 6 bullets com:
corretude, métrica dominante, risco residual, próximo experimento se volume dobrar.

@stats_engine.py @test_stats_correctness.py @test_benchmark_budget.py
```

---

## Checklist da aula

- Pergunta de benchmark está escrita em uma frase.
- Baseline e carga são reproduzíveis.
- Métrica primária foi escolhida com critério (não misturar tempo e ops sem explicar).
- Corretude foi travada antes da disputa de performance.
- Interpretação inclui limitações do harness.

---

## Máxima da aula

**Benchmark sem pergunta é ruído.** Orientar a medição é o que transforma número em decisão de engenharia.
