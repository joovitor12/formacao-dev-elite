# Aula 11 — Reescrita de algoritmos

**Objetivo:** usar IA para reescrever algoritmos mantendo o mesmo contrato funcional, reduzindo complexidade e aumentando clareza sem introduzir regressões.

**Material sugerido:**

| Caminho | Papel |
| -------- | ------ |
| `pre-changes/` | Baseline com algoritmo menos eficiente para reescrita guiada. |
| Raiz da pasta da aula | Versão reescrita para comparar corretude e custo. |

**Como usar:** anexe `@matcher.py`, `@dataset.py` e os testes. Sempre peça: contrato atual, plano de reescrita, riscos e evidências de validação.

---

## 1. Diagnosticar algoritmo atual antes de reescrever

```
Analise matcher.py e responda:
- qual problema o algoritmo resolve;
- qual a complexidade atual (tempo/memoria);
- quais trechos dificultam manutenção;
- qual risco ao reescrever.

Nao escreva código ainda.

@matcher.py
```

---

## 2. Plano de reescrita com segurança

```
Proponha um plano em 5 passos para reescrever o algoritmo mantendo o contrato.

Inclua:
1) hipótese de ganho;
2) invariantes que não podem quebrar;
3) pontos de teste obrigatórios;
4) critério de rollback.

@matcher.py @test_matcher_correctness.py
```

---

## 3. Reescrita mínima orientada a contrato

```
Reescreva o algoritmo para reduzir custo assintótico, mantendo assinatura pública e formato de saída.

Requisitos:
- preserva comportamento esperado;
- melhora legibilidade;
- sem refatorações fora de escopo.

@matcher.py @test_matcher_correctness.py
```

---

## 4. Validar equivalência funcional

```
Revise os testes e garanta cobertura de:
- caso feliz;
- ausência de correspondência;
- entradas com duplicidade;
- estabilidade de ordenação quando houver empate.

Se faltar, sugira testes novos.

@test_matcher_correctness.py @matcher.py
```

---

## 5. Validar ganho de custo

```
Analise test_rewrite_budget.py e explique:
- que regressão de algoritmo ele evita;
- como interpretar falha de budget;
- como calibrar limite sem mascarar piora real.

@test_rewrite_budget.py @matcher.py
```

---

## 6. Comparar antes e depois da reescrita

```
Compare pre-changes/matcher.py com matcher.py.

Entregue tabela:
trecho | antes | depois | impacto de complexidade | risco residual.

@pre-changes/matcher.py @matcher.py
```

---

## 7. Prompt curto de revisão final

```
Faça revisão final da reescrita:
- contrato funcional preservado?
- ganho de complexidade comprovado?
- algum trecho ainda merece simplificação?

Responda em até 6 bullets.

@matcher.py @test_matcher_correctness.py @test_rewrite_budget.py
```

---

## Checklist da aula

- Reescrita manteve contrato público.
- Complexidade melhorou com evidência.
- Testes funcionais cobrem casos críticos.
- Budget protege contra regressão.
- Antes/depois está documentado.

---

## Máxima da aula

**Reescrever não é “fazer bonito”:** é trocar estratégia com segurança, preservar comportamento e provar ganho real.
