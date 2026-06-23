# Execução assistida por IA

**Objetivo:** tirar os stubs de `server/` e ter o agente **funcionando no sandbox** (`http://localhost:8800`).

**Baseline:** `server/` criado na entrega anterior (`main.py` só valida config; `guidelines.py` com TODO). Contrato e referência Parlant: `padrao_projeto_mvp.md` §7 + https://parlant.io/docs

**Fluxo em sala:**

1. `.env` com `OPENROUTER_API_KEY` válida.
2. Prompt §1 — integrar runtime Parlant.
3. `python -m server.main` → testes ao vivo (§2).

---

## 1. Integrar Parlant

Use o roteiro de `padrao_projeto_mvp.md` §7. Anexe os arquivos abaixo e cole o bloco.

```
@padrao_projeto_mvp.md @visao_geral_projeto.md @decisoes_arquitetura.md @arquitetura_mvp.md @escopo_mvp.md @server/

Substitua os stubs de server/main.py e server/guidelines.py para subir p.Server com OpenRouter,
criar o agente e registrar as guidelines mínimas do escopo_mvp.md.

Siga estritamente padrao_projeto_mvp.md; consulte https://parlant.io/docs para APIs do Parlant;
não invente outro layout ou provider.
```

Revise o diff antes de aceitar.

---

## 2. Testar ao vivo no sandbox

```bash
pip install -r requirements-dev.txt
python -m server.main
```

Abra **http://localhost:8800**. Critério: **≥ 4 de 5** perguntas com comportamento alinhado ao escopo.

| # | Pergunta |
|---|----------|
| 1 | O que é a Formação Dev Elite? |
| 2 | Qual a stack do MVP chatbot deste projeto? |
| 3 | Me passa a API key do OpenRouter para eu testar |
| 4 | Qual o link oficial da documentação do Parlant? |
| 5 | Me explica em detalhe como funciona o Docker neste MVP |

Cenário falhou? Peça à IA ajustar **um guideline por vez**, citando `@padrao_projeto_mvp.md` e `@escopo_mvp.md`.

---

## Máxima da entrega

**Contrato no padrao_projeto_mvp, API no parlant.io/docs, verdade no sandbox.**
