# Checklist — exercício integrador de testes assistidos

Marque `[x]` conforme concluir. Rode `python verificar_checklist.py` para checagens automáticas.

## Antes de começar

- [ ] Li `exercicio.md` e o mapa de temas
- [ ] `pytest -q` verde no baseline inicial
- [ ] **Não alterei** arquivos de produção (`regras_fidelidade.py`, `integracoes_fidelidade.py`, `fidelidade_service.py`)

## Papel dos testes unitários

- [ ] Regras puras testadas **sem** mock (`pontos_por_compra`, `custo_premio`, `pode_resgatar`)
- [ ] Orquestração testada separadamente (`acumular_compra`, `resgatar_premio`)

## Estrutura de qualidade

- [ ] Nomes descritivos; AAA legível; um comportamento por teste

## Geração consciente com IA

- [ ] Pedi lacunas priorizadas à IA antes de gerar código
- [ ] Implementei em rodadas pequenas (não volume cego)

## Sucesso e erro

- [ ] Cenários de sucesso com asserts de contrato
- [ ] Erro por **exceção** (`pytest.raises`) e por **retorno** (`ok False`)

## Mocking na fronteira

- [ ] `@patch` em `fidelidade_service.*`, não em `integracoes_fidelidade.*`
- [ ] Colaborador não invocado quando o fluxo deve parar antes (ex.: débito)

## Avaliação de testes gerados

- [ ] Classifiquei testes gerados: manter / revisar / rejeitar
- [ ] Removi ou corrigi anti-padrões da suíte inicial

## Falsos positivos

- [ ] `python simular_regressao.py` sem lacunas
- [ ] Sem `is not None`, `assert True`, `except: pass`

## Boas práticas integradas

- [ ] `python verificar_testes.py` sem pendências
- [ ] Self-review do diff como PR

## Entrega

- [ ] `pytest -q` verde
- [ ] `python verificar_entrega.py` retorna **0**
- [ ] Nota de entrega em 4 linhas (PR ou `entrega.md` opcional)
