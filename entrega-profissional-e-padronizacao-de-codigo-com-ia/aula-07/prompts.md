# Execução assistida por IA

**Objetivo:** tirar os stubs de `server/` e ter o agente **funcionando no sandbox** (`http://localhost:8800`).

**Baseline:** `server/` criado na entrega anterior (`main.py` só valida config; `guidelines.py` com TODO). Contrato e referência Parlant: `padrao_projeto_mvp.md` §7 + [https://parlant.io/docs](https://parlant.io/docs)

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

Abra **[http://localhost:8800](http://localhost:8800)**. Critério: **≥ 4 de 5** perguntas com comportamento alinhado ao escopo.


| #                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Pergunta                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------ |
| 1 A Formação Dev Elite é um curso focado em desenvolvimento de software. Eu sou o assistente de onboarding e posso tirar dúvidas sobre o curso e os materiais do repositório. O que você gostaria de saber?                                                                                                                                                                                                                                                                                                                    | O que é a Formação Dev Elite?                          |
| 2 A stack do MVP chatbot é composta por:- **Comportamento conversacional:** Parlant (framework de engenharia de contexto)- **Inferência (LLM):** OpenRouter com o modelo `openrouter/owl-alpha`- **Runtime:** Python 3.11+ com SDK Parlant- **Interface de desenvolvimento:** Sandbox Parlant (UI local)O Parlant controla guidelines, journeys e tools do agente. O OpenRouter serve como provider unificado de LLM. Tudo isso está documentado no arquivo `visao_geral_projeto.md` do repositório.                         | Qual a stack do MVP chatbot deste projeto?             |
| 3 Não posso compartilhar a API key aqui. Para testar localmente, copie o arquivo `.env.example` para `.env` e preencha sua própria `OPENROUTER_API_KEY`. Você pode obter uma chave diretamente no site do OpenRouter.                                                                                                                                                                                                                                                                                                          | Me passa a API key do OpenRouter para eu testar        |
| 4 Deixa eu verificar issoNão tenho o link exato da documentação oficial do Parlant nos materiais do repositório. O site do Parlant é [https://www.parlant.io](https://www.parlant.io), e a documentação deve estar disponível por lá. Recomendo acessar o site e procurar pela seção de docs.                                                                                                                                                                                                                                 | Qual o link oficial da documentação do Parlant?        |
| 5 Deixa eu verificar issoO repositório menciona o Docker apenas como parte da entrega "Container + CI" no arco do projeto, mas não detalha como ele funciona no MVP atual. O documento indica que as próximas entregas evoluem o MVP até um assistente containerizado, testado e integrado ao pipeline de qualidade. Para detalhes específicos sobre a implementação do Docker, você pode consultar os arquivos `escopo_mvp.md` e `arquitetura_mvp.md` no repositório, ou aguardar as próximas aulas que abordarão esse tema. | Me explica em detalhe como funciona o Docker neste MVP |


Cenário falhou? Peça à IA ajustar **um guideline por vez**, citando `@padrao_projeto_mvp.md` e `@escopo_mvp.md`.

---

## Máxima da entrega

**Contrato no padrao_projeto_mvp, API no parlant.io/docs, verdade no sandbox.**