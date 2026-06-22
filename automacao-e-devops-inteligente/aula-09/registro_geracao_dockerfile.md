# Registro — Dockerfile gerado por IA

Documente o ciclo **gerar → revisar → iterar → validar**. O baseline **não** traz `Dockerfile` — você cria com IA durante a aula.

## Entrada para a IA

- Prompt principal usado (cole ou resuma): Gerar Dockerfile completo para produção com base fixa `python:3.12.x-slim`, cache de `requirements.txt`, USER não-root, CMD exec form, HEALTHCHECK em `/health`, COPY seletivo (sem `example.py` nem `.md`); gerar `.dockerignore` coerente.
- Arquivos referenciados (`@metrics_exporter.py`, `@requirements.txt`, `@especificacao_app.md`): os três referenciados no prompt.

---

## Versão 1 (gerada pela IA)

```dockerfile
FROM python:3.12.8-slim

WORKDIR /app

RUN addgroup --system app && adduser --system --group app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=app:app metrics_exporter.py .

USER app

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD ["python", "-c", "import urllib.request; r=urllib.request.urlopen('http://127.0.0.1:8080/health', timeout=2); exit(0 if r.read() == b'ok' else 1)"]

CMD ["python", "metrics_exporter.py"]
```

- `.dockerignore` gerado (sim / não — cole se sim): **sim**

```
# Smoke test e documentação — não entram na imagem
example.py
*.md

# Artefatos Python
__pycache__/
*.py[cod]
*.pyo
.pytest_cache/

# Baseline / material da aula
pre-changes/

# Git e IDE
.git/
.gitignore
.vscode/
.idea/
```

---

## Revisão humana da v1

### Estrutura — ordem dos blocos

| Etapa | Avaliação |
|-------|-----------|
| `FROM` → `WORKDIR` | Base fixa e diretório de trabalho definidos antes de qualquer `COPY`/`RUN` — correto. |
| Criação de usuário (`RUN addgroup/adduser`) | Antes do `USER app`, enquanto ainda há privilégios de root para provisionar — correto. |
| `COPY requirements.txt` → `pip install` → `COPY` código | Camada de cache de dependências separada do código da app — alinhado à especificação. |
| `USER app` antes de `EXPOSE` / `HEALTHCHECK` / `CMD` | Processo final não roda como root — correto. |
| `HEALTHCHECK` antes de `CMD` | Convenção legível; ambos descrevem runtime — aceitável. |

### Riscos — base, segredos, root

| Tema | Avaliação |
|------|-----------|
| **Base** | `python:3.12.8-slim` — tag fixa com patch, variante slim; sem `latest`. |
| **Segredos** | Nenhum `ENV`/`ARG` com credenciais ou tokens; conforme `especificacao_app.md`. |
| **Root** | `pip install` roda como root (esperado); app e `HEALTHCHECK` executam após `USER app`. |
| **Contexto de build** | `COPY` seletivo (só `requirements.txt` + `metrics_exporter.py`); `.dockerignore` exclui `example.py`, `*.md`, `pre-changes/`, cache Python e `.git`. |

### Runtime — `CMD` e `HEALTHCHECK`

| Tema | Avaliação |
|------|-----------|
| **CMD** | Exec form `["python", "metrics_exporter.py"]` — PID 1 correto, sem shell wrapper. |
| **HEALTHCHECK** | Exec form com stdlib (`urllib`); valida rota `/health` e corpo `b'ok'` — contrato da app respeitado. |
| **Porta** | `EXPOSE 8080` coerente com default da app; **ressalva:** health check fixo em `8080` — se `PORT` for alterado no `docker run`, o probe falha enquanto o serviço responde em outra porta. |
| **Observabilidade** | Sem `PYTHONUNBUFFERED=1` — logs Python podem bufferizar; aceitável neste baseline, melhoria opcional. |

### Hadolint

```
docker run --rm -i hadolint/hadolint < Dockerfile
```

**Resultado:** nenhum aviso.

---

| # | Achado (estrutura / risco / runtime) | Origem (humano / Hadolint / Copilot) | Correção pedida à IA |
|---|--------------------------------------|--------------------------------------|----------------------|
| 1 | Ordem dos blocos correta: base → usuário → cache de deps → código → `USER` → runtime (`EXPOSE`, `HEALTHCHECK`, `CMD`). | humano | nenhuma |
| 2 | Base com tag fixa (`3.12.8-slim`); sem segredos em `ENV`/`ARG`; processo da app como não-root; `.dockerignore` coerente com `COPY` seletivo. | humano | nenhuma |
| 3 | `HEALTHCHECK` hardcoded em `127.0.0.1:8080` — não acompanha env `PORT` configurável em `metrics_exporter.py`. | humano | opcional: declarar `ENV PORT=8080` e documentar que o health check assume essa porta; ou aceitar como ressalva (app minimalista usa 8080 fixo em produção). |

