# 🧪 Quizz: MVP Chatbot — visão, arquitetura, Parlant e entrega

**Módulo: Entrega Profissional e Padronização de Código com IA**

Este questionário verifica o arco completo do **MVP Chatbot** (Parlant + OpenRouter): **visão e escopo**, **decisões de arquitetura (ADRs)**, **integração do agente no sandbox**, **guidelines e tools**, e **fechamento com qualidade** (pytest, pipeline local, CI e container) — sem depender do código exato visto em sala.

---

### 1. Por que o MVP adota Parlant em vez de um único system prompt no provider?
   - A) Para ter regras declarativas (guidelines), sandbox local e evolução incremental sem “prompt spaghetti”.
   - B) Porque OpenRouter só funciona com Parlant.
   - C) Para substituir pytest por avaliação automática do texto do LLM.
   - D) Porque Parlant elimina a necessidade de revisão humana do diff.

### 2. Qual combinação de stack o MVP define para inferência e comportamento conversacional?
   - A) Ollama local + widget React em produção.
   - B) Parlant (`parlant.sdk`) + OpenRouter com modelo `openrouter/owl-alpha`.
   - C) Assistants API da OpenAI + RAG no monorepo inteiro desde o dia 1.
   - D) LangChain + GPT-4 direto, sem variáveis de ambiente.

### 3. No layout acordado em ADR, qual divisão de responsabilidades em `server/` está correta?
   - A) Tudo em `main.py` — config, agente, guidelines e tools no mesmo arquivo.
   - B) `config.py` importa Parlant e registra guidelines para isolar side effects.
   - C) `main.py` orquestra; `config.py` carrega env; `agent.py` cria o agente; `guidelines.py` registra regras; `tools/` para integrações Python.
   - D) Tools ficam em `main.py`; ADRs ficam dentro de `server/tools/`.

### 4. Sobre segredos e configuração no MVP, qual prática o material exige?
   - A) Commitar `.env` com a chave real para o CI funcionar.
   - B) Logar `OPENROUTER_API_KEY` em nível INFO quando o servidor sobe.
   - C) Hardcodar a API key em `config.py` com comentário “só dev”.
   - D) `.env` local gitignored + `.env.example` versionado; `obter_config()` valida a chave; nunca expor segredo em log.

### 5. Qual interface de desenvolvimento o MVP usa na fase inicial (sem front custom em produção)?
   - A) Sandbox Parlant em `http://localhost:8800` após `python -m server.main`.
   - B) Widget React deployado em produção.
   - C) Streamlit embutido no repositório.
   - D) Apenas `curl` na API, sem UI conversacional.

### 6. No fluxo de **arquitetura e decisões**, qual ordem está alinhada ao material?
   - A) Pedir à IA o pacote `server/` completo e só depois pensar nas ADRs.
   - B) Fechar ADRs em markdown, gerar `server/` com IA a partir do contrato, revisar diff, validar com portão arquitetural.
   - C) Copiar o quickstart do Parlant sem `@padrao_projeto_mvp.md`.
   - D) Pular `verificar_arquitetura.py` porque a IA já seguiu o prompt.

### 7. Na **execução assistida por IA** (integrar Parlant de fato), o roteiro de prompts com IA mais alinhado é:
   - A) Pedir código sem anexar `padrao_projeto_mvp.md` — o modelo já conhece Parlant.
   - B) Aceitar o primeiro diff se `ruff check` passou, mesmo sem testar conversa.
   - C) Implementar guidelines só no system prompt do OpenRouter, fora do SDK.
   - D) Anexar `@padrao_projeto_mvp.md` e docs do projeto; declarar aderência estrita; consultar https://parlant.io/docs; revisar diff; validar no sandbox ao vivo.

### 8. Sobre **guidelines** Parlant no escopo do MVP, qual afirmação é correta?
   - A) Devem cobrir escopo do curso, honestidade (não inventar URLs/módulos), tom em português e segurança (não repetir API keys) — ≥ 3 regras.
   - B) São opcionais se o modelo for “inteligente o suficiente”.
   - C) Substituem a necessidade de qualquer teste automatizado.
   - D) Devem ser escritas apenas em JSON estático, nunca via `create_guideline`.

### 9. Na **revisão final** (pytest, pipeline, CI, Docker), o que os testes automatizados devem cobrir?
   - A) Assertar texto exato de cada resposta do LLM no sandbox.
   - B) Apenas o Dockerfile — pytest é dispensável no MVP.
   - C) Contrato de tools e helpers Python (ex.: leitura de arquivo, erros previsíveis) — sem chamar OpenRouter/LLM nos testes.
   - D) Somente `example.py`; `verificar_pipeline.py` é decorativo.

### 10. Qual princípio de **entrega profissional** o fechamento do MVP reforça?
   - A) CI pode rodar comandos diferentes do portão local para ir mais rápido.
   - B) `verificar_pipeline.py` orquestra lint, format, smoke e pytest; o workflow em `ci/` deve espelhar o mesmo job — local verde, remoto verde.
   - C) Container substitui `.env` — variáveis sensíveis vão no Dockerfile commitado.
   - D) RAG em escala sobre o monorepo e SSO multi-tenant entram no DoD desta entrega.

---

## 🔑 Gabarito comentado

### 1. Resposta: A
**Justificativa:** ADR-001 e `escopo_mvp.md` priorizam comportamento previsível com guidelines declarativas e sandbox — alternativa ao prompt monolítico difícil de revisar e evoluir.

### 2. Resposta: B
**Justificativa:** Stack acordada: Parlant para engenharia de contexto + OpenRouter (`openrouter/owl-alpha`) via `NLPServices.openrouter` — ver `visao_geral_projeto.md` e ADR-002.

### 3. Resposta: C
**Justificativa:** ADR-003 separa bootstrap (`main`), config, agente, guidelines e `tools/` — monólito em `main.py` foi rejeitado por dificultar review e prompts de IA.

### 4. Resposta: D
**Justificativa:** ADR-004 e `padrao_projeto_mvp.md` §2: `.env` + exemplo versionado, validação em `obter_config()`, proibição de segredo em log ou no repositório.

### 5. Resposta: A
**Justificativa:** ADR-005: sandbox Parlant na porta 8800 para dev/demo; front custom em produção está fora do escopo inicial (`escopo_mvp.md`).

### 6. Resposta: B
**Justificativa:** Arquitetura antes do código: ADRs fechadas → geração de `server/` com IA → revisão contra `padrao_projeto_mvp.md` → `verificar_arquitetura.py`.

### 7. Resposta: D
**Justificativa:** `padrao_projeto_mvp.md` §7: anexar contrato e visão, citar docs oficiais do Parlant, revisar diff; validação conversacional é ao vivo no sandbox, não só lint.

### 8. Resposta: A
**Justificativa:** `escopo_mvp.md` lista guidelines mínimas (escopo, honestidade, tom, segurança); são o mecanismo central do Parlant nesta fase, não substituto de pytest nas tools.

### 9. Resposta: C
**Justificativa:** `padrao_projeto_mvp.md` §5 e `escopo_mvp.md`: pytest em tools/helpers; não assertar saída estocástica do LLM.

### 10. Resposta: B
**Justificativa:** `proximos_passos.md` e trilha de pipeline: paridade local/CI com `verificar_pipeline.py`; Docker injeta env em runtime — itens como RAG em escala e SSO ficam pós-MVP (`decisoes_arquitetura.md` § Decisões adiadas).
