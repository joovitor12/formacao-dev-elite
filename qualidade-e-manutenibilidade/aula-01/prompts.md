# Aula 01 — O que caracteriza código legado

**Objetivo:** reconhecer código legado pelo **risco de mudança**, não pela idade da linguagem — e usar o Copilot como **auditor forense** (diagnóstico primeiro, refatoração depois).

**Ferramenta:** GitHub Copilot Chat / Explorer (ou agente equivalente com `@workspace`).

**Material sugerido:**

| Arquivo | Papel |
| -------- | ------ |
| `pedido_service.py` | Exemplo propositalmente “difícil de mexer”: mistura de regras, efeitos colaterais e pouca clareza. |
| `example.py` | Execução rápida para ver o fluxo e alimentar perguntas no chat. |

**Como usar:** abra `pedido_service.py` no editor, use **`@workspace`** (ou anexe o arquivo) e cole os prompts abaixo. **Não peça refatoração completa ainda** — só diagnóstico e riscos, alinhado à abertura da aula.

---

## 1. Diagnóstico geral (auditor forense)

```
@pedido_service.py

Analise este arquivo como auditor de manutenibilidade. Não refatore nem escreva patch.

Responda em seções curtas:
1) Em uma frase: por que um dev poderia ter MEDO de alterar este código amanhã?
2) Liste sinais de falta de rede de proteção (testes, contratos, invariantes documentados).
3) Onde o acoplamento é mais rígido (mudança local que pode quebrar outro comportamento)?
4) Quais trechos têm lógica obscura (nomes, funções longas, múltiplas responsabilidades)?

Use linguagem direta; cite trechos por nome de função ou comentário “linha aproximada” se ajudar.
```

---

## 2. Testes e zona cega

```
@pedido_service.py

Este repositório não inclui testes automatizados para este módulo (de propósito, para o exercício).

Com base só no código:
- O que você inferiria sobre cobertura de testes?
- Quais regras de negócio seriam mais perigosas de mudar sem testes e por quê?
- Sugira 5 casos mínimos de teste (título + entrada + resultado esperado em linguagem natural), sem implementar ainda.
```

---

## 3. Acoplamento e efeitos colaterais

```
@pedido_service.py

Mapeie efeitos colaterais (mutação de estado global, I/O, logging, alteração de estruturas compartilhadas).

Para cada um, diga: “se eu mudar X, o que pode quebrar em Y?”
Priorize os 3 acoplamentos mais perigosos para o negócio.
```

---

## 4. Complexidade e “mapa da mina”

```
@pedido_service.py

Aponte trechos com alta complexidade ciclomática ou decisões encadeadas difíceis de seguir.

Explique em linguagem humana o que termos como “complexidade ciclomática” ou “side effects” significam aqui, sem jargão desnecessário.
```

---

## 5. Impacto no negócio (custo da mudança)

```
Imagine que o time precisa alterar a regra de imposto para um novo estado (UF) amanhã.

Com base em pedido_service.py, estime (qualitativo: baixo/médio/alto) o risco e o tempo de descoberta para:
- achar todos os pontos impactados;
- validar que nada mais quebrou;
- justificar a mudança para o negócio.

Não escreva código; só análise de custo de mudança.
```

---

## Máxima da aula

**Legado é custo de mudança.** O objetivo do módulo é usar IA para enxergar risco cedo — e na sequência dar nomes técnicos aos problemas (próximo tema: *code smells*).
