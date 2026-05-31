# Checklist — testes assistidos por IA

Marque `[x]` conforme concluir. Rode `python verificar_boas_praticas.py` para checagens automáticas.

## Antes de pedir testes à IA

- [ ] Rodei `pytest -q` na pasta de trabalho
- [ ] Li `guia_boas_praticas_testes_ia.md`
- [ ] Pedi **lacunas priorizadas** antes de gerar código
- [ ] Defini escopo: não alterar arquivos de produção nesta aula

## Geração consciente

- [ ] No máximo poucos testes por rodada (não volume)
- [ ] Cobri regra pura **sem** mock
- [ ] Cobri sucesso de orquestração **com** mock no caminho `ativacao_service.*`
- [ ] Cobri erro por **exceção** (`pytest.raises`) e por **retorno** (`ok False`)

## Qualidade e revisão

- [ ] Nomes descritivos; um comportamento por teste
- [ ] Sem `is not None`, `assert True` ou `except: pass`
- [ ] Mocks com assert de chamada quando o contrato exige efeito (recibo)
- [ ] Revisei output da IA: manter / revisar / rejeitar por teste
- [ ] Self-review do diff como se fosse PR de colega

## Entrega

- [ ] `pytest -q` verde
- [ ] `python verificar_boas_praticas.py` sem pendências críticas
- [ ] Descrevi em 3 linhas: lacunas fechadas, risco residual, o que não testei de propósito
