# Aula 03 — Refatoração segura com IA

**Objetivo:** refatorar código legado com smells **sem mudar o comportamento observável**, usando IA como parceiro em passos pequenos e testes como rede de proteção.

**Ferramenta:** GitHub Copilot Chat / Explorer (ou agente equivalente com `@workspace`).

**Material sugerido:**

| Caminho | Papel |
| -------- | ------ |
| `pre-changes/` | Ambiente de trabalho: código com smells + testes de caracterização que **já passam**. |
| `frete_service.py` (raiz) | Mesmo baseline da pasta `pre-changes/` — referência para comparar antes/depois. |
| `test_frete_characterization.py` | Contrato de comportamento: não altere asserts sem entender o impacto. |

**Como usar:** trabalhe em **`pre-changes/`** durante o exercício. Rode `pytest -q` antes e depois de cada micro-refatoração. Peça à IA **uma mudança por vez**, nunca “refatore tudo”.

---

## 1. Congelar comportamento (antes de tocar no código)

```
@pre-changes/frete_service.py @pre-changes/test_frete_characterization.py

Explique em linguagem simples o que os testes atuais garantem sobre calcular_frete.

Liste 3 invariantes de negócio que NÃO podem mudar durante a refatoração.

Não proponha código ainda.
```

---

## 2. Plano de refatoração em passos pequenos

```
@pre-changes/frete_service.py

Proponha um plano de refatoração em no máximo 5 passos, cada um:
- alteração única e reversível;
- smell que ataca;
- como validar (qual teste rodar).

Ordene do menor risco ao maior. Não implemente ainda.
```

---

## 3. Primeiro passo seguro (extrair função pura)

```
@pre-changes/frete_service.py

Sugira APENAS o primeiro passo do plano: extrair uma função pura para um trecho isolado
(ex.: cálculo de peso cubado ou taxa por região), sem mudar assinatura de calcular_frete.

Mostre o diff conceitual em pseudocódigo ou snippet curto. Lembre: pytest deve continuar verde.
```

---

## 4. IA como revisor, não como demolidora

```
Acabei de aplicar este patch em pre-changes/frete_service.py:
[cole o diff ou descreva a mudança]

Atue como revisor de refatoração segura:
- o comportamento público de calcular_frete mudou?
- surgiram novos efeitos colaterais?
- o passo ficou grande demais para reverter?

@pre-changes/frete_service.py @pre-changes/test_frete_characterization.py
```

---

## 5. Eliminar duplicação sem mudar total

```
@pre-changes/frete_service.py

Há regras de taxa por região repetidas em mais de um ramo.

Proponha unificação mínima (uma tabela ou função auxiliar) mantendo os mesmos totais
para os casos cobertos pelos testes. Implemente só se eu pedir na mensagem seguinte.
```

---

## 6. Checklist pós-refatoração

```
Com base no estado atual de pre-changes/, responda sim/não com justificativa curta:

1) Todos os testes de caracterização passam?
2) calcular_frete mantém mesma assinatura?
3) Estado global foi reduzido ou isolado sem mudar resultado dos testes?
4) Cada commit/passo poderia ser revertido sozinho?
5) Ficou documentado o que mudou na estrutura vs o que mudou no comportamento (deve ser: estrutura sim, comportamento não)?
```

## Comandos úteis

```bash
cd pre-changes
pytest -q
python example.py
```

---

## Máxima da aula

**Refatorar é mudar desenho, não mudar promessa.** Testes verdes + passos pequenos + IA disciplinada = refatoração segura.
