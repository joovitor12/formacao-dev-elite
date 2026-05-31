# Guia — Avaliando testes gerados por IA

Use ao revisar `test_campanha_desconto.py` **antes** de aceitar código no repositório.

## Skill recomendada

```bash
npx skills add https://github.com/wshobson/agents --skill python-testing-patterns
```

## Critérios de avaliação (rubrica)

| Dimensão | Pergunta | Sinal verde | Sinal vermelho |
|----------|----------|-------------|----------------|
| **Assert** | Prova contrato de negócio? | Valores/campos concretos | `is not None`, `assert True` |
| **Foco** | Um comportamento por teste? | Nome + corpo alinhados | Vários comportamentos no mesmo teste |
| **Erro** | Exceção testada corretamente? | `pytest.raises` + `match` | `try/except` genérico ou `pass` |
| **Nome** | Nome descreve cenário real? | `test_desconto_vip_soma_bonus` | Nome diz “erro” mas testa sucesso |
| **Duplicação** | Repete cenário sem valor? | Casos distintos com propósito | Cópia mecânica com assert fraco |
| **PR** | Aceitaria no review? | Falha clara se regredir | Verde no CI mas falsa segurança |

## Fluxo sugerido

1. `pytest -q` — confirmar verde (não confundir verde com qualidade).
2. `python verificar_avaliacao.py` — anti-padrões ainda presentes.
3. IA + rubrica — classificar cada teste: **manter / revisar / rejeitar**.
4. Corrigir **prioridade alta** (assert fraco, exceção engolida).
5. Registrar em `avaliacao_registro.md` → rodar verificador de novo.

## Perguntas-guia para a IA

1. Quais testes passam no CI mas **não provam** regra de negócio?
2. Onde o nome do teste **engana** sobre o cenário?
3. Qual teste você **manteria** como modelo e por quê?
4. Qual correção mínima daria **maior ganho** de confiança?

## Anti-padrões comuns em output de IA

- Inflar suite com asserts triviais após pedir “mais cobertura”.
- `try/except` com `assert True` em vez de `pytest.raises`.
- `except Exception: pass` — teste verde mesmo se o código parar de lançar erro.
- Misturar validação de cupom e cálculo no mesmo teste “para economizar linhas”.

## Decisão final

Para cada teste gerado, escolha explicitamente:

- **Manter** — já atende rubrica; no máximo ajuste cosmético.
- **Revisar** — ideia correta; assert, nome ou estrutura precisam mudar.
- **Rejeitar** — não agrega prova; substituir por caso novo bem escrito.
