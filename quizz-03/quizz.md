# 🧠 Quizz: Dominando AI Coding Agents

Este questionário avalia seu entendimento sobre a transição do Autocomplete para a era dos Agentes de IA e como utilizar o ecossistema do GitHub Copilot de forma estratégica.

---

### 1. Qual é a principal diferença conceitual entre um assistente de Autocomplete (como o Copilot tradicional) e um AI Coding Agent?
   - A) O Autocomplete usa modelos de linguagem e o Agente utiliza apenas algoritmos de busca locais.
   - B) O Autocomplete é reativo (espera você digitar), enquanto o Agente possui "agência" para executar tarefas completas e iterar sobre erros.
   - C) Agentes são mais lentos porque não possuem acesso à internet para consultar documentação.
   - D) Não há diferença real; "Agente" é apenas um termo de marketing para o novo Copilot Chat.

### 2. No fluxo de trabalho de um AI Coding Agent, o que significa o ciclo "Pensamento -> Ação -> Observação"?
   - A) É o processo onde a IA planeja o código, escreve, executa (ou lê o erro) e ajusta a estratégia baseada no resultado.
   - B) É um método de treinamento onde a IA observa o programador humano por meses antes de sugerir código.
   - C) Refere-se apenas à forma como o Copilot sugere nomes de variáveis baseadas no contexto das abas abertas.
   - D) É uma técnica de prompt engineering onde o usuário deve digitar esses três termos para ativar o modo agente.

### 3. Ao utilizar o comando `@workspace` no Copilot Chat, qual é o principal benefício para o desenvolvedor?
   - A) Permissão para que a IA envie seu código para ser treinado publicamente no GitHub.
   - B) Um comando que deleta os arquivos temporários da IDE para liberar memória RAM.
   - C) Fornecer à IA acesso para indexar e compreender as relações entre todos os arquivos e a arquitetura do projeto atual.
   - D) Acesso total às suas credenciais de banco de dados e chaves de API salvas no navegador.

### 4. Por que o modelo Claude 3.5 Sonnet tem se destacado em tarefas de "agência" dentro de ferramentas como o Copilot?
   - A) Porque ele é o único modelo que consegue escrever código em Python sem erros de indentação.
   - B) Porque ele é gratuito e não exige conexão com a internet para funcionar.
   - C) Por sua alta capacidade de raciocínio lógico (reasoning) e menor taxa de alucinações em refatorações complexas.
   - D) Porque ele automaticamente deleta códigos legados que não seguem o padrão Clean Code.

### 5. Como um Desenvolvedor de Elite deve utilizar o comando `/fix` do Copilot após um erro aparecer no terminal?
   - A) Apenas para que a IA peça desculpas formais pelo erro gerado anteriormente.
   - B) Para que a IA oculte os logs de erro e permita que o código continue rodando com bugs silenciosos.
   - C) Fornecendo o erro ao agente para que ele analise o stack trace, localize a falha no projeto e sugira a correção contextualizada.
   - D) Para resetar as configurações da IDE VS Code para o padrão de fábrica.

---

## 🔑 Gabarito e Justificativas

1. **Resposta B**: Enquanto o autocomplete prevê o próximo trecho de código, o agente consegue planejar uma sequência de ações (ler arquivo, editar, testar) para atingir um objetivo.
2. **Resposta A**: Este ciclo (conhecido como loop Agentic) permite que a IA se auto-corrija, lendo mensagens de erro do terminal e tentando novas soluções sem intervenção humana constante.
3. **Resposta C**: O comando `@workspace` expande o contexto da IA para além do arquivo aberto, permitindo que ela entenda como uma mudança no `service.py` afeta o `controller.py`, por exemplo.
4. **Resposta C**: Modelos de "Raciocínio" (Reasoning) como o Sonnet 3.5 são superiores em seguir instruções complexas e manter a consistência lógica em múltiplos arquivos.
5. **Resposta C**: O comando `/fix` é uma ferramenta de diagnóstico que usa o contexto do projeto para entender por que aquele erro específico ocorreu, poupando tempo de debug manual.