---

## Versão 2 (após iterar com IA)

Correção aplicada: **apenas achado #3** — `ENV PORT=8080` + `HEALTHCHECK` lê `PORT` do ambiente (alinha probe com `metrics_exporter.py`).

```dockerfile
FROM python:3.12.8-slim

WORKDIR /app

RUN addgroup --system app && adduser --system --group app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=app:app metrics_exporter.py .

# App e HEALTHCHECK leem PORT (default 8080; sobrescreva com -e PORT=... no run).
ENV PORT=8080

USER app

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD ["python", "-c", "import os, urllib.request; p=os.environ.get('PORT', '8080'); r=urllib.request.urlopen(f'http://127.0.0.1:{p}/health', timeout=2); exit(0 if r.read() == b'ok' else 1)"]

CMD ["python", "metrics_exporter.py"]
```

---

## Validação

| Passo | Resultado (ok / falhou / não rodei) | Observação |
|-------|-------------------------------------|------------|
| `python example.py` | ok | Smoke test local passou antes do build. |
| Hadolint no Dockerfile | ok | `docker run --rm -i hadolint/hadolint < Dockerfile` — nenhum aviso. |
| `docker build` | ok | `docker build -t metrics-exporter:ia .` — 11/11 steps, imagem `metrics-exporter:ia` criada (~5.9s). |
| `docker run` + `curl /health` | ok | `docker run --rm -p 8080:8080 metrics-exporter:ia` + `curl http://127.0.0.1:8080/health` → corpo `ok`. |

---

## Iterações com a IA

- O que a IA acertou de primeira:
  - Estrutura completa e ordem dos blocos (base → cache de deps → código → `USER` → runtime).
  - Base `python:3.12.8-slim` com tag fixa; sem `latest`, sem segredos em `ENV`/`ARG`.
  - Usuário não-root (`adduser`/`addgroup`, `USER app`, `--chown` no COPY do código).
  - `CMD` em exec form; `HEALTHCHECK` com stdlib (`urllib`) validando `/health` e corpo `ok`.
  - `COPY` seletivo e `.dockerignore` coerente (exclui `example.py`, `*.md`, `pre-changes/`, cache).
  - Hadolint passou sem avisos na v1.

- O que a IA errou ou omitiu (e você corrigiu no prompt):
  - **Achado #3 (v1):** `HEALTHCHECK` com porta `8080` hardcoded, enquanto `metrics_exporter.py` aceita `PORT` via env — inconsistência de runtime.
  - **Correção (prompt 4):** pedir à IA ajuste mínimo na v2 — `ENV PORT=8080` + probe lendo `os.environ.get('PORT', '8080')`.
  - Não foi necessário reescrever o Dockerfile; prompt inicial e `especificacao_app.md` já cobriram o restante.

- Algo que você **não** aceitou cegamente da sugestão da IA:
  - Aceitar a v1 só porque Hadolint não apontou nada. Linter não cobre alinhamento entre `HEALTHCHECK` e contrato da app (`PORT` configurável).
  - **Risco concreto:** deploy com `-e PORT=9090` — app sobe na 9090, probe continua em 8080 → orquestrador (Docker/K8s) marca o container como **unhealthy** e pode reiniciá-lo em loop, apesar do serviço estar funcional na porta correta.

---

## Síntese — Dockerfile gerado por IA

- **Qualidade da v1:** Com prompt estruturado + `especificacao_app.md`, a v1 saiu sólida de primeira — ordem de camadas, base fixa, não-root, exec form, `.dockerignore` e Hadolint limpo; suficiente para build e `curl /health` na porta default.
- **Valor da revisão humana:** Hadolint não substitui leitura do contrato da app — a v1 passava no linter, mas o `HEALTHCHECK` ignorava `PORT` configurável; só a revisão de runtime (humano + spec) expôs risco de falso unhealthy em deploy com porta customizada.
- **Iteração útil:** A v2 corrigiu **só** o achado #3 (`ENV PORT=8080` + probe lendo env) — uma iteração cirúrgica, sem rewrite; prova que iterar com critérios da revisão é mais eficiente que regerar o Dockerfile inteiro.
- **Critério de veredito final:** Aprovar quando estrutura, risco e runtime passam em **revisão humana + linter + build + smoke** (`example.py`, `docker run`, `curl /health`); rejeitar ou iterar se houver desalinhamento com a spec ou comportamento em runtime que ferramentas automáticas não detectam.

---

## Veredito

- Dockerfile final: **aprovado**
- Pronto para produção? **sim** — v2 validada end-to-end (build, run, health); app minimalista stdlib, sem segredos na imagem e probe alinhado com `PORT`.
