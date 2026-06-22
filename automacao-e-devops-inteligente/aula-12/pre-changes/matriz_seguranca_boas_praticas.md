# Matriz de segurança e boas práticas — imagem Docker

Audite o **Dockerfile**, **.dockerignore** e contexto de build. Registre achados e correções.

## Material auditado

- Arquivos: `Dockerfile`, `.dockerignore`, contexto de `COPY`
- Veredito de segurança: **aprovado / aprovar com ressalvas / bloqueante**

---

## Registro de achados

| # | Achado | Categoria (base / segredos / usuário / superfície / runtime / contexto) | Severidade (baixa / média / alta / crítica) | Quem detectou? (humano / Copilot / Hadolint / ninguém) | Bloqueia deploy? |
|---|--------|---------------------------------------------------------------------------|---------------------------------------------|--------------------------------------------------------|------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

---

## Lacunas de detecção

| # | Risco não sinalizado por ferramentas | Por que passou |
|---|--------------------------------------|----------------|
| 1 | | |
| 2 | | |

---

## Correções aplicadas

| # | Antes | Depois | Risco mitigado |
|---|-------|--------|----------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

---

## Checklist de boas práticas

- [ ] Tag da base **fixa** e adequada (sem `latest` em produção)
- [ ] Nenhum segredo em `ENV`, `ARG` ou camada persistida
- [ ] Processo roda como **usuário não-root**
- [ ] `CMD`/`ENTRYPOINT` em **exec form**
- [ ] Apenas portas necessárias em `EXPOSE`
- [ ] Sem pacotes de privilégio desnecessários (`sudo`, shells de debug)
- [ ] `.dockerignore` impede `.env`, `.git` e artefatos sensíveis no contexto
- [ ] `HEALTHCHECK` ou estratégia equivalente documentada
- [ ] Flags de debug desligadas na imagem de produção

---

## Validação pós-correção

| Passo | Resultado (ok / falhou / não rodei) |
|-------|-------------------------------------|
| `python example.py` | |
| Hadolint | |
| `docker build` | |
| `docker run` + `curl /health` | |

---

## Resumo

- Achado mais crítico:
- Boas prática que mais faltava no baseline:
- Algo que só o revisor humano percebeu:
