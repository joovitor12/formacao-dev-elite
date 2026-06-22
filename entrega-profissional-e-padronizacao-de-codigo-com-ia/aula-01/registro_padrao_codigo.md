# Registro — padrão de código e IA

Documente auditoria do baseline, implementação assistida e conformidade final.

## Material

- Padrão de referência: `padrao_codigo.md`
- Código: `notificacao_entrega.py`
- Conformidade final: **conforme**

---

## 1. Por que padrão importa (sua síntese)

- Em 3 bullets: o que o padrão evita quando o time cresce ou usa IA diariamente:

- **Estilo divergente por prompt** — sem contrato fixo (`ok`/`avisos`, `snake_case`), cada geração da IA traz nomenclatura e retornos diferentes, aumentando review e conflitos em merge.
- **Vazamento de risco em “código que funciona”** — `print` com token, bare `except` e logs sem padrão passam em smoke test, mas falham em auditoria e produção.
- **Retrabalho em escala** — validação, logging e erros implícitos obrigam o revisor humano a reescrever o que deveria estar no prompt desde o início.

## 2. Auditoria do baseline vs padrão

| # | Trecho / símbolo | Regra violada (§ do padrao_codigo.md) | Severidade | IA pegaria sozinha? |
|---|------------------|---------------------------------------|------------|---------------------|
| 1 | `def NotificarEntrega(...)` | §1 Nomenclatura — funções em `snake_case`; proibido `camelCase`/`PascalCase` | Alta | sim |
| 2 | `return {"success": ..., "msg": ...}` (L10, L23) | §3 Contrato de retorno — deve ser `{"ok": bool, "avisos": list[str], ...}` | Alta | parcial |
| 3 | `amb == "" or canal is None` → `{"success": True, "msg": "ignorado"}` | §3 Contrato — falha/ignorado esperado preenche `avisos`, sem exceção; chaves erradas | Alta | parcial |
| 4 | `def NotificarEntrega(payload, forcar=False)` e `def validar(p)` sem anotações | §2 Tipagem — type hints em parâmetros e retorno de funções públicas | Média | sim |
| 5 | `print(...)` L14 e L19 | §7 Logging — proibido `print` em caminho de entrega; usar `logging.getLogger(__name__)` | Alta | sim |
| 6 | `token={payload.get('token')}` dentro do `print` L14 | §7 Logging — proibido logar segredos, tokens ou PII completa | Crítica | parcial |
| 7 | `except:` + `pass` L20–21 | §8 Tratamento de erros — proibido bare `except:` sem re-raise ou registro explícito | Alta | sim |
| 8 | `qtd`, `amb` | §1 Nomenclatura — evitar abreviações obscuras (`quantidade`, `ambiente`) | Baixa | parcial |
| 9 | `def validar(p)` | §1 Nomenclatura — proibido nome de uma letra (`p`); §5 — validação dedicada deve ser `validar_*` | Média | parcial |
| 10 | `if qtd > 3` | §6 Constantes — limite de tentativas deve ser constante nomeada (`LIMITE_TENTATIVAS`) | Média | sim |
| 11 | `NotificarEntrega` e `validar` sem docstring de uma linha | §4 Docstrings — funções públicas descrevem efeito e entradas/saída | Baixa | sim |

---

## 3. Implementação com IA (seguindo o padrão)

- Prompt usado (cole ou resuma — deve incluir `@padrao_codigo.md`):

  ```
  @padrao_codigo.md @notificacao_entrega.py

  Refatore notificacao_entrega.py para conformidade com padrao_codigo.md:

  - renomear NotificarEntrega → notificar_entrega;
  - contrato {"ok", "avisos"} em vez de success/msg;
  - type hints, logging, constantes, validar_payload dedicada;
  - remover print, bare except e token em log.

  Siga ESTRITAMENTE padrao_codigo.md — não invente outro estilo.

  Registre prompt e desvios da IA na seção 3 do registro.
  ```

- Funcionalidade pedida (ex.: `registrar_tentativa_falha`, refatorar `NotificarEntrega`):

  Refatoração completa do baseline: renomear orquestrador, adotar contrato `ok`/`avisos`, extrair `validar_payload`, substituir `print` por `logging`, extrair `LIMITE_TENTATIVAS`, remover bare `except` e vazamento de token; atualizar `example.py` para o novo contrato.

- O que a IA **seguiu** do padrão:

  - §1: `notificar_entrega`, `validar_payload`, variáveis `ambiente`/`quantidade`/`canal` em `snake_case`.
  - §2: type hints em funções públicas; retorno `dict[str, Any]`.
  - §3: retornos `{"ok": bool, "avisos": list[str]}`; validação inválida preenche `avisos` sem exceção.
  - §4: docstring no módulo e uma linha em cada função pública.
  - §5–§6: validação dedicada; `LIMITE_TENTATIVAS = 3` no topo.
  - §7: `logger = logging.getLogger(__name__)`; sem `print`; alerta sem token.
  - §8: bare `except` removido (bloco era desnecessário após remoção do `print`).
  - §9: efeitos isolados em `_registrar_envio` e `_registrar_alerta_tentativas`.

- O que a IA **desviou** (e você corrigiu):

  - Tendência inicial a manter `ok=True` no payload ignorado (espelhando baseline `success: True`) — **corrigido** para `ok=False` + `avisos`, conforme §3 (falha esperada não usa exceção, mas `ok` só quando concluiu conforme regra).
  - Tendência a incluir `token` mascarado no log de alerta — **removido** por §7 (não logar segredos).
  - `example.py` ainda referenciava `NotificarEntrega` e `success` — **atualizado** para `notificar_entrega` e `ok`/`avisos`.

