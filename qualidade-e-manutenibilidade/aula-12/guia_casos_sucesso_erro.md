# Guia — Casos de sucesso e erro

Use ao ampliar `test_regras_resgate.py` com apoio da IA.

## Matriz de cenários (`regras_resgate.py`)

| Tipo | Entrada / condição | Resultado esperado |
|------|-------------------|-------------------|
| **Sucesso** | Código válido + saldo > custo | `ok: True`, `saldo_restante` correto |
| **Sucesso (borda)** | Saldo **igual** ao custo | `ok: True`, `saldo_restante: 0` |
| **Erro (exceção)** | Código vazio | `ValueError("codigo obrigatorio")` |
| **Erro (exceção)** | Código inexistente | `ValueError("codigo invalido")` |
| **Erro (exceção)** | Saldo negativo | `ValueError("saldo invalido")` |
| **Erro (retorno)** | Saldo válido mas < custo | `ok: False`, `erro: "saldo insuficiente"` |

## Como testar cada tipo

| Tipo | Ferramenta pytest |
|------|-------------------|
| Sucesso | `assert resultado["ok"] is True` + campos concretos |
| Erro com exceção | `with pytest.raises(ValueError, match="..."):` |
| Erro com retorno | `assert resultado["ok"] is False` + mensagem/código |

## Perguntas-guia para a IA

1. Quais linhas de `regras_resgate.py` só executam em **erro**?
2. Para cada erro, o contrato é **exceção** ou **dict com ok False**?
3. Qual caso de erro tem **maior risco** se ficar sem teste?

## Anti-padrão

- Só testar happy path e assumir que erro “nunca acontece”.
- Usar o mesmo assert genérico para exceção e para retorno de falha.
