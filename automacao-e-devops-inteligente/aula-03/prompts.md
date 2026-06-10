# Aula 03 — Comentários automáticos

**Objetivo:** triar **comentários automáticos** em PRs (Copilot, bots de CI, linters, scanners) — separar sinal de ruído, detectar duplicação e decidir o que vira ação.

**Ferramenta:** GitHub (PR com uma ou mais fontes de comentário automático).

**Material:**

| Arquivo | Papel |
| -------- | ------ |
| `release_gate.py` | **Baseline limpa** na branch principal; o diff do PR traz os achados. |
| `inventario_comentarios.md` | Planilha para catalogar e priorizar cada comentário automático. |
| `example.py` | Executar o gate antes e depois do PR (opcional). |

**Fluxo em sala:**

1. Manter `release_gate.py` **limpo** na branch principal (`main` / `master`).
2. Criar branch (ex.: `feat/release-gate-review`) e aplicar as mudanças da seção 2.
3. Abrir PR da branch → principal.
4. Coletar **todos** os comentários automáticos (não só o Copilot).
5. Preencher `inventario_comentarios.md` e discutir triagem.

---

## 1. Fontes de comentário automático

```
Antes de abrir o PR, liste em bullets:

- quais ferramentas no seu fluxo podem postar comentário automático no GitHub;
- diferença entre comentário **inline** no diff, **resumo** no PR e **check** de CI.

Não analise release_gate.py ainda.
```

---

## 2. Preparar o diff do PR (na branch)

Na branch do PR, altere `release_gate.py` introduzindo **vários** achados para bots diferentes comentarem, por exemplo:

- constante `GATE_API_TOKEN` hardcoded e citada em log;
- parâmetro `forcar_aprovacao` com `forcar_aprovacao or True` (sempre aprova);
- variável `unused_metric` não usada;
- constante `TIMEOUT_MS` declarada e não usada;
- `except Exception: pass` engolindo erro;
- trocar `score >= SCORE_MINIMO` por `score > SCORE_MINIMO` (fronteira 0,85);
- estado global `_validacoes_executadas` + função `consultar_validacoes()`.

Peça à IA só o patch desta branch — **não** altere a baseline da principal.

```
@release_gate.py

Gere o diff para a branch do PR com os achados acima, mantendo o arquivo executável.

Não abra o PR ainda.
```

---

## 3. Coletar comentários do PR

```
Abri o PR da branch para a principal.

Cole aqui cada comentário automático (Copilot, Action, linter, SAST — todos).

Para cada um, anote só: fonte + trecho citado + uma linha do texto.

Não classifique ainda.
```

---

## 4. Triagem no inventário

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

## 5. Sinal vs ruído

```
@inventario_comentarios.md

Dos comentários marcados como ruído ou parcial:

- qual critério você usou (risco, duplicação, estilo sem impacto)?
- qual você transformaria em comentário **humano** acionável para o autor?

Formato: comentário automático original → risco → texto humano sugerido.
```

---

## 6. Duplicação entre bots

```
No mesmo PR, dois bots comentaram o mesmo smell (ex.: segredo em log).

Como você evita que o autor corrija duas vezes ou ignore por fadiga?

Resposta em bullets — política de triagem, sem código.
```

---

## 7. Síntese da triagem

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
