# Aula 06 — Validacao da correcao

**Objetivo:** usar IA para validar se a correcao realmente resolveu o problema sem criar regressao. O foco aqui nao e implementar patch novo, e sim verificar comportamento esperado, cobertura de cenarios e qualidade de evidencias.

**Material sugerido:**

| Caminho | Papel |
| -------- | ------ |
| `pre-changes/` | Snapshot com comportamento antigo (bug conhecido), util para comparacao e demonstracao. |
| Raiz da pasta da aula | Versao corrigida em validacao (`mapper.py`, `ingest_service.py`, testes e `example.py`). |

**Como usar:** no chat do agente, use **`@workspace`** e anexe **`@mapper.py`**, **`@ingest_service.py`**, **`@schema.py`** e testes (`@test_api_id_characterization.py`, `@test_current_behavior_characterization.py`). Sempre peca evidencias objetivas (teste, tabela de casos, diff de comportamento).

---

## 1. Contrato de validacao (antes de rodar)

```
Quero validar uma correcao de ingestao JSON.

Com base em schema.py, mapper.py e ingest_service.py, escreva um contrato de validacao com no maximo 8 regras no formato:
"Dado payload X, o sistema deve Y".

Inclua explicitamente:
- id no root;
- envelope `record`;
- alias `recordId`;
- id aninhado em `data`;
- item em `items`;
- caso sem identificador (erro esperado).

Nao escreva patch. So criterios verificaveis.

@schema.py @mapper.py @ingest_service.py
```

---

## 2. Matriz de casos (cobertura minima)

```
Monte uma matriz de testes para validar a correcao com colunas:
caso | payload minimo | resultado esperado | tipo (happy-path, borda, erro).

Quero pelo menos 10 casos: 6 positivos e 4 negativos.
Nos negativos, diga qual erro deve aparecer e em qual camada (ingest ou mapper).

@mapper.py @ingest_service.py @schema.py
```

---

## 3. Revisao dos testes atuais

```
Revise os testes atuais e diga:
1) o que ja cobre bem;
2) quais lacunas de regressao ainda existem;
3) quais 3 testes eu deveria adicionar primeiro.

Nao altere codigo ainda. So analise e priorize por risco.

@test_api_id_characterization.py @test_current_behavior_characterization.py @test_mapper_api_shapes.py
```

---

## 4. Gerar testes de regressao faltantes

```
Com base nas lacunas identificadas, gere testes pytest adicionais para validar a correcao sem mudar o codigo de producao.

Requisitos:
- nomes de teste explicitos;
- casos positivos e negativos;
- asserts de mensagem/tipo de erro quando aplicavel.

@mapper.py @ingest_service.py @test_current_behavior_characterization.py
```

---

## 5. Comparacao com baseline antigo

```
Compare `pre-changes/` com os arquivos atuais e explique, em tabela:
arquivo | diferenca funcional | impacto na validacao.

Depois liste 3 cenarios que ainda podem falhar mesmo com a correcao aplicada.

@pre-changes/mapper.py @pre-changes/ingest_service.py @mapper.py @ingest_service.py
```

---

## 6. Teste de robustez do contrato

```
Proponha payloads "sujos" para stress da correcao:
- tipos inesperados (string em vez de dict, lista vazia, null);
- estruturas parcialmente validas;
- combinacao de chaves ambiguas.

Para cada payload, diga o comportamento ideal e como transformar isso em teste automatizado.

@mapper.py @ingest_service.py
```

---

## 7. Prompt curto para validacao final

```
Valide se a correcao esta pronta para merge:
- rode os testes existentes e os de regressao;
- confirme que casos aceitos continuam passando;
- confirme que casos invalidos falham de forma explicita;
- aponte qualquer risco residual em no maximo 3 bullets.

@test_api_id_characterization.py @test_current_behavior_characterization.py @mapper.py @ingest_service.py @example.py
```

---

## Checklist de saida

- Existe evidencia de comportamento correto para casos principais e bordas.
- Regressao coberta para envelopes (`record`, `data`, `items`) e alias (`recordId`).
- Caso sem identificador tem erro claro e estavel.
- Diferenca entre baseline antigo e versao atual esta documentada.
- A validacao nao depende de suposicao; depende de teste reproduzivel.

---

## Maxima da aula

**Correcao sem validacao e so otimismo.** A IA ajuda a acelerar analise e testes, mas a confianca vem de evidencias reproduziveis.
