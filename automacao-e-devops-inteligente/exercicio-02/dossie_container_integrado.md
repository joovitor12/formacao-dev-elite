# Dossiê integrador — containerização com IA

Preencha ao longo do exercício. Cada seção cobre um bloco do percurso.

## Material

- App: `metrics_exporter.py`
- Veredito final da imagem: **aprovar com ressalvas**

---

## 1. Revisão de containers e imagens

- Veredito de revisão: **rejeitar**
- Top 3 achados do baseline (categoria + severidade):

| # | Achado | Categoria | Severidade | Bloqueia produção? |
|---|--------|-----------|------------|-------------------|
| 1 | `ENV METRICS_API_KEY=pipe_live_integrador_9f2a` — chave persistida na imagem (`docker inspect`, histórico de camadas) | segredos | crítica | sim |
| 2 | Ausência de `USER` — processo principal roda como root (UID 0) | usuário | crítica | sim |
| 3 | `COPY` dos artefatos **antes** de `WORKDIR /app` — arquivos ficam em `/`, mas `pip install` e `CMD` executam em `/app`; build falha com *No such file or directory: requirements.txt* | estrutura | crítica | sim |

- Lacuna de ferramenta (achado que IA ou Hadolint não pegou):

  - **Pacotes de privilégio** (`sudo`, `vim`, `git`, `curl`) — Hadolint acusou pin de versão e limpeza de `apt` lists na mesma linha, mas **não avalia** quais pacotes ampliam superfície ou permitem escalada local.
  - **`EXPOSE 22`** sem serviço SSH legítimo — nenhuma regra do Hadolint valida se portas expostas são necessárias para a aplicação.
  - **Segredos em `ENV`** — Hadolint não analisa conteúdo sensível de variáveis; o BuildKit alertou (`SecretsUsedInArgOrEnv`), mas exige scanner dedicado (Gitleaks, Trivy secret scan) ou revisão humana para bloquear deploy.
  - **Impacto funcional do `COPY` sem `WORKDIR`** — Hadolint emitiu DL3045 (warning), porém não conecta o aviso ao **build quebrado** na etapa `pip install`.

### Inventário completo do baseline

| # | Trecho / contexto | Categoria | Severidade | Detectado por | Bloqueia produção? |
|---|-------------------|-----------|------------|---------------|-------------------|
| 1 | `FROM python:latest` | base | alta | Hadolint (DL3007) | sim |
| 2 | `ENV METRICS_API_KEY=...` | segredos | crítica | BuildKit + humano | sim |
| 3 | `ENV DEBUG=true` | runtime | média | humano | não |
| 4 | `COPY` antes de `WORKDIR /app` | estrutura | crítica | Hadolint (DL3045) + build | sim |
| 5 | `apt-get install gcc build-essential git curl vim sudo` | superfície | alta | humano | sim |
| 6 | `apt-get` sem pin, `--no-install-recommends` nem limpeza de lists | contexto | baixa | Hadolint (DL3008, DL3015, DL3009) | não |
| 7 | `pip install` sem `--no-cache-dir` | contexto | baixa | Hadolint (DL3042) | não |
| 8 | `pip install` com `requirements.txt` vazio (stdlib) — etapa desnecessária | otimização | baixa | humano | não |
| 9 | `EXPOSE 8080 22` | superfície | alta | humano | sim |
| 10 | Sem `USER` (root) | usuário | crítica | humano | sim |
| 11 | `CMD python metrics_exporter.py` (shell form) | runtime | média | Hadolint (DL3025) + BuildKit | não |
| 12 | Sem `HEALTHCHECK` | runtime | média | humano | não |
| 13 | `.dockerignore` só `__pycache__` | contexto | média | humano | não |
| 14 | Base `python:latest` completa (~1 GB) vs slim | otimização | média | humano | não |
| 15 | `metrics_exporter.py`: `HOST` default `0.0.0.0` | runtime | média | humano | não |
| 16 | `METRICS_API_KEY` definida mas não validada em `/metrics` | runtime | média | humano | não |

