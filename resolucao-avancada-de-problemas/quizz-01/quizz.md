# 🕵️ Quizz: O Detetive de Código
**Módulo: Resolução Avançada de Problemas**

Este quizz avalia sua capacidade de aplicar a mentalidade de debugging moderno, realizar triagem semântica de logs e analisar a hierarquia de falhas em stack traces complexos.

---

### 1. Na Mentalidade de Debugging Moderno, qual deve ser a sua primeira ação ao encontrar um erro inesperado no VS Code?
   - A) Clicar em "Fix with Copilot" e aceitar a primeira sugestão de código para economizar tempo.
   - B) Apagar o bloco de código suspeito e reescrevê-lo do zero usando apenas o autocomplete.
   - C) Usar o Copilot Chat para interrogar o estado atual do sistema e entender por que o dado está se comportando de forma anômala.
   - D) Desativar o Copilot para garantir que a IA não interfira no seu raciocínio lógico manual.

### 2. Ao lidar com um log de console de navegador extremamente extenso e ruidoso (como o do Checkout SPA), qual técnica de "Triagem Semântica" é a mais eficiente?
   - A) Copiar linha por linha e pesquisar individualmente no Google/Stack Overflow.
   - B) Fornecer o log bruto ao Copilot e solicitar que ele categorize os eventos por severidade e identifique padrões de recorrência.
   - C) Filtrar o log manualmente por palavras-chave como "Error" e ignorar avisos (Warnings) de performance.
   - D) Pedir para a IA limpar o arquivo de log e remover todas as entradas que não contenham a palavra "Critical".

### 3. Analisando um Traceback de Python, o interpretador indica um `KeyError: 'id'` em um mapeador de dados aninhados. Onde o "Dev de Elite" deve focar sua investigação assistida?
   - A) Apenas na última linha do Traceback, pois é ali que o código efetivamente parou de funcionar.
   - B) No topo do Traceback, para identificar o ponto de entrada da aplicação e reiniciar o servidor.
   - C) Na hierarquia completa de chamadas, usando a IA para entender se o erro é uma falha de lógica no mapeador ou uma quebra de contrato na origem do dado (ingestão).
   - D) Na instalação das bibliotecas do `requirements.txt`, pois KeyErrors geralmente são causados por versões de pacotes incompatíveis.

### 4. O comando `/explain` aplicado a um erro no terminal do VS Code serve primordialmente para:
   - A) Traduzir o erro do inglês para o português sem dar contexto técnico.
   - B) Gerar um script de teste que ignore o erro e permita o deploy em produção.
   - C) Analisar o erro de execução cruzando-o com o contexto do seu workspace para fornecer uma explicação da causa raiz e sugestões de correção.
   - D) Enviar um relatório automático para o suporte técnico do GitHub.

---

## 🔑 Gabarito e Justificativas Técnicas

### 1. Resposta: C
**Justificativa:** O Debugging Moderno prioriza a **validação sobre a tentativa**. Aceitar sugestões automáticas sem entender a causa raiz é "codar no escuro". O uso estratégico do Chat permite que você valide hipóteses antes de alterar o código.

### 2. Resposta: B
**Justificativa:** A IA é um filtro de alta performance. Em logs complexos, o cérebro humano sofre de fadiga visual. Delegar a categorização e identificação de padrões à IA permite que o desenvolvedor foque na resolução dos problemas de maior impacto (Severidade).

### 3. Resposta: C
**Justificativa:** Um `KeyError` em dicionários aninhados (`row["metadata"]["id"]`) é frequentemente um sintoma de um problema "corrente acima" (upstream). Analisar a hierarquia com a IA ajuda a decidir se você deve tratar o erro com um `.get()` ou se deve corrigir a validação no serviço de ingestão.

### 4. Resposta: C
**Justificativa:** O `/explain` no terminal é a integração máxima entre execução e assistência. Ele remove a necessidade de "copy-paste" e já carrega o contexto da última execução, tornando o diagnóstico quase instantâneo.