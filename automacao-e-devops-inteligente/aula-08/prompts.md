# Aula 08 — Estrutura de um Dockerfile

**Objetivo:** entender e reorganizar a **estrutura** de um Dockerfile — blocos (`FROM`, `WORKDIR`, dependências, app, `USER`, `EXPOSE`, `HEALTHCHECK`, `CMD`), **ordem das instruções** e impacto no **cache de camadas**.

**Enquadramento:** depois de revisar riscos na imagem, o próximo passo é saber **montar** o arquivo na ordem certa. Estrutura errada pode quebrar runtime, invalidar cache a cada commit ou esconder falhas de health check.

**Ferramentas:** Copilot Chat / agente com `@workspace`, opcionalmente **Hadolint**.

**Material:**

| Arquivo | Papel |
| -------- | ------ |
| `Dockerfile` | Baseline desorganizado — blocos fora de ordem para mapear e corrigir. |
| `.dockerignore` | Contexto de build pareado com `COPY`. |
| `requirements.txt` | Arquivo para camada de dependências (stdlib only). |
| `metrics_exporter.py` | App mínimo containerizado. |
| `mapa_estrutura_dockerfile.md` | Mapa de blocos, ordem atual vs ideal, checklist. |
| `example.py` | Smoke test local da app (antes do `docker build`). |

**Fluxo em sala:**

1. Mapear blocos e ordem atual → preencher `mapa_estrutura_dockerfile.md`.
2. Reorganizar o `Dockerfile` ao vivo (IA opcional).
3. Validar com `python example.py` e, opcionalmente, `docker build` / `docker run`.

---

## 1. Blocos de um Dockerfile

```
Antes de abrir arquivos, liste em ordem os blocos típicos de um Dockerfile bem estruturado:

- base, workspace, dependências, código, identidade, rede, saúde, entrada.

Para cada bloco: instruções comuns e por que a ordem importa.

Não analise o Dockerfile ainda.
```

---

## 2. Mapear o baseline

```
@Dockerfile @requirements.txt @.dockerignore

Para cada instrução do Dockerfile:

- qual bloco representa;
- se está na ordem ideal;
- efeito no cache de build ou no runtime.

Preencha a tabela "Blocos do Dockerfile" em mapa_estrutura_dockerfile.md.
```

---

## 3. Ordem atual vs ideal

```
@mapa_estrutura_dockerfile.md

Monte a sequência ideal de instruções para este app (metrics_exporter + requirements.txt).

Explique pelo menos três movimentos (ex.: WORKDIR antes do COPY do app, deps antes do código, USER antes de CMD).

Não reescreva o Dockerfile inteiro ainda.
```

---

## 4. Camadas e cache

```
@Dockerfile @requirements.txt

Responda:

- o que invalida a camada de pip a cada mudança no código hoje;
- como separar COPY de requirements.txt do COPY de metrics_exporter.py;
- quando usar COPY seletivo vs COPY . .

Preencha a seção "Camadas e cache" no mapa.
```

---

## 5. Cruzar com IA e Hadolint

```
Rode Hadolint (opcional):

docker run --rm -i hadolint/hadolint < Dockerfile

Peça ao Copilot: "Reorganize este Dockerfile por blocos, sem mudar o comportamento."

Registre sugestões úteis e ruído na seção "Lacunas de estrutura".
```

---

## 6. Reorganizar o Dockerfile

```
@Dockerfile

Reorganize o Dockerfile na ordem estrutural correta:

1. FROM
2. WORKDIR
3. COPY requirements.txt + RUN pip install
4. COPY metrics_exporter.py
5. RUN useradd + USER não-root
6. EXPOSE
7. HEALTHCHECK (comando disponível na imagem — ex.: python urllib, não curl ausente)
8. CMD em exec form

Rode python example.py e, se possível, docker build && docker run.
```

---

## 7. Validar build e runtime (opcional)

```
Após reorganizar:

docker build -t metrics-exporter:estrutura .
docker run --rm -p 8080:8080 metrics-exporter:estrutura
curl http://127.0.0.1:8080/health

O que quebrava no baseline e passou a funcionar? Registre no resumo do mapa.
```

---

## 8. Síntese

```
@mapa_estrutura_dockerfile.md

Em 4 bullets: o que aprendeu sobre **estrutura de um Dockerfile**?

Inclua: bloco mais fora de ordem, impacto no cache, armadilha de runtime e critério de checklist.
```

---

## Comandos úteis

```bash
cd automacao-e-devops-inteligente/aula-08
python example.py
```

**Build e smoke (opcional):**

```bash
docker build -t metrics-exporter:estrutura .
docker run --rm -p 8080:8080 metrics-exporter:estrutura
curl http://127.0.0.1:8080/health
```

**Hadolint (opcional):**

```bash
docker run --rm -i hadolint/hadolint < Dockerfile
```

---

## Máxima da aula

**Dockerfile não é lista de comandos soltos — é sequência de blocos; ordem errada quebra cache, runtime ou health check.**
