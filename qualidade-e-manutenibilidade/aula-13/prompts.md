# Aula 13 — Mocking assistido por IA

**Objetivo:** testar **orquestração** (`executar_resgate`) isolando portas externas com `unittest.mock`, usando IA para identificar **o que mockar**, **onde patchar** e **como assertar colaboradores** — sem mockar regra pura local.

**Ferramentas:** GitHub Copilot Chat / Explorer (ou agente equivalente) + skill:

```bash
npx skills add https://github.com/wshobson/agents --skill python-testing-patterns
```

**Material sugerido:**


| Caminho                   | Papel                                            |
| ------------------------- | ------------------------------------------------ |
| **Raiz** (`aula-13/`)     | Demo ao vivo                                     |
| `**pre-changes/`**        | Alunos -> ambiente de trabalho (baseline igual). |
| `regras_catalogo.py`      | Regra pura -> **não** mockar.                    |
| `integracoes.py`          | Portas externas (I/O simulado).                  |
| `resgate_service.py`      | Orquestrador sob teste.                          |
| `test_resgate_service.py` | Suíte inicial **só regra pura**.                 |
| `guia_mocking_ia.md`      | Matriz, caminho do patch, anti-padrões.          |
| `verificar_mocks.py`      | Checklist do que ainda falta mockar/testar.      |


**Setup:**

```bash
pip install -r requirements-dev.txt
```

**Como usar:** rode `pytest -q` e `python verificar_mocks.py` → complete orquestração com mocks (IA) → valide de novo.

---

## 1. Mapear colaboradores vs regra local

```
@resgate_service.py @integracoes.py @regras_catalogo.py @guia_mocking_ia.md

Liste:

- funções que são **regra pura local** (testar sem mock);
- funções que são **porta externa** (candidatas a mock);
- em `executar_resgate`, ordem em que cada uma é chamada.

Não gere testes ainda.
```

---

## 2. Onde aplicar o patch (armadilha clássica)

```
@resgate_service.py @guia_mocking_ia.md

Por que patchar `integracoes.consultar_saldo` pode **não** interceptar a chamada em teste?

Qual caminho correto de patch para este módulo?

Responda em bullets — sem código ainda.
```

---

## 3. Plano de um teste com mock (sucesso)

```
Use a skill python-testing-patterns.

@resgate_service.py @test_resgate_service.py @guia_mocking_ia.md

Proponha UM teste para o fluxo de **sucesso** de `executar_resgate`, com:

- decoradores `@patch` no caminho certo;
- valores de retorno dos mocks;
- asserts de negócio (`ok`, `saldo_restante`);
- assert de que `enviar_confirmacao` foi chamada com argumentos esperados.

Plano em bullets (AAA) — não implemente ainda.
```

---

## 4. Implementar teste de sucesso com IA

```
Use python-testing-patterns.

Implemente APENAS o teste de sucesso de `executar_resgate` em test_resgate_service.py.

Regras:
- patch em `resgate_service.*`, não em `integracoes.*`;
- não mockar `custo_resgate`;
- pytest -q verde;
- não alterar código de produção.

@test_resgate_service.py @resgate_service.py @guia_mocking_ia.md
```

---

## 5. Erro sem chamar colaborador errado

```
Implemente APENAS o teste de **saldo insuficiente**.

Regras:
- mock de `consultar_saldo` retornando valor abaixo do custo;
- assert `ok False` e mensagem;
- prove que `debitar_pontos` **não** foi chamado (`assert_not_called` ou equivalente).

@test_resgate_service.py @resgate_service.py @guia_mocking_ia.md
```

---

## 6. IA como revisor de mocks

```
@test_resgate_service.py @guia_mocking_ia.md

Revise os mocks adicionados:

- patch no módulo correto?
- regra pura ficou sem mock?
- algum assert só checa `called` sem argumentos?
- falta cenário **falha ao debitar** ou **código inválido**?

Sugira ajuste mínimo ou próximo teste prioritário (só 1). Não implemente nesta resposta.
```

---

## 7. Armadilha: mockar demais

```
A IA sugeriu mockar `custo_resgate` para forçar custo fixo no teste de sucesso.

@resgate_service.py @guia_mocking_ia.md

Explique por que isso enfraquece o teste de orquestração.
Proponha alternativa sem mockar a regra pura.

Não implemente ainda.
```

## Comandos úteis

**Facilitador (raiz):**

```bash
cd aula-13
pip install -r requirements-dev.txt
pytest -q
python verificar_mocks.py
python example.py
```

**Alunos:**

```bash
cd aula-13/pre-changes
pip install -r requirements-dev.txt
pytest -q
python verificar_mocks.py
python example.py
```

---

## Máxima da aula

**Mock isola fronteira — patch onde o código usa a dependência; regra pura continua real; asserts provam efeito de negócio e chamadas (ou ausência) dos colaboradores.**