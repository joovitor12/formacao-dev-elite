# 🧪 Quizz: Padrão de código e linting com IA

**Módulo: Entrega Profissional e Padronização de Código com IA**

Este questionário verifica os **temas** de **padrão de código como contrato do time** (nomenclatura, contrato de retorno, logging, prompts com `@padrao_codigo.md`, revisão humana) e de **linting assistido por IA** (Ruff, triagem, patch sugerido pela IA, validação contra o padrão) — sem depender do código visto em sala.

---

### 1. Por que documentar um padrão de código antes de pedir implementação à IA?
   - A) Para que a IA substitua o code review humano sem revisar o diff.
   - B) Para evitar que cada prompt gere estilo diferente (nomes, retornos, logging) no mesmo time.
   - C) Porque Python exige um arquivo markdown por repositório para compilar.
   - D) Para desativar type hints e deixar só o linter decidir tudo.

### 2. Qual formato de retorno o padrão exige para funções de fluxo de entrega?
   - A) `{"success": bool, "msg": str}` com exceção lançada em validação esperada.
   - B) Tupla `(bool, str)` sem dicionário estruturado.
   - C) `{"ok": bool, "avisos": list[str], ...}` — falhas de validação preenchem `avisos` sem exceção para fluxo esperado.
   - D) `None` em erro e objeto ORM em sucesso.

### 3. Ao pedir refatoração à IA, o padrão recomenda:
   - A) Anexar `@padrao_codigo.md`, declarar aderência estrita e revisar o diff antes de aceitar.
   - B) Confiar no estilo default do modelo sem documento de referência.
   - C) Pedir apenas “deixe o código bonito” para maximizar criatividade da IA.
   - D) Substituir o padrão pelo output do linter sozinho.

### 4. Depois que a IA refatora o baseline, o passo mais alinhado ao material é:
   - A) Merge imediato porque a IA citou o padrão no prompt.
   - B) Rodar só o smoke test e ignorar conformidade nominal e de contrato.
   - C) Deletar `padrao_codigo.md` para evitar conflito com o diff gerado.
   - D) Revisar o diff linha a linha contra o padrão e corrigir manualmente o que a IA errou.

### 5. No linting assistido por IA, qual divisão de papéis está correta?
   - A) Ruff decide merge; a IA ignora `padrao_codigo.md`.
   - B) Linter automatiza o objetivo (imports, naming, bare except); humano tria, IA sugere patch e valida contra o padrão.
   - C) A IA corrige tudo sozinha; triagem humana é opcional se `ruff check` passou.
   - D) Padrão documentado substitui Ruff — não é necessário rodar linter.

### 6. Antes de pedir patch à IA no fluxo de lint, o material pede:
   - A) Merge do código antes de classificar violações do Ruff.
   - B) Ignorar a saída do Ruff e confiar apenas no olho humano.
   - C) Registrar a saída do Ruff e triar cada violação (corrigir agora, ignorar documentado, alinhar ao padrão).
   - D) Rodar `ruff check --fix` em produção sem revisar o diff.

### 7. Eventos operacionais no código de entrega simulada devem usar:
   - A) `logging` via logger de módulo — `print` é proibido no caminho de produção/simulação conforme o padrão.
   - B) `print` exclusivamente porque é mais legível em review.
   - C) Token completo no log para facilitar debug em staging.
   - D) Bare `except:` para silenciar falhas de log sem registro.

### 8. Quando Ruff aponta função em PascalCase e o padrão exige `snake_case`, a correção mais alinhada é:
   - A) Renomear só no comentário e manter PascalCase para “compatibilidade”.
   - B) Ignorar Ruff porque PascalCase é preferência pessoal válida no time.
   - C) Usar `# noqa` em tudo sem documentar exceção no registro.
   - D) Alinhar lint e padrão (`confirmar_entrega`), validar com `ruff check` e smoke test.

---

## 🔑 Gabarito comentado

### 1. Resposta: B
**Justificativa:** Sem padrão explícito, cada prompt tende a gerar convenções diferentes; documentar e citar o arquivo reduz retrabalho e review surpresa — o padrão funciona como **contrato** do time.

### 2. Resposta: C
**Justificativa:** O contrato interno exige `{"ok": bool, "avisos": list[str], ...}`; validações esperadas preenchem `avisos` em vez de lançar exceção — diferente de pares `success`/`msg` ou tuplas ad hoc.

### 3. Resposta: A
**Justificativa:** A seção 10 de `padrao_codigo.md` pede anexar o documento, declarar aderência estrita e **revisar o diff** antes de aceitar — a IA acelera, não substitui o checklist humano.

### 4. Resposta: D
**Justificativa:** O fluxo de conformidade inclui checklist linha a linha e ajuste manual do que a IA errou; citar o padrão no prompt não garante aderência total.

### 5. Resposta: B
**Justificativa:** Máxima do linting assistido: **linter aponta — IA sugere patch — humano tria e valida contra o padrão**; Ruff cobre o objetivo, o documento cobre contrato e estilo além do alerta.

### 6. Resposta: C
**Justificativa:** A triagem humana vem **antes** do patch à IA: classificar se corrige agora, ignora com justificativa ou exige alinhar ao padrão (ex.: `ok`/`avisos`, logging).

### 7. Resposta: A
**Justificativa:** O padrão proíbe `print` no caminho de entrega simulada/produção e exige `logging`; também veda logar segredos — opções B–D violam regras explícitas.

### 8. Resposta: D
**Justificativa:** Quando lint e padrão convergem (naming, type hints, contrato), a correção alinha ambos, roda `ruff check`/`verificar_lint.py` e confirma comportamento com smoke test — não mascarar com noqa ou comentário.
