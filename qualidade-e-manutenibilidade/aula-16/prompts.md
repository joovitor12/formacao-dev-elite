# Aula 16 — Boas práticas de testes assistidos

**Objetivo:** consolidar o bloco **Testes unitários com IA** — montar suíte de qualidade em `test_ativacao_service.py` aplicando geração consciente, sucesso/erro, mock na fronteira, avaliação crítica e asserts que detectam regressão.

**Ferramentas:** GitHub Copilot Chat / Explorer (ou agente equivalente) + skills:

```bash
npx skills add https://github.com/github/awesome-copilot --skill pytest-coverage
npx skills add https://github.com/wshobson/agents --skill python-testing-patterns
```

**Material sugerido:**


| Caminho                           | Papel                                  |
| --------------------------------- | -------------------------------------- |
| **Raiz** (`aula-16/`)             | demo ao vivo.                          |
| `**pre-changes/`**                | ambiente de trabalho (baseline igual). |
| `regras_tier.py`                  | Regra pura — testar sem mock.          |
| `integracoes.py`                  | Portas externas (CRM, recibo).         |
| `ativacao_service.py`             | Orquestrador sob teste.                |
| `test_ativacao_service.py`        | Suíte **mínima** inicial (1 teste).    |
| `guia_boas_praticas_testes_ia.md` | Síntese dos princípios do bloco.       |
| `checklist_testes_assistidos.md`  | Checklist humano para marcar.          |
| `verificar_boas_praticas.py`      | Checagens automáticas da suíte.        |


**Setup:**

```bash
pip install -r requirements-dev.txt
```

**Como usar:** `pytest -q` → `python verificar_boas_praticas.py` → completar lacunas com IA em rodadas pequenas → checklist + verificador verdes.

---

## 1. Diagnóstico inicial (não gerar ainda)

```
Rodei pytest -q (verde) e python verificar_boas_praticas.py (pendências).

@ativacao_service.py @regras_tier.py @integracoes.py @guia_boas_praticas_testes_ia.md

Liste lacunas de teste por risco, separando:

- regra pura local;
- orquestração (sucesso / erro retorno);
- exceção;
- onde mock é necessário e onde não é.

Não implemente código ainda.
```

---

## 2. Plano em rodada única (máx. 3 testes)

```
Use python-testing-patterns.

@test_ativacao_service.py @guia_boas_praticas_testes_ia.md

Proponha no máximo 3 testes novos (prioridade decrescente), cada um com:

- nome descritivo;
- mock sim/não e caminho do patch;
- asserts concretos;
- tipo de erro (raises vs ok False).

Plano revisável — sem implementar.
```

---

## 3. Implementar regra pura + um erro com raises

```
Implemente em test_ativacao_service.py:

1) teste de regra pura adicional (sem mock);
2) teste de tier inválido com pytest.raises.

Não altere arquivos de produção. pytest -q verde.

@test_ativacao_service.py @regras_tier.py @ativacao_service.py
```

---

## 4. Orquestração com mock na fronteira

```
Implemente APENAS o teste de sucesso de ativar_tier.

Regras:
- @patch em ativacao_service.* (não integracoes.*);
- assert ok True + campos de contrato;
- assert enviar_recibo chamado com argumentos esperados;
- pytest -q verde.

@test_ativacao_service.py @ativacao_service.py @guia_boas_praticas_testes_ia.md
```

---

## 5. Erro por retorno + colaborador não invocado

```
Implemente APENAS saldo insuficiente (ok False).

Prove que creditar_tier NÃO foi chamado.

@test_ativacao_service.py @ativacao_service.py
```

---

## 6. Revisão estilo PR (avaliação + falsos positivos)

```
@test_ativacao_service.py @guia_boas_praticas_testes_ia.md

Revise a suíte como PR:

- manter / revisar / rejeitar por teste;
- algum assert fraco ou falso positivo de confiança?
- falta cenário da matriz mínima?

Sugira no máximo 2 ajustes. Não reescreva tudo.
```

---

## 7. Fechamento do checklist

```
Saída de python verificar_boas_praticas.py: [cole aqui]

@checklist_testes_assistidos.md @guia_boas_praticas_testes_ia.md

Quais itens do checklist humano ainda dependem de julgamento humano
mesmo com verificador verde?

O que você **deliberadamente** não testaria neste módulo (escopo)?

Resposta em bullets — sem código.
```

## Comandos úteis

**Facilitador (raiz):**

```bash
cd aula-16
pip install -r requirements-dev.txt
pytest -q
python verificar_boas_praticas.py
python example.py
```

**Alunos:**

```bash
cd aula-16/pre-changes
pip install -r requirements-dev.txt
pytest -q
python verificar_boas_praticas.py
python example.py
```

**Opcional (cobertura):**

```bash
pytest --cov=ativacao_service --cov=regras_tier --cov-report=term-missing -q
```

---

## Máxima da aula

**IA acelera lacunas e rascunhos — boa prática é poucos testes com contrato claro, mock na fronteira, revisão crítica e checklist antes do merge.**