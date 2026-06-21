# Inventário de revisão — containers e imagens

Registre achados no **Dockerfile**, **.dockerignore** e contexto de build.

## Material revisado

- Pasta: `aula-07/` (`Dockerfile`, `.dockerignore`, contexto de `COPY . .`)
- Veredito de imagem: **pedir mudanças** (segredo em layer + root + tag mutável)

---

## Registro de achados

| # | Achado | Categoria | Severidade | Quem detectou? | Bloqueia uso em prod? |
|---|--------|-----------|------------|----------------|----------------------|
| 1 | `FROM python:latest` — tag mutável na base | base/tag | alta | Hadolint (DL3007) | Sim |
| 2 | Ausência de `USER` — processo roda como root | usuário | alta | Copilot | Sim |
| 3 | `ENV METRICS_API_KEY=pipe_live_8c4f91a0e2bd` — credencial na imagem | segredos | crítica | Copilot | Sim |
| 4 | `RUN apt-get install -y curl vim` — pacotes sem pin de versão | camadas / tamanho | média | Hadolint (DL3008) | Não (ressalva) |
| 5 | `RUN apt-get install` sem `--no-install-recommends` | camadas / tamanho | baixa | Hadolint (DL3015) | Não |
| 6 | `RUN apt-get install` sem limpar `/var/lib/apt/lists` | camadas / tamanho | baixa | Hadolint (DL3009) | Não |
| 7 | `vim` (e `curl`) instalados sem necessidade de runtime | camadas / tamanho | média | Copilot | Não (ressalva) |
| 8 | `COPY . .` — contexto inteiro na imagem final | camadas / tamanho | média | Copilot | Não (ressalva) |
| 9 | `CMD python metrics_exporter.py` — forma shell, não exec JSON | runtime | média | Hadolint (DL3025) | Não (ressalva) |
| 10 | Ausência de `HEALTHCHECK` | runtime | média | Copilot | Não (ressalva) |
| 11 | `.dockerignore` só ignora `__pycache__` | ignore | média | Copilot | Não (ressalva) |
| 12 | `.dockerignore` não exclui `.env`, `.git`, artefatos de dev | segredos / ignore | alta | Copilot | Sim (se existirem no contexto) |

---

## Lacunas de detecção

| # | Problema de imagem não sinalizado | Por que passou (ferramenta ou contexto) |
|---|-----------------------------------|----------------------------------------|
| 1 | Segredo em `ENV` (`METRICS_API_KEY`) | Hadolint valida sintaxe e boas práticas de instruções, não classifica valores de `ENV` como credencial |
| 2 | Container roda como root (sem `USER`) | Hadolint não emitiu DL3002 neste Dockerfile; revisor humano/IA precisa checar identidade efetiva |
| 3 | `.dockerignore` incompleto | Hadolint analisa apenas o `Dockerfile`, não o pareamento `COPY` + contexto ignorado |
| 4 | `COPY . .` copia lixo de aula (`pre-changes/`, `prompts.md`, etc.) | Exige inspeção do diretório de build; fora do escopo do linter de Dockerfile |
| 5 | `vim` como ferramenta de dev em imagem de produção | Sem regra Hadolint para “pacote desnecessário”; DL3008 só pede pin de versão |
| 6 | Ausência de `HEALTHCHECK` | Hadolint default não exige health check; depende de política do time/orchestrator |

---

## Checklist de revisão (marque após analisar)

- [ ] Tag da imagem base é fixa e adequada (evitar `latest` em prod)
- [ ] Processo não roda como root sem justificativa
- [ ] Segredos não estão em `ENV`, `ARG` ou camadas do build
- [ ] `.dockerignore` evita vazar `.env`, `.git` e artefatos desnecessários
- [ ] `CMD`/`ENTRYPOINT` em forma exec quando possível
- [ ] `HEALTHCHECK` ou estratégia equivalente documentada
- [ ] Camadas de `RUN` minimizam lixo (cache apt, etc.)

---

## Priorização

- Top 2 achados que exigem correção antes de usar em produção:
  1. Remover `METRICS_API_KEY` do `ENV` e injetar segredo só no deploy (secret manager / mount / env do orchestrator).
  2. Fixar tag da base (`python:3.12.x-slim` ou equivalente) e adicionar `USER` não-root.
- 1 achado aceitável com mitigação documentada (se houver):
  - `EXPOSE 8080` — aceitável se documentado no chart/manifesto e rede restrita; health check pode ser probe HTTP em `/health` no Kubernetes em vez de `HEALTHCHECK` na imagem.

---

## Resumo

- Achado mais crítico na imagem: credencial `METRICS_API_KEY` persistida em layer via `ENV`.
- Ferramenta que mais ajudou: Hadolint (tag, apt, CMD) + revisão Copilot (segredos, root, ignore, HEALTHCHECK).
- Algo que só o revisor humano percebeu no contexto de deploy: política de injeção de segredos no ambiente (registry, RBAC, rotação de chave) e se arquivos sensíveis existem hoje no diretório local além do que o `.dockerignore` cobre.
