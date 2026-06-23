# Revisão final e próximos passos

Fechamento do arco do MVP Chatbot: do assistente no sandbox à **entrega profissional** (qualidade, testes, container, CI).

## Definition of Done

Marque em sala ao concluir `prompts.md`:

- [ ] Agente responde no sandbox (entrega anterior validada)
- [ ] `ruff check` e `ruff format --check` limpos em `server/` e `tests/`
- [ ] `pytest` verde — cobre tools/helpers, **não** texto do LLM
- [ ] `python verificar_pipeline.py` retorna **0**
- [ ] `docker build` + container sobe (sandbox `:8800`)
- [ ] Workflow em `ci/` espelha o portão local
- [ ] PR com CI verde

Critérios detalhados: `escopo_mvp.md` § Definition of Done.

## Portões desta entrega

| Portão | Onde | Papel |
|--------|------|--------|
| Lint | `ruff check` | Estilo e erros estáticos |
| Format | `ruff format --check` | Formatação consistente |
| Smoke | `example.py` | Docs e `server/` presentes |
| Testes | `pytest` | Contrato das tools Python |
| Pipeline | `verificar_pipeline.py` | Orquestra tudo localmente |
| CI | `ci/qualidade-mvp.yml` | Mesmo job no GitHub Actions |
| Container | `Dockerfile` | Runtime reproduzível |

## Cruzamento com trilhas

| Trilha | Aplicado no MVP |
|--------|-----------------|
| Fundamentos dev assistido por IA | Prompts com `@padrao_projeto_mvp.md`, revisão de diff |
| Qualidade de código | Ruff + pytest |
| Automação e deploy | Dockerfile + CI |
| Entrega profissional | Portão local = CI; padrão documentado |
| Resolução de problemas | Debug com camada (OpenRouter / Parlant / tool / pipeline) |

## Próximos passos (pós-MVP)

Não entram no DoD desta entrega — ideias para evolução:

- **Tools FAQ** — mais arquivos do repo como fonte estática (ADR-006 fase 2)
- **Journeys** — fluxos multi-passo no Parlant
- **Widget / front** — além do sandbox
- **RAG** — embeddings sobre docs do monorepo (fora do escopo atual)
- **Observabilidade** — métricas, tracing de conversas
- **Ambientes** — staging com secrets manager

Referência de decisões adiadas: `decisoes_arquitetura.md` § Decisões adiadas.
