# 🧪 Quizz: Revisão de imagens e estrutura de Dockerfile

**Módulo: Automação e DevOps inteligente**

Este questionário verifica os **temas** de **revisão de containers e imagens** (Dockerfile, `.dockerignore`, categorias de achado, lacunas de linter) e de **estrutura de um Dockerfile** (blocos, ordem das instruções, cache de camadas, runtime) — sem depender do código visto em sala.

---

### 1. Ao revisar um PR que altera só o `Dockerfile`, a postura mais alinhada ao material é:
   - A) Focar apenas no código Python — a imagem é gerada automaticamente pelo registry após o merge.
   - B) Tratar a imagem como artefato de entrega: base, usuário, segredos em camadas, contexto de `COPY` e runtime.
   - C) Aprovar se `docker build` passou localmente — build bem-sucedido equivale a imagem pronta para produção.
   - D) Delegar totalmente a Hadolint — linters substituem o inventário humano de achados.

### 2. A máxima “build que passa não prova imagem pronta para produção” apoia-se principalmente no fato de que:
   - A) `docker build` só valida sintaxe de Python, não de instruções Docker.
   - B) Imagens slim não suportam `HEALTHCHECK` — o build sempre omite essa instrução.
   - C) CI verde no repositório impede que segredos entrem em camadas via `ENV` ou `ARG`.
   - D) A imagem pode buildar com tag mutável, root ou credencial em layer — riscos persistem mesmo com build OK.

### 3. `FROM python:latest` em um Dockerfile de produção costuma ser classificado no inventário como achado de:
   - A) Runtime — forma shell no `CMD` impede sinais ao PID 1.
   - B) Segredos — `latest` expõe token da base no log de build.
   - C) Base/tag — tag flutuante compromete reprodutibilidade e previsibilidade do deploy.
   - D) Ignore — `.dockerignore` não exclui tags do registry remoto.

### 4. “Lacuna de detecção” ao cruzar Hadolint, Copilot e revisão humana na imagem significa:
   - A) Achado relevante que ferramentas não sinalizaram (ou sinalizaram mal) e o revisor registra no inventário.
   - B) Comentário duplicado entre dois linters no mesmo trecho do `Dockerfile`.
   - C) Timeout ao puxar a imagem base do registry durante o `docker build`.
   - D) Ausência de testes unitários no repositório, independentemente do diff do Dockerfile.

### 5. Copiar e instalar `requirements.txt` **antes** de copiar o código da app (`metrics_exporter.py`) beneficia principalmente:
   - A) Obrigar multi-stage build em todo Dockerfile Python.
   - B) Cache de camadas — mudanças só no código não invalidam a layer de `pip install`.
   - C) Eliminar a necessidade de `.dockerignore` no contexto de build.
   - D) Garantir que `EXPOSE` seja avaliado antes de qualquer `RUN`.

### 6. `CMD python metrics_exporter.py` (forma shell) em vez de `CMD ["python", "metrics_exporter.py"]` (exec) é achado de runtime porque:
   - A) A forma shell dificulta entrega correta de sinais (ex.: SIGTERM) ao processo principal como PID 1.
   - B) A forma exec impede definir `USER` não-root na mesma imagem.
   - C) Hadolint só permite shell form quando a base é `python:slim`.
   - D) Shell form é obrigatória para `HEALTHCHECK` com `curl` funcionar.

### 7. `HEALTHCHECK` que invoca `curl` quando `curl` não foi instalado na imagem ilustra falha de:
   - A) Cache — invalida a layer de dependências a cada commit no repositório.
   - B) Tag da base — só imagens `latest` permitem health check HTTP.
   - C) `.dockerignore` — curl é excluído do contexto de build por padrão.
   - D) Estrutura/runtime — o check referencia comando ausente na imagem final.

### 8. Definir `USER` não-root **antes** de `CMD` está alinhado ao mapa de estrutura porque:
   - A) `EXPOSE` só funciona se `USER` vier depois de `HEALTHCHECK`.
   - B) Hadolint exige root explícito no `CMD` para imagens Python oficiais.
   - C) O processo principal herda a identidade já definida — evita rodar a entrada da imagem como root.
   - D) `WORKDIR` deve ser a última instrução do Dockerfile em todo fluxo de build.

---

## 🔑 Gabarito comentado

### 1. Resposta: B
**Justificativa:** A revisão de imagem cobre artefato de entrega (base, identidade, segredos, camadas, runtime) — não substitui, mas complementa a leitura do código da app.

### 2. Resposta: D
**Justificativa:** Build bem-sucedido não elimina riscos de tag mutável, root, segredo em camada ou health check incoerente — eixo central do inventário de revisão.

### 3. Resposta: C
**Justificativa:** Tag flutuante (`latest`) entra na categoria **base/tag** — reprodutibilidade imprevisível em produção.

### 4. Resposta: A
**Justificativa:** Lacuna é o achado que passou pelas ferramentas (ex.: segredo em `ENV` não classificado como credencial) e precisa ser nomeado pelo revisor.

### 5. Resposta: B
**Justificativa:** Separar deps do código permite reutilizar cache da layer de `pip` quando só o `.py` muda — tema explícito de camadas e cache.

### 6. Resposta: A
**Justificativa:** Exec form é preferida para PID 1 e sinais; shell form é achado de **runtime** comum em inventários e Hadolint (DL3025).

### 7. Resposta: D
**Justificativa:** Health check deve usar comando presente na imagem (ex.: `python -c` + urllib) — `curl` ausente quebra coerência estrutural e runtime.

### 8. Resposta: C
**Justificativa:** Bloco de identidade (`USER`) precede entrada (`CMD`) para o processo principal não subir como root — ordem do mapa de estrutura.
