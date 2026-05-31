# Checklist — exercício integrador de testes assistidos

Marque `[x]` conforme concluir. Rode `python verificar_checklist.py` para checagens automáticas.

## Antes de começar

- [x] Li `exercicio.md` e o mapa de temas
- [x] `pytest -q` verde no baseline inicial
- [x] **Não alterei** arquivos de produção (`regras_fidelidade.py`, `integracoes_fidelidade.py`, `fidelidade_service.py`)

## Papel dos testes unitários

- [x] Regras puras testadas **sem** mock (`pontos_por_compra`, `custo_premio`, `pode_resgatar`)
- [x] Orquestração testada separadamente (`acumular_compra`, `resgatar_premio`)

## Estrutura de qualidade

- [x] Nomes descritivos; AAA legível; um comportamento por teste

## Geração consciente com IA

- [x] Pedi lacunas priorizadas à IA antes de gerar código
- [x] Implementei em rodadas pequenas (não volume cego)

## Sucesso e erro

- [x] Cenários de sucesso com asserts de contrato
- [x] Erro por **exceção** (`pytest.raises`) e por **retorno** (`ok False`)

## Mocking na fronteira

- [x] `@patch` em `fidelidade_service.*`, não em `integracoes_fidelidade.*`
- [x] Colaborador não invocado quando o fluxo deve parar antes (ex.: débito)

## Avaliação de testes gerados

- [x] Classifiquei testes gerados: manter / revisar / rejeitar
- [x] Removi ou corrigi anti-padrões da suíte inicial

## Falsos positivos

- [x] `python simular_regressao.py` sem lacunas
- [x] Sem `is not None`, `assert True`, `except: pass`

## Boas práticas integradas

- [x] `python verificar_testes.py` sem pendências
- [x] Self-review do diff como PR

## Entrega

- [x] `pytest -q` verde
- [x] `python verificar_entrega.py` retorna **0**
- [x] Nota de entrega em 4 linhas (PR ou `entrega.md` opcional)
