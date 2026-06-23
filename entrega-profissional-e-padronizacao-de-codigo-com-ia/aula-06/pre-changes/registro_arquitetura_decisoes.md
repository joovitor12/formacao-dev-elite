# Registro — arquitetura e decisões

Documente ADRs, estrutura `server/` e validação. Herda a documentação da visão geral (`visao_geral_projeto.md`, `mapa_disciplinas.md`, `escopo_mvp.md`, etc.).

## Material

- Decisões: `decisoes_arquitetura.md`
- Estrutura: `server/` + `pyproject.toml`
- Veredito: **arquitetura fechada / pendências / bloqueante**

---

## 1. Revisão das ADRs

Para cada ADR em `decisoes_arquitetura.md`, confirme se **concorda** ou se alteraria algo:

| ADR | Título | Concorda? | Observação |
|-----|--------|-----------|------------|
| 001 | Parlant | | |
| 002 | OpenRouter + owl-alpha | | |
| 003 | Pacote server/ | | |
| 004 | Config por ambiente | | |
| 005 | Sandbox | | |
| 006 | Tools faseada | | |
| 007 | Async entrypoint | | |

**ADR que você reforçaria no review de PR:** _(qual e por quê)_

---

## 2. Estrutura implementada

| Módulo | Responsabilidade | Criado via IA? |
|--------|------------------|----------------|
| `server/config.py` | Env + constantes | |
| `server/main.py` | Bootstrap | |
| `server/agent.py` | create_agent | |
| `server/guidelines.py` | Guidelines (stub) | |
| `server/tools/` | Tools fase 2 | |
| `pyproject.toml` | Deps | |

**Prompt §2 (criar server/):**

```
(cole aqui o prompt exato enviado à IA)
```

**Prompt §3 (deps):**

```
(cole aqui)
```

**O que a IA acertou:**

**O que você ajustou manualmente no diff:**

---

## 3. Validação

```bash
pip install -r requirements-dev.txt
python example.py
python verificar_arquitetura.py
python -m server.main   # requer .env com OPENROUTER_API_KEY
```

| Comando | Resultado |
|---------|-----------|
| `example.py` | |
| `verificar_arquitetura.py` | |
| `python -m server.main` | |

---

## 4. Riscos arquiteturais remanescentes

| Risco | Camada | Mitigação planejada |
|-------|--------|---------------------|
| | | |
| | | |

---

## Checklist

- [ ] ADRs preenchidas (sem "(preencha)")
- [ ] `server/` criado via IA e revisado
- [ ] `pyproject.toml` / requirements criados
- [ ] `.env` local (não commitado)
- [ ] `python verificar_arquitetura.py` retorna **0**
- [ ] Seções 1–4 preenchidas

---

## Resumo

- **Decisão mais crítica desta entrega:**
- **Prompt que mais funcionou para gerar `server/`:**
- **O que fica para a próxima entrega (agente no sandbox):**
