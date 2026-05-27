# Checklist de refatoração profissional — Operação Fulfillment

Marque `[x]` conforme concluir. Use junto com `python verificar_entrega.py` na entrega final.

## Antes de começar

- [ ] Rodei `pytest -q` e está verde
- [ ] Li `test_fulfillment_characterization.py` e sei o que não pode mudar
- [ ] Fiz diagnóstico de smells/riscos (IA ou notas próprias) **sem patch**
- [ ] Defini o incremento 1 com escopo fechado

## Durante cada incremento

- [ ] Apliquei **apenas** um incremento por vez
- [ ] Rodei `pytest -q` após o passo
- [ ] `test_equivalencia_funcional.py` continua verde
- [ ] Prompt com `@workspace` + testes quando usei IA

## Separação de responsabilidades (mínimo 2 extrações)

- [ ] Extraí validação OU precificação OU estoque para módulo dedicado
- [ ] Extraí persistência OU notificação para módulo dedicado
- [ ] `processar_fulfillment` permanece fachada fina

## Antes de entregar

- [ ] `python relatorio_antes_depois.py` — comportamento OK
- [ ] Self-review do diff completo
- [ ] Nota de entrega em 4 linhas (problema / mudança / evidência / risco)
- [ ] Todos os itens acima marcados `[x]`

## Uso consciente da IA

- [ ] Rejeitei “refatore tudo” sem fatiar
- [ ] Usei IA como revisor pelo menos uma vez
- [ ] Evidência separada de opinião do modelo
