# Revisão final e próximos passos

**Objetivo:** fechar o MVP com **pytest**, **pipeline local**, **CI** e **Docker** — checklist em `proximos_passos.md`.

**Baseline:** agente Parlant integrado (entrega anterior). Faltam `tests/`, `Dockerfile`, `verificar_pipeline.py` completo e workflow em `ci/`.

**Contrato:** `padrao_projeto_mvp.md` §5–§7 + `escopo_mvp.md` DoD.

**Fluxo em sala:**

1. Prompt §1 — testes.
2. Prompt §2 — pipeline + CI.
3. Prompt §3 — container.
4. `python verificar_pipeline.py` → revisar checklist em `proximos_passos.md`.

---

## 1. Testes automatizados

```
@padrao_projeto_mvp.md @escopo_mvp.md @server/tools/

Crie tests/ com pytest para server/tools/ (ex.: consultar_visao_geral_projeto).
Teste contrato e erros previsíveis — sem chamar LLM nem OpenRouter.
Atualize requirements-dev.txt e pyproject.toml se necessário.

Siga estritamente padrao_projeto_mvp.md.
```

---

## 2. Pipeline local e CI

```
@padrao_projeto_mvp.md @proximos_passos.md @verificar_pipeline.py @ci/qualidade-mvp.yml @pyproject.toml

Complete verificar_pipeline.py e ci/qualidade-mvp.yml para rodar, nesta ordem:
ruff check, ruff format --check, example.py, pytest — em server/ e tests/.

O job de CI deve espelhar verificar_pipeline.py (mesmos comandos, working-directory desta pasta).

Siga estritamente padrao_projeto_mvp.md.
```

---

## 3. Container

```
@padrao_projeto_mvp.md @arquitetura_mvp.md @server/ @requirements.txt

Crie Dockerfile para subir python -m server.main (sandbox :8800).
Python 3.11+, sem commitar .env — variáveis injetadas em runtime.
Inclua .dockerignore adequado.

Siga estritamente padrao_projeto_mvp.md.
```

---

## 4. Revisão final (ao vivo)

```bash
pip install -r requirements-dev.txt
python verificar_pipeline.py
docker build -t mvp-chatbot .
docker run --rm -p 8800:8800 --env-file .env mvp-chatbot
```

Confira o checklist de `proximos_passos.md` com o facilitador. Abra PR e valide CI verde.

---

## Máxima da entrega

**O que roda antes do merge é o que o CI executa — local verde, remoto verde, MVP entregue.**
