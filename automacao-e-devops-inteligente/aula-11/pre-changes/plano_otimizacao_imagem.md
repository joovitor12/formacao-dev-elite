# Plano de otimização de imagem

Registre **antes/depois** da otimização do Dockerfile inchado (funcional, porém pesado).

## Baseline (antes)

```bash
docker build -t metrics-exporter:antes .
docker images metrics-exporter:antes --format "{{.Repository}}:{{.Tag}} {{.Size}}"
```

- Tamanho registrado:
- Principais fontes de gordura identificadas:

| # | Fonte de tamanho / superfície | Categoria (base / apt / pip / COPY / camadas / runtime) | Ação de otimização |
|---|------------------------------|-----------------------------------------------------------|-------------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

---

## Otimizações aplicadas

| # | Mudança no Dockerfile / .dockerignore | Ganho esperado (tamanho / segurança / cache) |
|---|----------------------------------------|---------------------------------------------|
| 1 | | |
| 2 | | |
| 3 | | |

---

## Depois

```bash
docker build -t metrics-exporter:depois .
docker images metrics-exporter:depois --format "{{.Repository}}:{{.Tag}} {{.Size}}"
```

- Tamanho registrado:
- Redução aproximada (absoluta ou %):

---

## O que removemos vs o que mantivemos

**Removido da imagem final:**

- 

**Mantido (necessário ao runtime):**

- 

---

## Camadas e contexto

- Ajustes em `.dockerignore`:
- `COPY` seletivo vs `COPY . .`:
- `pip install --no-cache-dir` / combinação de `RUN`:

---

## Runtime e segurança (sem regredir)

- [ ] App responde em `/health` após otimização
- [ ] `USER` não-root
- [ ] `HEALTHCHECK` coerente (se adicionado na otimização)
- [ ] Ferramentas de build **ausentes** na imagem final
- [ ] Base enxuta (`slim` ou equivalente com tag fixa)

---

## Resumo

- Otimização com maior impacto neste app:
- Trade-off aceito (se houver):
- Algo que IA sugeriu e você validou ou rejeitou:
