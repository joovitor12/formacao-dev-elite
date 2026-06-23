# Escopo — MVP e limites

Define o que **entra** e o que **fica de fora** do projeto final neste arco (visão geral → entrega containerizada).

## Dentro do escopo (must have)

| # | Item | Critério de pronto |
|---|------|-------------------|
| 1 | Agente Parlant funcional | Responde no sandbox sobre onboarding da formação |
| 2 | OpenRouter + owl-alpha | `NLPServices.openrouter` com `openrouter/owl-alpha` |
| 3 | Guidelines mínimas | ≥ 3 regras (tom, limite de alucinação, escopo do curso) |
| 4 | Config por ambiente | `.env` + `.env.example`, sem segredos no repo |
| 5 | Padrão de código | `padrao_projeto_mvp.md` referenciado nos prompts |
| 6 | Portões locais | lint + format + smoke (evoluir para `verificar_pipeline.py`) |
| 7 | Testes básicos | pytest cobrindo tools/helpers Python (não o LLM em si) |
| 8 | Container | Dockerfile que sobe o servidor |
| 9 | CI | Workflow espelhando portão local |
| 10 | Dossiê final | Registro das decisões + troubleshooting |

## Fora do escopo (won't have no MVP)

- Front-end custom em produção (além do sandbox Parlant)
- Fine-tuning ou troca frequente de modelo sem justificativa
- Persistência de conversas multi-tenant
- Billing, auth corporativa ou SSO
- RAG em escala sobre todo o monorepo
- Suporte a múltiplos idiomas

## Guidelines sugeridas (rascunho)

1. **Escopo:** Responder apenas sobre a Formação Dev Elite e materiais do repositório.
2. **Honestidade:** Se não souber, dizer que não sabe — não inventar URLs ou nomes de módulos.
3. **Tom:** Português claro; respostas curtas salvo pedido de detalhe.
4. **Segurança:** Nunca pedir ou repetir API keys, tokens ou dados pessoais.

Alunos podem ajustar com IA; revisar no sandbox antes de considerar pronta.

## Definition of Done (projeto final)

- [ ] Sandbox responde coerentemente a 5 perguntas de teste documentadas
- [ ] `ruff check` e `ruff format --check` limpos no código Python do MVP
- [ ] `python verificar_pipeline.py` retorna **0**
- [ ] `docker build` + container sobe + healthcheck OK
- [ ] CI verde no PR de entrega
- [ ] Dossiê completo com mapa das trilhas aplicadas
