# Aula 12 — Casos de sucesso e erro

**Objetivo:** ampliar a suíte com **casos de sucesso (incluindo bordas)** e **casos de erro** (exceção vs retorno de falha), usando IA para mapear lacunas — não para gerar dezenas de testes genéricos.

**Ferramenta:** GitHub Copilot Chat / Explorer (ou agente equivalente com `@workspace`).

**Material sugerido:**

| Caminho | Papel |
| -------- | ------ |
| **Raiz** (`aula-12/`) | Facilitador — demo ao vivo. |
| **`pre-changes/`** | Alunos — ambiente de trabalho (baseline igual). |
| `regras_resgate.py` | Código com caminhos de sucesso e erro distintos. |
| `test_regras_resgate.py` | Suíte inicial **só happy path**. |
| `guia_casos_sucesso_erro.md` | Matriz sucesso/erro + como assertar cada tipo. |
| `verificar_casos.py` | Checklist textual do que ainda falta testar. |

**Como usar:** rode `pytest -q` e `python verificar_casos.py` → complete casos de erro com IA → valide de novo.

---

## 1. Mapear sucesso vs erro no código

```
@regras_resgate.py @guia_casos_sucesso_erro.md

Para cada função pública, separe:

- caminhos de **sucesso** (retorno ok ou valor esperado);
- caminhos de **erro** (exceção vs dict com ok False);
- uma **borda** de sucesso ainda não óbvia.

Não gere testes ainda.
```

---

## 2. Auditar lacunas na suíte atual

```
@test_regras_resgate.py @guia_casos_sucesso_erro.md

Quais cenários da matriz já têm teste dedicado?

Quais casos de **erro** estão totalmente descobertos? Priorize top 3 por risco.

Não implemente ainda.
```

---

## 3. Gerar testes de erro (exceção)

```
Implemente em test_regras_resgate.py APENAS os testes de erro que levantam ValueError
(código vazio e código inválido).

Regras:
- pytest.raises com match explícito;
- um comportamento por teste;
- pytest -q verde.

@test_regras_resgate.py @regras_resgate.py @guia_casos_sucesso_erro.md
```

---

## 4. Gerar teste de erro (retorno, não exceção)

```
Implemente APENAS o teste para saldo insuficiente (ok False, sem exceção).

Diferencie claramente no nome do teste que é erro por **retorno**, não por raises.

@test_regras_resgate.py @regras_resgate.py
```

---

## 5. IA como revisor (sucesso vs erro)

```
@test_regras_resgate.py

Revise a suíte:

- algum teste de erro usa assert genérico demais?
- sucesso e erro estão nomeados de forma simétrica e legível?
- falta alguma borda de sucesso da matriz?
- se está seguindo o padrão AAA

Sugira ajuste mínimo. Não adicione testes novos nesta resposta.
```

---

## 6. Parametrizar ou duplicar?

```
A IA sugeriu @pytest.mark.parametrize para 4 códigos inválidos.

@regras_resgate.py @test_regras_resgate.py

Quando parametrizar faz sentido aqui e quando manter testes separados?
Recomende abordagem para ESTE módulo (máx. 5 bullets).

Não gere código.
```

## Comandos úteis

```bash
cd aula-12/pre-changes
pytest -q
python verificar_casos.py
python example.py
```

---

## Máxima da aula

**Suíte madura equilibra happy path, bordas e erros — cada um com o assert certo (raises ou ok False), não um bloco genérico “testa erro”.**
