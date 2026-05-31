# Guia — Mocking assistido por IA

Use ao testar `executar_resgate` com apoio da IA, sem acoplar testes a APIs reais.

## Skill recomendada

```bash
npx skills add https://github.com/wshobson/agents --skill python-testing-patterns
```

A skill cobre padrões pytest, incluindo **onde aplicar `unittest.mock.patch`** e asserts em colaboradores.

## O que mockar vs o que não mockar

| Mockar | Não mockar |
|--------|------------|
| `consultar_saldo`, `debitar_pontos`, `enviar_confirmacao` em `integracoes.py` | `custo_resgate` em `regras_catalogo.py` (regra pura) |
| Fronteiras de I/O / serviços remotos | Lógica local já testável sem colaborador |

## Onde aplicar o patch

Patch no **módulo que usa** a dependência, não onde ela é definida:

```python
@patch("resgate_service.consultar_saldo", return_value=120)
@patch("resgate_service.debitar_pontos", return_value=True)
@patch("resgate_service.enviar_confirmacao")
def test_executar_resgate_sucesso(...):
    ...
```

Se patchar `integracoes.consultar_saldo` enquanto `resgate_service` já importou o nome, o mock **não intercepta** a chamada.

## Matriz de cenários (`executar_resgate`)

| Cenário | Mocks sugeridos | Assert principal |
|---------|-----------------|------------------|
| **Sucesso** | saldo ≥ custo; debitar `True`; notificação ok | `ok True`, `saldo_restante`; notificação chamada 1× |
| **Saldo insuficiente** | saldo < custo | `ok False`, erro; **debitar não deve ser chamado** |
| **Falha ao debitar** | saldo ok; debitar `False` | `ok False`, `"falha ao debitar"`; notificação **não** enviada |
| **Código inválido** | nenhum mock de porta necessário | `pytest.raises(ValueError)` antes de I/O |

## Perguntas-guia para a IA

1. Quais funções em `resgate_service.py` são **colaboradores externos**?
2. O patch deve apontar para qual **caminho de import**?
3. Em saldo insuficiente, quais mocks **não** devem ser invocados?
4. Como provar que `enviar_confirmacao` foi chamada com os argumentos certos?

## Anti-padrões

- Mockar `custo_resgate` — você deixa de testar a integração local real do serviço.
- Patch no módulo errado (`integracoes.*` em vez de `resgate_service.*`).
- Mock genérico sem `assert_called_once_with` quando o contrato exige notificação.
- Teste que só verifica `mock.called` sem checar argumentos ou efeito de negócio.
