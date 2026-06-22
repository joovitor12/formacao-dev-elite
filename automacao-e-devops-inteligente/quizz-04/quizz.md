# 🧪 Quizz: Dockerfile gerado por IA e multistage builds

**Módulo: Automação e DevOps inteligente**

Este questionário verifica os **temas** de **Dockerfile gerado por IA** (contexto para o modelo, revisão humana, iteração v1→v2, limites da geração automática) e de **multistage builds** (builder vs runtime, `COPY --from=`, superfície de ataque, tamanho da imagem) — alinhado às aulas 09 e 10, sem depender de colar trechos exatos vistos em sala.

---

### 1. Antes de pedir à IA um Dockerfile de produção, o material da aula 09 enfatiza fornecer principalmente:
   - A) Só o `Dockerfile` anterior do repositório — a IA não precisa ler `metrics_exporter.py`.
   - B) Token de registry em `ARG` para a IA autenticar o pull da base durante a geração.
   - C) Apenas o nome da linguagem — o modelo infere portas, health check e usuário da imagem base.
   - D) Código, deps, especificação com restrições (tag fixa, não-root, exec form, COPY seletivo) e o que **não** pedir (segredos em `ENV`, `python:latest`).

### 2. A máxima “IA acelera o rascunho — quem faz deploy valida estrutura, risco e runtime” implica que:
   - A) Aceitar a v1 gerada basta se `docker build` passou na máquina do autor.
   - B) Hadolint substitui revisão humana — warnings zero equivalem a veredito de merge.
   - C) Gerar o arquivo não dispensa inventário de achados, iteração (v2) e smoke test (`docker run`, `/health`).
   - D) A especificação em `.md` é opcional quando o Copilot já conhece imagens Python oficiais.

### 3. Incluir `example.py` e arquivos `.md` de documentação no contexto de build, **sem** `.dockerignore` coerente, conflita com a especificação da aula 09 porque:
   - A) A spec pede **COPY seletivo** — arquivos de smoke test e docs não devem ir para a imagem de produção.
   - B) `example.py` é obrigatório na imagem para o `HEALTHCHECK` funcionar.
   - C) Markdown aumenta o tamanho da base `python:slim` no registry remoto.
   - D) Hadolint proíbe `.dockerignore` em apps que usam só stdlib.

### 4. Iterar da v1 para a v2 com a IA, após revisão humana e Hadolint, deve seguir principalmente:
   - A) Rewrite total do Dockerfile para “modernizar” estilo, mesmo sem achados abertos.
   - B) Corrigir **apenas** os pontos listados no registro — diff focado, sem mudanças desnecessárias.
   - C) Remover `HEALTHCHECK` se o linter apontar complexidade no `CMD`.
   - D) Migrar para `python:latest` para simplificar upgrades de segurança da base.

### 5. Em um Dockerfile **single-stage** que instala `gcc`, `git` e `vim` no mesmo stage da app, o problema central para produção é:
   - A) `EXPOSE` deixa de documentar a porta quando há ferramentas de build.
   - B) Multistage é obrigatório por lei em imagens Python — single-stage nem compila.
   - C) `pip install` só funciona se `vim` estiver presente na mesma camada.
   - D) Ferramentas de compilação e dev permanecem na **imagem final** — aumentam tamanho e superfície de ataque sem uso no runtime.

### 6. No desenho builder + runtime da aula 10, a responsabilidade do stage **builder** inclui:
   - A) Concentrar toolchain (`gcc`, `build-essential`) e `pip install` (ex.: `--prefix=/install`); artefatos copiados depois para o runtime.
   - B) Servir `/health` e `/metrics` como PID 1 em produção.
   - C) Rodar como `USER app` e definir `HEALTHCHECK` — boas práticas ficam no builder.
   - D) Copiar `metrics_exporter.py` antes do `pip install` para cachear o código Python compilado.

### 7. `COPY --from=builder /install /usr/local` no stage runtime está correto quando a intenção é:
   - A) Replicar o filesystem inteiro do builder (incluindo `/usr/bin/gcc`) no runtime.
   - B) Substituir a necessidade de `FROM python:3.12-slim` no runtime.
   - C) Trazer **só** o prefixo com deps instaladas pelo pip — sem toolchain nem lixo de build.
   - D) Evitar `USER` não-root — root herda permissões do builder automaticamente.

### 8. Com `requirements.txt` sem pacotes externos, esquecer `mkdir -p /install` antes de `pip install --prefix=/install` pode fazer o build multistage falhar porque:
   - A) Hadolint DL3008 exige diretório `/install` vazio no runtime.
   - B) O pip pode não criar `/install` se nada for instalado — `COPY --from=builder /install` quebra com “not found”.
   - C) Python 3.12 proíbe `pip install` com prefix em imagens slim.
   - D) `gcc` no builder só instala deps listadas em comentários do `requirements.txt`.

---

## 🔑 Gabarito comentado

### 1. Resposta: D
**Justificativa:** A aula 09 lista contexto (código, deps, `especificacao_app.md`), restrições obrigatórias e anti-padrões explícitos antes de gerar — prompt incompleto produz v1 arriscada.

### 2. Resposta: C
**Justificativa:** Geração automática é rascunho; revisão (risco, estrutura, runtime), iteração e validação (`docker build`/`run`, `/health`) continuam responsabilidade de quem faz deploy.

### 3. Resposta: A
**Justificativa:** A especificação pede COPY seletivo e exclui `example.py` e `.md` da imagem — `.dockerignore` alinhado ao que entra no `COPY`.

### 4. Resposta: B
**Justificativa:** Fluxo v1→v2 corrige achados registrados na revisão, sem rewrite amplo — mesma postura de diff mínimo das aulas anteriores.

### 5. Resposta: D
**Justificativa:** Single-stage inchado deixa toolchain e utilitários de dev na imagem que sobe — tema central do baseline da aula 10 (tamanho, CVEs, lixo de build).

### 6. Resposta: A
**Justificativa:** Builder prepara deps e compilação; runtime executa app enxuta — “builder prepara; runtime executa” (máxima da aula 10).

### 7. Resposta: C
**Justificativa:** `COPY --from=` deve trazer artefatos necessários (prefix pip), não o ambiente completo do builder — copiar tudo anula o ganho do multistage.

### 8. Resposta: B
**Justificativa:** Com requirements vazio, `/install` pode não existir após o pip; `mkdir -p /install` evita falha no `COPY --from=builder` — achado registrado no mapa multistage.
