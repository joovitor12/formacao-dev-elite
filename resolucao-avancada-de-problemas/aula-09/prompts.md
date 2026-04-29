# Aula 09 — Identificacao de gargalos

**Objetivo:** usar IA para localizar gargalos reais de processamento, separar sintoma de causa raiz e priorizar melhorias com maior impacto no tempo total.

**Material sugerido:**

| Caminho | Papel |
| -------- | ------ |
| `pre-changes/` | Baseline com gargalos intencionais para investigacao. |
| Raiz da pasta da aula | Versao atual com fluxo mais eficiente para comparacao. |

**Como usar:** anexe **`@pipeline.py`**, **`@dataset.py`** e os testes. Peça sempre: onde esta o gargalo, como medir, e qual ganho esperado ao corrigir.

---

## 1. Mapa de custo por etapa

```
Analise pipeline.py e descreva as etapas do fluxo.

Para cada etapa, informe:
- operacoes dominantes;
- custo aproximado em Big-O;
- probabilidade de ser gargalo com dados grandes.

Nao refatore ainda.

@pipeline.py
```

---

## 2. Diferenciar gargalo principal de custos secundarios

```
Com base no codigo, separe em duas listas:
A) gargalos que dominam o tempo total;
B) custos pequenos que nao mudam o resultado final de performance.

Justifique cada item com evidencia do fluxo.

@pipeline.py
```

---

## 3. Instrumentacao leve para provar gargalo

```
Sugira instrumentacao minima (contadores, timestamps ou budget de operacoes) para provar qual trecho e o gargalo.

Quero:
- o que medir;
- onde medir;
- como interpretar o resultado.

@pipeline.py @test_bottleneck_budget.py
```

---

## 4. Refactor minimo orientado a impacto

```
Aplique a menor mudanca que reduz o gargalo principal sem mudar o contrato publico.

Requisitos:
- preservar corretude;
- manter codigo legivel;
- explicar em 2 frases por que essa mudanca ataca o gargalo dominante.

@pipeline.py @test_pipeline_correctness.py
```

---

## 5. Validacao antes/depois

```
Compare pre-changes/pipeline.py com pipeline.py e entregue:
trecho | antes | depois | efeito no gargalo | risco residual.

@pre-changes/pipeline.py @pipeline.py
```

---

## 6. Revisao de risco de regressao

```
Revise os testes e responda:
- o que protege corretude funcional;
- o que protege regressao de performance;
- qual caso extra voce adicionaria para evitar retorno do gargalo.

@test_pipeline_correctness.py @test_bottleneck_budget.py
```

---

## 7. Prompt curto de auditoria final

```
Faça auditoria final do modulo com foco em gargalos:
- gargalo principal foi eliminado ou apenas mascarado?
- existe novo gargalo relevante apos a mudanca?
- testes atuais sao suficientes para merge?

Responda em ate 6 bullets.

@pipeline.py @test_pipeline_correctness.py @test_bottleneck_budget.py
```

---

## Checklist da aula

- Gargalo principal identificado com evidencia.
- Melhoria atacou o ponto de maior impacto.
- Corretude funcional preservada.
- Regressao de performance coberta por teste/budget.
- Antes/depois documentado com clareza.

---

## Maxima da aula

**Nem todo custo e gargalo.** Melhorar performance de verdade exige medir, priorizar o trecho dominante e validar o impacto com evidencias.
