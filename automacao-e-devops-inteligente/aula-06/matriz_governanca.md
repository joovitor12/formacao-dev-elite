# Matriz de governança — PR em `merge_policy.py`

Defina **limites** da automação e **quem** pode autorizar merge.

## PR

- Link:
- Ambiente mais sensível no diff (dev / staging / prod):
- Veredito de governança: **conforme / ressalva / violação / bloqueante**

## Matriz de limites

| # | Ação ou regra no diff | Limite da automação (o que IA/bot **não** pode fazer) | Papel humano exigido | Viola política? (sim / não / parcial) |
|---|----------------------|------------------------------------------------------|----------------------|---------------------------------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |

## Conta-gotas de aprovação (prod)

| Critério | Exigido pela política | O que o código do PR faz |
|----------|----------------------|--------------------------|
| Aprovações humanas mínimas | | |
| CI verde | | |
| Sugestão do Copilot conta como aprovação? | Não | |

## Violações e mitigação

| # | Violação detectada | Severidade | Correção ou mitigação aceitável |
|---|-------------------|------------|--------------------------------|
| 1 | | | |
| 2 | | | |

## Resumo

- Limite de automação mais importante neste PR:
- Quem é **accountable** pelo merge em prod (papel, não ferramenta):
- Algo que a IA sugeriu e a governança **proíbe** aceitar sem humano:
