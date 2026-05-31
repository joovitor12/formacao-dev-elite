# Guia — Ajustando falsos positivos

Use quando pytest está **verde**, mas testes **não pegam regressão** (falso positivo de confiança).

## Skill recomendada

```bash
npx skills add https://github.com/wshobson/agents --skill python-testing-patterns
```

## Falso positivo vs falso negativo (neste módulo)

| Termo | O que significa aqui |
|-------|----------------------|
| **Falso positivo (confiança)** | Teste **passa** mesmo com comportamento errado — CI verde engana. |
| **Falso negativo** | Teste **falha** com código correto — ruído, flakiness ou assert errado. |

Esta aula foca em **corrigir testes que passam demais**.

## Sinais comuns em output de IA

| Padrão | Por que gera falso positivo |
|--------|----------------------------|
| Só `assert ok is True` | Valor, percentual ou mensagem podem regredir invisíveis. |
| `except Exception: pass` | Passa se código retorna erro estruturado **sem** exceção. |
| `try/except` + `assert True` | Prova que exceção ocorreu, mas não o contrato completo. |
| Assert parcial (só `%`) | Metade certa, valor final errado continua verde. |

## Fluxo sugerido

1. `pytest -q` — confirmar verde (ponto de partida).
2. `python simular_regressao.py` — ver cenários que **ainda passariam** com bug.
3. `python verificar_falsos_positivos.py` — checklist consolidado.
4. IA + guia — priorizar teste com maior lacuna.
5. Ajustar assert/contrato → rodar simulador até lacunas zerarem.

## Perguntas-guia para a IA

1. Se `valor_reembolso` voltasse errado, qual teste **continuaria verde**?
2. `test_prazo_expirado_rejeita` prova o quê hoje? O que deveria provar?
3. Qual teste da suíte serve de **modelo** de assert completo?
4. Qual ajuste mínimo dá **maior** ganho na detecção de regressão?

## Anti-padrão ao “corrigir”

- Adicionar `assert True` no final para “garantir verde”.
- Endurecer mock até o teste provar só o mock, não o contrato.
- Desabilitar teste flake com skip permanente sem investigar causa.

## Critério de pronto

- `pytest -q` verde.
- `python simular_regressao.py` sem lacunas pendentes.
- Testes frágeis revisados passam a falhar quando simulador injeta regressão.
