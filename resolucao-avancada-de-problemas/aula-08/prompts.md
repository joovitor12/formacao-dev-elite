# Aula 08 — Revisao de complexidade algoritmica

**Objetivo:** usar IA para revisar custo computacional de funcoes reais, encontrar gargalos de tempo, propor melhorias de estrutura de dados e validar se a complexidade ficou adequada ao volume esperado.

**Material sugerido:**

| Caminho | Papel |
| -------- | ------ |
| `pre-changes/` | Snapshot com versao menos eficiente para comparacao. |
| Raiz da pasta da aula | Versao atual para analise e validacao da melhoria. |

**Como usar:** no chat, combine **`@workspace`** com **`@analytics.py`**, **`@dataset.py`** e os testes. Sempre peca resposta com: complexidade atual, complexidade proposta, impacto pratico.

---

## 1. Diagnostico de complexidade (sem refatorar)

```
Analise as funcoes de analytics.py e identifique:
- complexidade de tempo (Big-O);
- complexidade de memoria;
- ponto de maior custo;
- efeito pratico quando o volume dobra.

Nao refatore ainda. Quero so diagnostico com justificativa.

@analytics.py
```

---

## 2. Encontrar loop aninhado evitavel

```
Marque trechos com risco de O(n*m) e explique como reduzir para algo proximo de O(n+m) usando estrutura auxiliar (dict/set).

Mostre o raciocinio em 4 passos:
1) onde repete trabalho;
2) qual indice auxiliar criar;
3) como muda o fluxo;
4) qual ganho esperado.

@analytics.py
```

---

## 3. Propor refactor minimo com mesmo contrato

```
Refatore mantendo assinatura publica das funcoes.

Requisitos:
- mesma saida funcional;
- menor custo assintotico;
- sem overengineering;
- comentarios curtos so em trechos nao obvios.

@analytics.py @test_spend_correctness.py
```

---

## 4. Validar corretude apos otimizacao

```
Revise os testes de corretude e confira se cobrem:
- cliente com varios pedidos;
- cliente sem pedido;
- pedidos de clientes inexistentes;
- valores acumulados.

Se faltar caso, proponha teste novo com nome claro.

@test_spend_correctness.py @analytics.py
```

---

## 5. Validar custo com budget de operacoes

```
Analise o teste de budget em test_complexity_budget.py.

Explique:
- por que esse tipo de teste ajuda em regressao de performance;
- qual comportamento faria o teste falhar;
- como ajustar threshold sem mascarar piora real.

@test_complexity_budget.py @analytics.py
```

---

## 6. Comparar baseline e versao atual

```
Compare pre-changes/analytics.py com analytics.py.

Entregue tabela:
trecho | antes | depois | impacto de complexidade | risco residual.

@pre-changes/analytics.py @analytics.py
```

---

## 7. Prompt curto para revisao final

```
Faça revisao final do modulo com foco em complexidade:
- ha regressao assintotica escondida?
- ha custo extra desnecessario de memoria?
- testes de corretude + budget sustentam o merge?

Responda em no maximo 6 bullets.

@analytics.py @test_spend_correctness.py @test_complexity_budget.py
```

---

## Checklist da aula

- Complexidade atual identificada com evidencia.
- Melhoria proposta reduz custo de forma mensuravel.
- Corretude preservada por testes.
- Budget de operacoes protege contra regressao.
- Comparacao antes/depois documentada.

---

## Maxima da aula

**Performance sem metodo vira chute.** Revisar complexidade com evidencias evita otimizar o lugar errado e protege o sistema de regressoes silenciosas.
