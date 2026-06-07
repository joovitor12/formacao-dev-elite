# 🧪 Quizz: Revisão de PR com IA

**Módulo: Automação e DevOps inteligente**

Este questionário verifica os **temas** de **papel do code review moderno** (veredito humano, severidade, CI vs merge) e de **o que a IA avalia em PRs** (dimensões da matriz, pontos cegos, falso positivo) — sem depender do código visto em sala.

---

### 1. No fluxo de revisão com GitHub Copilot Code Review, qual divisão de papéis está mais alinhada ao material?
   - A) O Copilot decide o merge; o humano só corrige o estilo do diff.
   - B) O Copilot acelera a leitura do diff; o revisor humano prioriza riscos e decide o merge.
   - C) O humano ignora o Copilot para evitar viés; a IA só serve para gerar commits.
   - D) O Copilot substitui comentários no PR; o humano não precisa classificar severidade.

### 2. Um PR passou no CI, mas o review aponta token em log e lógica que sempre dispara notificação. Por que isso **não** basta para merge?
   - A) CI verde só prova sintaxe; riscos de segurança e operação podem passar despercebidos nos jobs.
   - B) CI verde invalida qualquer comentário do Copilot — o pipeline já validou o comportamento.
   - C) Token em log é nit estético se o build compilou e os testes unitários rodaram.
   - D) Notificação sempre ativa é aceitável em DevOps porque facilita observabilidade em produção.

### 3. Um comentário de review **acionável** no GitHub, no estilo do material, deve conter principalmente:
   - A) Trecho citado, risco explicado e ação pedida ao autor — tom profissional e específico.
   - B) Apenas elogio ao autor para manter moral da equipe antes do merge.
   - C) Link genérico para documentação de Python, sem citar o trecho do diff.
   - D) Pedido de refatoração total do repositório, mesmo que o PR seja pequeno.

### 4. Ao cruzar sugestões do Copilot com sua análise, qual postura reflete o processo ensinado?
   - A) Aceitar tudo que a IA sugerir para acelerar o merge e reduzir atrito no time.
   - B) Marcar concordância (ou discordância), severidade final e o comentário que você deixaria no PR.
   - C) Ignorar achados de segurança se o Copilot não usou a palavra “crítico”.
   - D) Tratar todo comentário do Copilot como bloqueante, sem distinguir nit ou sugestão.

### 5. Na matriz de avaliação, um segredo (API key ou token) aparecendo em **log de produção** costuma ser classificado em qual dimensão e tratamento?
   - A) Manutenção — sugestão opcional de renomear variáveis para inglês.
   - B) Escopo — nit porque o arquivo de log não faz parte do diff principal.
   - C) Segurança — achado grave; exposição de credencial em runtime ou observabilidade.
   - D) Testes — irrelevante se a suíte unitária não asserta conteúdo de log.

### 6. Uma regra de negócio sutil na fronteira numérica (ex.: rollback só quando taxa **>** 0,05, não **>=**) ilustra principalmente:
   - A) Limite da IA em **correção** — padrões óbvios são flagrados; fronteiras de negócio podem escapar.
   - B) Limite da IA em **escopo** — arquivos pequenos nunca recebem comentários do Copilot.
   - C) Falha do revisor humano — quem decide merge não deve olhar comparações numéricas.
   - D) Prova de que CI verde já cobre regras de fronteira sem necessidade de review.

### 7. “Ponto cego” do Copilot Code Review, no sentido do material, é melhor definido como:
   - A) Comentário de estilo que você concorda mas considera nit no merge.
   - B) Achado importante que o revisor humano levantaria e a IA **não** comentou (ou comentou mal).
   - C) Qualquer sugestão da IA que demora mais de trinta segundos para aparecer no PR.
   - D) Arquivo do PR que o GitHub não conseguiu renderizar no diff por ser muito grande.

### 8. Diante de um comentário do Copilot sobre convenção de nomes sem risco de segurança ou operação, a decisão mais alinhada à matriz é:
   - A) Classificar como nit ou falso positivo se não houver impacto em risco — não bloquear merge por estilo.
   - B) Rejeitar o PR imediatamente — toda sugestão da IA tem peso de bloqueante.
   - C) Ignorar a matriz e mergear só porque o autor é sênior no time.
   - D) Exigir rewrite completo do módulo antes de qualquer outro comentário ser respondido.

---

## 🔑 Gabarito comentado

### 1. Resposta: B
**Justificativa:** A máxima do tema é explícita: a IA acelera triagem do diff; julgamento de risco e decisão de merge permanecem humanos.

### 2. Resposta: A
**Justificativa:** Pipeline verde não substitui review de segurança e comportamento operacional — exatamente a “armadilha” CI verde ≠ PR aprovado.

### 3. Resposta: A
**Justificativa:** Comentários acionáveis ligam trecho, risco e pedido claro ao autor — base do exercício de review no GitHub.

### 4. Resposta: B
**Justificativa:** O registro de revisão pede cruzar Copilot com análise: concordância, severidade e texto que você publicaria no PR.

### 5. Resposta: C
**Justificativa:** A matriz coloca segredo em código/log na dimensão **Segurança** — típico achado que a IA costuma pegar e que humanos tratam como grave.

### 6. Resposta: A
**Justificativa:** Fronteiras de regra de negócio são exemplo clássico do que a dimensão **Correção** pode deixar passar enquanto bugs sintáticos são mais visíveis.

### 7. Resposta: B
**Justificativa:** Ponto cego é lacuna da avaliação automática preenchida pelo revisor — eixo central da taxonomia e da planilha de classificação.

### 8. Resposta: A
**Justificativa:** Falso positivo e nit devem ser justificados por **risco e dimensão**, não por gosto de estilo — evita bloquear merge sem motivo operacional ou de segurança.
