# Aula 12 — Segurança e boas práticas

**Objetivo:** auditar e **endurecer** um Dockerfile funcional — mapear riscos de segurança, aplicar boas práticas e validar runtime (`/health`, `/metrics`) após as correções.

**Enquadramento:** a imagem **sobe e responde**, mas acumula más configurações típicas de produção: segredos em camada, processo root, tag mutável, superfície de rede ampla e contexto de build permissivo. Segurança aqui é **configuração e higiene da imagem**, não só vulnerabilidade de CVE em pacote.

**Ferramentas:** Copilot Chat / agente com `@workspace`, opcionalmente **Hadolint**.

**Material:**

| Arquivo | Papel |
| -------- | ------ |
| `Dockerfile` | Baseline funcional com **falhas de segurança** intencionais. |
| `.dockerignore` | Fraco — endurecer na correção. |
| `requirements.txt` | Dependências da app (stdlib neste baseline). |
| `metrics_exporter.py` | App HTTP mínimo (`/health`, `/metrics`). |
| `matriz_seguranca_boas_praticas.md` | Achados, lacunas, correções, checklist e veredito. |
| `example.py` | Smoke test local antes do `docker build`. |

**Fluxo em sala:**

1. Inventariar achados no baseline → `matriz_seguranca_boas_praticas.md`.
2. Cruzar com Copilot e Hadolint (opcional).
3. Priorizar o que bloqueia deploy.
4. Corrigir `Dockerfile` e `.dockerignore` ao vivo.
5. Validar build e `/health` → checklist e veredito.

---

## 1. Categorias de risco em imagem

```
Antes de abrir arquivos, defina em bullets:

- seis categorias de auditoria (base, segredos, usuário, superfície, runtime, contexto de build);
- diferença entre **CVE em pacote** e **má configuração** no Dockerfile;
- três exemplos de achado **bloqueante** para deploy em produção.

Não analise Dockerfile ainda.
```

---

## 2. Inventário no baseline

```
@Dockerfile @.dockerignore @requirements.txt @metrics_exporter.py

Liste cada falha visível:

- trecho → categoria → severidade → impacto em produção.

Preencha "Registro de achados" em matriz_seguranca_boas_praticas.md.

Não corrija ainda.
```

---

## 3. Cruzar com IA e Hadolint

```
Rode Hadolint (opcional):

docker run --rm -i hadolint/hadolint < Dockerfile

Cole sugestões do Copilot sobre segurança do Dockerfile.

@matriz_seguranca_boas_praticas.md

Para cada achado do inventário:
- foi sinalizado por alguma ferramenta?
- preencha "Quem detectou?" e "Lacunas de detecção".
```

---

## 4. Bloqueante vs aceitável

```
@matriz_seguranca_boas_praticas.md

Quais achados **bloqueiam** deploy e quais seguem com mitigação documentada?

Defina o veredito de segurança: aprovado / aprovar com ressalvas / bloqueante.

Justifique com risco — não com preferência de estilo.
```

---

## 5. Comentário humano de segurança

```
Escolha o achado mais crítico do Dockerfile.

Redija um comentário de review no formato:

trecho → risco em produção → ação pedida ao autor.

Tom profissional; uma ação clara.
```

---

## 6. Aplicar boas práticas

```
@Dockerfile @.dockerignore @matriz_seguranca_boas_praticas.md

Corrija o baseline. Exemplos de direção (adapte ao que inventariou):

- base com tag fixa (ex.: python:3.12.x-slim);
- remover segredos de ENV/ARG — injetar só no deploy;
- USER não-root;
- CMD em exec form;
- EXPOSE apenas porta da app;
- remover sudo e pacotes desnecessários;
- .dockerignore robusto (.env, .git, docs de aula);
- HEALTHCHECK em /health;
- remover DEBUG da imagem de produção.

Documente "Correções aplicadas".

Rode python example.py antes do build.
```

---

## 7. Validar pós-correção

```
docker build -t metrics-exporter:seguro .
docker run --rm -p 8080:8080 metrics-exporter:seguro
curl http://127.0.0.1:8080/health

Preencha "Validação pós-correção" e marque o checklist em matriz_seguranca_boas_praticas.md.
```

---

## 8. Síntese

```
@matriz_seguranca_boas_praticas.md

Em 4 bullets: o que aprendeu sobre **segurança e boas práticas** em imagens?

Inclua: achado mais crítico, lacuna de ferramenta, boa prática mais impactante e critério de bloqueio.
```

---

## Comandos úteis

```bash
cd automacao-e-devops-inteligente/aula-12
python example.py
```

**Build e smoke:**

```bash
docker build -t metrics-exporter:seguro .
docker run --rm -p 8080:8080 metrics-exporter:seguro
curl http://127.0.0.1:8080/health
```

**Hadolint (opcional):**

```bash
docker run --rm -i hadolint/hadolint < Dockerfile
```

---

## Máxima da aula

**Imagem que roda não é imagem segura — boas práticas no Dockerfile e no contexto de build fazem parte do contrato de deploy.**