**Hadolint** (`docker run --rm -i hadolint/hadolint < Dockerfile`): exit 0 com 6 avisos/info (DL3007, DL3045×2, DL3008, DL3015, DL3009, DL3042, DL3025).

**`docker build`**: falhou na etapa `pip install` — `requirements.txt` não encontrado em `/app`.

---

## 2. Estrutura do Dockerfile

- Ordem atual do baseline (liste instruções principais):

  `FROM` → `ENV`×2 → `COPY` app/deps (sem `WORKDIR`) → `WORKDIR /app` → `RUN apt-get` → `RUN pip` → `EXPOSE` → `CMD` (shell)

- Ordem ideal aplicada (resumo):

  `FROM` → `WORKDIR` → `ENV` → `RUN` deps de sistema → `COPY` deps → `RUN pip` → `COPY` app → `EXPOSE` → `CMD` (exec)

  Blocos ainda pendentes nas fases 4–6: `USER`, `HEALTHCHECK`, multistage, base slim com tag fixa.

- Três movimentos estruturais que você fez e por quê:

| # | Movimento | Motivo |
|---|-----------|--------|
| 1 | `WORKDIR /app` imediatamente após `FROM` | Garante que `COPY` e `RUN` operem no mesmo diretório; corrige o build quebrado (arquivos em `/` vs comandos em `/app`) |
| 2 | `COPY requirements.txt` + `pip install` **antes** de `COPY metrics_exporter.py` | Separa dependências do código da app — melhora cache de camadas e permite rebuild rápido quando só o `.py` muda |
| 3 | `EXPOSE` e `CMD` ao final, após toda cópia/instalação | Bloco de runtime no fim do Dockerfile; `CMD` em exec form (`["python", "..."]`) para PID 1 e sinais corretos |

---

## 3. Dockerfile gerado por IA

- Prompt principal usado (resumo ou cole):

  ```
  @metrics_exporter.py @requirements.txt @especificacao_app.md @dossie_container_integrado.md

  Gere ou refine um Dockerfile de produção conforme a especificação.
  Itere com base nos achados das seções 1 e 2.
  Endureça também o .dockerignore.
  ```

- O que a IA acertou na primeira sugestão:

  - Base `python:3.12.9-slim` com tag fixa
  - `WORKDIR /app` antes de `COPY`/`RUN`
  - `COPY` seletivo (`requirements.txt` + `metrics_exporter.py`)
  - `USER app` não-root com `groupadd`/`useradd`
  - `CMD` exec form e `HEALTHCHECK` em `/health` via stdlib (`urllib.request`)
  - Remoção de segredos (`METRICS_API_KEY`, `DEBUG`) e de pacotes de privilégio (`sudo`, `vim`, etc.)
  - `.dockerignore` ampliado (`.git`, `.env`, `*.md`, `example.py`, `pre-changes/`)

- O que você corrigiu manualmente ou na iteração v2:

  - **Multistage explícito** — stage `builder` com `pip install --prefix=/install` e `COPY --from=builder` no runtime (a 1ª sugestão era single-stage como aula-12)
  - **`mkdir -p /install` no builder** — `requirements.txt` é stdlib-only; sem isso `pip` não criava `/install` e o `COPY --from=builder` falhava
  - **`chown -R app:app /app`** após cópias — garante permissão de leitura para o usuário `app`
  - **`.dockerignore`** — inclusão de `verificar_*.py` e `dossie_container_integrado.md` além do que a spec lista
  - **`EXPOSE 8080` apenas** — removida porta 22 do baseline

