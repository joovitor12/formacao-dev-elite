# Plano de otimização de imagem

Registre **antes/depois** da otimização do Dockerfile inchado (funcional, porém pesado).

## Baseline (antes)

```bash
docker build -t metrics-exporter:antes .
docker images metrics-exporter:antes --format "{{.Repository}}:{{.Tag}} {{.Size}}"
```

- Tamanho registrado: `metrics-exporter:antes 1.71GB`
- Principais fontes de gordura identificadas:
  - Base **full** `python:3.12` (não `slim`), com toolchain Debian embutida na imagem oficial (~694 MB só na camada `apt` da base).
  - `apt` no **runtime**: `curl`, `vim`, `git`, `netcat-openbsd` — ferramentas de debug (~74.5 MB na camada `RUN`), sem limpeza de `/var/lib/apt/lists/*`.
  - `apt` no **builder**: `gcc`, `build-essential`, `git`, `curl`, `vim` — desnecessários para app stdlib-only; sem `--no-install-recommends` nem cleanup.
  - `COPY . .` com `.dockerignore` mínimo (só `__pycache__`) — contexto ~20 KB inclui `pre-changes/`, `prompts.md`, `plano_otimizacao_imagem.md`, `example.py`.
  - `COPY --from=builder /app` inteiro + `site-packages`/`bin` em bloco — leva lixo do contexto para a imagem final; `pip install` roda mesmo com `requirements.txt` vazio (stdlib only).

| # | Fonte de tamanho / superfície | Categoria (base / apt / pip / COPY / camadas / runtime) | Ação de otimização |
|---|------------------------------|-----------------------------------------------------------|-------------------|
| 1 | `FROM python:3.12` (imagem full, tag flutuante) | base | Trocar para `python:3.12-slim` com tag/digest fixo |
| 2 | `apt-get install` no runtime (`curl`, `vim`, `git`, `netcat-openbsd`) | apt / runtime | Remover pacotes de debug; manter só o essencial ao health/app |
| 3 | `apt-get install` no builder (`gcc`, `build-essential`, `git`, `curl`, `vim`) | apt / camadas | Eliminar ou restringir ao que `pip` realmente compila; `--no-install-recommends` + cleanup no mesmo `RUN` |
| 4 | `COPY . .` + `.dockerignore` com só `__pycache__` | COPY / contexto | Expandir `.dockerignore`; `COPY` seletivo (`metrics_exporter.py`, `requirements.txt`) |
| 5 | `COPY --from=builder /app` + `site-packages`/`bin` inteiros | COPY / camadas | Copiar só artefatos de runtime; evitar `pip install` quando deps = stdlib |

---

## Otimizações aplicadas

| # | Mudança no Dockerfile / .dockerignore | Ganho esperado (tamanho / segurança / cache) |
|---|----------------------------------------|---------------------------------------------|
| 1 | `FROM python:3.12.13-slim` (tag fixa) no runtime **e** no builder, em vez de `python:3.12` full | **Tamanho:** maior ganho (~1 GB+ → ~150–200 MB só na base). **Segurança:** superfície menor, builds reproduzíveis. |
| 2 | Remover `RUN apt-get install` no **runtime** (`curl`, `vim`, `git`, `netcat-openbsd`); app usa só stdlib (`http.server`) | **Tamanho:** ~75 MB a menos na camada `RUN`. **Segurança:** menos binários e vetores de exploração no container final. |
| 3 | `.dockerignore` robusto (`pre-changes/`, `*.md`, `example.py`, `.git`, `__pycache__/`, etc.) + `COPY metrics_exporter.py` e `COPY requirements.txt` em vez de `COPY . .` | **Tamanho/contexto:** contexto mínimo; nada de docs ou pasta espelho na imagem. **Cache:** rebuild mais rápido quando só o código muda. |
| 4 | Builder enxuto: remover `apt` de build (`gcc`, `build-essential`, `git`, `curl`, `vim`) enquanto `requirements.txt` for stdlib-only; `pip install --no-cache-dir -r requirements.txt`; copiar só `metrics_exporter.py` (e `site-packages`/`bin` se passar a haver deps) | **Tamanho:** elimina camada pesada no builder e evita cópia wholesale de `/app`. **Cache:** `pip` sem cache local na camada. |
| 5 | `RUN adduser --disabled-password app` + `USER app`; `HEALTHCHECK` em `GET /health` (via Python, sem `curl`); remover `ENV DEBUG=true`; manter `PORT` e `PYTHONUNBUFFERED` | **Segurança:** processo não-root + verificação de saúde nativa. **Superfície:** sem flag de debug em produção. Comportamento da app preservado. |

---

## Depois

```bash
docker build -t metrics-exporter:depois .
docker images metrics-exporter:depois --format "{{.Repository}}:{{.Tag}} {{.Size}}"
docker history metrics-exporter:depois --no-trunc | head
```

- Tamanho registrado: `metrics-exporter:depois 177MB`
- Redução aproximada (absoluta ou %): **~1.53 GB** (~**89,6%** menor que o baseline de 1.71 GB)

**Inspeção de camadas (`docker history`):**

| SIZE | Camada (resumo) |
|------|-----------------|
| 12.3 kB | `COPY --chown=app:app metrics_exporter.py` |
| 4.1 kB | `COPY /install /usr/local` (pip stdlib-only, quase vazio) |
| 45.1 kB | `RUN addgroup/adduser app` |
| 41.4 MB | Python compilado na base slim |
| 4.9 MB | `apt` mínimo da imagem oficial slim |
| 87.4 MB | Debian trixie slim (base) |

**Ausente em `:depois` (presente em `:antes`):**

- Camada `RUN apt-get install curl vim git netcat` (~74.5 MB)
- `COPY /app` inteiro (~77.8 kB + lixo de contexto)
- `COPY site-packages` (~5 MB) e `COPY /usr/local/bin`
- Base full com toolchain (~694 MB na camada `apt` da imagem oficial)

**Metadados de runtime adicionados:** `USER app`, `HEALTHCHECK` (Python → `/health`), sem `ENV DEBUG`.

---

## O que removemos vs o que mantivemos

**Removido da imagem final:**

- Base `python:3.12` full → substituída por `python:3.12.13-slim`
- `apt` no runtime (`curl`, `vim`, `git`, `netcat-openbsd`)
- `apt` no builder (`gcc`, `build-essential`, `git`, `curl`, `vim`)
- `COPY . .` e lixo de contexto (`pre-changes/`, `*.md`, `example.py`)
- `ENV DEBUG=true`
- Cópia wholesale de `/app`, `site-packages` e `/usr/local/bin` inteiros do builder

**Mantido (necessário ao runtime):**

- `metrics_exporter.py` e endpoints `/health`, `/metrics`
- `ENV PORT=8080` e `ENV PYTHONUNBUFFERED=1`
- `CMD ["python", "metrics_exporter.py"]` e `EXPOSE 8080`
- Multistage com `pip install --no-cache-dir --prefix=/install` (padrão para quando houver deps)

---

## Camadas e contexto

- Ajustes em `.dockerignore`: `pre-changes/`, `*.md`, `example.py`, `__pycache__/`, `.git/`
- `COPY` seletivo vs `COPY . .`: só `requirements.txt` no builder e `metrics_exporter.py` no runtime
- `pip install --no-cache-dir` / combinação de `RUN`: `--prefix=/install` no builder; sem `apt` enquanto deps = stdlib

---

## Runtime e segurança (sem regredir)

Validação: `python example.py` (antes do build) + container `metrics-exporter:depois` com `/health` → `200 ok` e `/metrics` com `uptime_seconds`.

- [x] App responde em `/health` após otimização
- [x] `USER` não-root (`adduser --system app` + `USER app`)
- [x] `HEALTHCHECK` coerente — `python -c` + `urllib` em `127.0.0.1:$PORT/health`, espera `b'ok'`
- [x] Ferramentas de build **ausentes** na imagem final (sem `gcc`, `build-essential`, `git`, `vim`, `curl` no runtime)
- [x] Base enxuta (`python:3.12.13-slim`, tag fixa)

---

## O que aprendi sobre otimização de imagens

- **Maior ganho medido:** trocar `python:3.12` full por `python:3.12.13-slim` e remover `apt` de debug no runtime levou de **1.71 GB → 177 MB** (~89,6%); `docker history` mostra que a base full sozinha carrega centenas de MB de toolchain que nunca rodam em produção.
- **Trade-off aceito:** nenhum funcional — ferramentas (`curl`, `vim`, `git`) e `DEBUG=true` saíram sem perder `/health` nem `/metrics`; mantivemos multistage com `pip` mesmo com deps stdlib-only para preservar o padrão da trilha (estágio único seria ainda mais simples).
- **Armadilha de COPY/contexto:** `COPY . .` com `.dockerignore` mínimo envia `pre-changes/`, `*.md` e `example.py` para o daemon e, pior, para a imagem via `COPY --from=builder /app`; contexto e camadas incham sem benefício — `.dockerignore` robusto + `COPY` seletivo resolvem.
- **Critério do checklist:** otimizar tamanho **sem regredir** — app em `/health`, `USER` não-root, `HEALTHCHECK` coerente, sem ferramentas de build na imagem final e base slim com tag fixa; ganho de MB não vale quebrar comportamento ou segurança.

---

## Resumo

- Otimização com maior impacto neste app: troca de `python:3.12` full para `python:3.12.13-slim` + remoção de `apt` no runtime
- Trade-off aceito (se houver): nenhum funcional — app stdlib-only não precisa de ferramentas de debug na imagem
- Algo que IA sugeriu e você validou ou rejeitou: estágio único sem `pip` (válido para stdlib-only, mas mantido multistage enxuto para o padrão da trilha)
