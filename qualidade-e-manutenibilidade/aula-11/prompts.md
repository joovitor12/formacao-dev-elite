# Aula 11 — Gerando testes com IA

**Objetivo:** usar IA **com skills de pytest e cobertura** para identificar lacunas, gerar testes **priorizados** (não em massa) e validar ganho real com `pytest-cov` — mantendo estrutura de qualidade.

**Ferramentas:** GitHub Copilot Chat / Explorer (ou agente equivalente) + skills:

```bash
npx skills add https://github.com/github/awesome-copilot --skill pytest-coverage
npx skills add https://github.com/wshobson/agents --skill python-testing-patterns
```

**Material sugerido:**

| Caminho | Papel |
| -------- | ------ |
| **Raiz** (`aula-11/`) | demo ao vivo. |
| **`pre-changes/`** | Alunos — ambiente de trabalho. |
| `regras_assinatura.py` | Código sob teste (igual nos dois ambientes). |
| `test_regras_assinatura.py` | Suíte **parcial** inicial (1 teste, cobertura baixa). |
| `guia_geracao_testes_ia.md` | Fluxo, skills, anti-padrões. |
| `verificar_cobertura.py` | Relatório `term-missing` no terminal. |
| `requirements-dev.txt` | `pytest` + `pytest-cov`. |

**Setup:**

```bash
pip install -r requirements-dev.txt
```

**Como usar:** rode cobertura → peça à IA (com skills) **poucos** testes de alto valor → implemente → rode de novo. Facilitador na **raiz**; alunos em **`pre-changes/`**.

---

## 1. Ler cobertura antes de pedir testes

```
Acabei de rodar:
  python verificar_cobertura.py

@regras_assinatura.py @test_regras_assinatura.py

Com base no relatório (linhas faltantes), quais **funções ou ramos** ainda não têm prova unitária?

Liste em ordem de risco de regressão — sem gerar código ainda.
```

*(Facilitador: anexe arquivos da raiz. Alunos: `@pre-changes/...`.)*

---

## 2. Pedir plano de testes (skill python-testing-patterns)

```
Use a skill python-testing-patterns.

@regras_assinatura.py @test_regras_assinatura.py @guia_geracao_testes_ia.md

Proponha no máximo 3 testes novos para as maiores lacunas, cada um com:
- nome descritivo (padrão test_*);
- Arrange / Act / Assert em bullets;
- assert concreto (valor ou exceção).

Não implemente ainda — só o plano revisável.
```

---

## 3. Gerar um único teste com IA

```
Use python-testing-patterns + pytest-coverage.

Implemente APENAS o teste de maior prioridade em test_regras_assinatura.py.

Regras:
- um comportamento por teste;
- pytest.raises para erros;
- não alterar regras_assinatura.py;
- pytest -q verde.

@test_regras_assinatura.py @regras_assinatura.py
```

---

## 4. Validar ganho de cobertura (skill pytest-coverage)

```
Rodei novamente: python verificar_cobertura.py

Cole aqui a saída do relatório.

Com a skill pytest-coverage, responda:
1) quais linhas deixaram de aparecer como missing;
2) a cobertura subiu com assert de regra ou só “passou por cima”;
3) qual próximo teste ainda vale a pena (só 1).
```

---

## 5. Revisar teste gerado (qualidade > percentual)

```
@test_regras_assinatura.py

Revise o último teste adicionado:

- estrutura AAA clara?
- assert prova contrato de negócio?
- seria aceitável num PR mesmo se a cobertura já estivesse “boa”?

Sugira ajuste mínimo se necessário. Não adicione outros testes.
```

---

## 6. Armadilha: IA infla cobertura sem prova

```
A IA sugeriu:

def test_calcular_fatura():
    assert calcular_fatura("basico", 1) is not None

@regras_assinatura.py

Explique por que isso pode aumentar cobertura mas falhar no papel do teste unitário.
Proponha asserts concretos para o mesmo cenário.

Não implemente ainda.
```

---

## 7. Prompt curto para gravação

```
@guia_geracao_testes_ia.md

Em uma frase: como usar IA + cobertura sem transformar teste em checklist de linha vermelha?
```

---

## Comandos úteis

**Facilitador (raiz):**

```bash
cd aula-11
pip install -r requirements-dev.txt
pytest -q
python verificar_cobertura.py
python example.py
```

**Alunos:**

```bash
cd aula-11/pre-changes
pip install -r requirements-dev.txt
pytest -q
python verificar_cobertura.py
python example.py
```

---

## Máxima da aula

**Cobertura mostra onde falta prova; a IA sugere candidatos — você escolhe asserts que documentam regra de negócio, não linhas pintadas de verde.**
