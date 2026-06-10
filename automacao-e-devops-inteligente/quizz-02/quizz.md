# 🧪 Quizz: Comentários automáticos e detecção de riscos

**Módulo: Automação e DevOps inteligente**

Este questionário verifica os **temas** de **comentários automáticos em PRs** (triagem, ruído, duplicação) e de **detecção de riscos** (severidade, lacunas, bloqueio de merge) — sem depender do código visto em sala.

---

### 1. No exercício de comentários automáticos, qual é o objetivo principal da triagem no inventário?
   - A) Desativar linters no repositório para reduzir fadiga do autor do PR.
   - B) Aplicar no merge todas as sugestões de bots para manter o pipeline sempre verde.
   - C) Converter comentários humanos em automáticos para padronizar o tom no GitHub.
   - D) Catalogar fonte e tipo de cada comentário e decidir o que vira ação, dismiss ou ruído.

### 2. Dois bots apontam o mesmo smell (ex.: segredo em log) com redações diferentes. A postura mais alinhada ao material é:
   - A) Tratar como um único achado na triagem e evitar que o autor corrija duas vezes por fadiga.
   - B) Ignorar os dois porque duplicação entre ferramentas prova falso positivo.
   - C) Bloquear merge só quando três ou mais bots repetirem o mesmo texto literal.
   - D) Exigir que cada bot remova o comentário antes de qualquer análise humana.

### 3. Um comentário automático de linter sobre variável não usada, sem impacto em segurança ou operação em produção, costuma ser classificado como:
   - A) Bloqueante — toda saída de bot tem prioridade sobre o revisor humano.
   - B) Crítico de compliance — linters sempre detectam exposição de dados pessoais.
   - C) Inexistente — linters nunca postam comentário inline no diff do GitHub.
   - D) Ruído ou parcial — candidato a dismiss se não houver risco real no contexto do PR.

### 4. A máxima “comentário automático acelera a triagem — quem revisa o PR decide o que vira ação” implica que:
   - A) Bots substituem o revisor quando o volume de comentários passa de dez por PR.
   - B) A triagem humana prioriza sinal, descarta ruído e define ações — os bots não decidem merge.
   - C) Comentários inline do Copilot têm precedência sobre resumos de CI no mesmo trecho.
   - D) Ferramentas automáticas só devem rodar após o merge na branch principal.

### 5. Na detecção de riscos, a diferença entre **code smell** e **risco** no material é melhor descrita como:
   - A) Smell é indício de desenho frágil; risco é impacto potencial em produção se o merge ocorrer.
   - B) Smell e risco são sinônimos — qualquer nit de estilo bloqueia deploy em produção.
   - C) Risco só existe quando o CI falha; smell é qualquer sugestão do Copilot Code Review.
   - D) Smell é bug comprovado; risco é apenas opinião estética do revisor.

### 6. PII (ex.: e-mail de cliente) incluído em log de deploy canário deve ser mapeado principalmente como risco de:
   - A) Manutenção — renomear variáveis resolve exposição em trilhas de observabilidade.
   - B) Escopo — logs não fazem parte do diff e não entram no mapa de riscos.
   - C) Performance — e-mail em log só afeta latência, não governança de dados.
   - D) Compliance — dado sensível em log pode violar política e gerar incidente.

### 7. “Lacuna de detecção” no mapa de riscos refere-se a:
   - A) Comentário duplicado entre Copilot e linter no mesmo trecho do diff.
   - B) Falha de rede ao carregar a página do PR no navegador do revisor.
   - C) Risco relevante que ferramentas não sinalizaram (ou sinalizaram mal) e o humano registra.
   - D) Ausência de testes unitários no repositório, independentemente do conteúdo do diff.

### 8. Um PR altera abort de canário de `taxa_erro >= 0,05` para `taxa_erro > 0,05` em produção. No mapa de riscos, isso tende a ser:
   - A) Risco de operação/correção — na fronteira exata o abort pode deixar de disparar.
   - B) Nit de estilo — comparações numéricas não afetam comportamento operacional.
   - C) Risco apenas de escopo — só importa se o arquivo tiver mais de cem linhas.
   - D) Falso alarme — CI verde garante que fronteiras de negócio foram validadas.

---

## 🔑 Gabarito comentado

### 1. Resposta: D
**Justificativa:** O inventário existe para classificar fonte, tipo e ação — separar o que corrige, responde, dismiss ou ignora.

### 2. Resposta: A
**Justificativa:** Duplicação entre bots é tema explícito: consolidar o achado na triagem evita retrabalho e fadiga do autor.

### 3. Resposta: D
**Justificativa:** Nem todo comentário automático vira ação; ruído e parcial são categorias da triagem quando não há risco operacional ou de segurança.

### 4. Resposta: B
**Justificativa:** Bots aceleram leitura; decisão de o que vira ação e merge permanece com quem revisa o PR.

### 5. Resposta: A
**Justificativa:** O material contrasta smell (indício de design) com risco (impacto se for para produção) — base do exercício de mapa de riscos.

### 6. Resposta: D
**Justificativa:** Exposição de e-mail em log é exemplo de risco de compliance/PII, não mera questão de nomenclatura ou performance.

### 7. Resposta: C
**Justificativa:** Lacuna é o risco que passou pelas ferramentas e precisa ser nomeado pelo revisor humano no mapa.

### 8. Resposta: A
**Justificativa:** Mudança na fronteira `>=` vs `>` é risco sutil de operação/correção — pode impedir abort no limite exato; CI verde não substitui essa análise.
