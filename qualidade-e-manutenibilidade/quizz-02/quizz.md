# 🧪 Quizz: IA na refatoração e na separação de módulos
**Módulo: Qualidade e manutenibilidade**

Este questionário foca em **como usar Copilot (ou agente equivalente) com método** ao refatorar e ao separar responsabilidades — não em teoria genérica de arquitetura.

---

### 1. Antes de pedir à IA para “consertar” um monólito, qual prompt está mais alinhado ao fluxo do módulo?
   - A) “Refatore tudo e deixe production-ready.”
   - B) “Analise este arquivo com `@workspace`: liste responsabilidades misturadas e riscos se eu mudar uma regra agora. Não escreva patch.”
   - C) “Apague funções longas e reescreva do zero.”
   - D) “Gere apenas comentários bonitos no código.”

### 2. Você quer **refatoração segura** com IA. O que deve ir no prompt além do arquivo?
   - A) Pedir para a IA ignorar testes existentes para ir mais rápido.
   - B) Anexar o arquivo **e** os testes de caracterização, pedindo **um passo por vez** e exigindo que os testes continuem passando.
   - C) Pedir dez refatorações diferentes na mesma mensagem para comparar.
   - D) Pedir só estilo de código (PEP8) sem mencionar comportamento.

### 3. A IA devolve um patch grande que “organiza validação, preço e banco” num único commit sugerido. O que fazer primeiro?
   - A) Aplicar tudo e rodar testes depois.
   - B) Recusar o escopo amplo e pedir **apenas o primeiro passo** (ex.: extrair validação), com diff mínimo.
   - C) Aceitar porque a IA “tem contexto do projeto”.
   - D) Apagar os testes que falharem.

### 4. Para separar responsabilidades com apoio da IA, qual pedido ajuda mais?
   - A) “Crie 20 arquivos novos com design patterns.”
   - B) “Proponha ordem de extração em 4 passos: arquivo sugerido, o que sai, o que fica na fachada, qual teste rodar — sem implementar ainda.”
   - C) “Mude o contrato público para ficar mais RESTful.”
   - D) “Traduza variáveis para inglês e pronto.”

### 5. Depois de aplicar um passo sugerido pela IA, qual prompt de **revisão** é o mais útil?
   - A) “Está bonito?”
   - B) “Atue como revisor: este patch mudou comportamento observável? Surgiu efeito colateral novo? O passo ficou grande demais para reverter?”
   - C) “Gere documentação de marketing do produto.”
   - D) “Reescreva em outra linguagem.”

### 6. A IA sugere juntar validação e cálculo de preço no mesmo módulo “para simplificar”. Qual postura de **engenheiro com IA** é correta?
   - A) Aceitar sempre: menos arquivos é objetivo da sprint.
   - B) Questionar: pedir à IA comparar trade-offs e manter fronteiras se os testes isolados e o motivo de mudança de cada parte forem diferentes.
   - C) Ignorar e nunca mais usar IA neste módulo.
   - D) Pedir à IA para remover os testes de caracterização.

### 7. Qual papel dos testes de caracterização **no diálogo com a IA**?
   - A) Substituir sua revisão humana — se a IA disse que passa, basta.
   - B) Servir de **contrato explícito** no prompt (“não quebre estes comportamentos”) e como verificação objetiva após cada sugestão da IA.
   - C) Só existir para a IA treinar modelos futuros.
   - D) Impedir qualquer refatoração estrutural.

### 8. Qual frase resume a “máxima” de uso da IA neste trecho do módulo?
   - A) “A IA decide a arquitetura; você só aprova o merge.”
   - B) “A IA propõe passos e alternativas; você segura escopo, contrato e evidência (testes) antes de aceitar.”
   - C) “Quanto maior o patch da IA, melhor o aprendizado.”
   - D) “Prompt genérico funciona igual a prompt com `@workspace` e testes anexados.”

---

## 🔑 Gabarito comentado

### 1. Resposta: B
**Justificativa:** Diagnóstico sem patch espelha o uso de IA como auditor — você entende o terreno antes de delegar refatoração.

### 2. Resposta: B
**Justificativa:** Contexto (`@workspace` + testes) + passo único + testes verdes é o combo de refatoração segura **assistida** por IA.

### 3. Resposta: B
**Justificativa:** IA tende a overdelivery; o humano fatia o trabalho para manter reversibilidade e entender cada diff.

### 4. Resposta: B
**Justificativa:** Plano em passos transforma a IA em parceira de estratégia, não demolidora de uma tacada só.

### 5. Resposta: B
**Justificativa:** Prompt de revisor força a IA (e você) a checar comportamento e tamanho do passo — não só estética.

### 6. Resposta: B
**Justificativa:** Você usa a IA para debater trade-offs, mas a decisão de fronteira continua baseada em testabilidade e motivo de mudança.

### 7. Resposta: B
**Justificativa:** Testes são a âncora objetiva na conversa com a IA; sem isso, “refatoração segura” vira opinião do modelo.

### 8. Resposta: B
**Justificativa:** IA acelera propostas; engenharia segura exige escopo, contrato e evidência na mão do desenvolvedor.
