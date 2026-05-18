# 🧪 Quizz: IA na refatoração e na separação de módulos
**Módulo: Qualidade e manutenibilidade**

Este questionário foca em **como usar Copilot (ou agente equivalente) com método** ao refatorar e ao separar responsabilidades — não em teoria genérica de arquitetura.

---

### 1. Antes de pedir à IA para “consertar” um monólito, qual prompt está mais alinhado ao fluxo do módulo?
   - A) “Analise este arquivo com `@workspace`: liste responsabilidades misturadas e riscos se eu mudar uma regra agora. Não escreva patch.”
   - B) “Refatore tudo e deixe production-ready.”
   - C) “Apague funções longas e reescreva do zero.”
   - D) “Gere apenas comentários bonitos no código.”

### 2. Você quer **refatoração segura** com IA. O que deve ir no prompt além do arquivo?
   - A) Pedir para a IA ignorar testes existentes para ir mais rápido.
   - B) Pedir dez refatorações diferentes na mesma mensagem para comparar.
   - C) Pedir só estilo de código (PEP8) sem mencionar comportamento.
   - D) Anexar o arquivo **e** os testes de caracterização, pedindo **um passo por vez** e exigindo que os testes continuem passando.

### 3. A IA devolve um patch grande que “organiza validação, preço e banco” num único commit sugerido. O que fazer primeiro?
   - A) Recusar o escopo amplo e pedir **apenas o primeiro passo** (ex.: extrair validação), com diff mínimo.
   - B) Aplicar tudo e rodar testes depois.
   - C) Aceitar porque a IA “tem contexto do projeto”.
   - D) Apagar os testes que falharem.

### 4. Para separar responsabilidades com apoio da IA, qual pedido ajuda mais?
   - A) “Crie 20 arquivos novos com design patterns.”
   - B) “Mude o contrato público para ficar mais RESTful.”
   - C) “Proponha ordem de extração em 4 passos: arquivo sugerido, o que sai, o que fica na fachada, qual teste rodar — sem implementar ainda.”
   - D) “Traduza variáveis para inglês e pronto.”

### 5. Depois de aplicar um passo sugerido pela IA, qual prompt de **revisão** é o mais útil?
   - A) “Está bonito?”
   - B) “Gere documentação de marketing do produto.”
   - C) “Reescreva em outra linguagem.”
   - D) “Atue como revisor: este patch mudou comportamento observável? Surgiu efeito colateral novo? O passo ficou grande demais para reverter?”

### 6. A IA sugere juntar validação e cálculo de preço no mesmo módulo “para simplificar”. Qual postura de **engenheiro com IA** é correta?
   - A) Aceitar sempre: menos arquivos é objetivo da sprint.
   - B) Questionar: pedir à IA comparar trade-offs e manter fronteiras se os testes isolados e o motivo de mudança de cada parte forem diferentes.
   - C) Ignorar e nunca mais usar IA neste módulo.
   - D) Pedir à IA para remover os testes de caracterização.

### 7. Qual papel dos testes de caracterização **no diálogo com a IA**?
   - A) Substituir sua revisão humana — se a IA disse que passa, basta.
   - B) Só existir para a IA treinar modelos futuros.
   - C) Servir de **contrato explícito** no prompt (“não quebre estes comportamentos”) e como verificação objetiva após cada sugestão da IA.
   - D) Impedir qualquer refatoração estrutural.

### 8. Qual frase resume a “máxima” de uso da IA neste trecho do módulo?
   - A) “A IA propõe passos e alternativas; você segura escopo, contrato e evidência (testes) antes de aceitar.”
   - B) “A IA decide a arquitetura; você só aprova o merge.”
   - C) “Quanto maior o patch da IA, melhor o aprendizado.”
   - D) “Prompt genérico funciona igual a prompt com `@workspace` e testes anexados.”

---

## 🔑 Gabarito comentado

### 1. Resposta: A
**Justificativa:** Diagnóstico sem patch espelha o uso de IA como auditor — você entende o terreno antes de delegar refatoração.

### 2. Resposta: D
**Justificativa:** Contexto (`@workspace` + testes) + passo único + testes verdes é o combo de refatoração segura **assistida** por IA.

### 3. Resposta: A
**Justificativa:** IA tende a overdelivery; o humano fatia o trabalho para manter reversibilidade e entender cada diff.

### 4. Resposta: C
**Justificativa:** Plano em passos transforma a IA em parceira de estratégia, não demolidora de uma tacada só.

### 5. Resposta: D
**Justificativa:** Prompt de revisor força a IA (e você) a checar comportamento e tamanho do passo — não só estética.

### 6. Resposta: B
**Justificativa:** Você usa a IA para debater trade-offs, mas a decisão de fronteira continua baseada em testabilidade e motivo de mudança.

### 7. Resposta: C
**Justificativa:** Testes são a âncora objetiva na conversa com a IA; sem isso, “refatoração segura” vira opinião do modelo.

### 8. Resposta: A
**Justificativa:** IA acelera propostas; engenharia segura exige escopo, contrato e evidência na mão do desenvolvedor.
