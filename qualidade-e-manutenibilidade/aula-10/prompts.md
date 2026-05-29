# Aula 10 — Estrutura de um teste de qualidade

**Objetivo:** reconhecer e aplicar **estrutura clara** em testes unitários (nome, AAA, foco, asserts idiomáticos) — usando IA para **revisar e reescrever** testes fracos, não para inflar a suíte.

**Ferramenta:** GitHub Copilot Chat / Explorer (ou agente equivalente com `@workspace`).

**Material sugerido:**

| Caminho | Papel |
| -------- | ------ |
| `pre-changes/` | Ambiente de trabalho: `test_regras_envio.py` **fraco** para reestruturar. |
| `regras_envio.py` (raiz) | Código sob teste — não altere regras de negócio. |
| `test_regras_envio.py` (raiz) | Referência de testes bem estruturados. |
| `guia_estrutura_teste.md` | Checklist AAA + anti-padrões. |

**Como usar:** compare raiz vs `pre-changes/test_regras_envio.py`. Reescreva os testes em `pre-changes/` mantendo `pytest -q` verde.

---

## 1. Auditar estrutura dos testes fracos

```
@pre-changes/test_regras_envio.py @pre-changes/guia_estrutura_teste.md

Para cada teste em pre-changes/test_regras_envio.py, liste:
- nome (claro ou genérico?);
- violação do checklist (nome, AAA, foco, assert);
- comportamento que ele tenta provar (1 frase).

Não reescreva ainda.
```

---

## 2. Comparar com referência

```
@pre-changes/test_regras_envio.py @test_regras_envio.py @guia_estrutura_teste.md

Escolha 1 teste fraco em pre-changes/ e o teste equivalente (ou mais próximo) na raiz.

Compare lado a lado: o que a referência faz melhor em nome, AAA e foco?

Não copie arquivo inteiro — só análise.
```

---

## 3. Reescrever um único teste

```
Reescreva APENAS o teste mais genérico (test_1) em pre-changes/test_regras_envio.py,
dividindo em testes menores se necessário.

Regras:
- nomes descritivos;
- padrão AAA visível;
- pytest.raises para exceções (quando aplicável);
- pytest -q verde;
- não alterar regras_envio.py.

@pre-changes/test_regras_envio.py @pre-changes/regras_envio.py @pre-changes/guia_estrutura_teste.md
```

---

## 4. IA como revisor de estrutura

```
@pre-changes/test_regras_envio.py

Revise a suíte após a última mudança:

- algum teste ainda mistura comportamentos?
- algum assert frágil ou número mágico sem contexto?
- sugira 1 melhoria mínima restante.

Não adicione testes de regra nova — só estrutura.
```

---

## 5. Plano para reescrever o restante

```
@pre-changes/test_regras_envio.py

Monte plano em 3 passos para reestruturar os testes restantes (test_frete, test_erro),
mantendo os mesmos comportamentos cobertos.

Cada passo: nome sugerido dos novos testes + o que sai do teste monolítico.

Não implemente ainda.
```

---

## 6. Armadilha: IA gera teste que passa mas não prova nada

```
A IA sugeriu:

def test_calcular_frete():
    assert calcular_frete("sudeste", 1) is not None

@pre-changes/regras_envio.py

Explique por que isso viola "estrutura de qualidade" mesmo passando no pytest.
Proponha assert concreto alinhado à regra de negócio.

Não gere código ainda.
```

## Comandos úteis

```bash
cd pre-changes
pytest -q
pytest -q test_regras_envio.py -v
python example.py
```

---

## Máxima da aula

**Teste verde não basta — estrutura clara é documentação que o próximo dev (e a IA) consegue revisar.**
