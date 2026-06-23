# Registro — arquitetura e decisões

Documente ADRs, estrutura `server/` e validação. Herda a documentação da visão geral (`visao_geral_projeto.md`, `mapa_disciplinas.md`, `escopo_mvp.md`, etc.).

## Material

- Decisões: `decisoes_arquitetura.md`
- Estrutura: `server/` + `pyproject.toml`
- Veredito: **arquitetura fechada**

---

## 1. Revisão das ADRs

Para cada ADR em `decisoes_arquitetura.md`, confirme se **concorda** ou se alteraria algo:


| ADR | Título                 | Concorda? | Observação |
| --- | ---------------------- | --------- | ---------- |
| 001 | Parlant                | Sim       |            |
| 002 | OpenRouter + owl-alpha | Sim       |            |
| 003 | Pacote server/         | Sim       |            |
| 004 | Config por ambiente    | Sim       |            |
| 005 | Sandbox                | Sim       |            |
| 006 | Tools faseada          | Sim       |            |
| 007 | Async entrypoint       | Sim       |            |


**ADR que você reforçaria no review de PR:** **ADR-004** — config e segredos são o ponto onde vazamento de API key ou env inconsistente quebra o projeto inteiro.

### Dúvidas levantadas ao fechar as ADRs


| #   | Dúvida                                                                                                                                                                                               | ADR relacionada | Hipótese / próximo passo                                                                                                                                                      |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| D1  | Nome da variável do modelo: `.env.example` usa `OPENROUTER_MODEL`, `visao_geral_projeto.md` cita `PARLANT_MODEL` e `padrao_projeto_mvp.md` também `PARLANT_MODEL`. Qual é o canônico em `config.py`? | 004             | Padronizar em um nome (`OPENROUTER_MODEL` alinhado ao provider) e documentar alias ou atualizar os três arquivos na implementação.                                            |
| D2  | Nesta entrega, `main.py` valida só config ou já sobe `p.Server`? `arquitetura_mvp.md` diz que o servidor completo fica para a próxima entrega.                                                       | 007             | Implementar validação mínima agora; `async with p.Server` na entrega do agente no sandbox — confirmar com instrutor se o portão `verificar_arquitetura.py` exige um ou outro. |
| D3  | `max_tokens=128_000` no esboço de `arquitetura_mvp.md` é suportado/adequado para `openrouter/owl-alpha` no OpenRouter?                                                                               | 002             | Consultar docs do modelo e OpenRouter antes de fixar em `config.py`; pode ser constante configurável com default conservador.                                                 |
| D4  | Onde vive o conteúdo da FAQ estática da fase 2 — JSON/YAML em `server/tools/`, markdown do repo ou hardcoded?                                                                                        | 006             | Preferir arquivo versionado pequeno (ex.: `faq.json`) para pytest determinístico; decidir ao implementar a tool.                                                              |
| D5  | Versão mínima do pacote `parlant` e compatibilidade com Python 3.11+ — fixar em `pyproject.toml` agora ou na §3 dos prompts?                                                                         | 001, 007        | Fixar faixa compatível ao gerar deps; smoke com `pip install` antes de aceitar diff da IA.                                                                                    |
| D6  | Sandbox na porta `:8800` — conflito com outros serviços locais do aluno; expor `PARLANT_PORT` no env?                                                                                                | 005             | Opcional no MVP; documentar no troubleshooting se bind falhar.                                                                                                                |


---

## 2. Estrutura implementada


| Módulo                 | Responsabilidade  | Criado via IA? |
| ---------------------- | ----------------- | -------------- |
| `server/config.py`     | Env + constantes  | Sim            |
| `server/main.py`       | Bootstrap         | Sim            |
| `server/agent.py`      | create_agent      | Sim            |
| `server/guidelines.py` | Guidelines (stub) | Sim            |
| `server/tools/`        | Tools fase 2      | Sim            |
| `pyproject.toml`       | Deps              | Sim            |


**Prompt §2 (criar server/):**

```
@padrao_projeto_mvp.md @decisoes_arquitetura.md @arquitetura_mvp.md

Crie o pacote server/ do zero conforme ADR-003:

- server/config.py — obter_config(), constantes, OPENROUTER via .env, sem logar API key
- server/main.py — bootstrap async; nesta entrega pode validar config (p.Server na próxima)
- server/agent.py — criar_agente(server, config)
- server/guidelines.py — registrar_guidelines stub com TODO
- server/tools/__init__.py — pacote vazio
- server/__init__.py

Siga ESTRITAMENTE padrao_projeto_mvp.md.

Cole o prompt exato em registro_arquitetura_decisoes.md §2.
```

**Prompt §3 (deps):**

```
@decisoes_arquitetura.md

Gere pyproject.toml e requirements.txt para:

- parlant>=3.0.0
- python-dotenv
- ruff em optional dev

Python >=3.11. Não commitar .env.

pip install -r requirements-dev.txt
```

**O que a IA acertou:**

