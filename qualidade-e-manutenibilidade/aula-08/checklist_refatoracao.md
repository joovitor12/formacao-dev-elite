# Checklist de refatoração profissional

Marque `[x]` conforme concluir cada item. Rode `python verificar_checklist.py` para checagens automáticas.

## Antes de começar

- [ ] Rodei `pytest -q` e está verde
- [ ] Li os testes de caracterização e sei o que não pode mudar
- [ ] Defini **um** incremento (smell + escopo) — não o redesign inteiro
- [ ] Anotei o risco principal se este passo der errado

## Durante cada incremento

- [ ] Apliquei **apenas** o incremento planejado
- [ ] Rodei `pytest -q` depois do passo
- [ ] Diff sem mudanças fora do escopo (sem “aproveitei e arrumei outra coisa”)
- [ ] Se usei IA: prompt com `@workspace` + arquivo de testes anexado

## Revisão do incremento (com ou sem IA)

- [ ] Revisei se o comportamento observável permaneceu o mesmo
- [ ] O passo ainda é reversível (tamanho razoável para reverter)
- [ ] Rejeitei patch grande da IA que misturou várias mudanças

## Antes de abrir PR / entregar

- [ ] Suite de testes verde na pasta de trabalho
- [ ] Revisei meu próprio diff (self-review)
- [ ] Descrevi em 3–4 linhas: problema, mudança, evidência, risco residual
- [ ] Rodei `python verificar_checklist.py` e tratei pendências críticas

## Uso consciente da IA

- [ ] Não aceitei “refatore tudo” sem fatiar
- [ ] Usei a IA como revisor (“este patch mudou comportamento?”) pelo menos uma vez
- [ ] Separei opinião da IA de evidência (testes / relatório / diff)
