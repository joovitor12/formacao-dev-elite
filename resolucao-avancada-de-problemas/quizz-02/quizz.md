# 🧪 Quizz: Ciência do Debugging e Correção Cirúrgica
**Módulo: Resolução Avançada de Problemas**

Este questionário avalia sua capacidade de transitar do "chutômetro" para um método científico de debugging assistido, utilizando o GitHub Copilot como parceiro estratégico.

---

### 1. Qual é a principal diferença entre a abordagem de um desenvolvedor comum e um "Dev de Elite" ao formular hipóteses com o Copilot?
   - A) O desenvolvedor comum pede para a IA consertar o código imediatamente, enquanto o Dev de Elite usa a IA para entender o estado do sistema e gerar causas prováveis.
   - B) O Dev de Elite sempre escreve o código manualmente para garantir que a IA não cometa erros de sintaxe.
   - C) O desenvolvedor comum usa logs de produção, enquanto o Dev de Elite foca apenas no código estático.
   - D) Não há diferença real, pois a IA sugere a mesma solução independente do prompt enviado.

### 2. Como o GitHub Copilot pode ser utilizado para descartar uma hipótese de erro de forma eficiente?
   - A) Pedindo para a IA apagar os arquivos que não estão envolvidos no Stack Trace atual.
   - B) Solicitando que a IA gere scripts de teste rápidos (caracterização) para simular comportamentos específicos e validar se o erro persiste.
   - C) Esperando que a IA monitore o servidor em tempo real e emita um alerta sonoro quando a hipótese for confirmada.
   - D) Aceitando todas as sugestões do Copilot Chat até que o código pare de quebrar.

### 3. No fluxo de "Correções Orientadas por IA", o que define um "Contrato de Aceite"?
   - A) Um documento legal assinado entre o desenvolvedor e a empresa detentora da IA.
   - B) Uma lista de critérios testáveis em linguagem natural que define exatamente como o sistema deve se comportar após a correção.
   - C) O arquivo de configuração que define quais extensões a IDE pode carregar.
   - D) Um prompt curto e genérico como "fix this bug" enviado ao Chat.

### 4. Por que o Dev de Elite deve pedir uma "Revisão de Regressão" ao Copilot após aplicar um patch?
   - A) Para garantir que o código gerado utilize o máximo possível de memória RAM disponível.
   - B) Porque a IA se sente mais valorizada quando o humano pede sua opinião técnica.
   - C) Para identificar se a correção introduziu novos riscos, como loops infinitos ou falhas de tratamento de dados nulos em outras camadas.
   - D) Para que a IA possa publicar o código automaticamente em um repositório público.

### 5. Qual é a vantagem de centralizar a normalização de dados em uma única camada (ex: Ingest Service) ao corrigir um erro de contrato JSON?
   - A) Torna o código mais complexo para evitar que outros desenvolvedores o alterem.
   - B) Evita a duplicação de lógica e mantém o mapeador de domínio limpo e focado estritamente em regras de negócio.
   - C) Permite que o projeto rode sem a necessidade de um ambiente virtual Python.
   - D) Reduz o custo mensal da assinatura do GitHub Copilot.

---

## 🔑 Gabarito Comentado

### 1. Resposta: A
**Justificativa:** O debugging de elite é investigativo. Formular hipóteses antes de tocar no código evita o "efeito colateral" de consertar um sintoma mas deixar a causa raiz intacta. A IA atua como um consultor forense neste estágio.

### 2. Resposta: B
**Justificativa:** No método científico, validamos hipóteses através de experimentos. Pedir que a IA gere um teste de caracterização (que reproduz o erro) permite confirmar se sua suspeita está correta antes de aplicar mudanças definitivas no código de produção.

### 3. Resposta: B
**Justificativa:** Sem critérios de aceite claros (Ex: "Dado X, o sistema deve retornar Y"), a IA pode sugerir refatorações excessivas que fogem do escopo do problema. O contrato mantém o agente (e o desenvolvedor) focado no alvo.

### 4. Resposta: C
**Justificativa:** Toda mudança em sistemas complexos gera risco de regressão. Usar a IA para "atacar" o próprio código recém-gerado ajuda a identificar falhas de segurança ou de lógica que o desenvolvedor pode ter ignorado na pressa da correção.

### 5. Resposta: B
**Justificativa:** Seguir o princípio de responsabilidade única (SRP) facilita a manutenção. Se o serviço de ingestão entrega dados já normalizados, o mapeador não precisa lidar com múltiplos formatos de entrada, reduzindo drasticamente a chance de novos `KeyErrors`.