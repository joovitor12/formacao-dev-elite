# Mapa de multistage build

Documente a refatoração do Dockerfile **single-stage** para **builder + runtime**.

## Baseline analisado

- Problema principal do single-stage (tamanho, ferramentas de build, superfície de ataque):
  - Build e runtime no mesmo stage: tudo instalado via `apt-get` e `pip` permanece na imagem que sobe em produção.
  - Ferramentas de compilação e desenvolvimento (`gcc`, `build-essential`, `git`, `vim`, `curl`) aumentam tamanho e superfície de ataque sem benefício para servir `/health` e `/metrics`.
  - A app usa só stdlib (`http.server`); `requirements.txt` está vazio (comentário), mas a camada `pip install` e as ferramentas de build foram incluídas “para simular” um app com deps — lixo de build fica no runtime mesmo sem pacotes pip reais.
  - Processo roda como **root** (padrão da imagem base); não há `HEALTHCHECK` para o orquestrador validar o container.
  - `EXPOSE 8080` documenta a porta, mas não substitui health check nem usuário não-root.
- O que **não** deve ir para a imagem final:
  - `gcc`, `build-essential` e headers/libs de compilação (só necessários no builder se deps tiverem extensões nativas).
  - `git` (clone de repos / metadados VCS — irrelevante em runtime).
  - `vim` (editor interativo — irrelevante em runtime).
  - `curl` (debug manual; health check deve usar stdlib Python, como na aula-09).
  - Camada inteira `apt-get update && apt-get install` (fica restrita ao stage builder).
  - `requirements.txt` no runtime (opcional manter; deps já instaladas via `COPY --from=builder`).
  - Artefatos intermediários de build: caches de apt/pip, objetos `.o`, binários de toolchain.

### Acúmulo do stage único (detalhe)

**Ferramentas de build desnecessárias no runtime**


| Pacote                    | Por que está no baseline                     | Por que não precisa no runtime                   |
| ------------------------- | -------------------------------------------- | ------------------------------------------------ |
| `gcc` / `build-essential` | Compilar wheels/extensões C no `pip install` | App e deps atuais não compilam nada em execução  |
| `git`                     | Simular ambiente “de dev” inchado            | `metrics_exporter.py` não clona repos            |
| `vim`                     | Simular ambiente “de dev” inchado            | Servidor HTTP não edita arquivos                 |
| `curl`                    | Debug / smoke manual                         | App expõe `/health`; check via Python (`urllib`) |


**Camadas que poderiam ficar só no builder**


| Camada (Dockerfile)                              | Conteúdo                                         | Destino ideal                                                             |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------------------------------- |
| `RUN apt-get … gcc build-essential git curl vim` | Toolchain + utilitários de dev                   | Stage **builder** apenas                                                  |
| `COPY requirements.txt` + `RUN pip install`      | Instalação de deps (hoje vazia, mas padrão real) | Stage **builder**; runtime recebe site-packages via `COPY --from=builder` |
| —                                                | `metrics_exporter.py`                            | Stage **runtime** (código da app, não depende de compilação)              |


**O que falta no runtime (baseline vs. boas práticas — cf. aula-09)**


| Item                   | Situação no baseline | Esperado no runtime final                                  |
| ---------------------- | -------------------- | ---------------------------------------------------------- |
| `USER` não-root        | Ausente (root)       | `adduser`/`addgroup` + `USER app`                          |
| `HEALTHCHECK`          | Ausente              | Probe em `/health` com `python -c` + `urllib` lendo `PORT` |
| `COPY --chown=app:app` | Ausente              | Dono dos arquivos alinhado ao usuário não-root             |
| `CMD` exec form        | OK                   | Manter `["python", "metrics_exporter.py"]`                 |
| `ENV PORT` / `EXPOSE`  | OK                   | Manter; app lê `PORT` (default 8080)                       |


---

## Estágios


| Stage | Nome (`AS`) | Base                                                          | Responsabilidade                                                                                                                                                     | Artefatos produzidos                                                                                            |
| ----- | ----------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| 1     | `builder`   | `python:3.12-slim`                                            | Instalar toolchain de compilação (`gcc`, `build-essential`); copiar `requirements.txt`; rodar `pip install --prefix=/install` (deps + wheels compilados, se houver). | Árvore `/install/` com `lib/python3.12/site-packages/` e `bin/` (scripts de entrypoint das deps, se existirem). |
| 2     | `runtime`   | `python:3.12-slim` (imagem limpa, **sem** `apt-get` de build) | Criar usuário não-root; importar deps do builder; copiar app; configurar `ENV`/`EXPOSE`; `HEALTHCHECK` e `CMD`.                                                      | Imagem final enxuta: Python slim + deps em `/usr/local` + `metrics_exporter.py` em `/app`, processo como `app`. |


**Decisões de desenho**

- `**pip install --prefix=/install`** no builder — isola deps num path copiável; evita misturar com site-packages da base e facilita `COPY --from=builder /install /usr/local` no runtime.
- **Toolchain só no builder** — `gcc`/`build-essential` (e `git`, se alguma dep vier de VCS) ficam no stage 1; o runtime não reinstala apt de build.
- **App copiada no runtime** — `metrics_exporter.py` usa só stdlib, não compila no build; `COPY` direto do contexto de build (não precisa passar pelo builder). Menos camadas e ownership claro com `--chown=app:app`.
- **Baseline inchado no builder** — `git`, `vim`, `curl` do single-stage **não** entram nem no builder (só o mínimo para compilar deps: `gcc` + `build-essential`); reduz lixo mesmo no stage descartado.

