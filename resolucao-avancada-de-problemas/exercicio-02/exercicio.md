# Exercício - Otimização de Elite

## Contexto

Um pipeline interno agrega pontos por usuário a partir de uma lista de eventos em memória. Em volumes maiores, o tempo de execução ultrapassa o orçamento aceitável e começa a afetar jobs em fila. O código atual foi escrito com foco em “funcionar primeiro”; agora é preciso **reduzir custo de processamento** sem alterar o significado do resultado.

## Estrutura do exercício

- `pre-changes/`: ambiente de trabalho (baseline lento + testes de corretude e de orçamento de operações).

## Objetivo técnico

Manter a função pública `summarize_points_by_user` com a **mesma assinatura** e o **mesmo significado** da saída:

- dicionário `user_id -> soma dos pontos`;
- segundo valor da tupla: **contagem de operações** dominantes no laço (para você medir impacto).

Redesenhar o interior para que o custo seja **linear no número de eventos**, não quadrático no pior caso atual.

## Competências que você vai exercitar

- Formular **o que** otimizar e **como medir** antes de codar no escuro.
- Localizar **onde nasce o custo extra** na versão atual.
- **Reescrever** o algoritmo com mudança pequena e reversível.
- Pensar **trade-off** (memória extra vs menos trabalho repetido, neste caso um mapa de acúmulo).
- Validar com **testes de corretude** e **orçamento de operações** como rede de segurança.
- Ao terminar, **registrar em poucas linhas** decisão, evidência e risco residual (para outra pessoa entender sem estar na sala).

## Regras do desafio

1. Trabalhe apenas dentro de `pre-changes/` (salvo instrução contrária do instrutor).
2. Não renomeie `summarize_points_by_user` nem altere o formato `(dict, int)` retornado.
3. Prefira uma **única passagem** sobre `events` para acumular totais (pista forte).
4. Cada mudança deve ser **justificável** com os testes ou com contagem de operações antes/depois.
5. Ao final, documente em texto curto (nota para o time ou descrição do PR interno):
  - onde estava o gargalo;
  - qual estrutura você escolheu e por quê;
  - como os testes passando sustentam merge.

## Critérios de aceite

- `pytest -q` dentro de `pre-changes/` **verde**.
- `test_metrics_budget.py` deve refletir custo **proporcional a `len(events)`**, não ao produto “usuários × eventos” da versão inicial.
- Corretude preservada nos cenários dos testes (incluindo usuários sem eventos não aparecendo no mapa).

## Execução sugerida

1. `python example.py` para ver baseline de operações vs tamanho da lista.
2. `pytest -q` para ver qual assert falha primeiro.
3. Inspecionar `metrics.py` e anotar onde o trabalho se repete.
4. Reescrever com acúmulo em mapa (ou estratégia equivalente **linear nos eventos**).
5. Repetir testes até verde.
6. Registrar decisão e métrica de operações (antes/depois em um tamanho fixo de exemplo).

## Comandos úteis

```bash
cd pre-changes
python example.py
pytest -q
```

