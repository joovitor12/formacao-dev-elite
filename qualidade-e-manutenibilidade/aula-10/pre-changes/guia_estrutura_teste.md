# Guia — Estrutura de um teste de qualidade

Use ao reescrever `test_regras_envio.py` em `pre-changes/`.

## Checklist

| Critério | Pergunta-guia |
|----------|----------------|
| **Nome** | Alguém entende o comportamento só lendo `test_*`? |
| **AAA** | Arrange (dado), Act (ação), Assert (verificação) estão separados? |
| **Foco** | Um comportamento principal por teste? |
| **Legibilidade** | Constantes ou nomes evitam “número mágico”? |
| **Assert idiomatico** | Erros esperados usam `pytest.raises`, não `try/except`? |
| **Independência** | O teste roda sozinho, em qualquer ordem? |

## Padrão AAA (mínimo)

```python
def test_tarifa_base_peso_leve_retorna_valor_fixo() -> None:
    peso = 3.0                          # Arrange

    resultado = tarifa_base_por_peso(peso)  # Act

    assert resultado == 18.0            # Assert
```

## Anti-padrões neste exercício

- `test_1`, `test_frete`, `test_erro` — nomes genéricos
- Vários comportamentos no mesmo teste
- `try/except` manual para exceção
- Misturar cálculo de peso, região e expresso num único caso

## Meta em pre-changes/

Reescrever os testes fracos mantendo **os mesmos comportamentos verificados** (pytest verde antes e depois).