---

## O que copia entre stages


| Origem (stage / path)                     | Destino (stage / path)                 | Por quê                                                                                          |
| ----------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `builder` → `/install/`                   | `runtime` → `/usr/local/`              | Único artefato de build necessário: pacotes pip (site-packages + bins) sem toolchain nem caches. |
| Contexto de build → `metrics_exporter.py` | `runtime` → `/app/metrics_exporter.py` | Código da app; não depende de compilação — copiado no runtime com `--chown=app:app`.             |


**O que *não* copia do builder para o runtime**

- `/usr/bin/gcc`, `build-essential`, headers em `/usr/include`
- `git`, `vim`, `curl` (presentes no baseline inchado, omitidos no desenho enxuto)
- `requirements.txt` (opcional no runtime — deps já materializadas em `/usr/local`)
- Caches de apt/pip, `/root/.cache`, objetos `.o`

Instruções `COPY --from=` usadas:

```dockerfile
COPY --from=builder /install /usr/local
```

(App copiada do contexto de build, não do builder:)

```dockerfile
COPY --chown=app:app metrics_exporter.py .
```

---

## O que ficou de fora do runtime

| Item removido da imagem final | Estava no baseline porque… |
| ----------------------------- | -------------------------- |
| `gcc`, `build-essential` | Compilar wheels no `pip install` — ficam só no stage `builder`. |
| `git`, `vim`, `curl` | Simular ambiente de dev inchado — omitidos no multistage enxuto. |
| `requirements.txt` no runtime | Só necessário no builder para `pip install`; deps já em `/usr/local`. |
| Caches apt/pip, toolchain, headers | Subproduto do build — não copiados com `COPY --from=builder /install`. |

---

## Runtime final

- `USER`: `app` (criado com `addgroup --system app && adduser --system --group app`)
- `HEALTHCHECK`: `python -c` + `urllib.request` em `http://127.0.0.1:${PORT}/health`, espera corpo `ok`
- `CMD`: `["python", "metrics_exporter.py"]`
- Porta / env (`PORT`): `ENV PORT=8080`, `EXPOSE 8080`; app lê `PORT` e `HOST` via `os.environ`

---

## Comparação (opcional)


| Métrica                                  | Single-stage (baseline) | Multistage (final) |
| ---------------------------------------- | ----------------------- | ------------------ |
| Tamanho da imagem (`docker images`)      | **758 MB**              | **177 MB**         |
| Ferramentas de build na final? (sim/não) | **sim** (gcc, build-essential, git, curl, vim) | **não** |

**Delta:** ~581 MB a menos no multistage (~77% menor). Baseline rebuild temporário: `docker build -f pre-changes/Dockerfile -t metrics-exporter:single-stage .`

**Revisão — builder vazou para o runtime?**

| Verificação | Resultado |
| ----------- | --------- |
| `gcc`, `g++`, `make` em `/usr/bin` | Ausentes |
| `git`, `vim`, `curl` | Ausentes |
| Pacotes apt (`dpkg-query`) gcc/build-essential/git/vim/curl | Nenhum instalado no runtime |
| Conteúdo copiado de `/install` | Diretório vazio (~4 KB) — `requirements.txt` sem pacotes; nada além do `mkdir -p` |
| `/usr/local/include`, headers Python | Da imagem base `python:3.12-slim`, **não** do builder |

**Conclusão:** nenhum vazamento de toolchain ou utilitários de dev. `COPY --from=builder /install /usr/local` trouxe só o prefix pip (vazio neste app); runtime permanece base slim + app.

**Hadolint:** sem warnings após pin `gcc=4:14.2.0-1` e `build-essential=12.12` no builder (DL3008).

---

## Resumo

- Maior ganho do multistage neste app: **~581 MB** a menos (758 → 177 MB) e **zero** ferramentas de build/dev no runtime; ganho extra de **USER** não-root e **HEALTHCHECK** vs. baseline inchado.
- Erro comum evitado (ex.: esquecer `COPY --from` das deps): sem `COPY --from=builder`, deps não chegam ao runtime; com `requirements.txt` vazio, **`mkdir -p /install`** antes do `pip install` evita falha `" /install": not found` no COPY.
- Algo que IA sugeriu e você validou ou rejeitou: **Validado** — multistage enxuto (só `gcc`/`build-essential` no builder, não replicar git/vim/curl); app no runtime via contexto; health check com `urllib`; pin apt (Hadolint DL3008). **Rejeitado** — copiar filesystem inteiro do builder em vez de `/install` apenas.

---

## Checklist multistage

- [x] Stage **builder** concentra `pip install` e ferramentas de compilação
- [x] Stage **runtime** usa base slim sem gcc/git/vim
- [x] Apenas artefatos necessários copiados com `COPY --from=builder`
- [x] Código da app copiado no runtime (stdlib — não passa pelo builder)
- [x] `USER` não-root e `HEALTHCHECK` no stage final
- [x] `docker build` e `curl /health` verdes no runtime
