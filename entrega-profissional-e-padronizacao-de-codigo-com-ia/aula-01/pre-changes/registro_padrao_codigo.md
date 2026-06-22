# Registro — padrão de código e IA

Documente auditoria do baseline, implementação assistida e conformidade final.

## Material

- Padrão de referência: `padrao_codigo.md`
- Código: `notificacao_entrega.py`
- Conformidade final: **conforme / parcial / não conforme**

---

## 1. Por que padrão importa (sua síntese)

- Em 3 bullets: o que o padrão evita quando o time cresce ou usa IA diariamente:

---

## 2. Auditoria do baseline vs padrão

| # | Trecho / símbolo | Regra violada (§ do padrao_codigo.md) | Severidade | IA pegaria sozinha? |
|---|------------------|---------------------------------------|------------|---------------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

---

## 3. Implementação com IA (seguindo o padrão)

- Prompt usado (cole ou resuma — deve incluir `@padrao_codigo.md`):
- Funcionalidade pedida (ex.: `registrar_tentativa_falha`, refatorar `NotificarEntrega`):
- O que a IA **seguiu** do padrão:
- O que a IA **desviou** (e você corrigiu):

---

## 4. Conformidade pós-correção

| Regra (resumo) | Conforme? (sim / parcial / não) | Evidência no código |
|----------------|----------------------------------|---------------------|
| Nomenclatura snake_case | | |
| Type hints em funções públicas | | |
| Contrato `ok` + `avisos` | | |
| Logging em vez de print | | |
| Sem bare except | | |
| Constantes para limites | | |

---

## Checklist de entrega

- [ ] `python example.py` verde após ajustes
- [ ] Prompt à IA referenciou `padrao_codigo.md`
- [ ] Seções 1–4 preenchidas
- [ ] Código alinhado ao contrato `{"ok", "avisos"}`

---

## Resumo

- Desvio mais grave no baseline:
- Regra do padrão que mais ajudou a revisar saída da IA:
- Uma prática que você passará a exigir em todo prompt daqui em diante:
