# 🧠 Quizz Final: Orquestração de Agentes e Desenvolvimento de Elite

Este questionário consolida os conceitos de agência, padrões de orquestração e governança para desenvolvedores que utilizam IA no nível profissional.

---

### 1. No padrão oficial de Agent Skills, qual é a função técnica do campo `description` no arquivo de configuração da Skill?
   - A) Serve apenas como comentário para documentação entre desenvolvedores humanos.
   - B) Define as instruções lógicas detalhadas que o agente deve executar internamente.
   - C) Atua como o gatilho para a **Invocação Implícita**, permitindo que o modelo selecione a competência correta via *semantic matching*.
   - D) Define o tempo máximo de execução que a IA tem para completar a tarefa.

### 2. O que caracteriza uma falha de "Chaining" (Encadeamento) em um fluxo de orquestração entre múltiplos agentes?
   - A) Quando a conexão de internet do desenvolvedor oscila durante o deploy.
   - B) Quando o output de uma Skill não é compatível com o formato de input esperado pela próxima etapa, quebrando a continuidade do workflow.
   - C) Quando o desenvolvedor utiliza mais de duas linguagens de programação no mesmo repositório.
   - D) Quando o agente se recusa a escrever código por atingir o limite de mensagens diárias.

### 3. O conceito de **Human-in-the-Loop (HITL)** na orquestração de software define que:
   - A) O desenvolvedor deve escrever 100% do código e a IA apenas formata o estilo visual.
   - B) A IA toma as decisões de arquitetura e o humano apenas executa o deploy final.
   - C) O desenvolvedor atua como o maestro (Tech Lead), definindo diretrizes, revisando planos da IA e validando a segurança.
   - D) O código entra em um loop infinito caso o humano não pressione "Enter" a cada 5 minutos.

### 4. Nas configurações de governança do GitHub Copilot, qual é a ação recomendada para evitar riscos de propriedade intelectual em projetos comerciais?
   - A) Desabilitar o Copilot Chat e utilizar apenas o preenchimento automático.
   - B) Ativar o filtro de "Suggestions matching public code" para o status **Block**.
   - C) Utilizar o agente apenas em arquivos com extensão `.txt`.
   - D) Apagar o arquivo de licença do repositório para a IA não o ler.

### 5. Qual é a vantagem de utilizar uma Skill de "Escopo de Repositório" (`REPO` scope) em vez de prompts genéricos?
   - A) Ela torna a execução do código mais rápida no servidor de produção.
   - B) Ela garante consistência arquitetural, forçando o agente a seguir padrões específicos (ex: Service/Controller) em todos os arquivos do projeto.
   - C) Ela permite que o agente acesse arquivos pessoais do usuário fora da pasta do projeto.
   - D) Ela substitui a necessidade de ter um compilador instalado na máquina.

### 6. Por que o "Progressive Disclosure" é uma estratégia importante em sistemas de agentes complexos?
   - A) Para revelar o código para o cliente final apenas após o pagamento.
   - B) Para economizar janela de contexto, carregando as instruções detalhadas de uma Skill apenas quando o agente decide que ela é necessária.
   - C) Para traduzir o código de forma progressiva enquanto o desenvolvedor digita.
   - D) Para esconder erros de sintaxe do desenvolvedor até o final do projeto.

---

## 🔑 Gabarito e Justificativas Técnicas

### 1. Resposta: C
**Justificativa:** A descrição é a "identidade" da Skill para o orquestrador. É através dela que o modelo entende se aquela ferramenta é adequada para resolver a dúvida do usuário, ativando-a sem que o humano precise chamá-la pelo nome.

### 2. Resposta: B
**Justificativa:** Orquestrar é gerenciar contratos entre tarefas. Se o Agente A entrega um PDF e o Agente B só sabe processar JSON, o encadeamento quebra. Resolver isso exige que o orquestrador (humano ou sistema) ajuste o "parse" dos dados.

### 3. Resposta: C
**Justificativa:** HITL é o pilar da engenharia responsável. O agente foca na execução e velocidade, enquanto o humano garante que o código segue as regras de negócio, padrões de segurança e a visão de longo prazo do produto.

### 4. Resposta: B
**Justificativa:** Bloquear sugestões que coincidem com código público é uma medida de governança essencial para evitar a ingestão acidental de códigos protegidos por licenças restritivas ou "copyleft".

### 5. Resposta: B
**Justificativa:** Skills de repositório servem como o "Style Guide" vivo do projeto. Elas garantem que a IA não "invente" um padrão novo a cada arquivo, mantendo a manutenibilidade do software.

### 6. Resposta: B
**Justificativa:** Modelos de IA têm limites de "memória" (context window). Carregar todas as regras de todas as Skills de uma vez causaria confusão e lentidão. O Progressive Disclosure garante que a IA foque apenas no que é relevante para o momento.