- Layout `server/` idêntico ao ADR-003 (`config`, `main`, `agent`, `guidelines`, `tools/`).
- Nomenclatura em português (`obter_config`, `criar_agente`, `registrar_guidelines`) e constantes `UPPER_SNAKE_CASE`.
- `obter_config()` com `python-dotenv`, validação de `OPENROUTER_API_KEY` e logs sem expor segredo.
- `main.py` assíncrono com `asyncio.run` e validação de config (sem `p.Server`, conforme ADR-007).
- `guidelines.py` e `tools/` como stub/fase 2 (ADR-006).
- `pyproject.toml` + `requirements.txt` / `requirements-dev.txt` com `parlant>=3.0.0`, `python-dotenv` e ruff em dev.

**O que você ajustou manualmente no diff:**

- `ruff format` em `server/config.py` (quebra de linha em `_obter_modelo`).
- Revisão manual confirmou alias `PARLANT_MODEL` em `config.py` (resolve parcialmente D1); docs ainda divergentes — ver §4.

### Revisão manual (§4 do fluxo)

| Critério | ADR / padrão | Status | Nota |
| -------- | ------------ | ------ | ---- |
| Pacote `server/` separado por responsabilidade | ADR-003, §1 padrão | OK | Árvore conforme decisão |
| OpenRouter + `openrouter/owl-alpha` | ADR-002 | OK | `MODELO_PADRAO` e env; `NLPServices.openrouter` na próxima entrega |
| `.env` + `obter_config()`, sem segredo em log | ADR-004, §2–3 padrão | OK | Placeholder rejeitado; log só modelo/agente/tokens |
| `logging`, sem `print` | §3 padrão | OK | Todos os módulos do servidor |
| Bootstrap async, config only | ADR-007 | OK | TODO explícito para `p.Server` |
| Guidelines stub | ADR-006 | OK | TODO lista 4 regras de `escopo_mvp.md` |
| `tools/` vazio (fase 2) | ADR-006 | OK | Pacote presente, sem import em `main` |
| Ruff limpo | §6 padrão | OK | `ruff check` + `format --check` passam |
| Sandbox `:8800` | ADR-005 | Pendente | Esperado — wiring na próxima entrega |

---

## 3. Validação

```bash
pip install -r requirements-dev.txt
python example.py
python verificar_arquitetura.py
python -m server.main   # requer .env com OPENROUTER_API_KEY
```


| Comando                    | Resultado |
| -------------------------- | --------- |
| `example.py`               | **0** — baseline OK (`server/` detectado) |
| `verificar_arquitetura.py` | **0** — ADRs fechadas, `server/` completo, `pyproject.toml` presente |
| `python -m server.main`    | **0** — `Config validada — modelo=openrouter/owl-alpha, agente=assistente-formacao, max_tokens=128000` |

Comandos adicionais da revisão: `ruff check server/` e `ruff format --check server/` — **0**.


---

## 4. Riscos arquiteturais remanescentes


| Risco | Camada | Mitigação planejada |
| ----- | ------ | ------------------- |
| Guidelines ainda stub — agente pode alucinar quando `p.Server` subir | `guidelines.py` | Implementar ≥ 3 guidelines antes de demo no sandbox; validar 5 perguntas de teste (`escopo_mvp.md`) |
| `main.py` não instancia `p.Server` nem chama `criar_agente` | `main.py` / Parlant | Próxima entrega: wire `NLPServices.openrouter` + sandbox `:8800` (ADR-005, ADR-007) |
| `max_tokens=128_000` não validado no provider | `config.py` / OpenRouter | Confirmar limite do owl-alpha; tornar `OPENROUTER_MAX_TOKENS` ajustável (já suportado) |
| Divergência de nome de env (`OPENROUTER_MODEL` vs `PARLANT_MODEL`) nos docs | `config.py` / docs | Código aceita ambos; alinhar `.env.example`, `visao_geral` e `padrao_projeto_mvp` numa PR de docs |
| Dependência de quota/latência OpenRouter em sala cheia | OpenRouter | Smoke local antes da aula; fallback documentado no troubleshooting |
| FAQ estática (fase 2) sem formato definido | `server/tools/` | Adotar `faq.json` versionado + pytest (hipótese D4) |


---

## Checklist

- [x] ADRs preenchidas (sem "(preencha)")
- [x] `server/` criado via IA e revisado
- [x] `pyproject.toml` / requirements criados
- [x] `.env` local (não commitado)
- [x] `python verificar_arquitetura.py` retorna **0**
- [x] Seções 1–4 preenchidas

---

## Resumo

- **Decisão mais crítica desta entrega:** ADR-003 + ADR-004 — pacote `server/` com config isolada e segredos fora do repo; base para todo o agente Parlant.
- **Prompt que mais funcionou para gerar `server/`:** §2 com `@padrao_projeto_mvp.md` + `@decisoes_arquitetura.md` + lista explícita de módulos e responsabilidades.
- **O que fica para a próxima entrega (agente no sandbox):** `async with p.Server(NLPServices.openrouter(...))`, `criar_agente`, `registrar_guidelines` reais, smoke no sandbox `:8800` e início da tool FAQ (fase 2).

