# Aula 09 — Dockerfile gerado por IA

**Objetivo:** **gerar dinamicamente** o `Dockerfile` (e `.dockerignore`) da aplicação com IA a partir do código e da especificação — revisar, iterar e validar antes de confiar na imagem.

**Enquadramento:** revisar e estruturar Dockerfile manualmente prepara o terreno; aqui a IA **produz** o artefato. Quem containeriza continua **responsável** por validar estrutura, riscos e runtime — o modelo sugere, o humano aprova.

**Ferramentas:** Copilot Chat / agente com `@workspace`, opcionalmente **Hadolint**.

**Material:**

| Arquivo | Papel |
| -------- | ------ |
| `metrics_exporter.py` | App HTTP mínimo — **sem** Dockerfile no repositório inicial. |
| `requirements.txt` | Camada de deps (stdlib only neste baseline). |
| `especificacao_app.md` | Restrições e contexto para orientar a geração (exemplo preenchido desta aula). |
| `especificacao_app.template.md` | Template reutilizável — copiar e preencher para outras apps. |
| `registro_geracao_dockerfile.md` | Registro de prompts, versões, revisão e validação. |
| `example.py` | Smoke test local **antes** do `docker build`. |

**Baseline:** não há `Dockerfile` nem `.dockerignore` — você os **cria com IA** durante a aula.

**Fluxo em sala:**

1. Confirmar app local (`python example.py`).
2. Prompt à IA → **Dockerfile v1** (+ `.dockerignore` se aplicável).
3. Revisar v1 com critérios de risco e estrutura (aulas anteriores do bloco docker).
4. Iterar com IA → **v2** → Hadolint / `docker build` / `docker run`.
5. Preencher `registro_geracao_dockerfile.md`.

---

## 1. O que a IA precisa saber antes de gerar

```
Antes de pedir o Dockerfile, liste em bullets:

- quais arquivos/contexto a IA deve ler (código, deps, especificação);
- restrições obrigatórias (tag fixa, não-root, exec form, health check);
- o que **não** pedir (segredo em ENV, python:latest, COPY . . sem ignore).

Não gere Dockerfile ainda.
```

---

## 2. Gerar Dockerfile v1

```
@metrics_exporter.py @requirements.txt @especificacao_app.md

Gere um Dockerfile completo para containerizar esta app em produção.

Requisitos:
- python:3.12.x-slim com tag fixa
- camada de cache para requirements.txt antes do código
- USER não-root, CMD exec form, HEALTHCHECK em /health
- COPY seletivo (não copiar example.py nem arquivos .md)

Gere também um .dockerignore coerente.

Salve os arquivos e cole o Dockerfile v1 em registro_geracao_dockerfile.md.
```

---

## 3. Revisar a v1 (humano + linter)

```
@Dockerfile @.dockerignore @registro_geracao_dockerfile.md

Revise o Dockerfile gerado como na revisão de imagens e na estrutura:

- ordem dos blocos, riscos (base, segredos, root), runtime (CMD, HEALTHCHECK).

Rode Hadolint (opcional):

docker run --rm -i hadolint/hadolint < Dockerfile

Preencha a tabela "Revisão humana da v1".
```

---

## 4. Iterar com a IA (v2)

```
@Dockerfile @registro_geracao_dockerfile.md

Com base nos achados da revisão, peça à IA corrigir **apenas** os pontos listados — sem rewrite desnecessário.

Cole Dockerfile v2 no registro.
```

---

## 5. Validar build e runtime

```
Após v2:

python example.py
docker build -t metrics-exporter:ia .
docker run --rm -p 8080:8080 metrics-exporter:ia
curl http://127.0.0.1:8080/health

Registre resultados na seção Validação do registro.
```

---

## 6. Limites da geração automática

```
@registro_geracao_dockerfile.md

Responda:

- o que a IA acertou sem ajuda;
- o que você precisou corrigir no prompt ou no arquivo manualmente;
- um risco que a IA poderia introduzir se você aceitasse a v1 cegamente.
```

---

## 7. Síntese

```
@registro_geracao_dockerfile.md

Em 4 bullets: o que aprendeu sobre **Dockerfile gerado por IA**?

Inclua: qualidade da v1, valor da revisão humana, iteração útil e critério de veredito final.
```

---

## Comandos úteis

```bash
cd automacao-e-devops-inteligente/aula-09
python example.py
```

**Após gerar Dockerfile:**

```bash
docker build -t metrics-exporter:ia .
docker run --rm -p 8080:8080 metrics-exporter:ia
curl http://127.0.0.1:8080/health
```

**Hadolint (opcional):**

```bash
docker run --rm -i hadolint/hadolint < Dockerfile
```

---

## Máxima da aula

**IA acelera o rascunho do Dockerfile — quem faz deploy valida estrutura, risco e runtime; gerar não substitui revisar.**
