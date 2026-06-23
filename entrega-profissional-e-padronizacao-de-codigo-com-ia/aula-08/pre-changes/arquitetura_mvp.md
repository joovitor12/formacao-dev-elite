# Arquitetura — MVP Chatbot

Visão técnica para alinhar implementação, testes, container e CI.

> **Nesta entrega:** agente integrado (entrega anterior). Feche **pytest**, **verificar_pipeline.py**, **CI** e **Dockerfile** via `prompts.md`.

## 1. Componentes (estrutura alvo)

```
aula-08/
├── server/                 # ← agente Parlant (herdado)
│   ├── main.py
│   ├── config.py
│   ├── agent.py
│   ├── guidelines.py
│   └── tools/
├── tests/                  # ← criar na aula (pytest)
├── ci/                     # ← completar qualidade-mvp.yml
├── Dockerfile              # ← criar na aula
├── verificar_pipeline.py   # ← completar (baseline incompleto)
├── verificar_arquitetura.py
├── pyproject.toml
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

Nesta entrega o runtime já sobe `p.Server` — o foco é **qualidade, testes, container e CI**.

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
- Smoke: `python example.py` → `python verificar_pipeline.py` (lint + format + pytest)

## 6. Decisões adiadas (pós-MVP)

- Widget React em produção
- Vector DB / RAG no monorepo inteiro
- Autenticação do usuário final
