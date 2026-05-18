# Aula 07 — Avaliação antes vs depois

**Objetivo:** medir e comparar **comportamento** e **métricas estruturais** após uma refatoração, usando snapshots “antes” e relatório objetivo — com IA ajudando a **interpretar** o delta, não para substituir a evidência.

**Ferramenta:** GitHub Copilot Chat / Explorer (ou agente equivalente com `@workspace`).

**Material sugerido:**

| Caminho | Papel |
| -------- | ------ |
| `pre-changes/` | Ambiente de trabalho: refatore `cobranca_service.py` e reavalie. |
| `snapshots/antes_*.json` | Linha de base congelada (comportamento + métricas do “antes”). |
| `relatorio_antes_depois.py` | Relatório no terminal: métricas e paridade de comportamento. |
| `test_comportamento_snapshot_antes.py` | Teste que falha se o comportamento divergir do snapshot. |
| `gerar_snapshots_antes.py` | Só para instrutor — regenerar snapshots se o baseline mudar. |

**Como usar:** em `pre-changes/`, rode `pytest -q` e `python relatorio_antes_depois.py` **antes** de refatorar (deve estar verde e sem divergência). Refatore em passos pequenos; após cada passo, rode de novo o relatório e os testes.

---

## 1. Definir o que entra na avaliação

```
@pre-changes/relatorio_antes_depois.py @pre-changes/metricas_codigo.py @pre-changes/snapshot_comportamento.py

O que este exercício compara entre “antes” e “depois”?

Separe em duas colunas:
- o que é **comportamento** (não pode mudar sem justificativa);
- o que é **métrica estrutural** (pode melhorar ou piorar — e o que significa cada uma aqui).

Não escreva código.
```

---

## 2. Ler o relatório antes de refatorar

```
Acabei de rodar em pre-changes/:
  pytest -q
  python relatorio_antes_depois.py

Explique o que espero ver quando ainda NÃO refatorei nada (baseline = depois).

@pre-changes/snapshots/antes_metricas.json @pre-changes/snapshots/antes_comportamento.json
```

---

## 3. Plano de refatoração com critério de sucesso

```
@pre-changes/cobranca_service.py @pre-changes/test_cobranca_characterization.py

Proponha 3 incrementos de refatoração (um por vez), cada um com:
- smell atacado;
- métrica que você espera melhorar (loc, funções ou ramos);
- como validar (pytest + relatorio_antes_depois.py).

Não implemente ainda.
```

---

## 4. Aplicar um incremento e reavaliar

```
Implemente APENAS o incremento 1 em pre-changes/cobranca_service.py.

Depois descreva como interpretar a saída de:
  python relatorio_antes_depois.py

Regras: comportamento deve permanecer OK; métricas podem mudar.

@pre-changes/cobranca_service.py @pre-changes/relatorio_antes_depois.py
```

---

## 5. IA interpreta o delta (sem vender ilusão)

```
Cole aqui a saída do relatorio_antes_depois.py após sua refatoração.

@pre-changes/

Responda:
1) O comportamento permaneceu equivalente ao snapshot? Como você sabe?
2) Quais métricas melhoraram e quais pioraram? Isso é aceitável neste passo?
3) Há algum ganho “só nas métricas” que não vale o risco do diff?

Tom: parecer técnico de PR, não marketing.
```

## Comandos úteis

```bash
cd pre-changes
pytest -q
python relatorio_antes_depois.py
python example.py
```

---

## Máxima da aula

**Antes vs depois só vale com duas trilhas:** comportamento amarrado ao snapshot e métricas lidas com contexto — a IA explica o relatório; ela não é o relatório.
