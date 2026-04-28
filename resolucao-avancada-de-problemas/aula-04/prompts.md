# Aula 39 — Prompts para formulação de hipóteses (debugging)

**Como usar:** no GitHub Copilot Chat (ou agente equivalente), use **`@workspace`** e referencie os arquivos da pasta desta aula — em especial `@schema.py`, `@ingest_service.py` e `@mapper.py`. Cole o stack trace ou descreva o sintoma quando o bloco pedir. **Ainda não peça o fix final:** o objetivo é listar hipóteses testáveis e provas rápidas.

---

## 1. Hipóteses a partir de evidência + código (prompt de elite)

```
Analisei o stack trace e sei que o erro é um KeyError no mapper.py (acesso à chave 'id').

Olhando para ingest_service.py e o schema de entrada (exemplos em schema.py), gere exatamente 3 hipóteses distintas para o campo 'id' estar ausente no dict que chega ao mapper.

Considere, em hipóteses separadas:
- falha ou mudança na API externa (nomes de campos, envelope, versão);
- erro de parse ou de extração do JSON (nível errado do dict, lista vs objeto);
- mudança de contrato (snake_case vs camelCase, chave renomeada, id aninhado).

Para cada hipótese, diga em uma frase como eu poderia provar ou refutar com um teste ou um log pontual (sem escrever o patch de produção ainda).

@schema.py @ingest_service.py @mapper.py
```

---

## 2. Só sintoma + arquivos (sem stack completo)

```
Tenho KeyError: 'id' ao ingerir JSON. Não vou colar o traceback agora.

Com base apenas nestes arquivos do projeto, quais são as 3 causas mais plausíveis e em que ordem você investigaria? Justifique a ordem com “o que costuma mudar primeiro” (deploy, fornecedor, refactor local).

@ingest_service.py @mapper.py @schema.py
```

---

## 3. Aprofundar uma hipótese (API / contrato)

```
Hipótese: a API externa mudou o formato (ex.: camelCase em vez de snake_case, ou renomeou 'id' para outro nome).

Com base em schema.py e no que mapper.py assume, liste sinais no JSON que confirmariam ou enfraqueceriam essa hipótese. Não sugira código de produção; sugira o que inspecionar (campo a campo) ou um caso de teste mínimo.
```

---

## 4. Aprofundar uma hipótese (parse / nível do dict)

```
Hipótese: o JSON está correto, mas ingest_service.py entrega ao mapper o dict errado (ex.: envelope inteiro, ou nó 'data' / 'items' não tratado).

Explique o fluxo atual: de `json.loads` até `map_record_to_internal`. Onde um payload válido poderia virar um dict sem 'id' no topo? Cite linhas ou nomes de função dos arquivos anexados.

@ingest_service.py @mapper.py
```

---

## 5. Prova rápida — script de teste (hipótese “mudança na API”)

```
Gere um script de teste (unittest ou pytest, o que for mais simples no repo) que simule respostas da API com o identificador do recurso em posições ou nomes diferentes (ex.: 'id' no root, 'id' dentro de 'data', 'recordId', primeiro item de 'items').

O objetivo é ver em quais formatos map_record_to_internal / ingest_raw_json quebram com KeyError 'id' e em quais não — ainda não quero corrigir o código de produção, só caracterizar o comportamento.

@mapper.py @ingest_service.py
```

---

## 6. Prova rápida — log mental / assert exploratório

```
Quero uma lista de 5 asserts ou prints temporários (em pseudocódigo ou Python curto) que eu colocaria antes da linha que acessa record['id'], para registrar: tipo de `record`, chaves de primeiro nível, e se 'id' ou aliases comuns existem. Ordene do menos invasivo ao mais verboso.
```

---

## 7. Filtro do especialista (probabilidade vs possibilidade)

```
A IA sugeriu várias hipóteses, incluindo algumas muito improváveis (ex.: bug no interpretador Python, corrupção de memória).

Separe em duas listas: (A) hipóteses que merecem teste neste sprint com o contexto de um ingest JSON; (B) hipóteses que eu deveria descartar até ter evidência forte. Use como critério: o que mudou recentemente (API, dependência, meu PR) vs especulação genérica.
```

---

## Checklist antes de “consertar” de verdade

- Cada hipótese tem uma **prova** (teste, log, request real) que a valida ou a mata?
- A hipótese escolhida explica **por que agora** (mudança recente), não só “pode acontecer”?
- Evite patch que **mascara** KeyError sem validar o contrato na borda (ingestão).
- Depois de corrigir, um caso que **passava antes** ainda passa (regressão)?

---

## Máxima da aula

**O Copilot traz possibilidades; você traz probabilidade.** Formular hipóteses testáveis evita horas de código que ataca a causa errada — primeiro prova qual mundo você está, depois faz a cirurgia (próxima aula: correções orientadas por IA).
