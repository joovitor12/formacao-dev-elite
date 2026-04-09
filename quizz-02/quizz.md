# 🧠 Quizz: Utilidades do Copilot na sua Base de Código

Este quizz avalia sua capacidade de utilizar o GitHub Copilot de forma estratégica em projetos reais, focando em contextos de código novo, legado e manutenção.

---

### 1. Ao iniciar um arquivo totalmente novo em um projeto, qual é a prática recomendada de um "Desenvolvedor de Elite" para garantir que o Copilot seja preciso?
   - A) Começar a digitar a lógica da primeira função imediatamente para a IA aprender por tentativa e erro.
   - B) Definir um comentário de cabeçalho (docstring) explicando o propósito do módulo e as regras de negócio principais.
   - C) Copiar o código de outro arquivo semelhante para que a IA tenha algo para ler.
   - D) Desativar o Copilot até que pelo menos 50 linhas de código tenham sido escritas manualmente.

### 2. Você encontrou uma função complexa e sem documentação em um projeto legado de 2 anos atrás. Qual recurso do Copilot é o mais indicado para entender o que ela faz rapidamente?
   - A) Usar o comando `/explain` no Chat contextual.
   - B) Apagar a função e esperar que o Copilot a reescreva do zero.
   - C) Usar o prompt inline (`Ctrl+I`) com a palavra "Explique".
   - D) Abrir 10 arquivos vizinhos e esperar que a IA entenda por osmose.

### 3. O conceito de "Neighboring Tabs" (Abas Vizinhas) no Copilot significa que:
   - A) O Copilot lê todos os arquivos da sua pasta `node_modules` para dar sugestões.
   - B) A IA prioriza o contexto dos arquivos que estão abertos no seu editor no momento para gerar sugestões mais assertivas.
   - C) O Copilot consegue sugerir código baseado no que seus colegas de equipe estão digitando em outras máquinas.
   - D) A IDE cria automaticamente abas de sugestões para você escolher a melhor.

### 4. Ao realizar uma refatoração em um código existente usando o Prompt Inline (`Ctrl + I`), qual a principal vantagem visual para o desenvolvedor antes de aplicar a mudança?
   - A) O código é alterado instantaneamente sem chance de reversão.
   - B) A IA abre um navegador com a documentação da nova biblioteca sugerida.
   - C) A interface de "Diff", que permite comparar linha a linha o código original (vermelho) com a sugestão da IA (verde).
   - D) Um popup que avisa se o código vai rodar mais rápido ou mais devagar.

### 5. Se o Copilot começar a sugerir nomes de variáveis ou padrões de projeto diferentes do que o restante da sua empresa utiliza, qual a melhor forma de "corrigi-lo"?
   - A) Criar um arquivo de configuração `.txt` com todas as regras e deixar a aba sempre aberta.
   - B) Reinstalar a extensão do Copilot.
   - C) Ignorar as sugestões e continuar digitando manualmente até ele aprender.
   - D) Garantir que arquivos que seguem o padrão correto (como um `StyleGuide.py` ou `models.py`) estejam abertos e bem estruturados.

---

## 🔑 Gabarito Comentado

1. **B** - Definir o contexto inicial (Top-Down) ancora a IA no domínio do problema e reduz drasticamente as alucinações.
2. **A** - O `/explain` é otimizado para análise semântica e leitura de fluxo lógico.
3. **B** - O contexto imediato é a maior fonte de precisão para a geração de código assistida.
4. **C** - O "Diff" é essencial para a curadoria técnica, permitindo que o dev valide a alteração antes de aceitá-la.
5. **D** - Manter exemplos de "bom código" abertos reforça o aprendizado de contexto da IA para aquele workspace específico.