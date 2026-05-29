# 🧪 Quizz: Geração de testes e casos de sucesso/erro com IA
**Módulo: Qualidade e manutenibilidade**

Este questionário verifica os **temas** de gerar testes com IA (cobertura, priorização) e de montar suítes com **casos de sucesso e erro** — sem depender do código visto em sala.

---

### 1. O relatório de cobertura com linhas *missing* serve principalmente para:
   - A) Certificar prontidão de produção quando o percentual global atinge o limiar configurado no CI.
   - B) Mapear linhas ainda não exercitadas e orientar onde falta prova executável — sem tratar percentual como meta final.
   - C) Priorizar remoção de regras de negócio com baixa frequência de uso em ambiente produtivo.
   - D) Substituir leitura do código de produção porque linha coberta implica comportamento validado.

### 2. Ao pedir testes à IA, qual postura está mais alinhada ao tema de **geração consciente**?
   - A) Reiniciar a suíte do zero quando a IA sugere casos novos conflitantes com os existentes.
   - B) Pedir volume máximo inicial para bater 100% de cobertura antes de revisar qualquer assert.
   - C) Aceitar asserts fracos desde que a linha alvo apareça como executada no relatório.
   - D) Começar listando lacunas de alto risco (entrada, saída, assert) antes de pedir implementação.

### 3. Cobertura subiu, mas o novo teste só faz `assert resultado is not None`. O problema central é:
   - A) O pytest invalida testes cujo assert não compara tipos primitivos explicitamente.
   - B) A linha foi exercitada, mas o contrato de negócio segue sem prova — cobertura alta pode mascarar isso.
   - C) Cobertura de branch deveria diminuir quando o assert não inspeciona o valor retornado.
   - D) Apenas testes E2E são autorizados a validar valores numéricos ou mensagens de erro.

### 4. Skills como **pytest-coverage** e **python-testing-patterns** ajudam principalmente a:
   - A) Automatizar a decisão final sobre quais fluxos entram ou saem do escopo de teste da sprint.
   - B) Acelerar geração de código de produção refatorado a partir do relatório de cobertura.
   - C) Apoiar leitura de relatórios de coverage e aplicação de padrões pytest ao gerar ou revisar testes.
   - D) Substituir execução local de pytest por análise estática integrada ao editor.

### 5. Uma suíte que cobre **só happy path** deixa o sistema vulnerável porque:
   - A) O happy path representa tão pouco tráfego real que testá-lo não reduz risco operacional.
   - B) O pytest descarta automaticamente exceções não cobertas durante a coleta de testes.
   - C) Casos de sucesso são redundantes quando já existe documentação funcional aprovada.
   - D) Falhas previstas, entradas inválidas e bordas podem regredir sem alerta se ninguém as exercita.

### 6. Quando o código sinaliza erro com **exceção** (`ValueError`), o assert idiomático em pytest costuma ser:
   - A) Envolver a chamada em `with pytest.raises(ValueError, match="...")` validando tipo e mensagem.
   - B) Capturar com try/except genérico e usar `assert True` quando qualquer exceção ocorrer.
   - C) Assert `funcao() is None` assumindo que erro sempre retorna valor nulo.
   - D) Marcar o cenário com skip fixo porque exceções não são determinísticas em teste.

### 7. Quando o código sinaliza erro por **retorno** (`ok: False`, mensagem no payload), o teste deve:
   - A) Manter `pytest.raises` para padronizar a suíte, mesmo quando a API retorna erro estruturado.
   - B) Verificar apenas que nenhuma exceção foi lançada — o retorno de falha fica implícito.
   - C) Assert `ok` falso (ou equivalente) e checar mensagem/código de erro esperado, sem esperar exceção.
   - D) Omitir o cenário: contratos por retorno são considerados não testáveis em unitário.

### 8. Casos de **borda** de sucesso (ex.: saldo exatamente igual ao custo) importam porque:
   - A) Operadores de comparação e off-by-one costumam falhar exatamente nos limites mínimo e máximo.
   - B) Fronteiras numéricas só importam quando a IA não consegue gerar casos intermediários.
   - C) Se o happy path passa, valores na fronteira são estatisticamente equivalentes ao meio do intervalo.
   - D) Bordas pertencem exclusivamente a testes de integração porque exigem estado persistente.

### 9. A IA sugere `@pytest.mark.parametrize` para oito códigos inválidos semelhantes. Quando isso **faz sentido**?
   - A) Sempre que houver mais de três casos — a parametrização reduz duplicação em qualquer contexto.
   - B) Nunca — testes parametrizados ocultam qual input falhou e devem ser evitados.
   - C) Somente quando a meta da sprint é elevar o percentual numérico de cobertura acima de 95%.
   - D) Quando entrada, tipo de falha e forma do assert são iguais — evitando cópia mecânica de testes quase idênticos.

### 10. Qual frase resume melhor **geração + sucesso/erro** com IA neste trecho do módulo?
   - A) Percentual alto de cobertura dispensa revisão de asserts; erros em produção são exceção estatística.
   - B) Prompts volumosos substituem critério humano — a IA fecha o desenho da suíte e você só roda o CI.
   - C) Relatório de lacunas orienta prioridade; a IA sugere testes; você valida asserts para sucesso, borda e erro (raises ou ok False).
   - D) Prazo curto justifica suíte só de happy path; caminhos negativos entram na próxima release.

---

## 🔑 Gabarito comentado

### 1. Resposta: B
**Justificativa:** Cobertura é mapa de lacunas de execução, não certificado de release — guia **onde** investir em prova.

### 2. Resposta: D
**Justificativa:** Geração consciente começa com lacunas priorizadas e revisáveis, não volume automático nem restart cego.

### 3. Resposta: B
**Justificativa:** Executar linha ≠ provar comportamento — tema central da geração assistida por IA.

### 4. Resposta: C
**Justificativa:** Skills apoiam **leitura de coverage** e **qualidade pytest**, não substituem julgamento humano.

### 5. Resposta: D
**Justificativa:** Suíte madura inclui erro e borda; só sucesso deixa regressões silenciosas.

### 6. Resposta: A
**Justificativa:** Exceção esperada → `pytest.raises` com match explícito — padrão idiomático.

### 7. Resposta: C
**Justificativa:** Erro por retorno exige assert no **contrato de falha**, não raises.

### 8. Resposta: A
**Justificativa:** Bordas são onde regras de comparação e arredondamento quebram com frequência.

### 9. Resposta: D
**Justificativa:** Parametrize quando a estrutura do teste é a mesma; casos distintos de falha podem pedir testes separados.

### 10. Resposta: C
**Justificativa:** Integra os dois temas: cobertura + IA + sucesso/borda/erro com assert adequado a cada contrato.
