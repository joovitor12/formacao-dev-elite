# Aula 10 — Multistage builds

**Objetivo:** refatorar um Dockerfile **single-stage inchado** para **multistage** (`builder` + `runtime`) — separar instalação de dependências/ferramentas de build do artefato final enxuto.

**Enquadramento:** depois de gerar e estruturar Dockerfile, multistage reduz tamanho, superfície de ataque e lixo de build na imagem que sobe em produção. Só o necessário chega ao stage final via `COPY --from=`.

**Ferramentas:** Copilot Chat / agente com `@workspace`, opcionalmente **Hadolint** e `docker images` para comparar tamanho.

**Material:**


| Arquivo                    | Papel                                                                   |
| -------------------------- | ----------------------------------------------------------------------- |
| `Dockerfile`               | Baseline **single-stage** com gcc, git, vim e pip no mesmo stage final. |
| `.dockerignore`            | Contexto de build pareado com `COPY`.                                   |
| `requirements.txt`         | Deps instaladas no stage builder.                                       |
| `metrics_exporter.py`      | App HTTP mínimo (`/health`, `/metrics`).                                |
| `mapa_multistage_build.md` | Mapa de stages, `COPY --from`, checklist e comparação.                  |
| `example.py`               | Smoke test local antes do `docker build`.                               |


**Fluxo em sala:**

1. Analisar o single-stage baseline → preencher `mapa_multistage_build.md` (problemas).
2. Desenhar stages builder e runtime.
3. Refatorar `Dockerfile` ao vivo (IA opcional).
4. `docker build`, `docker run`, comparar tamanho (opcional).
5. Completar checklist e resumo no mapa.

---

## 1. Por que multistage

```
Antes de editar o Dockerfile, explique em bullets:

- o que permanece na imagem final de um single-stage com gcc/git/vim;
- o que um stage builder resolve;
- diferença entre "copiar tudo" e `COPY --from=builder` só o necessário.

Não reescreva o Dockerfile ainda.
```

---

## 2. Diagnosticar o baseline single-stage

```
@Dockerfile @requirements.txt @metrics_exporter.py

Liste o que o stage único acumula hoje:

- ferramentas de build desnecessárias no runtime;
- camadas que poderiam ficar só no builder;
- o que falta no runtime (USER, HEALTHCHECK, etc.).

Preencha "Baseline analisado" em mapa_multistage_build.md.
```

---

## 3. Desenhar os stages

```
@mapa_multistage_build.md

Proponha dois stages:

1. **builder** — pip install (prefix ou site-packages), ferramentas de compilação se precisar.
2. **runtime** — base slim, COPY --from=builder das deps, COPY do app, USER, HEALTHCHECK, CMD.

Preencha as tabelas "Estágios" e "O que copia entre stages".

Não implemente ainda.
```

---

## 4. Refatorar para multistage

```
@Dockerfile @mapa_multistage_build.md

Refatore para multistage seguindo o desenho:

- FROM ... AS builder
- RUN pip install --prefix=/install ... (ou padrão equivalente)
- FROM ... AS runtime
- COPY --from=builder /install /usr/local
- COPY metrics_exporter.py
- USER não-root, HEALTHCHECK com python urllib, CMD exec form

Cole trechos COPY --from= no mapa.
```

---

## 5. Validar build e runtime

```
python example.py
docker build -t metrics-exporter:multistage .
docker run --rm -p 8080:8080 -e PORT=8080 metrics-exporter:multistage
curl http://127.0.0.1:8080/health

Opcional — comparar tamanho:

docker images metrics-exporter:multistage
# (rebuild temporário do single-stage baseline para comparar, se quiser)

Registre na seção Comparação do mapa.
```

---

## 6. Revisar com IA e Hadolint

```
Rode Hadolint (opcional):

docker run --rm -i hadolint/hadolint < Dockerfile

Peça ao Copilot: "Revise este multistage — algo do builder vazou para o runtime?"

Registre achados no resumo do mapa.
```

---

## Comandos úteis

```bash
cd automacao-e-devops-inteligente/aula-10
python example.py
```

**Build e smoke:**

```bash
docker build -t metrics-exporter:multistage .
docker run --rm -p 8080:8080 metrics-exporter:multistage
curl http://127.0.0.1:8080/health
```

**Comparar tamanho (opcional):**

```bash
docker images | grep metrics-exporter
```

**Hadolint (opcional):**

```bash
docker run --rm -i hadolint/hadolint < Dockerfile
```

---

## Máxima da aula

**Multistage não é ornamento — builder prepara; runtime executa; o que sobra no final é o mínimo que produção precisa.**