- Trecho do Dockerfile final que veio da IA vs editado por você:

  | Origem | Trecho |
  |--------|--------|
  | IA (mantido) | `FROM python:3.12.9-slim`, `USER app`, `HEALTHCHECK`, `CMD ["python", "metrics_exporter.py"]` |
  | IA → editado (v2) | Multistage: `AS builder` + `pip install --prefix=/install` + `COPY --from=builder /install /usr/local` |
  | Manual | `RUN chown -R app:app /app` antes de `USER app` |

---

## 4. Multistage build

| Stage | Nome (`AS`) | Responsabilidade | O que **não** vai para o runtime |
|-------|-------------|------------------|----------------------------------|
| 1 | `builder` | Copia `requirements.txt` e executa `pip install --prefix=/install` | Camada de build do pip como root; diretório de trabalho `/app` do builder; `requirements.txt` (não copiado para o runtime) |
| 2 | `runtime` | Imagem final: usuário `app`, app Python, `HEALTHCHECK`, `CMD` | `gcc`, `build-essential`, `git`, `curl`, `vim`, `sudo`; segredos em `ENV`; stage `builder` inteiro (descartado após `COPY --from`) |

- Instruções `COPY --from=` usadas:

  ```dockerfile
  COPY --from=builder /install /usr/local
  ```

  Apenas os pacotes Python instalados no prefixo `/install` do builder entram no runtime. Ferramentas de sistema, caches de `apt`/`pip` e o próprio filesystem do builder ficam fora da imagem final.

---

## 5. Otimização de imagem

- Tamanho antes (`docker images`): **1,74 GB** (`metrics-exporter:estrutura` — pós-§2, ainda com `python:latest` + `apt-get install gcc build-essential git curl vim sudo`)
- Tamanho depois: **186 MB** (`metrics-exporter:integrador` — multistage + `python:3.12.9-slim`)
- Maior fonte de redução: troca de **`python:latest` (imagem completa Debian)** para **`python:3.12.9-slim`** e remoção dos pacotes de sistema (`sudo`, `vim`, `gcc`, etc.) que o baseline instalava no runtime
- Trade-off aceito (se houver): com `requirements.txt` stdlib-only, o stage `builder` não reduz pacotes Python neste exercício, mas adiciona uma etapa de build — o ganho imediato vem da base slim e da ausência de ferramentas; o multistage passa a valer quando houver dependências com wheels/binários compilados

**Comando usado:** `docker images metrics-exporter:estrutura metrics-exporter:integrador`

**Redução aproximada:** ~89% (~1,55 GB a menos)

---

## 6. Segurança e boas práticas

- Veredito de segurança: **aprovar com ressalvas**
- Correção de segurança mais crítica aplicada: remoção de `ENV METRICS_API_KEY` e `ENV DEBUG` do Dockerfile — segredos e flags de debug não persistem mais na imagem; injeção só no deploy (`docker run -e` / orchestrator secrets)
- Checklist (marque ao concluir):

- [x] Tag fixa em base slim
- [x] Sem segredos em ENV/ARG
- [x] USER não-root
- [x] CMD exec form
- [x] HEALTHCHECK coerente
- [x] `.dockerignore` robusto
- [x] Sem ferramentas de privilégio no runtime

### Validação

| Passo | Resultado |
|-------|-----------|
| Hadolint (`docker run --rm -i hadolint/hadolint < Dockerfile`) | ok — exit 0, sem avisos |
| `docker build -t metrics-exporter:integrador .` | ok |
| `docker run` + `curl /health` | ok — `200 ok` |
| `python example.py` | ok |

### Ressalvas pendentes (app, fora do Dockerfile)

- `metrics_exporter.py` escuta `0.0.0.0` por padrão — aceitável em container, mas rede do host/orquestrador deve restringir exposição
- `/metrics` sem autenticação — se `METRICS_API_KEY` for exigida em produção, validar no código ou proteger via proxy/mTLS

---

## Checklist de entrega

- [x] `python example.py` verde
- [x] `docker build` e `curl /health` verdes
- [x] Seções 1–6 preenchidas
- [x] `python verificar_entrega.py` retorna **0**
