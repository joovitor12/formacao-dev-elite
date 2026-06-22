# Matriz de segurança e boas práticas — imagem Docker

Audite o **Dockerfile**, **.dockerignore** e contexto de build. Registre achados e correções.

## Material auditado

- Arquivos: `Dockerfile`, `.dockerignore`, contexto de `COPY`
- Veredito de segurança: **aprovar com ressalvas** (Dockerfile/contexto corrigidos; ressalva: `/metrics` ainda sem auth — segredo só no deploy)

---

## Registro de achados

| # | Achado | Categoria (base / segredos / usuário / superfície / runtime / contexto) | Severidade (baixa / média / alta / crítica) | Quem detectou? (humano / Copilot / Hadolint / ninguém) | Bloqueia deploy? |
|---|--------|---------------------------------------------------------------------------|---------------------------------------------|--------------------------------------------------------|------------------|
| 1 | `FROM python:latest` — tag flutuante, build não reproduzível e base sem pin de patch/CVE | base | alta | Hadolint | sim |
| 2 | `ARG REGISTRY_TOKEN=reg_live_default_insecure` — token com valor default embutido na camada de build | segredos | crítica | humano | sim |
| 3 | `ENV METRICS_API_KEY=pipe_live_8c4f91a0e2bd` — chave de API persistida na imagem (`docker inspect`, histórico) | segredos | crítica | humano | sim |
| 4 | Ausência de `USER` — processo principal roda como root (UID 0) | usuário | crítica | humano | sim |
| 5 | `RUN apt-get install -y curl sudo` — `sudo` permite escalada local; `curl` amplia superfície sem necessidade aparente | superfície | alta | humano | sim |
| 6 | `EXPOSE 8080 22` — porta 22 (SSH) declarada sem serviço legítimo; documenta/intenciona superfície de rede indevida | superfície | alta | humano | sim |
| 7 | `COPY . .` com `.dockerignore` mínimo — envia `pre-changes/`, `prompts.md`, `matriz_seguranca_boas_praticas.md`, `example.py` para contexto e imagem | contexto | alta | humano | não |
| 8 | `.dockerignore` lista só `__pycache__` — não exclui `.git`, `.env`, `*.md`, `pre-changes/`, artefatos de teste | contexto | alta | humano | não |
| 9 | `ENV DEBUG=true` — flag de debug ativa na imagem de produção | runtime | média | humano | não |
| 10 | `CMD python metrics_exporter.py` — forma shell (invoca `/bin/sh -c`); sinal de parada e PID 1 subótimos | runtime | média | Hadolint | não |
| 11 | Sem `HEALTHCHECK` — orquestrador não distingue container saudável de travado | runtime | média | humano | não |
| 12 | `metrics_exporter.py`: `HOST` default `0.0.0.0` — serviço escuta em todas as interfaces sem restrição de bind | runtime | média | humano | não |
| 13 | `metrics_exporter.py`: `/metrics` sem autenticação — `METRICS_API_KEY` definida no Dockerfile mas não validada no código | runtime | média | humano | não |
| 14 | `apt-get` sem limpeza de cache (`rm -rf /var/lib/apt/lists/*`) — camada maior e resíduos de índice de pacotes | contexto | baixa | Hadolint | não |

---

## Lacunas de detecção

Referência Hadolint executado: `docker run --rm -i hadolint/hadolint < Dockerfile` (exit 1; regras DL3007, DL3008, DL3015, DL3009, DL3042, DL3025).

