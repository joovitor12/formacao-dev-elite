# Checklist de refatoração profissional — Operação Fulfillment

Marque `[x]` conforme concluir. Use junto com `python verificar_entrega.py` na entrega final.

## Antes de começar

- [x] Rodei `pytest -q` e está verde
- [x] Li `test_fulfillment_characterization.py` e sei o que não pode mudar
- [x] Fiz diagnóstico de smells/riscos (IA ou notas próprias) **sem patch**
- [x] Defini o incremento 1 com escopo fechado

## Durante cada incremento

- [x] Apliquei **apenas** um incremento por vez
- [x] Rodei `pytest -q` após o passo
- [x] `test_equivalencia_funcional.py` continua verde
- [x] Prompt com `@workspace` + testes quando usei IA

## Separação de responsabilidades (mínimo 2 extrações)

- [x] Extraí validação OU precificação OU estoque para módulo dedicado
- [x] Extraí persistência OU notificação para módulo dedicado
- [x] `processar_fulfillment` permanece fachada fina

## Antes de entregar

- [x] `python relatorio_antes_depois.py` — comportamento OK
- [x] Self-review do diff completo
- [x] Nota de entrega em 4 linhas (problema / mudança / evidência / risco)
- [x] Todos os itens acima marcados `[x]`

## Uso consciente da IA

- [x] Rejeitei “refatore tudo” sem fatiar
- [x] Usei IA como revisor pelo menos uma vez
- [x] Evidência separada de opinião do modelo

## Nota de entrega (4 linhas)

- Problema: fluxo legado concentrava validação e notificação dentro da função principal.
- Mudança: extraí responsabilidades para `validacao.py` e `notificacao.py` mantendo contrato público.
- Evidência: `pytest -q`, equivalência funcional e `relatorio_antes_depois.py` permaneceram verdes.
- Risco: próximas extrações devem continuar incrementais para preservar equivalência com baseline.
