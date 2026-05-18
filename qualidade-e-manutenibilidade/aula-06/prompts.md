# Aula 06 — Garantindo equivalência funcional

**Objetivo:** provar que uma refatoração **não alterou o comportamento observável**, comparando a implementação em evolução com um **baseline congelado** e uma **matriz de casos** — usando IA para ampliar cobertura, não para “achar que está igual”.

**Ferramenta:** GitHub Copilot Chat / Explorer (ou agente equivalente com `@workspace`).

**Material sugerido:**

| Caminho | Papel |
| -------- | ------ |
| `pre-changes/` | Ambiente de trabalho: refatore `comissao_service.py` mantendo testes verdes. |
| `comissao_baseline.py` | Referência congelada — **não editar** durante o exercício. |
| `comissao_service.py` | Implementação que você pode limpar/refatorar. |
| `casos_equivalencia.py` | Matriz de entradas para comparação service × baseline. |
| `test_equivalencia_funcional.py` | Prova automática de equivalência em todos os casos. |

**Como usar:** em `pre-changes/`, rode `pytest -q` antes de refatorar. Após cada mudança em `comissao_service.py`, os testes de equivalência devem continuar passando.

---

## 1. Definir o que “equivalente” significa aqui

```
@pre-changes/comissao_baseline.py @pre-changes/comissao_service.py @pre-changes/test_equivalencia_funcional.py

O que exatamente este exercício considera “equivalência funcional”?

Liste:
- campos da saída que entram na comparação;
- o que fica de fora (efeitos colaterais, performance, legibilidade);
- 2 formas de “passar no teste” mas ainda introduzir bug sutil.

Não escreva código.
```

---

## 2. Ampliar a matriz de casos com IA

```
@pre-changes/casos_equivalencia.py @pre-changes/comissao_baseline.py

Analise as regras de calcular_comissao e proponha 5 casos NOVOS para casos_equivalencia.py,
cobrindo bordas ainda não presentes (ex.: limite de valor > 10000, combinações de meta, erros).

Formato por caso: id, entrada (dict), resultado esperado em uma frase.

Não implemente ainda — só a lista revisável.
```

---

## 3. Adicionar casos e validar equivalência

```
Implemente em pre-changes/casos_equivalencia.py apenas os 3 casos de maior risco da lista anterior.

Regras:
- não alterar comissao_baseline.py;
- rodar pytest -q em test_equivalencia_funcional.py;
- ids dos casos descritivos.

@pre-changes/casos_equivalencia.py @pre-changes/test_equivalencia_funcional.py
```

---

## 4. Refatorar com rede de equivalência

```
Refatore APENAS pre-changes/comissao_service.py em um passo (ex.: extrair tabela de percentuais por nível).

Regras:
- comissao_baseline.py intocado;
- test_equivalencia_funcional.py e test_comissao_characterization.py verdes;
- diff mínimo neste passo.

@pre-changes/comissao_service.py @pre-changes/test_equivalencia_funcional.py
```

---

## 5. Revisar equivalência (IA como auditor)

```
Revise o último diff em pre-changes/comissao_service.py:

- a refatoração poderia divergir do baseline em algum caso não coberto por CASOS?
- há arredondamento, ordem de operações ou tipo (float) que o teste atual não pegaria?
- sugira 1 caso extra se houver lacuna clara.

Não refatore de novo — só análise e sugestão de caso.

@pre-changes/ @pre-changes/casos_equivalencia.py
```

## Comandos úteis

```bash
cd pre-changes
pytest -q
pytest -q test_equivalencia_funcional.py
python example.py
```

---

## Máxima da aula

**Equivalência funcional é evidência comparável, não opinião.** Baseline congelado + matriz de casos + teste automático valem mais que “a IA disse que ficou igual”.
