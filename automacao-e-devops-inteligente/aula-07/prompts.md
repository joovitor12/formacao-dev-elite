# Aula 07 — Revisão de containers e imagens

**Objetivo:** revisar **Dockerfile**, **.dockerignore** e contexto de build — identificar riscos de imagem (base, usuário, segredos, camadas, runtime) e cruzar achados com IA e linters.

**Enquadramento:** a partir desta aula o módulo entra no bloco de **dockerização assistida por IA**. O review deixa de ser só código da app e passa a incluir o **artefato de entrega** (imagem). Build que passa não garante imagem segura ou operável em produção.

**Ferramentas:** Copilot Chat / agente com `@workspace`, opcionalmente **Hadolint**.

**Material:**


| Caminho                        | Quem usa                   | Papel                                                                               |
| ------------------------------ | -------------------------- | ----------------------------------------------------------------------------------- |
| **Raiz** (`aula-07/`)          | **Facilitador**            | Mesmo baseline problemático — **corrige ao vivo** durante a aula.                   |
| `**pre-changes/`**             | **Alunos**                 | **Cópia idêntica** da raiz no início; cada um revisa e corrige no próprio ambiente. |
| `metrics_exporter.py`          | Ambos                      | App mínimo containerizado.                                                          |
| `inventario_revisao_imagem.md` | Alunos (em `pre-changes/`) | Inventário de achados, lacunas e veredito.                                          |
| `example.py`                   | Ambos                      | Smoke test local antes do `docker build`.                                           |


---

## 1. O que revisar em uma imagem

```
Antes de analisar arquivos, defina em bullets:

- diferença entre revisar **código da app** e revisar **Dockerfile/imagem**;
- cinco categorias de achado em container (base/tag, usuário, segredos, camadas/tamanho, runtime).

Não abra Dockerfile ainda.
```

---

## 2. Inventário inicial

```
@Dockerfile @.dockerignore

Liste cada achado visível:

- trecho → categoria → severidade → impacto em produção.

Não proponha rewrite completo ainda.
```

---

## 3. Cruzar com IA e linters

```
Rode Hadolint (opcional):

docker run --rm -i hadolint/hadolint < Dockerfile

@inventario_revisao_imagem.md

Para cada achado: foi sinalizado por alguma ferramenta? Preencha "Quem detectou?".

Registre lacunas.
```

---

## 4. Bloqueante vs aceitável

```
inventario_revisao_imagem.md

Quais achados **bloqueiam** uso em produção e quais seguem com mitigação documentada?

Justifique com risco em runtime — não com preferência de estilo.
```

---

## 6. Comentário humano de review

```
Escolha o achado mais crítico do Dockerfile.

Redija um comentário de review no formato:

trecho → risco na imagem em produção → ação pedida.

Tom profissional; uma ação clara.
```

---

## 7. Corrigir achados

```
@Dockerfile

Corrija os achados críticos um a um (tag fixa, remover segredo de ENV, usuário não-root, exec form, HEALTHCHECK, .dockerignore, etc.).

Rode python example.py e, se possível, docker build na pasta de trabalho.
```

---

## 8. Síntese

```
inventario_revisao_imagem.md

Em 4 bullets: o que aprendeu sobre **revisão de containers e imagens**?

Inclua: achado mais crítico, lacuna de ferramenta, falso alarme evitado e critério de bloqueio.
```

---

## Comandos úteis

**Alunos (`pre-changes/`):**

```bash
cd automacao-e-devops-inteligente/aula-07/pre-changes
python example.py
```

**Build e smoke (opcional):**

```bash
docker build -t metrics-exporter:review .
docker run --rm -p 8080:8080 metrics-exporter:review
curl http://127.0.0.1:8080/health
```

**Hadolint (opcional):**

```bash
docker run --rm -i hadolint/hadolint < Dockerfile
```

---

## Máxima da aula

**Build que passa não prova imagem pronta para produção — quem revisa o Dockerfile nomeia risco de runtime, segredo e operação antes do deploy.**