# Aula 03 — Formatação automática

**Objetivo:** usar **`ruff format`** (e IA para revisar o diff) para normalizar layout em `fechamento_entrega.py` — entendendo o que o **formatador** resolve sozinho e o que continua sendo **lint** ou **padrão documentado**.

**Enquadramento:** formatação automática cuida do **mecânico** (espaços, quebras de linha, aspas, espaçamento em hints); não substitui linter nem `padrao_codigo.md`. IA ajuda a **interpretar o diff** e a garantir que o formatador não mascarou mudança semântica indesejada.

**Ferramentas:** Ruff (`format` + `check`), Copilot Chat / agente com `@workspace`.

**Material:**


| Arquivo                      | Papel                                                              |
| ---------------------------- | ------------------------------------------------------------------ |
| `pyproject.toml`             | Configuração Ruff — lint **e** `[tool.ruff.format]`.               |
| `requirements-dev.txt`       | Instalar Ruff localmente.                                          |
| `padrao_codigo.md`           | Padrão do time — revisar diff após formatar.                       |
| `fechamento_entrega.py`      | Baseline **lint limpo**, **format pendente** (proposital).         |
| `registro_formatacao_ia.md`  | Saída `--check`, diff, triagem format vs lint, pós-correção.       |
| `example.py`                 | Smoke test do comportamento.                                       |
| `verificar_formatacao.py`    | Portão: `ruff format --check` limpo em `fechamento_entrega.py`.    |


**Fluxo em sala:**

1. Rodar `ruff format --check` e `ruff check` no baseline → registrar diferença format vs lint.
2. Triar o que o formatador corrige sozinho vs o que exigiria lint/padrão.
3. Aplicar `ruff format` (ou pedir à IA explicar/revisar o diff com `@padrao_codigo.md`).
4. Revisar diff manualmente; rodar `verificar_formatacao.py`, `ruff check` e `example.py`.
5. Completar `registro_formatacao_ia.md`.

---

## 1. Baseline — format vs lint

```
Instale dependências (se necessário):

pip install -r requirements-dev.txt

Rode os dois comandos e compare:

python -m ruff check fechamento_entrega.py
python -m ruff format --check fechamento_entrega.py

Cole as saídas em registro_formatacao_ia.md (seção 1).

Responda: por que o lint pode passar enquanto a formatação falha?
```

---

## 2. Inspecionar diff antes de aplicar

```
@fechamento_entrega.py @pyproject.toml

Mostre o diff que ruff format aplicaria (sem editar ainda):

python -m ruff format --diff fechamento_entrega.py

Liste 5 mudanças mecânicas que o formatador fará (espaços, aspas, quebras).

Confirme se alguma mudança **poderia** alterar comportamento — neste baseline, deve ser só layout.

Preencha seção 2 do registro.
```

---

## 3. Formatar e revisar com IA

```
Cole o diff do ruff format --diff.

@padrao_codigo.md @fechamento_entrega.py

Aplique apenas formatação conforme pyproject.toml (quote-style double, line-length 100).

Revise se o diff mantém contrato ok/avisos, snake_case e logging — sem refatorar lógica.

Registre prompt e observações na seção 3 do registro.

Depois rode:

python -m ruff format fechamento_entrega.py
```

---

## 4. Validar portões

```
Revise o diff manualmente (formatador não substitui review humano).

python -m ruff format --check fechamento_entrega.py
python verificar_formatacao.py
python -m ruff check fechamento_entrega.py
python example.py

Preencha seção 4 e checklist do registro.
```

---

## Comandos úteis

```bash
cd entrega-profissional-e-padronizacao-de-codigo-com-ia/aula-03
pip install -r requirements-dev.txt
python -m ruff check fechamento_entrega.py
python -m ruff format --check fechamento_entrega.py
python -m ruff format --diff fechamento_entrega.py
python -m ruff format fechamento_entrega.py
python verificar_formatacao.py
python example.py
```

---

## Máxima da aula

**Formatador alinha layout — linter e padrão continuam valendo — humano revisa o diff antes de merge.**
