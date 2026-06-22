# Dossiê integrador — containerização com IA

Preencha ao longo do exercício. Cada seção cobre um bloco do percurso.

## Material

- App: `metrics_exporter.py`
- Veredito final da imagem: **aprovada / aprovar com ressalvas / bloqueante**

---

## 1. Revisão de containers e imagens

- Veredito de revisão: **aprovar / aprovar com ressalvas / pedir mudanças / rejeitar**
- Top 3 achados do baseline (categoria + severidade):

| # | Achado | Categoria | Severidade | Bloqueia produção? |
|---|--------|-----------|------------|-------------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

- Lacuna de ferramenta (achado que IA ou Hadolint não pegou):

---

## 2. Estrutura do Dockerfile

- Ordem atual do baseline (liste instruções principais):
- Ordem ideal aplicada (resumo):
- Três movimentos estruturais que você fez e por quê:

| # | Movimento | Motivo |
|---|-----------|--------|
| 1 | | |
| 2 | | |
| 3 | | |

---

## 3. Dockerfile gerado por IA

- Prompt principal usado (resumo ou cole):
- O que a IA acertou na primeira sugestão:
- O que você corrigiu manualmente ou na iteração v2:
- Trecho do Dockerfile final que veio da IA vs editado por você:

---

## 4. Multistage build

| Stage | Nome (`AS`) | Responsabilidade | O que **não** vai para o runtime |
|-------|-------------|------------------|----------------------------------|
| 1 | | | |
| 2 | | | |

- Instruções `COPY --from=` usadas:

---

## 5. Otimização de imagem

- Tamanho antes (`docker images`):
- Tamanho depois:
- Maior fonte de redução:
- Trade-off aceito (se houver):

---

## 6. Segurança e boas práticas

- Veredito de segurança: **aprovado / aprovar com ressalvas / bloqueante**
- Correção de segurança mais crítica aplicada:
- Checklist (marque ao concluir):

- [ ] Tag fixa em base slim
- [ ] Sem segredos em ENV/ARG
- [ ] USER não-root
- [ ] CMD exec form
- [ ] HEALTHCHECK coerente
- [ ] `.dockerignore` robusto
- [ ] Sem ferramentas de privilégio no runtime

---

## Checklist de entrega

- [ ] `python example.py` verde
- [ ] `docker build` e `curl /health` verdes
- [ ] Seções 1–6 preenchidas
- [ ] `python verificar_entrega.py` retorna **0**
