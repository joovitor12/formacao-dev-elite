# 🧪 Quizz: Reescrita e Trade-offs com IA
**Módulo: Resolução Avançada de Problemas (Aulas 11 e 12)**

Este questionário avalia sua capacidade de reescrever algoritmos com segurança e tomar decisões de engenharia baseadas em trade-offs reais com apoio de IA.

---

### 1. Em uma reescrita de algoritmo assistida por IA, qual deve ser o primeiro passo?
   - A) Aplicar imediatamente a versão mais rápida sugerida.
   - B) Definir o contrato funcional que não pode ser quebrado e como validá-lo.
   - C) Remover os testes antigos para evitar conflito.
   - D) Priorizar redução de linhas de código acima de tudo.

### 2. Qual cenário caracteriza uma boa reescrita de algoritmo?
   - A) Melhorou performance, mas mudou resultados em empates e casos de borda.
   - B) Manteve o contrato, reduziu custo assintótico e preservou legibilidade.
   - C) Ficou mais “sofisticado”, porém sem validação por testes.
   - D) Passou em um caso manual e foi direto para produção.

### 3. Ao avaliar trade-offs entre estratégia com cache e sem cache, qual afirmação é mais correta?
   - A) Cache sempre é melhor, independentemente do contexto.
   - B) Sem cache sempre é melhor por ser mais simples.
   - C) A escolha depende do volume, padrão de acesso, custo operacional e risco de manutenção.
   - D) Trade-off só importa em sistemas distribuídos.

### 4. Qual pergunta é mais “nível elite” para guiar a IA na Aula 12?
   - A) “Deixa esse código mais top.”
   - B) “Qual opção equilibra custo de tempo, memória e risco de manutenção para este volume?”
   - C) “Troca tudo para usar a estrutura mais famosa.”
   - D) “Pode ignorar teste e focar em otimizar.”

### 5. Um teste de budget de operações existe para:
   - A) substituir todos os testes de corretude.
   - B) validar estilo e nomenclatura.
   - C) detectar regressão de custo quando alguém reintroduz estratégia pior.
   - D) remover a necessidade de profiling.

### 6. A IA sugeriu uma alternativa com ganho de performance, mas custo de memória muito maior. O que fazer?
   - A) Aceitar automaticamente porque tempo sempre pesa mais.
   - B) Rejeitar automaticamente porque memória sempre pesa mais.
   - C) Comparar o ganho real vs limite operacional e decidir pelo contexto do sistema.
   - D) Escolher a alternativa com menos linhas.

### 7. Qual evidência torna uma decisão de trade-off tecnicamente defensável?
   - A) “Pareceu melhor durante leitura do código.”
   - B) comparação antes/depois, testes funcionais e budget de custo passando.
   - C) opinião da IA com alta confiança.
   - D) benchmark sem controle de cenário.

### 8. Sobre risco residual após reescrita/otimização, a postura correta é:
   - A) ocultar riscos para acelerar merge.
   - B) documentar riscos, limites e sinais de monitoramento pós-merge.
   - C) assumir que teste local elimina todo risco.
   - D) adiar toda discussão para quando houver incidente.

---

## 🔑 Gabarito Comentado

### 1. Resposta: B
**Justificativa:** Sem contrato claro, a IA pode otimizar o que não devia. Primeiro define invariantes e critérios de validação.

### 2. Resposta: B
**Justificativa:** Reescrita boa preserva comportamento e melhora custo com manutenção viável.

### 3. Resposta: C
**Justificativa:** Trade-off é contextual. Não existe resposta universal; depende do cenário operacional.

### 4. Resposta: B
**Justificativa:** Prompt de elite traz critério explícito de decisão, não só pedido genérico de “melhoria”.

### 5. Resposta: C
**Justificativa:** Budget protege contra regressão de performance/complexidade em mudanças futuras.

### 6. Resposta: C
**Justificativa:** Engenharia decide por impacto no contexto, equilibrando recursos e risco.

### 7. Resposta: B
**Justificativa:** Decisão defensável exige evidência reproduzível, não intuição isolada.

### 8. Resposta: B
**Justificativa:** Transparência de risco residual melhora operação e evita surpresas pós-merge.
