# Mapa das trilhas → MVP Chatbot

Como cada **disciplina da formação** se aplica ao projeto final. Use este mapa ao pedir ajuda à IA: anexe o documento da trilha relevante junto com `@visao_geral_projeto.md`.

---

## Fundamentos de desenvolvimento assistido por IA

| Tema | Aplicação no MVP |
|------|------------------|
| Prompts e `@workspace` | Gerar/refinar guidelines, tools e estrutura do servidor Parlant |
| Arquitetura (camadas, módulos) | Separar `server/`, config, tools e testes |
| Variáveis de ambiente | `OPENROUTER_API_KEY`, model id — nunca hardcoded |
| Human-in-the-loop | Revisar diff da IA antes de merge; validar respostas do agente no sandbox |
| Skills / agentes | Reutilizar skills do repo (pytest, create-pr) quando aplicável |

**Pergunta-guia:** *A IA acelerou — o humano validou arquitetura e segurança?*

---

## Qualidade e manutenibilidade

| Tema | Aplicação no MVP |
|------|------------------|
| Testes de caracterização | Congelar comportamento do agente/tools antes de refatorar |
| Refatoração segura | Extrair tools e config sem mudar contrato observável |
| Cobertura e casos de erro | Payload inválido, API indisponível, resposta vazia do LLM |
| Boas práticas de testes com IA | Pedir testes **por comportamento**, não por implementação interna do Parlant |

**Pergunta-guia:** *Mudança no código alterou o que o usuário vê no chat?*

---

## Automação e DevOps inteligente

| Tema | Aplicação no MVP |
|------|------------------|
| Review de PR / CI verde ≠ merge | Pipeline passa, mas guidelines frágeis ainda bloqueiam release |
| Comentários automáticos | Triar bots (Copilot, linters) vs achados reais de risco |
| Integração Git | PRs pequenos, Conventional Commits, template preenchido |
| Docker / imagem | Container do servidor Parlant para deploy reproduzível |
| Governança | Quem aprova mudança de guideline vs mudança de infra |

**Pergunta-guia:** *O check verde cobre o que importa para o agente em produção?*

---

## Entrega profissional e padronização de código com IA

| Tema | Aplicação no MVP |
|------|------------------|
| Padrão documentado | `padrao_projeto_mvp.md` em todo prompt de implementação |
| Lint (Ruff) | `ruff check` no código Python do servidor e tools |
| Formatação automática | `ruff format` — layout uniforme no monorepo do MVP |
| Pipeline | `verificar_pipeline.py` + workflow GitHub Actions espelhado |

**Pergunta-guia:** *Local e CI executam os mesmos portões?*

---

## Resolução avançada de problemas

| Tema | Aplicação no MVP |
|------|------------------|
| Causa raiz | Falha OpenRouter vs guideline vs tool vs rede — não “trocar modelo no escuro” |
| Observação → hipótese → teste | Reproduzir no sandbox; isolar camada (LLM, Parlant, tool) |
| Fronteiras e contratos | Schema de tool, timeout, fallback quando LLM não responde |
| Debug assistido por IA | Colar stack trace + `@arquitetura_mvp.md` — pedir hipóteses ordenadas |

**Pergunta-guia:** *Qual camada falhou: provider, framework ou regra de negócio?*

---

## Matriz resumida (entrega final)

| Disciplina | Artefato esperado no MVP |
|------------|--------------------------|
| Fundamentos | Servidor Parlant estruturado, `.env`, prompts revisados |
| Qualidade | Testes + smoke do fluxo principal |
| Automação | Dockerfile + CI com portões |
| Entrega profissional | Padrão + lint + format + pipeline |
| Resolução | Runbook curto de troubleshooting no dossiê |

Use este mapa ao revisar ADRs (`decisoes_arquitetura.md`) e ao documentar riscos em `registro_arquitetura_decisoes.md` §4.
