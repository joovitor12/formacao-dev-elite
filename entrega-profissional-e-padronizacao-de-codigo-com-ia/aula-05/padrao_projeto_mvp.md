# Padrão de código — MVP Chatbot

Contrato do time para o **projeto final**. Toda implementação com IA deve citar este arquivo (`@padrao_projeto_mvp.md`) e `@visao_geral_projeto.md`.

> Herda espírito da trilha de **entrega profissional** (nomenclatura, logging, revisão humana), adaptado a servidor Parlant + tools.

## 1. Nomenclatura

- Módulos e funções: `snake_case` em português claro (`criar_agente`, `registrar_guidelines`).
- Pacote do servidor: `server/` com responsabilidades separadas (`main`, `agent`, `guidelines`, `tools/`).
- Constantes: `UPPER_SNAKE_CASE` (`MODELO_PADRAO`, `NOME_AGENTE`).

## 2. Configuração e segredos

- **Proibido** commitar `OPENROUTER_API_KEY` ou `.env`.
- Modelo default via env: `PARLANT_MODEL=openrouter/owl-alpha`.
- Carregar env com `python-dotenv` ou equivalente no entrypoint.

## 3. Logging

- Usar `logging` — **proibido** `print` em caminho de produção/simulação do servidor.
- **Proibido** logar API keys, prompts completos com PII ou tokens.

## 4. Tools Parlant

- Uma tool = uma responsabilidade; type hints + docstring curta.
- Retornos previsíveis (`str` ou dict serializável); erros esperados com mensagem acionável.
- Sem I/O oculto — efeitos explícitos e testáveis.

## 5. Testes

- pytest para tools e helpers; mock de HTTP para OpenRouter quando necessário.
- Não assertar texto exato do LLM — assertar contrato da tool e smoke do servidor.

## 6. Qualidade automatizada

- Ruff: `ruff check` + `ruff format --check` (config em `pyproject.toml`).
- Pipeline local espelhado no CI — ver trilha de **entrega profissional**.

## 7. Prompts com IA

1. Anexar `@padrao_projeto_mvp.md`, `@visao_geral_projeto.md` e arquivo alvo.
2. Declarar: *“Siga estritamente padrao_projeto_mvp.md; não invente outro layout ou provider.”*
3. Revisar diff **antes** de aceitar — especialmente guidelines e tools.

## 8. Troubleshooting (resolução de problemas)

Ao debugar com IA, incluir: camada suspeita (OpenRouter / Parlant / tool), log sanitizado, `@arquitetura_mvp.md`. Pedir hipóteses ordenadas — não patch imediato.
