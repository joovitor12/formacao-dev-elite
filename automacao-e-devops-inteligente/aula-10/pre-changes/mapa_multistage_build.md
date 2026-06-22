# Mapa de multistage build

Documente a refatoração do Dockerfile **single-stage** para **builder + runtime**.

## Baseline analisado

- Problema principal do single-stage (tamanho, ferramentas de build, superfície de ataque):
- O que **não** deve ir para a imagem final:

---

## Estágios

| Stage | Nome (`AS`) | Base | Responsabilidade | Artefatos produzidos |
|-------|-------------|------|------------------|----------------------|
| 1 | | | | |
| 2 | | | | |

---

## O que copia entre stages

| Origem (stage / path) | Destino (stage / path) | Por quê |
|-----------------------|------------------------|---------|
| | | |

Instruções `COPY --from=` usadas:

```dockerfile
# Cole trechos relevantes
```

---

## O que ficou de fora do runtime

| Item removido da imagem final | Estava no baseline porque… |
|-------------------------------|----------------------------|
| | |
| | |

---

## Runtime final

- `USER`:
- `HEALTHCHECK`:
- `CMD`:
- Porta / env (`PORT`):

---

## Comparação (opcional)

| Métrica | Single-stage (baseline) | Multistage (final) |
|---------|-------------------------|---------------------|
| Tamanho da imagem (`docker images`) | | |
| Ferramentas de build na final? (sim/não) | | |

---

## Checklist multistage

- [ ] Stage **builder** concentra `pip install` e ferramentas de compilação
- [ ] Stage **runtime** usa base slim sem gcc/git/vim
- [ ] Apenas artefatos necessários copiados com `COPY --from=builder`
- [ ] Código da app copiado no runtime (ou no builder + copiado — justifique)
- [ ] `USER` não-root e `HEALTHCHECK` no stage final
- [ ] `docker build` e `curl /health` verdes no runtime

---

## Resumo

- Maior ganho do multistage neste app:
- Erro comum evitado (ex.: esquecer `COPY --from` das deps):
- Algo que IA sugeriu e você validou ou rejeitou:
