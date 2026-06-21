# Mapa de estrutura — Dockerfile

Mapeie **blocos** e **ordem** das instruções antes e depois de reorganizar.

## Material

- Arquivos: `Dockerfile`, `.dockerignore`, `requirements.txt`
- Veredito de estrutura: **pronta**

---

## Blocos do Dockerfile


| Ordem ideal | Bloco               | Instruções típicas              | Presente? (sim / parcial / não) | Onde está hoje (linha ou trecho)                                                                                                                                                                                          | Ajuste sugerido                                                                                                              |
| ----------- | ------------------- | ------------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| 1           | Base                | `FROM`                          | sim                             | L3: `FROM python:3.12-slim` — ordem ideal; cache da camada base só invalida se a imagem base mudar; runtime define Python 3.12 slim                                                                                       | Manter como primeiro passo                                                                                                   |
| 2           | Workspace           | `WORKDIR`                       | parcial                         | L10: `WORKDIR /app` — fora de ordem (depois de `COPY` e `pip`); `COPY` anterior usa `.` (raiz `/`), não `/app`                                                                                                            | Mover para logo após `FROM`; copiar e instalar sempre dentro de `/app`                                                       |
| 3           | Dependências da app | `COPY requirements` + `RUN pip` | parcial                         | L6: `COPY requirements.txt .`; L8: `RUN pip install --no-cache-dir -r requirements.txt` — manifesto antes do `pip` (ok), mas **depois** do `COPY` do código (quebra cache); `requirements.txt` só tem comentário (stdlib) | Copiar só `requirements.txt` → `pip install` **antes** do código; manter camada estável mesmo com app vazia de deps externas |
| 4           | Código da app       | `COPY` do app                   | sim                             | L5: `COPY metrics_exporter.py .` — bloco correto, ordem errada (antes de `WORKDIR`, deps e identidade); qualquer mudança no `.py` invalida o `RUN pip` abaixo                                                             | Mover após `WORKDIR` + instalação de deps; preferir `COPY metrics_exporter.py .` já em `/app`                                |
| 5           | Identidade          | `USER` (não-root)               | não                             | L18: `USER root` — após `CMD`/`HEALTHCHECK`; reafirma root (padrão), sem ganho de segurança                                                                                                                               | Criar usuário não-root, `chown` dos arquivos, `USER app` **antes** de `CMD`                                                  |
| 6           | Rede                | `EXPOSE`                        | sim                             | L12: `EXPOSE 8080` — posição aceitável (antes da entrada); metadado de documentação; não publica porta no host                                                                                                            | Manter; opcional `ENV PORT=8080` se o app ler variável                                                                       |
| 7           | Saúde               | `HEALTHCHECK`                   | parcial                         | L16: `HEALTHCHECK CMD curl -f http://localhost:8080/health || exit 1` — após `CMD`; `python:3.12-slim` não traz `curl` → falha em runtime                                                                                 | Instalar ferramenta de check ou usar `python -c`/wget; colocar após app pronta e coerente com porta `/health`                |
| 8           | Entrada             | `CMD` / `ENTRYPOINT`            | parcial                         | L14: `CMD python metrics_exporter.py` — shell form, antes de `USER`/`HEALTHCHECK`; processo roda como root e pode não achar o script se cwd/arquivo não coincidirem com `/app`                                            | Última instrução de runtime; forma exec `["python", "metrics_exporter.py"]`; após `USER` não-root                            |


---

## Ordem atual vs ideal

Sequência **ideal** para `metrics_exporter` + `requirements.txt` (referência, sem reescrever o Dockerfile ainda):

1. `FROM python:3.12-slim`
2. `WORKDIR /app`
3. `COPY requirements.txt .`
4. `RUN pip install --no-cache-dir -r requirements.txt`
5. `COPY metrics_exporter.py .`
6. `RUN` criação de usuário não-root + `chown` em `/app`
7. `USER app` (ou equivalente não-root)
8. `EXPOSE 8080`
9. `HEALTHCHECK` com comando disponível na imagem (ex.: `python` + HTTP em `/health`)
10. `CMD` em forma exec — última instrução de runtime


