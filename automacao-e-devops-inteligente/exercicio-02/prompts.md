# Exercício 02 — Prompts (containerização integrador)

Use com Copilot Chat / agente com `@workspace`.

---

## 1. Revisão do baseline

```
@Dockerfile @.dockerignore @metrics_exporter.py

Liste achados de revisão de imagem:

- trecho → categoria → severidade → impacto em produção.

Preencha seção 1 de dossie_container_integrado.md.

Não corrija ainda.
```

---

## 2. Estrutura e ordem

```
@Dockerfile @dossie_container_integrado.md

Mapeie ordem atual vs ideal dos blocos (FROM, WORKDIR, deps, app, USER, EXPOSE, HEALTHCHECK, CMD).

Preencha seção 2 — três movimentos estruturais prioritários.
```

---

## 3. Gerar / refinar com IA

```
@metrics_exporter.py @requirements.txt @especificacao_app.md @especificacao_app.template.md

Gere ou refine um Dockerfile de produção conforme a especificação.

Itere uma vez com base nos achados das seções 1 e 2.

Registre prompt, acertos e correções na seção 3 do dossiê.
```

---

## 4. Multistage

```
@Dockerfile @dossie_container_integrado.md

Refatore para dois stages (builder + runtime).

Documente stages e COPY --from= na seção 4.
```

---

## 5. Otimizar imagem

```
@Dockerfile

Meça tamanho antes e depois (docker images).

Remova peso evitável sem quebrar /health.

Preencha seção 5 do dossiê.
```

---

## 6. Segurança e boas práticas

```
@Dockerfile @.dockerignore @dossie_container_integrado.md

Endureça: tag fixa slim, sem segredos em ENV, USER, exec CMD, HEALTHCHECK, .dockerignore.

Preencha seção 6 e marque checklist de entrega.
```

---

## 7. Portão final

```bash
python example.py
docker build -t metrics-exporter:integrador .
docker run --rm -p 8080:8080 metrics-exporter:integrador
curl http://127.0.0.1:8080/health
python verificar_entrega.py
```
