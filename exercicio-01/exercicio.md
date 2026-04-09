# 🎯 Desafio: Orquestrando o Copilot - Calculadora Financeira

**Objetivo:** Construir um script (Em qualquer linguagem) funcional utilizando exclusivamente técnicas de Programação Assistida por IA (Comentários de Contexto e Prompts Inline).

### 📝 O Cenário
Você precisa criar uma ferramenta de análise rápida para um fundo de investimento. A ferramenta deve receber dados de um aporte e calcular o retorno real.

### 🚀 Requisitos Técnicos
1. **Modelagem de Dados**: Use `dataclasses` para definir um `Investimento` (Ticker, Valor Inicial, Taxa Anual, Meses).
2. **Cálculo de Juros**: Implementar a lógica de juros compostos mensais.
3. **Regra de Imposto (IR)**: Implementar uma função que desconte 15% sobre o **lucro** se o tempo for maior que 12 meses, e 20% se for menor.
4. **Tratamento de Erros**: Garantir que taxas ou valores negativos não quebrem o código.

### 🤖 Regras do Jogo
- Você **não pode** escrever a lógica manual (o interior das funções).
- Você **deve** usar Docstrings detalhadas para guiar o Autocomplete.
- Você **deve** usar Prompts Inline (`Ctrl+I`) para refatoração e validação.