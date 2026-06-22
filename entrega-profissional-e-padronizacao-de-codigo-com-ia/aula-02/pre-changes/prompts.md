# Aula 02 — Linting assistido por IA

**Objetivo:** usar **Ruff** (e IA) para encontrar, triar e corrigir violações em `confirmacao_entrega.py` — alinhando correções ao **`padrao_codigo.md`** quando lint e padrão convergem.

**Enquadramento:** linter automatiza o que é **objetivo** (imports, naming, bare except, linha longa); IA acelera o patch, mas **quem mergeia** decide o que corrigir, ignorar ou refatorar além do alerta.

**Ferramentas:** Ruff, Copilot Chat / agente com `@workspace`.

**Material:**

| Arquivo | Papel |
| -------- | ------ |
| `pyproject.toml` | Configuração Ruff (`E`, `F`, `I`, `N`, `UP`). |
| `requirements-dev.txt` | Instalar Ruff localmente. |
| `padrao_codigo.md` | Padrão do time — anexar ao pedir correção à IA. |
| `confirmacao_entrega.py` | Baseline com **violações intencionais** de lint. |
| `registro_lint_ia.md` | Saída Ruff, triagem, prompt à IA, pós-correção. |
| `example.py` | Smoke test do comportamento. |
| `verificar_lint.py` | Portão: `ruff check` limpo em `confirmacao_entrega.py`. |

**Fluxo em sala:**

1. Instalar Ruff e rodar baseline → registrar saída.
2. Triar violações (corrigir vs ignorar documentado).
3. Pedir correção à IA com saída do Ruff + `@padrao_codigo.md`.
4. Revisar diff; rodar `ruff check` e `python example.py`.
5. Completar `registro_lint_ia.md`.

---

## 1. Papel do linting com IA

```
Antes de rodar o linter, explique em bullets:

- o que o Ruff verifica vs o que só um humano (ou padrao_codigo.md) avalia;
- risco de aceitar cegamente o patch sugerido pela IA;
- quando usar `ruff check --fix` vs corrigir manualmente.

Não rode ruff ainda.
```

---

## 2. Baseline — rodar Ruff

```
Instale dependências (se necessário):

pip install -r requirements-dev.txt

Rode:

python -m ruff check confirmacao_entrega.py

Cole a saída em registro_lint_ia.md (seção 1).

Classifique cada violação por categoria.
```

---

## 3. Triagem humana

```
@confirmacao_entrega.py @padrao_codigo.md @registro_lint_ia.md

Para cada violação do Ruff:

- deve corrigir agora?
- lint sozinho basta ou exige alinhar ao padrão (ok/avisos, logging)?

Preencha seção 2 do registro.

Não peça patch à IA ainda.
```

---

## 4. Corrigir com IA

```
Cole a saída completa do Ruff.

@padrao_codigo.md @confirmacao_entrega.py

Corrija as violações listadas. Onde lint e padrao_codigo.md convergem:

- snake_case, type hints, contrato ok/avisos, logging em vez de print, sem bare except.

Siga padrao_codigo.md — não invente outro estilo.

Registre prompt e observações na seção 3 do registro.
```

---

## 5. Revisar e validar

```
Revise o diff manualmente.

python -m ruff check confirmacao_entrega.py
python verificar_lint.py
python example.py

Ajuste example.py se o contrato mudou para ok/avisos.

Preencha seção 4 e checklist do registro.
```

---

## 6. Síntese

```
@registro_lint_ia.md

Em 4 bullets: o que aprendeu sobre **linting assistido por IA**?

Inclua: violação mais crítica, limite da IA, uso de --fix e frase padrão para próximos prompts.
```

---

## Comandos úteis

```bash
cd entrega-profissional-e-padronizacao-de-codigo-com-ia/aula-02
pip install -r requirements-dev.txt
python -m ruff check confirmacao_entrega.py
python -m ruff check confirmacao_entrega.py --fix
python verificar_lint.py
python example.py
```

---

## Máxima da aula

**Linter aponta — IA sugere patch — humano tria e valida contra o padrão do time.**
