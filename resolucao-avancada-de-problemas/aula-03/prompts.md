# Aula 03 — Prompts para analisar stack trace

**Como usar:** copie o bloco, cole no chat do agente e **preencha** `[]` ou anexe o traceback (`@arquivo.txt`). Quando tiver o código, referencie com `@caminho/do/arquivo.py`.

---

## 1. Leitura do traceback (ordem e “quem chamou quem”)

```
Explique este traceback em linguagem simples: de baixo para cima, quem chamou quem, em qual frame o erro foi levantado, e qual a diferença entre “última linha do traceback” e “linha onde a exceção surgiu”.

Stack trace:
[cole aqui ou @arquivo]
```

---

## 2. Só traceback, sem código (inferências seguras vs especulação)

```
Tenho apenas o stack trace abaixo — não tenho o código-fonte aberto nem o estado dos dados em runtime.

Separe em duas listas: (A) o que dá para concluir com segurança só a partir do traceback; (B) o que seria especulação até eu abrir o arquivo ou inspecionar dados.

Stack trace:
[cole aqui]
```

---

## 3. Causa raiz sem pedir correção

```
Não quero patch nem refatoração ainda. Com base no traceback (e, se eu anexar, no trecho de código da linha indicada), explique a causa raiz provável e o fluxo lógico até a exceção.

Stack trace:
[cole aqui]

Código opcional:
[@arquivo:linhas relevantes]
```

---

## 4. KeyError, IndexError, AttributeError — onde a estrutura quebrou

```
No frame que levantou [KeyError / IndexError / AttributeError], a expressão era [cole a linha do arquivo se aparecer no trace].

Explique qual acesso (qual chave, índice ou atributo) falhou e o que isso implica sobre a estrutura esperada vs a estrutura que provavelmente existia (ex.: cadeia `a["b"]["c"]` — qual nível faltou).

Stack trace + linha do código:
[cole aqui]
```

---

## 5. Código meu vs biblioteca (onde investir tempo)

```
Neste traceback, quais frames são do meu projeto (caminho do workspace) e quais são biblioteca padrão ou `site-packages`?

Onde faz mais sentido começar a investigação e o que normalmente significa quando o erro “estoura” dentro de `node_modules` ou pacote instalado?

Stack trace:
[cole aqui]
```

---

## 6. Exceção encadeada (`Caused by` / `__cause__`)

```
Este traceback tem exceção encadeada (ex.: “During handling…”, “Caused by”, ou vários blocos Traceback).

Qual exceção é o sintoma e qual é a causa original? Em que ordem eu deveria ler os blocos para entender o bug?

Stack trace completo:
[cole aqui]
```

---

## 7. Async / threads (pilha confusa)

```
O stack envolve asyncio, `run_in_executor`, threads ou `Future`. Explique qual pilha é relevante para o bug e como relacionar o frame assíncrono ao código que eu escrevi.

Stack trace:
[cole aqui]
```

---

## 8. Próximo passo concreto (evidência, não achismo)

```
A partir deste traceback, liste no máximo 3 ações concretas de debug (ex.: breakpoint na linha X, log do valor de variável Y, reproduzir com input Z). Para cada uma, diga que evidência ela deve produzir.

Stack trace:
[cole aqui]
```

---

## 9. Checklist antes de aceitar um “fix” sugerido pela IA

- O patch ataca o **frame do meu código** ou mascara erro em biblioteca?
- A exceção indica **contrato de dados** (schema, JSON, CSV) que precisa validação na borda?
- Consigo **reproduzir** com um caso mínimo após o fix?
- O traceback de **teste** (pytest, etc.) aponta para asserção ou para o mesmo bug de produção?

---

## Máxima da aula

**O traceback é um mapa parcial: ele mostra o caminho da execução até a falha; a causa completa muitas vezes está no dado ou no contrato que o código assumiu.**
