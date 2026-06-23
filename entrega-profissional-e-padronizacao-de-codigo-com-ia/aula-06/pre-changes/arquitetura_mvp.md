# Arquitetura — MVP Chatbot

Visão técnica para alinhar implementação, testes, container e CI.

> **Nesta entrega:** `arquitetura_mvp.md` continua como mapa; `decisoes_arquitetura.md` registra o *porquê*; o pacote `server/` é **criado por você via IA** (não vem pronto no baseline).

## 1. Componentes (estrutura alvo)

```
aula-06/
├── server/                 # ← criar na aula (prompt §2–§3)
│   ├── main.py
│   ├── config.py
│   ├── agent.py
│   ├── guidelines.py
│   └── tools/
├── decisoes_arquitetura.md # ← preencher ADRs antes do código
├── pyproject.toml          # ← criar com IA após ADRs
├── tests/                  # (entrega posterior)
├── ci/                     # (entrega posterior)
├── .env.example
└── padrao_projeto_mvp.md
```

## 2. Runtime (esboço — referência para prompts)

```python
# Não copie cegamente — use como alvo ao pedir server/ à IA
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
        # guidelines — ver escopo_mvp.md

asyncio.run(main())
```

Nesta aula o `main.py` pode **apenas validar config**; subir `p.Server` completo fica para a próxima entrega.

## 3. Integração OpenRouter

| Item | Decisão sugerida |
|------|------------------|
| Provider | OpenRouter (`https://openrouter.ai/api/v1`) |
| Modelo | `openrouter/owl-alpha` |
| Auth | `OPENROUTER_API_KEY` em `.env` |
| Config | Centralizar em `server/config.py` |

## 4. Interfaces

| Interface | Uso no MVP |
|-----------|------------|
| Sandbox Parlant (`:8800`) | Desenvolvimento e demo |
| API Parlant | Integração futura |
| Tools Python | FAQ estática (fase 2) |

## 5. Observabilidade (mínimo)

- `logging` no servidor — sem API key em log
- Smoke: `python example.py` (docs) → `python verificar_arquitetura.py` (após criar `server/`)

## 6. Decisões adiadas (pós-MVP)

- Widget React em produção
- Vector DB / RAG no monorepo inteiro
- Autenticação do usuário final
