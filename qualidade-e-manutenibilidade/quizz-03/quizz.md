# 🧪 Quizz: Refatoração em ritmo e equivalência funcional com IA
**Módulo: Qualidade e manutenibilidade**

Este questionário foca em **como usar Copilot (ou agente equivalente) com método** ao refatorar em passos pequenos e ao **provar** que o comportamento não mudou — sem depender de “a IA disse que ficou igual”.

---

### 1. Você vai refatorar um módulo que já tem testes verdes. Qual pedido à IA está mais alinhado a **refatoração incremental**?
   - A) “Redesenhe a arquitetura inteira e unifique tudo em um único serviço.”
   - B) “Aplique todas as melhorias possíveis de uma vez.”
   - C) “Com base no estado atual, qual é o **próximo** incremento (só um), com menor risco, arquivos tocados e o que **não** entra neste passo? Não implemente ainda.”
   - D) “Remova os testes para o diff ficar menor.”

### 2. Depois de cada incremento aplicado com ajuda da IA, qual hábito de engenharia é o mais importante?
   - A) Confiar na mensagem “refatoração concluída” do chat.
   - B) Fazer merge sem rodar testes se o diff parecer pequeno.
   - C) Pedir à IA o próximo passo antes de validar o anterior.
   - D) Rodar a suíte de testes (ex.: `pytest -q`) e só então pedir o próximo passo ou registrar o que mudou.

### 3. A IA devolve um patch que extrai validação **e** reorganiza persistência no mesmo passo. O que fazer?
   - A) Pedir revisão como revisor: o passo misturou duas mudanças? Sugerir dividir e manter diff mínimo.
   - B) Aceitar: dois problemas resolvidos de uma vez.
   - C) Ignorar testes que falharem só neste arquivo.
   - D) Apagar o baseline de referência para não “confundir” a IA.

### 4. Você tem um **baseline congelado** e uma implementação em evolução. O que significa **equivalência funcional** neste contexto?
   - A) O código novo ter menos linhas que o antigo.
   - B) A IA afirmar em texto que “o comportamento é o mesmo”.
   - C) Para as mesmas entradas da matriz de casos, a saída da implementação em evolução ser **idêntica** à do baseline (no contrato testado).
   - D) Os nomes das funções permanecerem iguais.

### 5. Qual combinação é a melhor **evidência** de equivalência antes de abrir PR?
   - A) Screenshot do chat com a IA.
   - B) Apenas revisão visual do diff.
   - C) Só rodar o linter.
   - D) Baseline intocado + matriz de casos + teste automatizado que compara saídas (ex.: parametrizado em pytest).

### 6. Os testes de equivalência passam, mas a matriz cobre só happy path. Qual prompt à IA ajuda mais a reduzir risco?
   - A) “Analise as regras do baseline e proponha casos de **borda e erro** ainda ausentes na matriz — com id e entrada, sem implementar ainda.”
   - B) “Está bom, pode mergear.”
   - C) “Remova casos de erro para simplificar o CI.”
   - D) “Reescreva o baseline para ficar mais legível.”

### 7. A IA sugere remover uma regra de negócio porque “parece redundante”. Como responder com método?
   - A) Aceitar: a IA leu todo o repositório.
   - B) Remover a regra e os testes que falharem.
   - C) Pedir qual **caso da matriz** quebraria se a regra sumisse; só remover se a evidência (teste/caso) mostrar que é seguro.
   - D) Alterar o baseline para bater com a sugestão da IA.

### 8. Após três incrementos verdes, a IA lista mais quatro refatorações “óbvias”. Como decidir parar e abrir PR?
   - A) Usar critérios objetivos: escopo do card, tamanho do diff acumulado, risco residual e se o ganho do próximo passo justifica mais uma rodada de review.
   - B) Continuar até a IA não sugerir mais nada.
   - C) Parar só quando não houver mais smells no universo.
   - D) Nunca parar na mesma branch.

### 9. Qual frase resume a postura correta sobre **ritmo** e **prova** ao refatorar com IA?
   - A) “Quanto maior o patch da IA, mais incremental é o trabalho.”
   - B) “Baseline e matriz de casos atrapalham a IA — melhor refatorar sem referência.”
   - C) “Se os testes de estilo passam, o comportamento está garantido.”
   - D) “Um incremento bom cabe na cabeça, nos testes e no review; equivalência é evidência comparável, não opinião do modelo.”

### 10. Você quer registrar o que fez para o time (daily ou PR). Qual pedido à IA é o mais útil?
   - A) “Com base no último diff: o que estava ruim, o que mudou neste incremento, evidência (comando/teste) e risco residual — em 4 linhas objetivas.”
   - B) “Escreva um poema sobre clean code.”
   - C) “Gere 50 bullet points genéricos de melhoria contínua.”
   - D) “Não documente nada para economizar tempo.”

---

## 🔑 Gabarito comentado

### 1. Resposta: C
**Justificativa:** Refatoração incremental começa definindo **um** próximo passo com limites claros — a IA não deve puxar o redesign inteiro.

### 2. Resposta: D
**Justificativa:** O ritmo é **incremento → evidência (testes) → próximo passo**; sem verificação objetiva, “incremental” vira só rótulo.

### 3. Resposta: A
**Justificativa:** Um incremento = uma intenção reversível; misturar extrações no mesmo patch anula a vantagem do método e dificulta o review.

### 4. Resposta: C
**Justificativa:** Equivalência funcional aqui é **comparável e repetível** nas entradas acordadas — não estética nem opinião do chat.

### 5. Resposta: D
**Justificativa:** Baseline congelado + matriz + teste de paridade transformam “ficou igual” em **prova** que qualquer revisor pode rerodar.

### 6. Resposta: A
**Justificativa:** A IA ajuda a **ampliar cobertura de casos** antes de confiar no verde atual; lacunas em borda/erro são onde equivalência falsa mora.

### 7. Resposta: C
**Justificativa:** Regra de negócio só sai com **caso/teste** que mostre o impacto; baseline existe justamente para não “negociar” comportamento no chat.

### 8. Resposta: A
**Justificativa:** Parar é decisão de engenharia (escopo, diff, risco), não esgotar a lista de sugestões da IA.

### 9. Resposta: D
**Justificativa:** Resume as duas máximas do trecho: ritmo de incremento verificável + equivalência por evidência, não por afirmação do modelo.

### 10. Resposta: A
**Justificativa:** Diário curto e factual comunica **o que mudou e como provou** — alinhado a PR e daily técnica, sem jargão vazio.
