# Quizz: Indexacao e Contexto Local utilizando IDEs AI Native (Cursor)

## Instrucoes
Escolha a alternativa correta em cada questao.

---

## 1) Em uma IDE AI Native como o Cursor, qual e o papel principal da indexacao do projeto?

A) Substituir totalmente o controle de versao (Git)  
B) Permitir que a IA encontre e compreenda partes relevantes do codigo com mais rapidez  
C) Compilar o codigo automaticamente sem precisar de build  
D) Criptografar todos os arquivos do repositorio

## 2) O que melhor descreve "contexto local" para um assistente de IA dentro da IDE?

A) Somente o codigo aberto na aba atual  
B) Todo o conteudo da internet acessivel ao modelo  
C) O conjunto de informacoes do projeto (arquivos, trechos, simbolos e historico relevante) usado para responder melhor  
D) Apenas mensagens do chat atual, sem relacao com o codigo

## 3) Qual pratica melhora a qualidade das respostas da IA ao pedir alteracoes em codigo?

A) Fazer pedidos vagos, como "melhora isso ai"  
B) Informar arquivo, objetivo, restricoes e comportamento esperado  
C) Evitar mencionar o contexto do projeto para nao confundir  
D) Pedir varias tarefas nao relacionadas no mesmo prompt, sem prioridade

## 4) Em relacao ao uso de @arquivos e @pastas no prompt, a melhor afirmacao e:

A) Nao muda nada, pois a IA ignora referencias explicitas  
B) Ajuda a ancorar a IA nas fontes corretas do projeto, reduzindo ambiguidades  
C) Serve apenas para renomear arquivos durante a conversa  
D) Funciona somente em arquivos .md

## 5) Qual risco e mais comum quando o contexto fornecido e insuficiente?

A) A IA sempre se recusa a responder  
B) A IA pode "alucinar" detalhes e sugerir mudancas incoerentes com o codigo real  
C) O projeto e apagado automaticamente  
D) O compilador para de funcionar permanentemente

## 6) Ao trabalhar em um monorepo grande, qual estrategia tende a ser mais eficiente?

A) Enviar o repositorio inteiro em todo prompt  
B) Fornecer contexto incremental e direcionado para o modulo relevante  
C) Nao usar indexacao, apenas copiar e colar codigo manualmente  
D) Pedir para a IA adivinhar a arquitetura

## 7) Sobre seguranca e privacidade no uso de contexto local, qual alternativa esta correta?

A) E recomendavel sempre incluir secrets e credenciais no prompt para "acelerar"  
B) Devemos evitar expor dados sensiveis e revisar o que esta sendo compartilhado no contexto  
C) Privacidade nao importa em ambiente de desenvolvimento  
D) Arquivos .env devem ser publicados para melhorar a indexacao

## 8) Qual comportamento indica bom uso de IA para refatoracao com contexto local?

A) Aplicar todas as sugestoes sem revisar diff nem rodar testes  
B) Pedir mudancas pequenas, revisar o diff e validar com testes/lint  
C) Refatorar dezenas de arquivos criticos de uma vez sem checkpoints  
D) Ignorar convencoes do projeto para ficar "mais criativo"

## 9) Qual e a vantagem de combinar busca semantica com leitura de arquivos especificos?

A) Eliminar completamente a necessidade de entender o dominio  
B) Encontrar rapidamente onde esta a logica e confirmar detalhes no codigo fonte  
C) Aumentar o tamanho do prompt sem ganho de precisao  
D) Evitar qualquer verificacao manual

## 10) Qual frase resume melhor uma boa estrategia de contexto em IDE AI Native?

A) "Quanto mais texto aleatorio, melhor a resposta"  
B) "Contexto relevante, objetivo claro e verificacao tecnica apos a resposta"  
C) "Nao preciso validar nada se a IA parecer confiante"  
D) "A IA funciona melhor sem informacoes do projeto"

---

## Gabarito com justificativas

**1) B** - A indexacao permite localizar simbolos, arquivos e trechos relevantes com eficiencia, aumentando a precisao das respostas e edicoes sugeridas.

**2) C** - Contexto local e tudo que da "situacao" para a IA no projeto (arquivos, referencias, historico e objetivo da tarefa), nao apenas uma aba isolada.

**3) B** - Quanto mais claro o pedido (onde mexer, o que mudar e restricoes), menor a ambiguidade e maior a chance de uma resposta util.

**4) B** - Referenciar `@arquivos` e `@pastas` guia a IA para as fontes corretas, evitando interpretacoes genericas ou fora do escopo.

**5) B** - Sem contexto suficiente, a IA pode completar lacunas com suposicoes incorretas (alucinacoes), gerando sugestoes inconsistentes.

**6) B** - Em projetos grandes, contexto direcionado por modulo/feature e mais eficiente do que despejar tudo de uma vez.

**7) B** - Boas praticas exigem cuidado com dados sensiveis: nunca compartilhar credenciais desnecessariamente e revisar o que entra no contexto.

**8) B** - Fluxo seguro e produtivo inclui mudancas menores, revisao de diff e validacao tecnica (testes, lint, build).

**9) B** - Busca semantica acelera descoberta de pontos relevantes; leitura pontual confirma implementacao real e reduz erro de interpretacao.

**10) B** - Resultado consistente vem de contexto relevante + objetivo claro + verificacao posterior, nao de volume de texto sem foco.
