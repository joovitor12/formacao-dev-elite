# 🧪 Quizz: Mocking e avaliação de testes gerados com IA
**Módulo: Qualidade e manutenibilidade**

Este questionário verifica os **temas** de **mocking assistido por IA** (fronteiras, patch, asserts em colaboradores) e de **avaliar testes gerados** (rubrica, anti-padrões, decisão antes do merge) — sem depender do código visto em sala.

---

### 1. Onde aplicar `@patch` quando o serviço já importou a dependência?
   - A) No módulo onde a função foi **definida** — o mock substitui a implementação na origem.
   - B) No módulo de **teste** — o patch só vale dentro do arquivo que declara o decorador.
   - C) No módulo onde o nome foi **importado e usado** — o mock intercepta a referência local.
   - D) Em qualquer módulo da árvore de pacotes — pytest redireciona automaticamente para o alvo.

### 2. Em teste unitário de orquestração, candidato típico a mock é:
   - A) Porta externa de saldo, débito ou notificação simulando I/O remoto.
   - B) Regra pura de cálculo local sem efeitos colaterais nem rede.
   - C) Função que normaliza string antes de comparar cupom ou código.
   - D) Constante de módulo usada apenas como tabela de lookup estática.

### 3. Mockar a regra pura local dentro do teste de orquestração tende a:
   - A) Garantir que o fluxo valida percentuais reais da tabela de negócio em produção.
   - B) Reduzir duplicação porque a regra pura deixa de precisar de testes próprios.
   - C) Isolar o serviço de regressões em operadores matemáticos da biblioteca padrão.
   - D) Enfraquecer a prova porque o caminho real entre regra local e orquestração deixa de ser exercitado.

### 4. No cenário saldo insuficiente, além de assert de falha de negócio, convém:
   - A) Confirmar que notificação foi enviada com status de tentativa negada.
   - B) Verificar que débito **não** foi invocado — a operação deve parar antes da cobrança.
   - C) Mockar a regra pura para forçar custo zero e simplificar o assert final.
   - D) Esperar exceção genérica em vez de retorno estruturado com flag de erro.

### 5. Quando o contrato exige e-mail ou evento após sucesso, o assert em mock deve:
   - A) Usar `assert_called_once_with` (ou equivalente) validando destino e payload esperados.
   - B) Checar apenas `mock.called` — presença de chamada prova o efeito esperado.
   - C) Ignorar argumentos se o mock retornou valor truthy na configuração do teste.
   - D) Substituir assert de mock por snapshot de log capturado em arquivo temporário.

### 6. Suíte verde no CI mas com `assert resultado is not None`:
   - A) Pode dar falsa segurança — a linha executou, mas o contrato de negócio não foi provado.
   - B) Indica qualidade suficiente se o percentual de cobertura global superar 80%.
   - C) Falha no pytest por configuração padrão que exige asserts numéricos explícitos.
   - D) É aceitável em PR porque o CI verde substitui revisão humana de asserts.

### 7. `except Exception: pass` em teste de erro é problemático porque:
   - A) pytest proíbe blocos except em testes unitários desde a versão 8.
   - B) O teste fica vermelho no CI mesmo quando o código lança a exceção correta.
   - C) O teste só falha se a exceção for do tipo ValueError, nunca com Exception.
   - D) O teste permanece verde mesmo se o código **deixar** de lançar erro.

### 8. Para exceção esperada em output gerado por IA, a correção idiomática é:
   - A) Manter try/except com `assert True` no bloco except por legibilidade.
   - B) Remover o teste — exceções não são determinísticas o suficiente para unitário.
   - C) Substituir por `pytest.raises` com tipo e, quando couber, `match` na mensagem.
   - D) Converter o cenário em teste de integração com banco real e revert no teardown.

### 9. Fluxo manter / revisar / rejeitar ao avaliar testes gerados:
   - A) Rejeitar tudo e pedir nova geração completa antes de qualquer pytest local.
   - B) Classificar cada teste na rubrica e corrigir primeiro os anti-padrões de maior risco.
   - C) Manter tudo que passa no CI; revisar só falhas intermitentes ou flakes.
   - D) Revisar apenas nomes de função; asserts fracos podem ser tratados em sprint futura.

### 10. Qual frase resume melhor **mocking + avaliação** com IA neste trecho do módulo?
   - A) Mockar toda importação garante qualidade; testes verdes da IA entram sem review.
   - B) Avaliar testes gerados limita-se a contar quantidade de funções `test_*` adicionadas.
   - C) Patch na definição sempre intercepta; asserts triviais bastam se a cobertura subir.
   - D) Mock isola fronteira no caminho de uso; avaliar se asserts provam contrato antes do merge.

---

## 🔑 Gabarito comentado

### 1. Resposta: C
**Justificativa:** O patch deve apontar para onde o nome está **ligado** no código sob teste — armadilha clássica da aula de mocking.

### 2. Resposta: A
**Justificativa:** Mock isola **fronteiras** (I/O, remoto); regra pura local continua real e testável separadamente.

### 3. Resposta: D
**Justificativa:** Mockar regra pura no fluxo de orquestração corta a integração local que o teste deveria exercitar.

### 4. Resposta: B
**Justificativa:** Falha antes do débito — provar que colaborador de cobrança **não** foi chamado é parte do contrato.

### 5. Resposta: A
**Justificativa:** `called` sozinho não prova parâmetros; contratos de notificação pedem assert explícito na chamada.

### 6. Resposta: A
**Justificativa:** Verde no CI ≠ prova — tema central da avaliação de testes gerados.

### 7. Resposta: D
**Justificativa:** `pass` engole a falha — teste continua verde se o erro deixar de existir (falsa segurança).

### 8. Resposta: C
**Justificativa:** Substitui try/except frágil por padrão idiomático com tipo e mensagem quando aplicável.

### 9. Resposta: B
**Justificativa:** Rubrica + priorização de risco — manter/revisar/rejeitar com correções focadas, não descarte cego nem aceite cego.

### 10. Resposta: D
**Justificativa:** Integra os dois temas: patch no uso + julgamento de qualidade antes de merge.
