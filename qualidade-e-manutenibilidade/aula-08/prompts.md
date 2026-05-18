# Aula 08 — Checklist de refatoração profissional

**Objetivo:** conduzir uma refatoração com **disciplina de time sênior**: checklist explícito, incrementos pequenos, evidência em testes e uso da IA alinhado ao processo — não como atalho para pular etapas.

**Ferramenta:** GitHub Copilot Chat / Explorer (ou agente equivalente com `@workspace`).

**Material sugerido:**

| Caminho | Papel |
| -------- | ------ |
| `pre-changes/` | Ambiente de trabalho: `catalogo_precos.py` + checklist + testes. |
| `checklist_refatoracao.md` | Checklist para marcar `[x]` a cada etapa. |
| `verificar_checklist.py` | Checa `pytest -q` + itens marcados no checklist. |
| `test_catalogo_characterization.py` | Contrato que o checklist manda preservar. |

**Como usar:** em `pre-changes/`, marque o checklist **em paralelo** à refatoração. Rode `pytest -q` e `python verificar_checklist.py` nos marcos “antes de começar” e “antes de entregar”.

---

## 1. Auditar o checklist contra o código

```
@pre-changes/checklist_refatoracao.md @pre-changes/catalogo_precos.py @pre-changes/test_catalogo_characterization.py

Para cada seção do checklist, cite 1 item que seria fácil pular neste exercício e qual evidência prova que você não pulou.

Não refatore ainda.
```

---

## 2. Pré-voo (antes do primeiro incremento)

```
@pre-changes/catalogo_precos.py @pre-changes/test_catalogo_characterization.py

Com base nos testes, liste 3 comportamentos que o checklist manda preservar.

Proponha o incremento 1 (único): smell alvo, arquivos, como validar (comando).

Formato: checklist item → ação concreta.

Não implemente ainda.
```

---

## 3. Executar incremento 1 com IA (checklist “Durante”)

```
Implemente APENAS o incremento 1 em pre-changes/catalogo_precos.py.

Regras do checklist:
- pytest -q verde;
- diff mínimo;
- sem mudar assinatura de calcular_carrinho.

@pre-changes/catalogo_precos.py @pre-changes/test_catalogo_characterization.py
```

Depois marque manualmente os itens concluídos em `checklist_refatoracao.md`.

---

## 4. Prompt de revisor (checklist “Revisão”)

```
@pre-changes/catalogo_precos.py @pre-changes/test_catalogo_characterization.py

Atue como revisor de PR:

1) Este diff mudou comportamento coberto pelos testes?
2) O passo viola algum item do checklist (escopo, tamanho, drive-by)?
3) Ajuste mínimo sugerido, se houver.

Não proponha o incremento 2 ainda.
```

---

## 5. Registrar entrega (checklist “Antes do PR”)

```
Com base no último diff e em pytest -q, escreva a nota de entrega em 4 linhas:

1) problema / smell;
2) mudança deste incremento;
3) evidência (comandos);
4) risco residual + próximo item do checklist.

Tom: descrição de PR — sem buzzwords.
```

## Comandos úteis

```bash
cd pre-changes
pytest -q
python verificar_checklist.py
python example.py
```

---

## Máxima da aula

**Checklist profissional não é burocracia — é memória externa do que você já sabe que esquece quando a IA acelera demais o teclado.**
