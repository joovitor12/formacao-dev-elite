# Guia — Gerando testes com IA e cobertura

## Skills recomendadas (instalar antes da aula)

```bash
npx skills add https://github.com/github/awesome-copilot --skill pytest-coverage
npx skills add https://github.com/wshobson/agents --skill python-testing-patterns
```

- **pytest-coverage** — interpretar relatório, priorizar linhas faltantes, evitar cobertura vazia.
- **python-testing-patterns** — padrões pytest (fixtures, parametrize, `pytest.raises`, AAA).

Referência da skill de padrões: [python-testing-patterns — wshobson/agents](https://www.skills.sh/wshobson/agents/python-testing-patterns)

## Dependências Python

```bash
pip install -r requirements-dev.txt
```

## Onde trabalhar

| Ambiente | Quem |
|----------|------|
| **Raiz** (`aula-11/`) | Facilitador — demo ao vivo |
| **`pre-changes/`** | Alunos |

Os dois ambientes começam **iguais**: suíte parcial + cobertura baixa (~36%).

## Fluxo sugerido

1. `pytest -q` — baseline verde (poucos testes).
2. `python verificar_cobertura.py` — ver **linhas faltantes**.
3. IA + skills — propor **1–3 testes** de alto valor (não dezenas).
4. Implementar → `pytest -q` → `python verificar_cobertura.py` de novo.
5. Revisar: assert concreto? estrutura AAA? cobertura subiu com propósito?

## Anti-padrão

- Gerar teste só porque a linha está vermelha no coverage, sem assert de regra de negócio.
- Meta numérica de 100% sem critério de risco.
