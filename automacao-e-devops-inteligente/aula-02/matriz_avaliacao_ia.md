# Matriz — O que a IA costuma avaliar em PRs

Use para **classificar** cada comentário do Copilot Code Review (aula 02).

| Dimensão | O que a IA costuma pegar | O que costuma escapar |
|----------|--------------------------|------------------------|
| **Segurança** | Segredo em código/log, input óbvio sem validação | Autorização de negócio, abuso de fluxo já “válido” |
| **Correção** | Bug sintático, comparação suspeita, null/empty | Regra de negócio sutil (fronteira 0.05, rollback errado) |
| **Operação** | Log perigoso em prod, passo de pipeline fora de ordem | Impacto em incidente às 3h, runbook ausente |
| **Manutenção** | Função longa, nome ruim, duplicação | Acoplamento com contexto de time |
| **Testes** | Teste ausente em mudança “óbvia” | Teste verde mas assert fraco |
| **Escopo** | Arquivo não relacionado no PR | Feature creep “aceitável” no diff |

## Perguntas desta aula (não da aula 01)

1. Em qual **dimensão** o Copilot comentou cada achado?
2. Qual achado **humano** importante ficou **sem** comentário da IA?
3. O comentário da IA é **correção**, **sugestão de estilo** ou **falso positivo**?

## Diferença em relação à aula 01

| Aula 01 | Aula 02 |
|---------|---------|
| **Papel** do review (quem decide o merge) | **Conteúdo** da avaliação (o que entra no radar da IA) |
| Veredito e responsabilidade humana | Taxonomia e pontos cegos |
| Inventário geral de smells | Classificação dos achados do Copilot |
