# Aula 06 — Arquitetura e decisões

**Objetivo:** fechar **ADRs** e **criar o pacote `server/` com IA** — herdando toda a documentação da visão geral.

**Enquadramento:** o baseline **não inclui** `server/`, `pyproject.toml` nem deps prontas. Você preenche ADRs, depois usa **prompt engineering** (§2–§3) para gerar estrutura e módulos; **revisa o diff** antes de aceitar. Raiz e `pre-changes/` começam iguais — o código nasce na aula.

**Ferramentas:** Copilot Chat / agente com `@workspace`.

**Material:**


| Arquivo | Papel |
|---------|--------|
| _(herdados da visão geral)_ | `visao_geral_projeto.md`, `mapa_disciplinas.md`, `arquitetura_mvp.md`, `escopo_mvp.md`, `padrao_projeto_mvp.md`, `.env.example` |
| `decisoes_arquitetura.md` | Template de ADRs — **preencher antes do código**. |
| `registro_arquitetura_decisoes.md` | Entregável: prompts, ADRs, validação. |
| `verificar_arquitetura.py` | Portão **após** criar `server/` (falha no baseline). |
| `example.py` | Smoke do baseline (docs presentes; `server/` ainda ausente). |

**O que você cria em sala (via IA):**

- `server/` (`config`, `main`, `agent`, `guidelines`, `tools/`)
- `pyproject.toml` + `requirements.txt` (ou equivalente)

**Fluxo em sala:**

1. Ler `arquitetura_mvp.md` (estrutura alvo).
2. Preencher ADRs em `decisoes_arquitetura.md` → registro §1.
3. Pedir à IA o pacote `server/` + deps → registro §2 (prompts colados).
4. Revisar diff contra `padrao_projeto_mvp.md` e ADRs.
5. `python verificar_arquitetura.py` → registro §3.

---

## 1. Fechar ADRs (sem código)

```
@arquitetura_mvp.md @escopo_mvp.md @visao_geral_projeto.md @decisoes_arquitetura.md

Para ADR-001 a ADR-007:

- preencha Status, Decisão, Alternativas e Consequências;
- remova todos os placeholders "(preencha)";
- desenhe o diagrama de camadas no final.

Não gere arquivos Python ainda.

Registre dúvidas na seção 1 do registro_arquitetura_decisoes.md.
```

---

## 2. Criar pacote server/ com IA

```
@padrao_projeto_mvp.md @decisoes_arquitetura.md @arquitetura_mvp.md

Crie o pacote server/ do zero conforme ADR-003:

- server/config.py — obter_config(), constantes, OPENROUTER via .env, sem logar API key
- server/main.py — bootstrap async; nesta entrega pode validar config (p.Server na próxima)
- server/agent.py — criar_agente(server, config)
- server/guidelines.py — registrar_guidelines stub com TODO
- server/tools/__init__.py — pacote vazio
- server/__init__.py

Siga ESTRITAMENTE padrao_projeto_mvp.md.

Cole o prompt exato em registro_arquitetura_decisoes.md §2.
```

---

## 3. Criar dependências com IA

```
@decisoes_arquitetura.md

Gere pyproject.toml e requirements.txt para:

- parlant>=3.0.0
- python-dotenv
- ruff em optional dev

Python >=3.11. Não commitar .env.

pip install -r requirements-dev.txt
```

---

## 4. Revisar e validar

```
Revise o diff manualmente contra decisoes_arquitetura.md e padrao_projeto_mvp.md.

python example.py
python verificar_arquitetura.py
python -m server.main

Preencha seções 3–4 do registro.
```

---

## Comandos úteis

```bash
cd entrega-profissional-e-padronizacao-de-codigo-com-ia/aula-06
python example.py
# após criar server/ e preencher ADRs:
pip install -r requirements-dev.txt
python verificar_arquitetura.py
python -m server.main
```

---

## Máxima da aula

**ADR no markdown, código na IA, merge no humano — server/ nasce do prompt, não do zip.**
