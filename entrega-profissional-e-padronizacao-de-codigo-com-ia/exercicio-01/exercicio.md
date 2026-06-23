# Exercício integrador — Entrega profissional com IA

## Contexto

O time mantém três módulos Python no fluxo de entrega (`notificacao_entrega.py`, `confirmacao_entrega.py`, `fechamento_entrega.py`) e um portão de qualidade (`verificar_pipeline.py` + workflow em `ci/`).

O **baseline** executa smoke tests, mas concentra desvios de **padrão documentado**, **lint**, **formatação automática** e **integração ao pipeline**.

Sua missão é percorrer o **ciclo completo** com IA como parceira — código conforme `padrao_codigo.md`, portões locais verdes e CI espelhando o mesmo job.

## Estrutura


| Caminho                    | Quem usa        | Papel                                                  |
| -------------------------- | --------------- | ------------------------------------------------------ |
| **Raiz** (`exercicio-01/`) | **Facilitador** | Mesmo baseline no início; referência ao final da demo. |
| `**pre-changes/`**         | **Alunos**      | Cópia idêntica — **único lugar para trabalhar**.       |


## Onde trabalhar

- **Alunos:** somente `pre-changes/`.
- **Facilitador:** demonstra na **raiz** no mesmo roteiro.

## Mapa do percurso (temas do módulo)


| Fase | Tema                     | Evidência esperada                                              |
| ---- | ------------------------ | --------------------------------------------------------------- |
| 1    | Padrão de código         | Auditoria vs `padrao_codigo.md` → dossiê §1                     |
| 2    | Linting assistido por IA | `ruff check` + triagem + patch → dossiê §2                      |
| 3    | Formatação automática    | `ruff format --check` / `--diff` → dossiê §3                    |
| 4    | Integração ao pipeline   | `verificar_pipeline.py` + `ci/qualidade-codigo.yml` → dossiê §4 |
| 5    | Entrega                  | Checklist + `python verificar_entrega.py` retorna **0**         |


Use Copilot (ou agente com `@workspace`) citando `**@padrao_codigo.md`** — revisão humana antes de aceitar diff.

## Regras

1. Trabalhe **somente** em `pre-changes/` (alunos e demonstração ao vivo).
2. Siga **estritamente** `padrao_codigo.md` — contrato `ok`/`avisos`, `snake_case`, `logging`.
3. **Não** mascarar violações com `# noqa` sem justificativa no dossiê.
4. Pipeline local e CI devem executar **os mesmos portões**.
5. Documente cada fase no dossiê **antes** de pular para a próxima.

## Critérios de aceite

- [x] Três módulos conformes a `padrao_codigo.md`.
- [x] `python -m ruff check` limpo nos três módulos.
- [x] `python -m ruff format --check` limpo nos três módulos.
- [x] `python verificar_pipeline.py` retorna **0**.
- [x] `ci/qualidade-codigo.yml` espelha o portão local.
- [x] `python example.py` verde (contrato `ok`/`avisos`).
- [x] Dossiê §1–§4 preenchido; checklist com todos `[x]`.
- [x] `python verificar_entrega.py` retorna **0**.

## Comandos úteis

**Alunos (`pre-changes/`):**

```bash
cd entrega-profissional-e-padronizacao-de-codigo-com-ia/exercicio-01/pre-changes
pip install -r requirements-dev.txt
python -m ruff check notificacao_entrega.py confirmacao_entrega.py fechamento_entrega.py
python -m ruff format --check notificacao_entrega.py confirmacao_entrega.py fechamento_entrega.py
python verificar_pipeline.py
python example.py
python verificar_entrega.py
```

**Facilitador (raiz, após demo):**

```bash
cd entrega-profissional-e-padronizacao-de-codigo-com-ia/exercicio-01
python verificar_entrega.py
```

