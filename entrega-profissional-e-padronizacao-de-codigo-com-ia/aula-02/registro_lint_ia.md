# Registro — linting assistido por IA

Documente saída do linter, triagem e correções em `confirmacao_entrega.py`.

## Material

- Linter: **Ruff** (`pyproject.toml`)
- Padrão: `padrao_codigo.md`
- Veredito final: **limpo**

---

## 1. Baseline — saída do Ruff

Cole a saída de:

```bash
python -m ruff check confirmacao_entrega.py
```

```
confirmacao_entrega.py:3:8: F401 [*] `os` imported but unused
  |
1 | """confirmacao entrega - baseline com violacoes de lint (proposital)."""
2 |
3 | import os
  |        ^^ F401
4 | import sys
5 | from typing import Any
  |
  = help: Remove unused import: `os`

confirmacao_entrega.py:4:8: F401 [*] `sys` imported but unused
  |
3 | import os
4 | import sys
  |        ^^^ F401
5 | from typing import Any
  |
  = help: Remove unused import: `sys`

confirmacao_entrega.py:5:20: F401 [*] `typing.Any` imported but unused
  |
3 | import os
4 | import sys
5 | from typing import Any
  |                    ^^^ F401
  |
  = help: Remove unused import: `typing.Any`

confirmacao_entrega.py:8:5: N802 Function name `ConfirmarEntrega` should be lowercase
   |
 8 | def ConfirmarEntrega(payload, forcar=False):
   |     ^^^^^^^^^^^^^^^^ N802
 9 |     _marcador_nao_usado = 42
10 |     try:
   |

confirmacao_entrega.py:12:5: E722 Do not use bare `except`
   |
10 |     try:
11 |         confirmado = payload.get("confirmado") or True
12 |     except:
   |     ^^^^^^ E722
13 |         confirmado = False
14 |     token = payload.get("token", "")
   |

Found 5 errors.
[*] 3 fixable with the `--fix` option.
```

| # | Código Ruff | Linha | Mensagem (resumo) | Categoria (estilo / bug / naming / imports) |
|---|-------------|-------|-------------------|---------------------------------------------|
| 1 | F401 | 3 | `os` importado mas não utilizado | imports |
| 2 | F401 | 4 | `sys` importado mas não utilizado | imports |
| 3 | F401 | 5 | `typing.Any` importado mas não utilizado | imports |
| 4 | N802 | 8 | Nome de função `ConfirmarEntrega` deve ser lowercase (snake_case) | naming |
| 5 | E722 | 12 | Uso de `except` bare (sem tipo de exceção) | bug |

- Total de violações no baseline: **5** (3 corrigíveis com `ruff check --fix`)

---

## 2. Triagem (humano)

Estado após `uv run ruff check . --fix`: **6 corrigidas automaticamente** (F401 nos imports); **4 restantes** em `confirmacao_entrega.py` e espelho em `pre-changes/` — triagem abaixo foca o arquivo alvo **`confirmacao_entrega.py`**.

| # | Violação | Ação (corrigir / ruff --fix / ignorar documentado) | Alinhada ao padrao_codigo.md? |
|---|----------|-----------------------------------------------------|-------------------------------|
| 1 | F401 — `os` importado e não usado | **ruff --fix** (já aplicado) | Sim — import morto não agrega valor (§10: diff limpo). |
| 2 | F401 — `sys` importado e não usado | **ruff --fix** (já aplicado) | Sim — idem #1. |
| 3 | F401 — `typing.Any` importado e não usado | **ruff --fix** (já aplicado) | Sim — idem #1; quando precisarmos de hints, usar `Any` só se necessário (§2). |
| 4 | N802 — `ConfirmarEntrega` (PascalCase) | **corrigir** na próxima rodada (IA/manual): renomear para `confirmar_entrega` e ajustar `example.py` | Sim — §1 exige `snake_case` em funções públicas. Lint sozinho não basta: exige rename + atualizar chamadores. |
| 5 | E722 — `except:` bare | **corrigir** na próxima rodada (IA/manual): remover bare except; tratar entrada inválida via validação/`avisos`, não captura genérica | Sim — §8 proíbe `except:`; erros esperados devem ir para `avisos` no retorno (§3), não para `except` silencioso. Lint aponta o sintoma; alinhar ao padrão exige refatorar fluxo de validação. |

**Pendências fora do Ruff (não triadas como “ignorar”, mas incluir no patch com IA):**

| Item | Ruff alerta? | Decisão | Referência no padrão |
|------|--------------|---------|----------------------|
| Retorno `{"success": ...}` em vez de `ok`/`avisos` | Não | **corrigir** junto com IA | §3 |
| `print(...)` no fluxo | Não | **corrigir** → `logging` | §7 |
| Sem type hints em funções públicas | Não | **corrigir** | §2 |
| `_marcador_nao_usado = 42` (número mágico) | Não | **corrigir** ou remover | §6 |
| Linha longa concatenada (linhas 12–14) | Não (dentro do limite após quebra) | **corrigir** estilo se IA reorganizar | §5 |

