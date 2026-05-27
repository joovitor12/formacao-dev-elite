# Exercício integrador — Operação Fulfillment legado

## Contexto

O time de operações depende de um único módulo Python que processa pedidos de fulfillment (validação, taxa de canal, cupom, estoque, persistência e notificação). O código **funciona hoje**, mas ninguém quer mexer: medo de regressão, função longa, estado global e `print` espalhado.

Sua missão é uma **refatoração profissional assistida por IA**: melhorar estrutura e manutenibilidade **sem mudar o comportamento coberto pelos testes**.

## Estrutura do repositório

| Pasta / raiz | Quem usa | Papel |
|--------------|----------|--------|
| **Raiz** (`exercicio-01/`) | **Facilitador / gabarito** | Solução de referência já refatorada (`solucao.md` resume o raciocínio). |
| **`pre-changes/`** | **Alunos** (e demo ao vivo) | Baseline monolítico + testes + checklist — **único lugar para trabalhar**. |

Não edite `fulfillment_baseline.py` (referência congelada de comportamento).

## Onde trabalhar

- **Alunos:** somente `pre-changes/`.
- **Facilitador (ao vivo):** também em `pre-changes/`, na mesma ordem do roteiro — a **raiz** serve para comparar ou mostrar o resultado esperado ao final (não como ponto de partida da aula).

## Objetivo técnico

Evoluir `pre-changes/fulfillment_flow.py` até atender os **critérios de aceite**, em passos pequenos, com evidência em cada fase.

## Mapa do percurso (conceitos do módulo)

| Fase | Foco | Evidência esperada |
|------|------|-------------------|
| 1 — Diagnóstico | Legado, medo de mudar, *code smells*, efeitos colaterais | Notas curtas (riscos + smells) antes de codar |
| 2 — Rede de segurança | Refatoração segura | `pytest -q` verde **antes** da primeira linha alterada |
| 3 — Incremento + SRP | Um passo por vez; extrair responsabilidades | Módulos/funções menores; fachada `processar_fulfillment` preservada |
| 4 — Equivalência | Baseline + matriz de casos | `test_equivalencia_funcional.py` verde |
| 5 — Antes vs depois | Métricas + comportamento | `python relatorio_antes_depois.py` com comportamento OK |
| 6 — Checklist + entrega | Disciplina de PR | `checklist_refatoracao.md` completo + `python verificar_entrega.py` |

Use Copilot (ou agente com `@workspace`) como **auditor, revisor e parceiro de passos** — não como “refatore tudo”.

## Regras

1. Trabalhe **somente** em `pre-changes/` (alunos e demonstração ao vivo).
2. **Não altere** a assinatura nem o contrato de `processar_fulfillment` / `listar_fulfillments`.
3. **Não altere** `fulfillment_baseline.py`.
4. **Não copie** os módulos da raiz para `pre-changes/` antes de concluir o exercício.
5. Um **incremento** por vez → `pytest -q` → só então o próximo.
6. Toda afirmação de “continua igual” deve apontar para **teste, snapshot ou relatório**.

## Critérios de aceite (entrega)

- [ ] `pytest -q` verde em `pre-changes/`.
- [ ] `test_equivalencia_funcional.py` verde.
- [ ] `python relatorio_antes_depois.py` — comportamento **OK**.
- [ ] `checklist_refatoracao.md` com todos os itens `[x]`.
- [ ] `python verificar_entrega.py` retorna **0**.
- [ ] Pelo menos **duas** responsabilidades em arquivos separados.
- [ ] Nota de entrega em 4 linhas (PR ou `entrega.md` opcional).

## Roteiro sugerido (apresentação ao vivo)

1. `cd pre-changes && pytest -q` — baseline verde.
2. IA: diagnóstico **sem patch**.
3. IA: plano de 4–6 incrementos.
4. Incrementos com testes entre cada um.
5. `python relatorio_antes_depois.py`.
6. Checklist + `python verificar_entrega.py`.
7. (Opcional) Comparar com a solução na **raiz** do exercício.

## Comandos úteis

```bash
cd exercicio-01/pre-changes
pytest -q
python relatorio_antes_depois.py
python verificar_entrega.py
python example.py
```

**Conferir gabarito (facilitador, pós-aula):**

```bash
cd exercicio-01
pytest -q
python verificar_entrega.py
# ver também solucao.md
```

## Dica para facilitadores

Resolva **em `pre-changes/`** para os alunos acompanharem o mesmo caminho. Use a **raiz** só como referência final ou para code review comparativo — evite começar a aula já com os módulos extraídos na raiz visíveis demais no compartilhamento de tela, se quiser preservar o desafio.