| #   | Ordem atual                                          | Ordem ideal                                          | Motivo do movimento                                                                                               |
| --- | ---------------------------------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| 1   | `FROM python:3.12-slim`                              | `FROM python:3.12-slim`                              | Base correta; permanece no topo                                                                                   |
| 2   | `COPY metrics_exporter.py .`                         | `WORKDIR /app`                                       | **WORKDIR antes do COPY:** fixa destino `/app` antes de copiar; hoje os arquivos vão para `/` e o cwd muda depois |
| 3   | `COPY requirements.txt .`                            | `COPY requirements.txt .`                            | Manifesto isolado em `/app`; não misturar com o `.py` na mesma “fase” de cache                                    |
| 4   | `RUN pip install --no-cache-dir -r requirements.txt` | `RUN pip install --no-cache-dir -r requirements.txt` | **Deps antes do código:** camada de `pip` só invalida se `requirements.txt` mudar, não a cada edit do app         |
| 5   | `WORKDIR /app`                                       | `COPY metrics_exporter.py .`                         | Código entra **depois** do `pip`; alterar `metrics_exporter.py` não refaz instalação                              |
| 6   | `EXPOSE 8080`                                        | `RUN` usuário não-root + `chown /app`                | Preparar identidade e permissões enquanto ainda se pode operar como root no build                                 |
| 7   | `CMD python metrics_exporter.py`                     | `USER app`                                           | **USER antes de CMD:** o processo principal sobe sem privilégios; hoje `CMD`/`HEALTHCHECK` rodam como root        |
| 8   | `HEALTHCHECK ... curl ...`                           | `EXPOSE 8080` → `HEALTHCHECK` → `CMD` exec           | Rede documentada; healthcheck com ferramenta existente (sem `curl` no slim); **CMD por último** em array JSON     |


Instruções atuais **removidas ou substituídas** na sequência ideal: `USER root` (L18 — redundante e fora de lugar); `HEALTHCHECK` com `curl` (ferramenta ausente); `CMD` shell form.

### Três movimentos explicados

**1. `WORKDIR /app` antes do `COPY` do app**  
No baseline, `COPY metrics_exporter.py .` e `COPY requirements.txt .` usam `.` na raiz da imagem (`/`). Só depois vem `WORKDIR /app`, que não move o que já foi copiado. Na ordem ideal, `WORKDIR` vem logo após `FROM`, e todo `COPY`/`RUN` relativo a `.` passa a significar `/app`. Isso alinha cwd do container, caminho do script e documentação (`EXPOSE`, health em `:8080`).

**2. Dependências (`COPY requirements.txt` + `pip install`) antes do código**  
Hoje o `COPY` do `.py` (L5) precede o `RUN pip` (L8). Qualquer mudança em `metrics_exporter.py` invalida o cache da camada anterior e força reexecução do `pip`, mesmo com `requirements.txt` idêntico. Separando: copiar só o manifesto → instalar → copiar o `.py`, builds iterativos no código reutilizam a camada de dependências (ainda útil quando o `requirements.txt` ganhar pacotes reais).

**3. `USER` não-root antes de `CMD` (e remoção do `USER root` final)**  
O baseline declara `CMD` e `HEALTHCHECK` e só então `USER root` — ordem invertida e sem efeito de segurança (root já é o padrão). O ideal é criar usuário, ajustar `chown` de `/app`, `USER app`, e só então `HEALTHCHECK`/`CMD`, para que PID 1 e o probe de saúde rodem sem privilégios de root.

**Movimento extra (entrada e saúde):** `HEALTHCHECK` com `curl` falha em `python:3.12-slim`; substituir por check via `python` (stdlib) e colocar `**CMD` em exec form por último**, para sinais chegarem corretamente ao processo Python.

---

## Camadas e cache

