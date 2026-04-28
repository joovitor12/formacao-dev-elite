# Aula 05 — Correções orientadas por IA

**Objetivo:** usar o agente como **executor disciplinado**: você define evidência (stack, contrato da API, testes de caracterização); a IA propõe mudanças pequenas e revertíveis; você mantém critérios de aceite claros antes de aceitar o patch.

**Material sugerido:**

| Caminho | Papel |
| -------- | ------ |
| `pre-changes/` | Snapshot **antes** da correção: ingest ingênuo + mapper estrito que reproduzem o erro da aula (útil como diff e para resetar o exercício). |
| Raiz da pasta da aula | **Código de trabalho** — onde você aplica ingestão, mapper, testes `pytest` e `example.py`. |

Se ainda não tiver uma cópia local do cenário em `pre-changes/`, duplique os arquivos base da própria pasta da aula para esse snapshot e mantenha a mesma estrutura.

**Como usar:** no chat do agente, use **`@workspace`** e anexe **`@mapper.py`**, **`@ingest_service.py`**, **`@schema.py`** e, quando existir, **`@test_api_id_characterization.py`**. Separe **caracterização** (comportamento atual) de **correção** (comportamento desejado) nos seus próprios prompts.

---

## 1. Da hipótese ao contrato de aceite (sem código ainda)

```
Tenho hipóteses para KeyError em 'id' durante ingestão de JSON.

Quero transformar isso em **critérios de aceite testáveis**: liste bullets do tipo "dado payload X (cite schema.py ou JSON inline), o sistema deve produzir internal_id=Y sem KeyError".

Inclua explicitamente: envelope `record`, `id` só em `data`, lista em `items`, e alias camelCase `recordId`. Não escreva patch de produção — só o contrato em linguagem natural + exemplos mínimos.

@schema.py @mapper.py @ingest_service.py
```

---

## 2. Script de caracterização antes de corrigir (mantém o bug visível)

```
Gere um arquivo de testes com pytest que **caracterize** o comportamento atual de `ingest_raw_json` e `map_record_to_internal`: para cada formato de payload (id no root, id em data, recordId em record, items[]), indique se hoje esperamos KeyError 'id' ou sucesso.

Requisitos:
- parametrização ou tabela clara nos nomes dos casos;
- não alterar o código de produção neste passo.

@mapper.py @ingest_service.py
```

---

## 3. Correção mínima guiada pelos testes (passo único)

```
Os testes de caracterização mostram onde estoura KeyError. Implemente a **correção mínima** para que todos os formatos aceitos no contrato definido acima passem, preferindo:

1) normalização de envelope num único lugar (mapper ou ingest — escolha e justifique em 2 frases);
2) resolver identificador com `id` ou fallback `recordId`;
3) sem alterar nomes públicos das funções exportadas sem necessidade.

Atualize ou substitua os testes para refletirem o comportamento **correto**, não o bug.

@mapper.py @ingest_service.py @test_api_id_characterization.py
```

---

## 4. Revisão da IA como “reviewer” (regressão e escopo)

```
Acabei de aplicar um patch que normaliza JSON da API. Atue como revisor de PR:

- O diff resolve o KeyError sem esconder payloads inválidos?
- Há risco de loop infinito ou de descer níveis demais em dicts aninhados?
- Liste 3 cenários de regressão que eu devo cobrir com teste manual ou assert.

Cole ou referencie o diff / arquivos atuais com @mapper.py @ingest_service.py
```

---

## 5. Comparar baseline `pre-changes` vs versão corrigida

```
Tenho duas árvores: `pre-changes/` (bug conhecido) e os arquivos na raiz (corrigidos).

Resuma em uma tabela: arquivo, o que mudou em uma frase, e qual hipótese esta mudança endereça.

Não proponha novas features — só amarrar mudança ↔ evidência.

@pre-changes/mapper.py @pre-changes/ingest_service.py @mapper.py @ingest_service.py
```

*(Se `pre-changes/` não existir nesta pasta, ajuste os `@` para os caminhos reais do seu workspace.)*

---

## 6. Erro claro quando o contrato não bate

```
Após normalização, um payload ainda pode não ter identificador (`id` nem `recordId`). 

Sugira comportamento consistente: manter KeyError('id'), ou ValueError com mensagem explícita — em uma única função de resolução de ID. Escreva o snippet enxuto e onde encaixar no fluxo atual.

@mapper.py
```

---

## 7. Prompt curto para “só integrar e rodar testes”

```
Integre as validações/normalizações necessárias em mapper.py e ingest_service.py conforme os testes em test_api_id_characterization.py. Rode mentalmente o fluxo de example.py e garanta que pytest passa.

@test_api_id_characterization.py @mapper.py @ingest_service.py @example.py
```

---

## Checklist antes do merge

- Os testes descrevem **comportamento desejado**, não só “o que o código faz hoje”.
- Uma única camada é responsável por **desembrulhar** envelope (`record` / `data` / `items`) para evitar duplicar lógica entre ingest e mapper — ou a duplicação está documentada de propósito.
- Caso feliz **e** caso sem ID estão cobertos (sucesso explícito ou erro explícito).
- Você comparou `pre-changes/` com a versão final para não misturar exercício com fix parcial no branch errado.

---

## Máxima da aula

**A IA acelera o patch; você segura o escopo.** Defina antes o contrato (testes + exemplos em `schema.py`), peça mudanças pequenas e exija revisão contra regressão — sobretudo na borda com sistemas externos (JSON, APIs, nomes de campos).