| # | Risco não sinalizado por ferramentas | Por que passou |
|---|--------------------------------------|----------------|
| 1 | Segredos em `ARG`/`ENV` (#2, #3) — bloqueante | Hadolint não analisa conteúdo sensível de variáveis; exige scanner de secrets (Gitleaks, Trivy secret scan) ou revisão humana |
| 2 | Processo como root — ausência de `USER` (#4) — bloqueante | DL3002 não apareceu nesta execução; regra depende de configuração/versão; risco de deploy “verde” no linter |
| 3 | Pacotes de privilégio `sudo` e `curl` (#5) — bloqueante | Hadolint sinalizou a mesma linha por pin de versão (DL3008), `--no-install-recommends` (DL3015) e limpeza de listas (DL3009), mas não avalia *quais* pacotes ampliam superfície ou escalada |
| 4 | `EXPOSE 22` sem serviço SSH (#6) — bloqueante | Hadolint não valida se portas expostas são necessárias para a aplicação |
| 5 | Contexto de build amplo — `COPY . .` + `.dockerignore` fraco (#7, #8) | Hadolint não lê `.dockerignore` nem o filesystem do contexto; Copilot não foi executado nesta auditoria |
| 6 | `ENV DEBUG=true` (#9) e lógica de app (#12, #13) | Fora do escopo do Dockerfile linter; exige revisão de código e política de configuração |
| 7 | Ausência de `HEALTHCHECK` (#11) | Hadolint não exige `HEALTHCHECK` por padrão nesta imagem; gap coberto por checklist humano ou política de cluster |
| 8 | `pip install` sem `--no-cache-dir` (linha 14) | Hadolint acusou (DL3042), mas achado **não estava** no inventário inicial — linter encontrou problema extra não catalogado na primeira passada humana |

---

## Correções aplicadas

| # | Antes | Depois | Risco mitigado |
|---|-------|--------|----------------|
| 1 | `FROM python:latest` | `FROM python:3.12.9-slim` | Base reproduzível, menor superfície, tag fixa |
| 2 | `ARG REGISTRY_TOKEN=reg_live_default_insecure` | removido — injetar no CI/deploy (`docker secret`, K8s Secret) | Token fora de camadas de build |
| 3 | `ENV METRICS_API_KEY=pipe_live_...` | removido — `-e METRICS_API_KEY=...` só no `docker run`/orchestrator | Chave não persistida na imagem |
| 4 | sem `USER` (root) | `groupadd`/`useradd app` + `USER app` + `chown` | Menor privilégio em runtime |
| 5 | `apt-get install curl sudo` | linha removida (stdlib + slim bastam) | Sem escalada via `sudo` nem `curl` extra |
| 6 | `EXPOSE 8080 22` | `EXPOSE 8080` | Superfície de rede alinhada à app |
| 7 | `COPY . .` | `COPY requirements.txt` + `COPY metrics_exporter.py` | Só artefatos necessários na imagem |
| 8 | `.dockerignore` só `__pycache__` | exclusões: `.git`, `.env`, `*.md`, `pre-changes/`, `example.py`, docs de aula | Contexto de build sem vazamento acidental |
| 9 | `ENV DEBUG=true` | removido | Sem modo debug na imagem de produção |
| 10 | `CMD python metrics_exporter.py` (shell) | `CMD ["python", "metrics_exporter.py"]` (exec) | PID 1 e sinais corretos |
| 11 | sem `HEALTHCHECK` | `HEALTHCHECK` via `python` em `http://127.0.0.1:8080/health` | Orquestrador detecta instância saudável |
| 14 | `pip install` sem flag | `pip install --no-cache-dir` | Camadas menores, sem cache pip na imagem |

---

## Checklist de boas práticas

- [x] Tag da base **fixa** e adequada (sem `latest` em produção)
- [x] Nenhum segredo em `ENV`, `ARG` ou camada persistida
- [x] Processo roda como **usuário não-root**
- [x] `CMD`/`ENTRYPOINT` em **exec form**
- [x] Apenas portas necessárias em `EXPOSE`
- [x] Sem pacotes de privilégio desnecessários (`sudo`, shells de debug)
- [x] `.dockerignore` impede `.env`, `.git` e artefatos sensíveis no contexto
- [x] `HEALTHCHECK` ou estratégia equivalente documentada
- [x] Flags de debug desligadas na imagem de produção

---

## Validação pós-correção

| Passo | Resultado (ok / falhou / não rodei) |
|-------|-------------------------------------|
| `python example.py` | ok |
| Hadolint | ok (exit 0, sem avisos) |
| `docker build` | ok (`metrics-exporter:aula12`) |
| `docker run` + `curl /health` | ok (`200 ok`) |

---

## Resumo

- Achado mais crítico (antes): segredos em `ARG`/`ENV` — **mitigado** com injeção só no deploy.
- Boas prática que mais faltava no baseline: usuário não-root e gestão de segredos fora da imagem — **corrigido**.
- Ressalva pendente (#12, #13): `metrics_exporter.py` ainda escuta `0.0.0.0` e `/metrics` sem validar `METRICS_API_KEY` em runtime.
