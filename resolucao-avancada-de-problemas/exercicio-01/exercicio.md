# Exercício - Operação resgate

## Contexto

Uma ingestão de dados de parceiros externos começou a falhar em produção após mudança de formato no payload JSON. O sintoma principal observado no monitoramento é `KeyError: 'id'`.

Seu papel é liderar a operação de resgate aplicando as competências treinadas: leitura de erro, formulação de hipóteses, validação com testes, correção mínima, revisão de regressão e documentação do aprendizado.

## Estrutura do exercício

- `pre-changes/`: ambiente de trabalho do aluno (código quebrado + testes de contrato).

## Objetivo técnico

Fazer `ingest_raw_json()` e `map_record_to_internal()` aceitarem os formatos válidos de entrada e falharem de forma clara para payload inválido, sem quebrar assinatura pública das funções.

## Regras do desafio

1. Trabalhe apenas dentro de `pre-changes/`.
2. Não mude nomes públicos de funções já usadas (`ingest_raw_json`, `map_record_to_internal`).
3. Evite solução "gigante": prefira correção mínima com responsabilidade bem definida.
4. Todo ajuste deve ser sustentado por evidência (teste automatizado ou reprodução objetiva).
5. Ao final, registre em poucas linhas:
   - o que falhava;
   - o que foi alterado;
   - como validou;
   - risco residual.

## Critérios de aceite

- Casos válidos devem produzir `internal_id` sem erro:
  - `id` no root;
  - `record.recordId`;
  - `data.id`;
  - `items[0].id`.
- Caso inválido (sem `id` e sem `recordId`) deve falhar com erro explícito e estável.
- Testes em `pre-changes/` passando.

## Execução sugerida (ao vivo)

1. Rodar `python example.py` para ver o comportamento atual.
2. Rodar `pytest -q` para mapear falhas.
3. Levantar hipóteses antes de codar.
4. Aplicar correção mínima.
5. Rodar testes novamente.
6. Documentar aprendizado técnico da operação de resgate.

## Comandos úteis

```bash
cd pre-changes
python example.py
pytest -q
```
