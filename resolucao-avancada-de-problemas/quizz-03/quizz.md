# 🧪 Quizz: Resolução Avançada de Problemas com IA
**Módulo: Aulas 08, 09 e 10**

Este questionário mede sua capacidade de usar IA como parceira de engenharia para revisar complexidade, identificar gargalos e escolher algoritmos com método.

---

### 1. Qual prompt representa melhor uma postura de "resolução avançada com IA" na revisão de complexidade?
   - A) "Melhora esse código aí, qualquer jeito serve."
   - B) "Refatora tudo para ficar mais bonito."
   - C) "Analise a função, estime Big-O atual, proponha 2 alternativas com trade-offs e sugira como validar por teste."
   - D) "Troca os nomes das variáveis para parecer mais otimizado."

### 2. Ao investigar gargalos com IA, qual sequência é mais correta?
   - A) Refatorar primeiro, medir depois.
   - B) Medir por etapa, formular hipótese, validar com evidência e só então otimizar.
   - C) Aceitar a primeira sugestão da IA e seguir.
   - D) Ignorar testes para ganhar velocidade.

### 3. Um assistente de IA sugere otimização agressiva, mas quebra regra de desempate do ranking. Qual decisão é mais alinhada ao método das aulas?
   - A) Aceitar, pois performance importa mais que contrato funcional.
   - B) Rejeitar a sugestão e manter corretude + critérios de aceite antes de qualquer ganho.
   - C) Publicar mesmo assim e corrigir depois.
   - D) Remover os testes de desempate.

### 4. Em "Sugestões algorítmicas com IA", o que diferencia um bom uso da ferramenta de um uso amador?
   - A) Pedir sempre "o algoritmo mais rápido do mundo".
   - B) Pedir código pronto sem contexto.
   - C) Fornecer contexto do domínio, volume esperado e limites, e exigir comparação entre alternativas.
   - D) Evitar mostrar testes para a IA "não se confundir".

### 5. Qual é o papel de testes de budget de operações no fluxo com IA?
   - A) Substituir todos os testes funcionais.
   - B) Servir como guarda de regressão para impedir retorno de soluções assintoticamente piores.
   - C) Medir estilo de código.
   - D) Eliminar a necessidade de revisão humana.

### 6. A IA apontou três possíveis gargalos. Como um dev de elite prioriza?
   - A) Pelo trecho com mais linhas de código.
   - B) Pelo trecho mais difícil de entender.
   - C) Pelo custo dominante no tempo total, validado por medição/instrumentação.
   - D) Pelo trecho sugerido com mais confiança pela IA.

### 7. Qual saída final melhor documenta aprendizado após otimização com IA?
   - A) "Ficou mais rápido."
   - B) "Troquei o algoritmo e deu certo."
   - C) Antes/depois com complexidade, evidência de teste, risco residual e próximo passo.
   - D) "A IA falou que está bom."

---

## 🔑 Gabarito Comentado

### 1. Resposta: C
**Justificativa:** O método avançado exige contexto, hipótese e validação. Não é só pedir "código melhor"; é guiar a IA por critérios objetivos.

### 2. Resposta: B
**Justificativa:** Resolver gargalo com método começa por evidência. Medir -> hipotetizar -> validar -> otimizar reduz retrabalho e evita "otimização de achismo".

### 3. Resposta: B
**Justificativa:** Performance sem corretude é regressão. Contrato funcional e critérios de aceite vêm antes de ganho de velocidade.

### 4. Resposta: C
**Justificativa:** IA rende mais quando recebe contexto técnico real (volume, limites, contrato, risco). Isso melhora a qualidade das sugestões algorítmicas.

### 5. Resposta: B
**Justificativa:** Budget de operações protege contra regressões de complexidade em mudanças futuras, funcionando como alarme no pipeline de testes.

### 6. Resposta: C
**Justificativa:** Gargalo é o trecho que domina o custo total, não o mais longo ou mais "complicado". Priorização correta depende de medição.

### 7. Resposta: C
**Justificativa:** Aprendizado técnico reutilizável inclui decisão tomada, evidência de validação e riscos restantes. Isso transforma correção pontual em conhecimento de equipe.
