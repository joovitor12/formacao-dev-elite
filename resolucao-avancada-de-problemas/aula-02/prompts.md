# Aula 02 — Prompts para analisar logs (console, rede, servidor)

**Como usar:** copie o bloco, cole no chat do agente e **preencha** `[]` ou anexe o arquivo de log (`@caminho/do/export.txt`).

---

## 1. Visão geral e severidade

```
Analise este log de console (ou servidor) e categorize os problemas por severidade: Erro, Aviso, Performance (e outras categorias que fizerem sentido, ex.: rede, deprecação).

Identifique os principais ofensores: arquivos, funções e linhas quando aparecerem em stack traces.

Log:
[cole aqui ou @arquivo]
```

---

## 2. Correlação temporal (o que veio antes do erro)

```
No trecho abaixo do log, o erro em [LINHA ou TIMESTAMP] é precedido por [ex.: PUT /api/..., warning do React, violation]. 

Qual a hipótese mais provável que liga esses eventos? Distinga correlação de causa e diga o que confirmar no Network tab ou no código.

Trecho do log (ordenado por tempo):
[cole aqui ou @arquivo com intervalo de linhas]
```

---

## 3. Erro + stack → causa raiz (sem pedir patch)

```
Não quero correção de código ainda. Com base apenas neste log (mensagens, stacks, requisições adjacentes), explique a causa raiz provável deste erro e o fluxo que leva até ele.

Erro + stack:
[cole aqui]

Contexto opcional (arquivo do projeto):
[@arquivo]
```

---

## 4. Rede + corpo da resposta (contrato de API)

```
Relacione falhas ou exceções no log com as requisições HTTP imediatamente anteriores. 

Hipótese: a resposta de [MÉTODO] [PATH] tem formato diferente do que o cliente assume (ex.: PUT sem `user`, GET com `user`). O que o log permite inferir e o que exigiria inspeção manual no DevTools?

Log + trechos de axios/fetch se houver:
[cole ou @arquivo]
```

---

## 5. Performance (Violations, long tasks, frames)

```
Liste entradas do log relacionadas a performance: [Violation], long tasks, measureLayout, etc.

Para cada uma, indique severidade relativa, possível origem a partir de stacks ou nomes de handlers, e uma pergunta concreta para o profiler ou para o código.

Log:
[cole ou @arquivo]
```

---

## 6. Ruído vs sinal (HMR, extensões, devtools)

```
Separe este log em: (A) problemas que provavelmente existem em produção, (B) ruído de desenvolvimento (HMR, Vite, Redux DevTools), (C) possível interferência de extensão de browser (ex.: chrome-extension://).

O que eu deveria filtrar ou reproduzir em janela anônima antes de priorizar correções?

Log:
[cole ou @arquivo]
```

---

## 7. Padrão recorrente (contagem e priorização)

```
Este log tem muitas repetições. Agrupe mensagens idênticas ou similares, estime frequência, e ordene grupos por impacto (usuário bloqueado, degradação, aviso futuro).

Sugira no máximo 3 frentes de trabalho para a próxima sprint.

Log:
[cole ou @arquivo]
```

---

## 8. React: warning de atualização durante render

```
O log mostra avisos do tipo "Cannot update a component (X) while rendering a different component (Y)". 

Explique o anti-padrão, onde costuma estar o bug (quem dispara setState durante render), e que perguntas fazer ao código sem ainda reescrever componentes.

Trecho do log + nomes dos componentes:
[cole aqui]
```

---

## 9. Checklist antes de “consertar pelo log”

- O erro está **amarrado** a um request/response ou só a **ordem** no log?
- Existe **race** (várias chamadas paralelas ao mesmo endpoint)?
- O stack aponta para **código meu** ou para **node_modules / extensão**?
- Há **sanitização** do log (PII removida) que esconde o corpo útil da resposta?

---

## Máxima da aula

**Log ordenado no tempo é evidência; stack e método HTTP sugerem onde olhar; confirmação final é no contrato (rede + código).**
