# Aula 07 — Documentando o aprendizado

**Objetivo:** transformar a resolucao tecnica em conhecimento reutilizavel. Nesta aula, a IA ajuda a organizar evidencias, registrar decisoes, explicitar trade-offs e deixar um historico claro para quem vai manter o codigo depois.

**Material sugerido:**

| Caminho | Papel |
| -------- | ------ |
| `pre-changes/` | Snapshot do comportamento antigo para comparacao e narrativa de evolucao. |
| Raiz da pasta da aula | Versao atual com codigo e testes que servem como fonte de evidencia. |

**Como usar:** no chat do agente, use **`@workspace`** e anexe **`@mapper.py`**, **`@ingest_service.py`**, **`@schema.py`**, **`@test_api_id_characterization.py`** e, quando util, os arquivos em `pre-changes/`. Peca saidas curtas, objetivas e com foco em comunicacao tecnica.

---

## 1. Resumo executivo da evolucao

```
Com base nos arquivos do projeto, escreva um resumo executivo em ate 8 bullets:
- problema observado;
- impacto no fluxo;
- estrategia adotada;
- resultado final validado.

Fale em linguagem de engenharia (nao marketing) e cite artefatos de evidencia (testes, exemplos, funcoes).

@mapper.py @ingest_service.py @schema.py @test_api_id_characterization.py
```

---

## 2. Linha do tempo tecnica (causa -> acao -> evidencia)

```
Monte uma linha do tempo em 4 etapas:
1) sintoma;
2) hipotese;
3) mudanca aplicada;
4) validacao.

Para cada etapa, inclua:
- entrada usada (arquivo/trace/payload);
- decisao tomada;
- evidencia produzida.

@pre-changes/mapper.py @pre-changes/ingest_service.py @mapper.py @ingest_service.py @test_current_behavior_characterization.py
```

---

## 3. ADR enxuto (registro de decisao)

```
Escreva um ADR curto (Architecture Decision Record) com as secoes:
Contexto, Decisao, Alternativas consideradas, Consequencias.

Tema: normalizacao de formatos JSON para resolver identificador (`id`/`recordId`) sem quebrar interfaces publicas.
Maximo de 15 linhas.

@mapper.py @ingest_service.py @schema.py
```

---

## 4. Post-mortem sem culpados

```
Crie um mini post-mortem tecnico sem blame, com:
- o que falhou;
- por que nao detectamos antes;
- o que mudou no processo para reduzir repeticao;
- metricas/sinais que valem monitorar.

Nao invente incidentes externos; use apenas o contexto do repositorio.

@pre-changes/mapper.py @ingest_service.py @test_mapper_api_shapes.py
```

---

## 5. FAQ de manutencao do modulo

```
Gere uma FAQ de 6 perguntas e respostas curtas para manutencao futura.

Inclua perguntas como:
- onde normalizar payload;
- quando retornar erro explicito;
- como adicionar novo formato de entrada sem regressao;
- quais testes atualizar primeiro.

@mapper.py @ingest_service.py @test_api_id_characterization.py
```

---

## 6. Checklist de handoff para outro dev

```
Monte um checklist de handoff para outro desenvolvedor assumir esse modulo.

Quero itens praticos:
- como reproduzir;
- quais testes rodar;
- quais arquivos ler primeiro;
- sinais de regressao;
- limites conhecidos.

Formato: checklist com [ ].

@example.py @mapper.py @ingest_service.py @pytest.ini
```

---

## 7. Changelog tecnico orientado a evidencia

```
Escreva um changelog tecnico com tres blocos:
Added / Changed / Verified.

Em Verified, liste explicitamente quais cenarios estao cobertos por testes e quais ficam como risco residual.

@test_api_id_characterization.py @test_current_behavior_characterization.py @test_mapper_api_shapes.py
```

---

## 8. Prompt curto para documentacao final

```
Consolide toda a aprendizagem desta implementacao em uma pagina tecnica curta:
contexto, decisao, validacao, riscos residuais e proximos passos.

Use evidencias do codigo e testes. Seja direto e sem referencia a aulas externas.

@workspace
```

---

## Checklist de qualidade da documentacao

- A documentacao explica o "por que", nao so o "o que".
- Cada afirmacao importante tem evidencia em codigo, teste ou reproducao.
- Decisoes e trade-offs estao explicitos.
- Riscos residuais estao nomeados com proximos passos claros.
- Outra pessoa consegue continuar o trabalho sem contexto oral.

---

## Maxima da aula

**Codigo resolve hoje; documentacao sustenta amanha.** O aprendizado so vira ativo do time quando fica claro, verificavel e reutilizavel.
