# 🧪 Quizz: Legado, medo de mudar e code smells

Este questionário verifica se você consegue relacionar conceitos de código legado, custo de mudança e identificação de *code smells* com o uso de IA como apoio ao diagnóstico.

---

### 1. Na prática de engenharia, o que melhor define “código legado” neste módulo?
   - A) Qualquer código escrito há mais de cinco anos, independentemente de testes.
   - B) Código que só existe em linguagens antigas, como COBOL ou Fortran.
   - C) Código em que você tem **medo de mudar** porque o custo e o risco de quebra são altos.
   - D) Código que não segue o padrão de formatação da equipe.

### 2. Qual dos “três pilares do medo” está mais ligado a “mudar uma linha e não saber o que vai quebrar”?
   - A) Falta de testes e rede de proteção.
   - B) Uso excessivo de comentários no código.
   - C) Preferência por funções muito curtas.
   - D) Uso de tipagem estática obrigatória.

### 3. Ao usar Copilot como **auditor forense** na primeira aula, qual postura é a mais adequada?
   - A) Pedir refatoração completa e merge automático.
   - B) Pedir diagnóstico de riscos, acoplamento e pontos sensíveis **antes** de pedir refatoração.
   - C) Pedir só correção de sintaxe e estilo.
   - D) Evitar anexar o arquivo para a IA não “viciar” a análise.

### 4. “Side effects” (efeitos colaterais), no contexto de manutenibilidade, referem-se principalmente a:
   - A) Funções que retornam mais de um valor.
   - B) Comportamentos que alteram estado fora do retorno explícito (globais, I/O, mutações compartilhadas), dificultando prever o impacto de uma mudança.
   - C) Uso de variáveis com nomes em inglês.
   - D) Código que roda mais rápido em produção do que em desenvolvimento.

### 5. O que é um **code smell** na segunda aula do módulo?
   - A) Um erro de sintaxe que impede o programa de compilar.
   - B) Um bug comprovado em produção.
   - C) Um sinal de possível problema de desenho ou risco de mudança — não é necessariamente bug hoje.
   - D) Qualquer código que outra pessoa escreveu e você não gosta.

### 6. Duplicação de regra de negócio (por exemplo, desconto calculado em dois lugares parecidos) é perigosa principalmente porque:
   - A) O código fica com mais linhas e ocupa mais disco.
   - B) Uma parte pode ser corrigida e a outra ficar defasada, gerando inconsistência e bug silencioso.
   - C) Compiladores não aceitam código duplicado.
   - D) Duplicação sempre melhora a performance.

### 7. Na priorização de smells, o critério “elite” alinhado ao material é:
   - A) Corrigir primeiro o que for mais fácil de renomear.
   - B) Priorizar o que tem **maior risco para o negócio** (cobrança, estoque, bloqueio de cliente, etc.).
   - C) Corrigir primeiro apenas questões estéticas de formatação.
   - D) Ignorar estado global se o sistema for pequeno.

### 8. Uma “rede de proteção mínima” sugerida na aula de smells pode incluir:
   - A) Apenas comentários explicando o código antigo.
   - B) Testes de caracterização e invariantes documentados que reduzem medo de mudar regras críticas.
   - C) Desligar logs para o sistema ficar mais rápido.
   - D) Remover tipos e usar só `Any` para flexibilidade.

---

## 🔑 Gabarito comentado

### 1. Resposta: C
**Justificativa:** Legado é sobre risco e custo de mudança, não sobre idade da stack.

### 2. Resposta: A
**Justificativa:** Sem testes (e sem contratos claros), cada alteração é aposta cega — pilar central do “medo”.

### 3. Resposta: B
**Justificativa:** O papel da IA como auditor é mapear risco primeiro; refatoração vem depois, com critério.

### 4. Resposta: B
**Justificativa:** Efeitos colaterais tornam o comportamento dependente de contexto global ou I/O, não só dos argumentos e do retorno.

### 5. Resposta: C
**Justificativa:** Smell é indício de design frágil ou dívida técnica; pode estar “funcionando” ainda.

### 6. Resposta: B
**Justificativa:** Divergência entre cópias da mesma regra é uma fonte clássica de bug e retrabalho.

### 7. Resposta: B
**Justificativa:** O material enfatiza impacto no negócio e custo operacional, não cosmética.

### 8. Resposta: B
**Justificativa:** Testes de caracterização e invariantes documentados atacam diretamente o medo de mudar e reduzem regressão.
