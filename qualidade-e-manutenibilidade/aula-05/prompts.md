# Aula 05 — Refatoração incremental

**Objetivo:** evoluir o código em **incrementos pequenos e verificáveis**, usando IA para sugerir o *próximo* passo — não o redesign completo — e testes como semáforo entre cada incremento.

**Ferramenta:** GitHub Copilot Chat / Explorer (ou agente equivalente com `@workspace`).

**Material sugerido:**

| Caminho | Papel |
| -------- | ------ |
| `pre-changes/` | Ambiente de trabalho: baseline + testes verdes + diário de incrementos (opcional). |
| `estoque_service.py` (raiz) | Referência do estado inicial. |
| `test_estoque_characterization.py` | Contrato que cada incremento deve preservar. |

**Como usar:** em `pre-changes/`, faça **um incremento por vez** → `pytest -q` → registre o que mudou → só então peça o próximo passo à IA.

---

## 1. Definir o próximo incremento (não o projeto inteiro)

```
@pre-changes/estoque_service.py @pre-changes/test_estoque_characterization.py

Com base no estado atual, qual seria o PRÓXIMO incremento de refatoração (apenas um),
com menor risco e maior clareza ganha?

Formato:
- objetivo do incremento (1 frase);
- arquivos tocados;
- o que NÃO entra neste incremento;
- teste que valida que nada quebrou.

Não implemente ainda.
```

---

## 2. Congelar antes de mexer

```
Liste o que os testes atuais garantem sobre registrar_movimento.

Quais 2 comportamentos seriam os primeiros a quebrar se eu refatorar sem cuidado?

@pre-changes/test_estoque_characterization.py
```

---

## 3. Implementar um único incremento com IA

```
Implemente APENAS o incremento descrito abaixo em pre-changes/estoque_service.py:

[cole aqui o incremento escolhido — ex.: extrair validação para validacao_movimento.py]

Regras:
- não alterar assinatura de registrar_movimento;
- pytest deve continuar verde;
- diff mínimo.

@pre-changes/estoque_service.py @pre-changes/test_estoque_characterization.py
```

---

## 4. Revisar o incremento (IA como revisor)

```
Revise o último incremento aplicado em pre-changes/:

- o incremento ficou maior que o necessário?
- misturou duas responsabilidades no mesmo passo?
- há código morto ou duplicado introduzido?

Sugira ajuste mínimo se precisar. Não proponha o incremento seguinte ainda.

@pre-changes/
```

---

## 5. Registrar o incremento (disciplina de time)

```
Com base no diff do último incremento, escreva uma entrada de diário em 4 linhas:

1) o que estava ruim antes;
2) o que mudou neste incremento;
3) evidência (testes/comando);
4) risco residual para o próximo passo.

Tom: nota para PR ou daily técnica — sem jargão vazio.
```

---

## 6. Quando parar e commitar

```
Tenho 3 incrementos feitos e testes verdes. A IA sugere mais 4 refatorações.

Como decidir se paro agora e abro PR, ou continuo na mesma branch?

Responda com critérios objetivos (tamanho do diff, escopo do card, risco acumulado).
```

---

## 7. Prompt curto para gravação

```
@pre-changes/estoque_service.py

Qual o menor próximo incremento de refatoração que ainda vale a pena,
mantendo registrar_movimento e os testes atuais? Só um passo — sem refatorar o arquivo inteiro.
```

---

## Comandos úteis

```bash
cd pre-changes
pytest -q
python example.py
```

---

## Máxima da aula

**Refatoração incremental é ritmo, não tamanho do patch da IA.** Um incremento bom cabe na cabeça, nos testes e no review.