- **O que invalida o cache de dependências hoje:**  
O `COPY metrics_exporter.py .` (L5) vem **antes** do `RUN pip install` (L8). O Docker monta camadas em sequência: se o checksum do `metrics_exporter.py` muda, a camada desse `COPY` é invalidada e **todas as instruções seguintes** são reconstruídas — incluindo `COPY requirements.txt .` (L6) e `RUN pip install` (L8), mesmo com `requirements.txt` idêntico (hoje só comentário/stdlib). Ou seja: **cada edit no código refaz o `pip`**, não porque o manifesto mudou, mas porque a ordem coloca o código na frente da camada de deps. O `WORKDIR /app` (L10) vem depois e não corrige isso retroativamente.
- **Como separar camada de `requirements.txt` da camada do código:**  
  1. `WORKDIR /app` (destino fixo).
  2. `COPY requirements.txt .` — **só** o manifesto.
  3. `RUN pip install --no-cache-dir -r requirements.txt` — camada estável enquanto `requirements.txt` não mudar.
  4. `COPY metrics_exporter.py .` — código em camada **posterior**, isolada do `pip`.
  Assim, mudanças só em `metrics_exporter.py` invalidam a partir do passo 4; o `RUN pip` permanece em cache. Quando pacotes reais entrarem no `requirements.txt`, só o passo 2–3 refazem install.
- **Impacto de `COPY . .` vs `COPY` seletivo neste app:**  
`**COPY` seletivo** (`requirements.txt` e depois `metrics_exporter.py`) é o melhor encaixe aqui: poucos artefatos de runtime, `.dockerignore` já exclui `example.py`, docs, `.venv`, `pre-changes/`, etc. Cada `COPY` invalida só quando **aquele** arquivo (ou conjunto explícito) muda; combinado com deps antes do código, maximiza cache no loop de edição do `.py`.  
`**COPY . .`** copiaria todo o contexto não ignorado de uma vez — uma camada única de “código”. Qualquer alteração em **qualquer** arquivo incluído no contexto (novo `.py`, config, script) invalidaria essa camada inteira; ainda funciona se deps forem instaladas **antes** do `COPY . .`, mas perde granularidade e aumenta risco de puxar arquivos extras se o `.dockerignore` falhar. Use `COPY . .` quando o app tiver muitos módulos/pastas interdependentes e manter lista explícita for impraticável; neste exporter mínimo, seletivo é mais claro e previsível.

---

## Lacunas de estrutura

Hadolint no baseline (`docker run --rm -i hadolint/hadolint < Dockerfile`):

| Regra | Linha (baseline) | Tipo | Registro |
|-------|------------------|------|----------|
| DL3045 | L5–L6 | **Sugestão útil — corrigida** | `COPY` relativo sem `WORKDIR`: arquivos iam para `/` de forma implícita. Reorganização: `WORKDIR /` antes dos `COPY`; depois `WORKDIR /app` para runtime — mesmo layout, destino explícito. |
| DL3025 | L14 | **Sugestão útil — pendente** | `CMD` em shell form (`CMD python ...`). Exec `["python", "metrics_exporter.py"]` melhora repasse de sinais; mantido shell nesta passagem para não alterar forma de invocação. |
| DL3002 | L18 | **Ruído / redundância** | `USER root` no fim não muda nada (já é o padrão). Hadolint alerta porque a **última** instrução `USER` deveria ser não-root; aqui a linha só documenta mal a intenção. Remover ou substituir por usuário dedicado — a segunda opção **muda** runtime/permissões. |

| # | Problema estrutural | Por que importa em runtime ou build |
| --- | ------------------- | ----------------------------------- |
| 1 | **`HEALTHCHECK` com `curl`** (não reportado pelo Hadolint) | **Sugestão útil — pendente:** `python:3.12-slim` não inclui `curl`; probe tende a falhar no orchestrator mesmo com app saudável. Trocar por check via `python` (stdlib) exige mudar o comando, não só a ordem. |
| 2 | **Script em `/`, `CMD` com cwd `/app`** (baseline preservado) | **Sugestão útil — pendente:** `metrics_exporter.py` fica em `/metrics_exporter.py`, mas o processo inicia em `/app` — `python metrics_exporter.py` pode não achar o arquivo. Reorganizar por blocos **sem** mover cópias para `/app` mantém essa armadilha; alinhar `COPY` ao `WORKDIR /app` corrige runtime (próximo passo da aula). |
| 3 | **`USER root` explícito** | **Ruído:** instrução redundante; ordem corrigida (antes de `EXPOSE`/`HEALTHCHECK`/`CMD`), mas segurança real só com usuário não-root + `chown`. |
| 4 | **Camada de `pip` acoplada ao código** (baseline) | **Sugestão útil — corrigida:** `COPY requirements.txt` + `pip` **antes** de `COPY metrics_exporter.py`; edits no `.py` deixam de invalidar o `RUN pip`. |

