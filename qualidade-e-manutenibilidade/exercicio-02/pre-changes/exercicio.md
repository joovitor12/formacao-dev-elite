# Exercício integrador — Programa Fidelidade (testes assistidos)

## Contexto

O time recebeu um **programa de fidelidade** já implementado (`regras_fidelidade.py`, `integracoes_fidelidade.py`, `fidelidade_service.py`) e uma suíte inicial gerada por IA: **pytest verde**, mas com lacunas de qualidade, mocks ausentes e **falsos positivos**.

Sua missão é construir uma **suíte de testes unitários de qualidade assistida por IA** — **sem alterar o código de produção**.

## Estrutura do repositório

| Caminho | Quem usa | Papel |
|---------|----------|--------|
| **Raiz** (`exercicio-02/`) | **Facilitador** — demo ao vivo | Baseline igual ao dos alunos. |
| **`pre-changes/`** | **Alunos** | Ambiente de trabalho — **mesmo baseline** da raiz. |

Raiz e `pre-changes/` começam **iguais** (produção + suíte mínima com anti-padrões).

## Onde trabalhar

- **Alunos:** `pre-changes/`.
- **Facilitador:** **raiz** (ou `pre-changes/` se preferir o mesmo caminho nos comandos).

## Objetivo técnico

Evoluir `test_programa_fidelidade.py` até atender os **critérios de aceite**, aplicando os temas do bloco de testes assistidos por IA.

## Mapa do percurso (temas)

| Fase | Tema | Foco | Evidência |
|------|------|------|-----------|
| 1 | Papel dos testes unitários | Regra pura vs orquestração | Testes diretos em `regras_fidelidade` sem mock |
| 2 | Estrutura de qualidade | AAA, nomes descritivos | Um comportamento por teste |
| 3 | Geração consciente | Lacunas antes de código | Rodadas pequenas com IA |
| 4 | Sucesso e erro | Contratos distintos | `pytest.raises` + retorno `ok False` |
| 5 | Mocking assistido | Fronteira de I/O | `@patch` em `fidelidade_service.*` |
| 6 | Avaliar testes gerados | Crítica antes do merge | manter / revisar / rejeitar |
| 7 | Falsos positivos | Prova de regressão | `python simular_regressao.py` limpo |
| 8 | Boas práticas | Checklist integrado | `python verificar_testes.py` + checklist |

Use Copilot (ou agente com `@workspace`) como **planejador, gerador parcial e revisor** — não como “gere 50 testes”.

## Regras

1. **Não altere** `regras_fidelidade.py`, `integracoes_fidelidade.py` nem `fidelidade_service.py`.
2. Um **incremento** por vez → `pytest -q` → depois verificadores.
3. Toda melhoria deve **aumentar prova de contrato**, não só contagem de testes.
4. Alunos permanecem em `pre-changes/`; facilitador demonstra na **raiz** (código inicial idêntico).

## Critérios de aceite (entrega)

- [ ] `pytest -q` verde na pasta de trabalho.
- [ ] `python verificar_testes.py` sem pendências.
- [ ] `python simular_regressao.py` sem lacunas.
- [ ] `checklist_testes_integrador.md` com todos os itens `[x]`.
- [ ] `python verificar_entrega.py` retorna **0**.
- [ ] Nota de entrega em 4 linhas (PR ou `entrega.md` opcional).

## Roteiro sugerido (apresentação ao vivo)

1. `pytest -q` — baseline verde.
2. `python simular_regressao.py` — mostrar lacunas.
3. IA: mapa de lacunas **sem código**.
4. Rodadas: regra pura → mock sucesso → erros retorno/exceção.
5. IA revisor + eliminar falsos positivos.
6. Checklist + `python verificar_entrega.py`.

## Comandos úteis

**Facilitador (raiz):**

```bash
cd exercicio-02
pytest -q
python simular_regressao.py
python verificar_testes.py
python verificar_entrega.py
python example.py
```

**Alunos:**

```bash
cd exercicio-02/pre-changes
pytest -q
python simular_regressao.py
python verificar_testes.py
python verificar_entrega.py
python example.py
```

## Dica para facilitadores

Comece na **raiz** com o mesmo baseline dos alunos. Ao evoluir a suíte ao vivo, eles replicam em `pre-changes/`. O critério de pronto é o verificador + checklist, não um gabarito separado no repositório.