- Falso positivo ou nit que você **não** corrigiu (justifique): **Nenhum** entre as violações Ruff do baseline — F401, N802 e E722 são legítimas. Itens fora do linter (contrato, logging, hints) não são falso positivo; ficam de propósito fora do escopo do `--fix` e entram na correção assistida alinhada ao `padrao_codigo.md`.

---

## 3. Correção assistida por IA

- **Prompt usado:**

```
@padrao_codigo.md @confirmacao_entrega.py

Corrija as violações listadas. Onde lint e padrao_codigo.md convergem:

- snake_case, type hints, contrato ok/avisos, logging em vez de print, sem bare except.

Siga padrao_codigo.md — não invente outro estilo.

Registre prompt e observações na seção 3 do registro.
```

**Saída Ruff pós `--fix` (pendências antes da IA):**

```
confirmacao_entrega.py:5:5: N802 Function name `ConfirmarEntrega` should be lowercase
confirmacao_entrega.py:9:5: E722 Do not use bare `except`
Found 4 errors (6 fixed, 4 remaining).
```

- **O que a IA corrigiu bem:**
  - N802: `ConfirmarEntrega` → `confirmar_entrega` (+ `example.py` atualizado).
  - E722: removido `except:` bare; validação extraída para `validar_payload()` com retorno `(bool, list[str])` e falhas em `avisos` (§3/§8).
  - Contrato `{"success": ...}` → `{"ok": bool, "avisos": list[str]}` alinhado a `notificacao_entrega.py` e §3.
  - `print` substituído por `logging.getLogger(__name__)` em `_registrar_confirmacao()` — token não logado (§7).
  - Type hints em funções públicas e auxiliares (§2).
  - Removidos número mágico `_marcador_nao_usado = 42` e função genérica `validar(x)` sem uso.
  - Docstrings de módulo e funções públicas (§4).

- **O que a IA errou ou ignorou (e você ajustou manualmente):**
  - Nada pendente nesta rodada — `ruff check`, `verificar_lint.py` e `example.py` passaram sem ajuste manual.
  - **Observação de comportamento:** o baseline usava `payload.get("confirmado") or True`, que tratava `False` como `True`; a correção usa `bool(payload.get("confirmado", True))` para respeitar o valor explícito do payload.

- **Usou `ruff check --fix`?** sim — **antes** desta correção (imports F401); a IA corrigiu N802/E722 e itens do padrão manualmente no patch.

---

## 4. Pós-correção

**Revisão manual do diff** (vs. baseline em `pre-changes/confirmacao_entrega.py`):

| Aspecto | Baseline | Pós-correção | Veredito |
|---------|----------|--------------|----------|
| Nomenclatura | `ConfirmarEntrega` (PascalCase) | `confirmar_entrega` + `validar_payload` | ok |
| Imports | `os`, `sys`, `Any` mortos | só `logging` + `Any` usado | ok |
| Erros | `except:` bare | `validar_payload()` + `avisos` | ok |
| Saída | `print` com token | `logger.info` sem token | ok |
| Contrato | `{"success": bool}` | `{"ok": bool, "avisos": list[str]}` | ok |
| Hints / docstrings | ausentes | presentes em funções públicas | ok |
| `example.py` | `ConfirmarEntrega` + `success` | `confirmar_entrega` + `ok` | ok (já ajustado) |

Nenhum ajuste manual adicional necessário após revisão.

```bash
python -m ruff check confirmacao_entrega.py
python verificar_lint.py
python example.py
```

**Saída:**

```
$ python -m ruff check confirmacao_entrega.py
All checks passed!

$ python verificar_lint.py
=== ruff check ===
...
Lint OK — confirmacao_entrega.py sem violações ruff.

$ python example.py
confirmacao_entrega OK — baseline executável
```

| Passo | Resultado (ok / falhou) |
|-------|-------------------------|
| Ruff limpo | **ok** — `All checks passed!` |
| `verificar_lint.py` | **ok** — exit code **0** |
| `example.py` | **ok** — smoke test verde |
| Contrato `ok`/`avisos` (se aplicou padrão) | **ok** — retorno `{"ok": True, "avisos": []}` no cenário feliz; falha de payload retorna `ok=False` + `avisos` |

---

## Checklist

- [x] Saída Ruff baseline registrada
- [x] Triagem humana antes de aceitar diff da IA
- [x] `python verificar_lint.py` retorna **0**
- [x] `python example.py` verde
- [x] Código alinhado a `padrao_codigo.md` onde aplicável

---

## Resumo

- **Violação mais importante corrigida:** E722 (`except:` bare) — substituída por validação explícita com `validar_payload()` e falhas no contrato `ok`/`avisos` (§3/§8), eliminando captura silenciosa de erros.
- **Limite da IA (o que o linter pegou e ela não):** Ruff não alertava `print`, contrato `success`, ausência de type hints, número mágico nem logging — exigiu `@padrao_codigo.md` no prompt para convergir lint + padrão do time.
- **Regra que passará a exigir no prompt de lint daqui em diante:** *“Siga estritamente `padrao_codigo.md`; corrija violações Ruff **e** alinhe contrato `ok`/`avisos`, logging (sem token/PII) e type hints em funções públicas.”*
