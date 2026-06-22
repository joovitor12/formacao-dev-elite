# Registro — linting assistido por IA

Documente saída do linter, triagem e correções em `confirmacao_entrega.py`.

## Material

- Linter: **Ruff** (`pyproject.toml`)
- Padrão: `padrao_codigo.md`
- Veredito final: **limpo / pendências aceitas documentadas**

---

## 1. Baseline — saída do Ruff

Cole a saída de:

```bash
python -m ruff check confirmacao_entrega.py
```

| # | Código Ruff | Linha | Mensagem (resumo) | Categoria (estilo / bug / naming / imports) |
|---|-------------|-------|-------------------|---------------------------------------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

- Total de violações no baseline:

---

## 2. Triagem (humano)

| # | Violação | Ação (corrigir / ruff --fix / ignorar documentado) | Alinhada ao padrao_codigo.md? |
|---|----------|-----------------------------------------------------|-------------------------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

- Falso positivo ou nit que você **não** corrigiu (justifique):

---

## 3. Correção assistida por IA

- Prompt usado (deve incluir saída do Ruff + `@padrao_codigo.md` + `@confirmacao_entrega.py`):
- O que a IA corrigiu bem:
- O que a IA errou ou ignorou (e você ajustou manualmente):
- Usou `ruff check --fix`? (sim / não — quando):

---

## 4. Pós-correção

```bash
python -m ruff check confirmacao_entrega.py
python example.py
```

| Passo | Resultado (ok / falhou) |
|-------|-------------------------|
| Ruff limpo | |
| example.py | |
| Contrato `ok`/`avisos` (se aplicou padrão) | |

---

## Checklist

- [ ] Saída Ruff baseline registrada
- [ ] Triagem humana antes de aceitar diff da IA
- [ ] `python verificar_lint.py` retorna **0**
- [ ] `python example.py` verde
- [ ] Código alinhado a `padrao_codigo.md` onde aplicável

---

## Resumo

- Violação mais importante corrigida:
- Limite da IA (o que o linter pegou e ela não):
- Regra que passará a exigir no prompt de lint daqui em diante:
