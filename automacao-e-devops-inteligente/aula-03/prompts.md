# Aula 03 — Comentários automáticos

**Objetivo:** triar **comentários automáticos** em PRs (Copilot, bots de CI, linters, scanners) — separar sinal de ruído, detectar duplicação e decidir o que vira ação.

**Ferramenta:** GitHub (PR com uma ou mais fontes de comentário automático).

**Material:**

| Arquivo | Papel |
| -------- | ------ |
| `release_gate.py` | Código simples com achados que disparam comentários de bots diferentes. |
| `inventario_comentarios.md` | Planilha para catalogar e priorizar cada comentário automático. |
| `example.py` | Executar comportamento atual do gate. |

**Fluxo em sala:**

1. Abrir PR alterando `release_gate.py`.
2. Coletar **todos** os comentários automáticos (não só o Copilot).
3. Preencher `inventario_comentarios.md` com fonte, tipo e ação.
4. Discutir: o que corrigir, o que dismiss e o que virar comentário humano ao autor.

---

## 1. Fontes de comentário automático

```
Antes de abrir o PR, liste em bullets:

- quais ferramentas no seu fluxo podem postar comentário automático no GitHub;
- diferença entre comentário **inline** no diff, **resumo** no PR e **check** de CI.

Não analise release_gate.py ainda.
```

---

## 2. Coletar comentários do PR

```
Abri um PR sobre release_gate.py.

Cole aqui cada comentário automático (Copilot, Action, linter, SAST — todos).

Para cada um, anote só: fonte + trecho citado + uma linha do texto.

Não classifique ainda.
```

---

## 3. Triagem no inventário

```
@inventario_comentarios.md

Preencha a tabela de triagem para cada comentário coletado:

- fonte e tipo;
- acionável (sim / parcial / ruído);
- se duplica outro bot;
- ação (corrigir / responder / dismiss / ignorar).

Não implemente correções no código.
```

---

## 4. Sinal vs ruído

```
@inventario_comentarios.md

Dos comentários marcados como ruído ou parcial:

- qual critério você usou (risco, duplicação, estilo sem impacto)?
- qual você transformaria em comentário **humano** acionável para o autor?

Formato: comentário automático original → risco → texto humano sugerido.
```

---

## 5. Duplicação entre bots

```
No mesmo PR, dois bots comentaram o mesmo smell (ex.: segredo em log).

Como você evita que o autor corrija duas vezes ou ignore por fadiga?

Resposta em bullets — política de triagem, sem código.
```

---

## 6. Síntese da triagem

```
@inventario_comentarios.md

Em 4 bullets: o que aprendeu sobre **volume** e **qualidade** de comentários automáticos?

Inclua: fonte mais útil, fonte mais ruidosa, um dismiss justificado e um achado que exige ação.
```

## Comandos úteis

```bash
cd aula-03
python example.py
```

---

## Máxima da aula

**Comentário automático acelera a triagem — quem revisa o PR decide o que vira ação.**