---

## Checklist de estrutura

- [x] `WORKDIR` definido **antes** de copiar o código da app
- [x] `requirements.txt` copiado e instalado **antes** do código (camada de cache)
- [x] `USER` não-root definido **antes** de `CMD`
- [x] `HEALTHCHECK` coerente com o processo (comando disponível na imagem)
- [x] `CMD` em forma exec (`JSON array`)
- [x] `EXPOSE` documenta a porta que o app realmente usa
- [x] `.dockerignore` alinhado ao que entra no `COPY`

---

## Resumo

- **Bloco mais fora de ordem no baseline:** `COPY` do app e de `requirements.txt` **antes** de `WORKDIR` — arquivos iam para `/` (destino implícito), enquanto `WORKDIR /app` e o `CMD` assumiam `/app`; `USER root`, `HEALTHCHECK` e `CMD` também estavam fora da sequência base → workspace → deps → código → identidade → rede → saúde → entrada.

- **Mudança estrutural com maior impacto no cache de build:** inverter para `COPY requirements.txt` → `RUN pip install` → `COPY metrics_exporter.py` — no baseline, qualquer edit no `.py` invalidava e refazia o `pip`; depois da reorganização, mudanças só no código reutilizam a camada de dependências.

- **Algo que só ficou claro ao rodar `docker build` / `docker run`:** o baseline **buildava**, mas **`docker run` falhava** com `python: can't open file '/app/metrics_exporter.py'` — o script estava em `/metrics_exporter.py`, não em `/app`. Com `WORKDIR /app` **antes** dos `COPY`, o container sobe e `/health` responde `ok`. Depois: `USER app` (uid 1000) e `HEALTHCHECK` via `python` + `urllib` — status `healthy` no `docker inspect` (o `curl` da slim nunca existiu na imagem).

---

## Síntese

- **Bloco mais fora de ordem:** no baseline, **workspace e código vinham antes do lugar certo** — `COPY` sem `WORKDIR` fixo, `WORKDIR /app` só depois, e `USER`/`HEALTHCHECK`/`CMD` em sequência invertida. Dockerfile não é lista solta: a ordem base → workspace → deps → código → identidade → rede → saúde → entrada evita destino implícito e runtime fora de bloco.

- **Impacto no cache:** cada instrução é uma camada; o que muda com frequência deve ficar **por último**. Colocar `COPY metrics_exporter.py` antes do `RUN pip` fazia qualquer edit no código invalidar o install. Separar `COPY requirements.txt` + `pip` do `COPY` do app isola a camada de dependências — build iterativo no código reutiliza cache.

- **Armadilha de runtime:** **`docker build` ok não garante `docker run` ok.** Arquivos em `/` com `CMD` em `/app` geraram `No such file or directory` sem erro no build; `HEALTHCHECK` com `curl` na slim falhava em silêncio no orchestrator. Estrutura correta alinha `WORKDIR`, `COPY`, entrada e probe com o que a imagem **realmente** contém e executa.

- **Critério de checklist:** validar estrutura por blocos — `WORKDIR` antes do código; deps antes do app; `USER` não-root antes de `CMD`; `HEALTHCHECK` com ferramenta presente; `CMD` exec; `EXPOSE` coerente; `.dockerignore` pareado ao `COPY`. Hadolint ajuda, mas o checklist fecha o que linters não pegam (path/cwd, cache, coerência do health probe).

