# Inventário de revisão — containers e imagens

Registre achados no **Dockerfile**, **.dockerignore** e contexto de build.

## Material revisado

- Pasta: `pre-changes/`
- Veredito de imagem: **aprovada / aprovar com ressalvas / pedir mudanças / rejeitar**

---

## Registro de achados

| # | Achado | Categoria (base/tag / usuário / camadas / segredos / tamanho / runtime / ignore) | Severidade (baixa / média / alta / crítica) | Quem detectou? (humano / Copilot / Hadolint / ninguém) | Bloqueia uso em prod? |
|---|--------|----------------------------------------------------------------------------------|---------------------------------------------|--------------------------------------------------------|----------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

---

## Lacunas de detecção

| # | Problema de imagem não sinalizado | Por que passou (ferramenta ou contexto) |
|---|-----------------------------------|----------------------------------------|
| 1 | | |
| 2 | | |

---

## Checklist de revisão (marque após analisar)

- [ ] Tag da imagem base é fixa e adequada (evitar `latest` em prod)
- [ ] Processo não roda como root sem justificativa
- [ ] Segredos não estão em `ENV`, `ARG` ou camadas do build
- [ ] `.dockerignore` evita vazar `.env`, `.git` e artefatos desnecessários
- [ ] `CMD`/`ENTRYPOINT` em forma exec quando possível
- [ ] `HEALTHCHECK` ou estratégia equivalente documentada
- [ ] Camadas de `RUN` minimizam lixo (cache apt, etc.)

---

## Priorização

- Top 2 achados que exigem correção antes de usar em produção:
- 1 achado aceitável com mitigação documentada (se houver):

---

## Resumo

- Achado mais crítico na imagem:
- Ferramenta que mais ajudou (Copilot, Hadolint, outro):
- Algo que só o revisor humano percebeu no contexto de deploy:
