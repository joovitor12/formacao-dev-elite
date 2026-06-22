# Aula 11 — Otimização de imagens

**Objetivo:** **otimizar** uma imagem Docker já funcional — reduzir tamanho, camadas desnecessárias e superfície de ataque sem quebrar runtime (`/health`, `/metrics`).

**Enquadramento:** imagem que **builda e roda**, mas carrega peso evitável — base pesada (`python:3.12` full), pacotes apt extras, `COPY . .`, cache de pip, `.dockerignore` fraco e cópias amplas entre estágios do Dockerfile.

**Ferramentas:** Copilot Chat / agente com `@workspace`, `docker images`, opcionalmente **Hadolint** e `docker history`.

**Material:**

| Arquivo | Papel |
| -------- | ------ |
| `Dockerfile` | Baseline **funcional porém inchado** — medir, diagnosticar e otimizar. |
| `.dockerignore` | Fraco (`__pycache__` só) — reforçar na otimização. |
| `requirements.txt` | Deps (stdlib) — camada de pip no build. |
| `metrics_exporter.py` | App HTTP mínimo. |
| `plano_otimizacao_imagem.md` | Antes/depois, ações, checklist e resumo. |
| `example.py` | Smoke test local antes do `docker build`. |

**Fluxo em sala:**

1. Medir baseline (`docker build` + `docker images`).
2. Diagnosticar fontes de gordura → `plano_otimizacao_imagem.md`.
3. Otimizar Dockerfile e `.dockerignore` ao vivo (IA opcional).
4. Rebuild, medir de novo, validar `/health`.
5. Completar checklist e resumo.

---

## 1. O que otimizar em uma imagem

```
Antes de editar arquivos, liste em bullets:

- cinco alavancas de tamanho e superfície (base, apt, pip, COPY/contexto, camadas RUN);
- como medir ganho (`docker images`, `docker history`);
- o que **não** sacrificar (health, usuário não-root, comportamento da app).

Não abra Dockerfile ainda.
```

---

## 2. Medir e diagnosticar o baseline

```
@Dockerfile @.dockerignore @requirements.txt

Build e meça:

docker build -t metrics-exporter:antes .
docker images metrics-exporter:antes

Liste fontes de gordura no baseline (base full, apt no runtime, COPY . ., etc.).

Preencha "Baseline (antes)" em plano_otimizacao_imagem.md.
```

---

## 3. Plano de otimização

```
@plano_otimizacao_imagem.md @Dockerfile

Priorize 3–5 mudanças concretas, por exemplo:

- trocar para python:3.12.x-slim com tag fixa;
- remover apt desnecessário no runtime (curl, vim, git);
- COPY seletivo + .dockerignore robusto;
- pip --no-cache-dir; copiar só artefatos necessários da instalação;
- USER não-root + HEALTHCHECK; remover ENV de debug.

Preencha a tabela "Otimizações aplicadas" — sem implementar ainda.
```

---

## 4. Aplicar otimizações

```
@Dockerfile @.dockerignore @plano_otimizacao_imagem.md

Implemente o plano sem alterar o comportamento da app.

Rode python example.py antes do build.
```

---

## 5. Medir depois e validar

```
docker build -t metrics-exporter:depois .
docker images metrics-exporter:depois
docker run --rm -p 8080:8080 -e PORT=8080 metrics-exporter:depois
curl http://127.0.0.1:8080/health

Opcional — inspecionar camadas:

docker history metrics-exporter:depois --no-trunc | head

Preencha "Depois" e checklist em plano_otimizacao_imagem.md.
```

---

## 6. Revisar com IA e Hadolint

```
Rode Hadolint (opcional):

docker run --rm -i hadolint/hadolint < Dockerfile

Peça ao Copilot: "Esta imagem ainda carrega algo desnecessário no runtime?"

Registre no resumo do plano.
```

---

## 7. Síntese

```
@plano_otimizacao_imagem.md

Em 4 bullets: o que aprendeu sobre **otimização de imagens**?

Inclua: maior ganho medido, trade-off aceito, armadilha de COPY/contexto e critério do checklist.
```

---

## Comandos úteis

```bash
cd automacao-e-devops-inteligente/aula-11
python example.py
```

**Antes / depois:**

```bash
docker build -t metrics-exporter:antes .
docker build -t metrics-exporter:depois .
docker images | grep metrics-exporter
```

**Smoke:**

```bash
docker run --rm -p 8080:8080 metrics-exporter:depois
curl http://127.0.0.1:8080/health
```

**Histórico de camadas (opcional):**

```bash
docker history metrics-exporter:depois
```

**Hadolint (opcional):**

```bash
docker run --rm -i hadolint/hadolint < Dockerfile
```

---

## Máxima da aula

**Imagem otimizada não é a menor de qualquer jeito — é a menor que ainda roda segura, observável e igual em produção.**