---

## 4. Conformidade pós-correção

### Checklist linha a linha (`notificacao_entrega.py` × `padrao_codigo.md`)

| § | Regra | Linhas | Status | Observação |
|---|-------|--------|--------|------------|
| 1 | `snake_case` em funções/variáveis | L13, L49, L59–61 | sim | `notificar_entrega`, `validar_payload`, `ambiente`, `quantidade`, `canal` |
| 1 | Constantes `UPPER_SNAKE_CASE` | L10 | sim | `LIMITE_TENTATIVAS` |
| 1 | Sem abreviações obscuras | L31 log | sim | Corrigido manualmente: `amb=` → `ambiente=` |
| 2 | Type hints em funções públicas | L13–14, L49–52 | sim | Parâmetros e retorno anotados |
| 2 | Retorno negócio `dict[str, Any]` | L52, L56, L72 | sim | Contrato padronizado |
| 2 | Evitar `Any` no domínio | L13, L50 | parcial | `dict[str, Any]` aceitável aqui; `TypedDict` seria melhoria futura |
| 3 | Contrato `{"ok", "avisos"}` | L56, L72 | sim | Chaves corretas em todos os retornos |
| 3 | Falha esperada → `avisos`, sem exceção | L16–30, L55–56 | sim | Validação retorna avisos acionáveis |
| 3 | `ok=True` só quando concluiu | L72 | sim | Envio registrado antes do retorno |
| 4 | Docstring no módulo | L1 | sim | Responsabilidade descrita |
| 4 | Docstring uma linha (públicas) | L14, L53 | sim | `validar_payload`, `notificar_entrega` |
| 5 | Uma função = uma responsabilidade | L13–32, L49–72 | sim | Validação, efeitos e orquestração separados |
| 5 | Função pública ≤ 25 linhas | L49–72 (~24) | sim | Dentro do limite |
| 5 | `validar_*` dedicada | L13 | sim | Três regras de validação extraídas |
| 6 | Constantes para limites | L10, L64 | sim | Sem literal `3` solto |
| 7 | `logging.getLogger(__name__)` | L8 | sim | Logger de módulo |
| 7 | Sem `print` no fluxo | — | sim | Nenhum `print` no arquivo |
| 7 | Sem segredos/tokens em log | L37–41 | sim | Alerta sem token |
| 8 | Sem bare `except` | — | sim | Nenhum `except` no módulo |
| 8 | Erro esperado → `avisos` | L26–30 | sim | Corrigido manualmente: `tentativas` inválida validada em `validar_payload` |
| 9 | Validação pura sem I/O | L13–32 | sim | `validar_payload` sem log/envio |
| 9 | Efeitos isolados | L35–46, L70 | sim | `_registrar_*` chamados pela orquestração |

### Ajustes manuais pós-IA (esta revisão)

| Desvio residual da IA | Correção aplicada |
|-----------------------|-------------------|
| `enviar = forcar or True` sempre verdadeiro (L59 baseline IA) | Removido; `_registrar_envio` chamado diretamente (L70) |
| `amb=` abreviado no log de alerta | Renomeado para `ambiente=` (L38) |
| `int(tentativas)` podia lançar `ValueError` (§8) | Validação de `tentativas` em `validar_payload` (L26–30) |
| `payload` tipado só como `dict` | Ampliado para `dict[str, Any] \| None` (L50) + `assert` pós-validação (L58) |

### Tabela resumo (§4)

| Regra (resumo) | Conforme? (sim / parcial / não) | Evidência no código |
|----------------|----------------------------------|---------------------|
| Nomenclatura snake_case | sim | L10, L13, L49, L59–61 |
| Type hints em funções públicas | sim | L13–14, L49–52 |
| Contrato `ok` + `avisos` | sim | L56, L72 |
| Logging em vez de print | sim | L8, L37–46; zero `print` |
| Sem bare except | sim | Nenhum `except`; tentativas inválida → avisos L26–30 |
| Constantes para limites | sim | L10 `LIMITE_TENTATIVAS`; uso L64 |

---

## Checklist de entrega

- [x] `python example.py` verde após ajustes
- [x] Prompt à IA referenciou `padrao_codigo.md`
- [x] Seções 1–4 preenchidas
- [x] Código alinhado ao contrato `{"ok", "avisos"}`

---

## 5. Validação de execução

| Campo | Valor |
|-------|-------|
| Comando | `python example.py` |
| Diretório | `entrega-profissional-e-padronizacao-de-codigo-com-ia/aula-01` |
| Data | 2026-06-22 |
| Exit code | **0** (sucesso) |
| Saída | `notificacao_entrega OK — contrato ok/avisos` |

**Cenários exercitados em `example.py`:**

1. Payload válido (`staging` / `email` / `tentativas: 1`) → `ok=True`.
2. Payload inválido (`ambiente: ""`, `canal: None`) → `ok=False` e `avisos` não vazio.

**Alteração no teste:** `example.py` já atualizado na refatoração — usa `notificar_entrega` e assertivas sobre `ok`/`avisos` (substituiu `NotificarEntrega` e `success` do baseline).

---

## Resumo

- Desvio mais grave no baseline: log de `token` via `print` (§7 — severidade crítica).
- Regra do padrão que mais ajudou a revisar saída da IA: §3 contrato `ok`/`avisos` — expôs retorno legado `success`/`msg` e semântica errada de `ok=True` em payload ignorado.
- Uma prática que você passará a exigir em todo prompt daqui em diante: anexar `@padrao_codigo.md` e declarar *“Siga estritamente padrao_codigo.md; não invente outro estilo de retorno ou nomenclatura.”*
