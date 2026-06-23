# Arquitetura — MVP Chatbot

Visão técnica para alinhar implementação, testes, container e CI.

## 1. Componentes

```
entrega-profissional-e-padronizacao-de-codigo-com-ia/
├── server/                 # Servidor Parlant (Python)
│   ├── main.py             # Entrypoint: Server + NLPServices.openrouter
│   ├── agent.py            # create_agent + metadata
│   ├── guidelines.py       # Regras de comportamento
│   └── tools/              # Tools opcionais (FAQ, busca em docs)
├── tests/                  # pytest — smoke e caracterização
├── ci/                     # Workflow GitHub Actions (evoluir)
├── pyproject.toml          # Ruff + deps
├── Dockerfile              # (entrega posterior) runtime do servidor
├── .env.example
└── padrao_projeto_mvp.md   # Contrato de código do MVP
```

> Estrutura **alvo** — na visão geral ainda não é obrigatório ter todos os arquivos; serve como mapa.

## 2. Runtime (servidor Parlant)

```python
# Esboço conceitual — implementação nas próximas entregas
import asyncio
import parlant.sdk as p

async def main() -> None:
    async with p.Server(
        nlp_service=p.NLPServices.openrouter(
            model_name="openrouter/owl-alpha",
            max_tokens=128_000,
        ),
    ) as server:
        agent = await server.create_agent(
            name="assistente-formacao",
            description="Assistente de onboarding da Formação Dev Elite.",
        )
        # guidelines, journeys, tools — ver escopo_mvp.md
        ...

asyncio.run(main())
```

## 3. Integração OpenRouter

| Item | Decisão |
|------|---------|
| Provider | OpenRouter (`https://openrouter.ai/api/v1`) |
| Modelo | `openrouter/owl-alpha` |
| Auth | Header `Authorization: Bearer $OPENROUTER_API_KEY` |
| Config | Variáveis de ambiente — ver `.env.example` |

**Riscos a tratar cedo:**

- Key vazada em log ou commit → usar `.env` + `.gitignore`
- Rate limit / indisponibilidade → mensagem amigável no agente (guideline ou tool fallback)
- Resposta fora do domínio → guidelines restritivas + glossary

## 4. Interfaces

| Interface | Uso no MVP |
|-----------|------------|
| Sandbox Parlant (`:8800`) | Desenvolvimento e demo |
| API Parlant | Integração futura (widget, front) |
| Tools Python | Consultar docs estáticos / FAQ do curso |

## 5. Observabilidade (mínimo)

- Logs estruturados no servidor (sem API key, sem PII desnecessária)
- Healthcheck HTTP quando containerizado (`/healthz` — suportado pelo Parlant)
- Smoke test local: `python example.py` → validações documentais e, depois, agente up

## 6. Decisões adiadas (pós-MVP)

- Widget React em produção
- Vector DB / RAG sobre todo o monorepo
- Multi-agente ou handoff entre especialistas
- Autenticação de usuário final
