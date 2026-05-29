# 🧪 Quizz: Papel e estrutura de testes unitários com IA
**Módulo: Qualidade e manutenibilidade**

Este questionário verifica se você domina os **temas** de testes unitários — **para que servem**, **como estruturá-los com qualidade** e **como usar IA** nesse processo — sem depender do código específico visto em sala.

---

### 1. Qual é o papel principal de um teste **unitário** bem aplicado?
   - A) Validar layout, formatação e convenções de nomenclatura do repositório.
   - B) Substituir revisão humana e testes de integração em todo o sistema.
   - C) Provar regras locais de forma rápida e isolada, com falha próxima da causa.
   - D) Garantir que o deploy em produção não terá incidentes.

### 2. Qual situação costuma ser **menos** adequada como foco exclusivo de teste unitário?
   - A) Validação de entrada com retorno de erro explícito.
   - B) Orquestração que altera estado global, grava histórico e emite notificação.
   - C) Função pura que calcula desconto a partir de valor e percentual.
   - D) Regra de arredondamento em uma função sem efeitos colaterais.

### 3. “Documentação viva” é um papel citado para testes unitários porque:
   - A) Exemplos executáveis mostram como a unidade se comporta em casos concretos.
   - B) Os testes substituem README e wiki oficial do produto.
   - C) Só documentação escrita por PM conta como documentação.
   - D) pytest gera PDF automaticamente após cada execução.

### 4. Ao usar IA para testes, qual pergunta-guia ajuda a escolher **unitário vs integração**?
   - A) “Este comportamento deve ser provado isolado na unidade ou no fluxo com estado e colaboradores?”
   - B) “Quantos testes a IA consegue gerar em um minuto?”
   - C) “O teste fica verde na primeira tentativa?”
   - D) “O arquivo tem mais de 100 linhas?”

### 5. No padrão **AAA** (Arrange–Act–Assert), o que caracteriza a fase **Act**?
   - A) Preparar dados, mocks e entradas do cenário.
   - B) Comparar resultado obtido com o esperado.
   - C) Refatorar o código de produção após o assert.
   - D) Executar a ação sob teste (chamar a função/método alvo).

### 6. O que torna a **estrutura** de um teste de qualidade, além de passar no CI?
   - A) Nome genérico para evitar nomes longos.
   - B) Vários comportamentos independentes no mesmo teste para “economizar arquivos”.
   - C) Nome descritivo, foco em um comportamento, AAA legível e asserts idiomáticos.
   - D) Uso de `try/except` manual em todo teste de exceção.

### 7. A IA sugere dezenas de testes genéricos só para subir cobertura. Qual postura é mais alinhada ao tema do módulo?
   - A) Pedir lacunas priorizadas (função, entrada, saída, risco) e implementar poucos casos de alto valor.
   - B) Aceitar tudo — cobertura alta sempre significa qualidade.
   - C) Apagar testes existentes que já passam.
   - D) Converter toda a suíte em um único teste parametrizado sem critério.

### 8. Um teste passa com `assert resultado is not None`, mas não verifica valor nem regra. Qual o problema **de qualidade**?
   - A) Nenhum — verde no CI basta.
   - B) pytest proíbe asserts fracos por configuração padrão.
   - C) Só testes de integração podem usar asserts numéricos.
   - D) O teste não documenta nem protege o contrato; regressões reais podem passar despercebidas.

### 9. Ao **reestruturar** testes fracos com apoio da IA, qual é o critério de sucesso mais correto?
   - A) Menos arquivos, mesmo que comportamentos deixem de ser verificados.
   - B) Copiar sugestões da IA sem rodar pytest.
   - C) Suite verde **e** melhor nome/AAA/foco, preservando o que já era garantido antes.
   - D) Renomear testes sem alterar estrutura interna.

### 10. Qual frase resume melhor o uso consciente de **IA** em testes unitários neste trecho?
   - A) “A IA decide o que testar; você só aprova o merge.”
   - B) “Unitário e integração são equivalentes se usarem pytest.”
   - C) “A IA acelera análise de lacunas e revisão de estrutura; você define o comportamento que cada assert deve provar.”
   - D) “Quanto mais testes a IA gerar, melhor a arquitetura.”

---

## 🔑 Gabarito comentado

### 1. Resposta: C
**Justificativa:** Unitário protege **unidade de comportamento** com feedback rápido — rede fina, não substituto de todo tipo de teste.

### 2. Resposta: B
**Justificativa:** Orquestração com estado e efeitos colaterais pede outra camada de prova; unitário concentra-se em regras isoláveis.

### 3. Resposta: A
**Justificativa:** Documentação viva = exemplos **executáveis** do contrato da unidade, úteis para dev e para revisão com IA.

### 4. Resposta: A
**Justificativa:** Separar o que é prova local do que é prova de fluxo evita confundir papéis e pedir o tipo errado à IA.

### 5. Resposta: D
**Justificativa:** Act é a execução sob teste; Arrange prepara, Assert verifica — eixo central da estrutura de qualidade.

### 6. Resposta: C
**Justificativa:** Qualidade estrutural = legibilidade + foco + idioma do framework, não só CI verde.

### 7. Resposta: A
**Justificativa:** IA como auditor priorizador, não fábrica de volume; poucos casos com propósito valem mais que cobertura vazia.

### 8. Resposta: D
**Justificativa:** Assert fraco dá falsa segurança — tema central: **verde ≠ prova**.

### 9. Resposta: C
**Justificativa:** Reestruturar é melhorar forma **sem perder** o contrato já garantido — comportamento preservado + pytest verde.

### 10. Resposta: C
**Justificativa:** IA apoia lacunas e revisão; o engenheiro mantém o **porquê** de cada assert e o tipo de teste adequado.
