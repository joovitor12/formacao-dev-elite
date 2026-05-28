# Aula 09 — Papel dos testes unitários

**Objetivo:** entender **para que servem** os testes unitários (documentação viva, feedback rápido, rede fina) e **onde não são a ferramenta principal** — usando IA para analisar cobertura de papéis, não para gerar testes em massa sem critério.

**Ferramenta:** GitHub Copilot Chat / Explorer (ou agente equivalente com `@workspace`).

**Material sugerido:**

| Caminho | Papel |
| -------- | ------ |
| `pre-changes/` | Ambiente de trabalho (mesmo código da raiz). |
| `regras_pontos.py` | Funções **puras** — alvo clássico de teste unitário. |
| `fidelidade_service.py` | Orquestração com estado global e `print`. |
| `test_regras_pontos_unitarios.py` | Exemplos de testes unitários bem delimitados. |
| `test_fidelidade_service.py` | Testes de fluxo (mais integrados). |
| `guia_papel_testes.md` | Referência rápida dos papéis. |

**Como usar:** rode `pytest -q` e `python example.py`. Compare os dois arquivos de teste antes de pedir à IA novos casos.

---

## 1. Mapear papéis nos testes existentes

```
@pre-changes/test_regras_pontos_unitarios.py @pre-changes/guia_papel_testes.md

Para cada teste em test_regras_pontos_unitarios.py, classifique o papel principal:
- documentação viva;
- feedback rápido;
- rede fina / contrato local.

Cite o nome do teste e uma frase de justificativa. Não gere testes novos.
```

---

## 2. O que NÃO é teste unitário aqui

```
@pre-changes/fidelidade_service.py @pre-changes/test_fidelidade_service.py

Liste 3 comportamentos do serviço que os testes atuais cobrem de forma mais “integrada”.

Para cada um, explique por que testar só com unitário puro em regras_pontos.py seria insuficiente
e o que um teste unitário ainda poderia cobrar antes da orquestração.

Não escreva código.
```

---

## 3. IA como auditor de lacunas (não como fábrica)

```
@pre-changes/regras_pontos.py @pre-changes/test_regras_pontos_unitarios.py

Quais regras ou bordas em regras_pontos.py ainda NÃO têm teste unitário?

Proponha no máximo 3 casos faltantes, no formato:
- função;
- entrada;
- saída esperada;
- qual papel do unitário esse teste cumpriria.

Não implemente ainda.
```

---

## 4. Implementar um único teste unitário com propósito

```
Implemente APENAS 1 teste novo em pre-changes/test_regras_pontos_unitarios.py,
escolhido da lista anterior (o de maior valor pedagógico).

Regras:
- um comportamento por teste;
- nome descritivo;
- sem mock desnecessário;
- pytest -q deve passar.

@pre-changes/test_regras_pontos_unitarios.py @pre-changes/regras_pontos.py
```

---

## 5. Revisar teste gerado pela IA

```
@pre-changes/test_regras_pontos_unitarios.py

Revise o último teste adicionado:

- ele testa implementação ou comportamento observável?
- é unitário de verdade (isolado, rápido) ou já é integração disfarçada?
- sugira ajuste mínimo se necessário.

Não adicione outros testes.
```

---

## 6. Contraste: pedir “teste unitário” do serviço inteiro

```
A IA sugeriu: "gere testes unitários para fidelidade_service.py cobrindo tudo".

@pre-changes/fidelidade_service.py @pre-changes/regras_pontos.py

Explique em 5 bullets por que isso confunde papel de teste unitário com teste de integração,
e qual divisão de responsabilidade você manteria entre os dois arquivos de teste.

Não gere código.
```

## Comandos úteis

```bash
cd pre-changes
pytest -q
pytest -q test_regras_pontos_unitarios.py
python example.py
```

---

## Máxima da aula

**Teste unitário não é “qualquer teste que roda no pytest” — é prova barata e local de uma unidade de comportamento.** A IA ajuda a decidir *onde* unitarizar; você segura o *porquê*.
