# Mapa de estrutura — Dockerfile

Mapeie **blocos** e **ordem** das instruções antes e depois de reorganizar.

## Material

- Pasta: `pre-changes/`
- Veredito de estrutura: **incompleta / reorganizada / pronta**

---

## Blocos do Dockerfile

| Ordem ideal | Bloco | Instruções típicas | Presente? (sim / parcial / não) | Onde está hoje (linha ou trecho) | Ajuste sugerido |
|-------------|-------|--------------------|---------------------------------|----------------------------------|-----------------|
| 1 | Base | `FROM` | | | |
| 2 | Workspace | `WORKDIR` | | | |
| 3 | Dependências da app | `COPY requirements` + `RUN pip` | | | |
| 4 | Código da app | `COPY` do app | | | |
| 5 | Identidade | `USER` (não-root) | | | |
| 6 | Rede | `EXPOSE` | | | |
| 7 | Saúde | `HEALTHCHECK` | | | |
| 8 | Entrada | `CMD` / `ENTRYPOINT` | | | |

---

## Ordem atual vs ideal

Liste a sequência **atual** das instruções (uma por linha) e, ao lado, a ordem **ideal** que você aplicaria:

| # | Ordem atual | Ordem ideal | Motivo do movimento |
|---|-------------|-------------|---------------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |

---

## Camadas e cache

- O que invalida o cache de dependências hoje:
- Como separar camada de `requirements.txt` da camada do código:
- Impacto de `COPY . .` vs `COPY` seletivo neste app:

---

## Lacunas de estrutura

| # | Problema estrutural | Por que importa em runtime ou build |
|---|---------------------|-------------------------------------|
| 1 | | |
| 2 | | |

---

## Checklist de estrutura

- [ ] `WORKDIR` definido **antes** de copiar o código da app
- [ ] `requirements.txt` copiado e instalado **antes** do código (camada de cache)
- [ ] `USER` não-root definido **antes** de `CMD`
- [ ] `HEALTHCHECK` coerente com o processo (comando disponível na imagem)
- [ ] `CMD` em forma exec (`JSON array`)
- [ ] `EXPOSE` documenta a porta que o app realmente usa
- [ ] `.dockerignore` alinhado ao que entra no `COPY`

---

## Resumo

- Bloco mais fora de ordem no baseline:
- Mudança estrutural com maior impacto no cache de build:
- Algo que só ficou claro ao rodar `docker build` / `docker run`:
