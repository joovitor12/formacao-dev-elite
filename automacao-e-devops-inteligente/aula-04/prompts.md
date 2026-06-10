# Aula 04 — Detecção de riscos

**Objetivo:** **detectar e priorizar riscos** em um PR de DevOps — mapear impacto, severidade, quem sinalizou (humano vs ferramentas) e o que bloqueia merge.

**Ferramenta:** GitHub (PR + Copilot Code Review e/ou scanners do repositório).

**Material:**

| Arquivo | Papel |
| -------- | ------ |
| `canary_deploy.py` | **Baseline limpa** na branch principal; o diff do PR introduz riscos. |
| `mapa_riscos.md` | Registro de riscos, lacunas de detecção e priorização. |
| `example.py` | Executar comportamento do canary antes e depois do PR (opcional). |

**Fluxo em sala:**

1. Manter `canary_deploy.py` **limpo** na branch principal.
2. Criar branch (ex.: `feat/canary-risk-review`) e aplicar as mudanças da seção 2.
3. Abrir PR da branch → principal.
4. Preencher `mapa_riscos.md` cruzando diff, Copilot e análise humana.
5. Decidir: corrigir, mitigar ou bloquear merge.

---

## 1. O que é risco neste contexto

```
Antes de abrir o PR, defina em bullets:

- diferença entre **code smell**, **bug** e **risco** em um deploy canário;
- três tipos de risco que você espera ver (segurança, operação, negócio).

Não analise canary_deploy.py ainda.
```

---

## 2. Preparar o diff do PR (na branch)

Na branch do PR, altere `canary_deploy.py` introduzindo **riscos variados** (alguns óbvios, outros sutis), por exemplo:

- token `CANARY_API_KEY` hardcoded e impresso em log;
- parâmetro `forcar_prod` que faz deploy direto em prod ignorando limite de percentual;
- `pular_health_check: bool` com `pular_health_check or True`;
- e-mail de usuário (`email_cliente`) incluído em log — risco de compliance/PII;
- trocar `taxa_erro >= LIMITE` por `taxa_erro > LIMITE` (fronteira 0,05 não aborta);
- estado global `CANARY_ATIVO` alterado sem validar serviço em execução;
- permitir `percentual=100` em prod sem etapa intermediária.

Peça à IA só o patch desta branch — **não** altere a baseline da principal.

```
@canary_deploy.py

Gere o diff para a branch do PR com os riscos acima, mantendo o arquivo executável.

Não abra o PR ainda.
```

---

## 3. Inventário de riscos no diff

```
@canary_deploy.py @mapa_riscos.md

Liste cada risco visível no diff do PR:

- trecho → tipo → severidade sugerida → impacto se for para produção.

Não proponha refactor completo ainda.
```

---

## 4. Cruzar com Copilot e scanners

```
Cole achados do Copilot Code Review e de scanners (se houver) no PR.

@mapa_riscos.md

Para cada risco do inventário:
- foi sinalizado por alguma ferramenta?
- preencha a coluna "Quem detectou?".

Identifique lacunas na seção correspondente do mapa.
```

---

## 5. Bloqueante vs aceitável

```
@mapa_riscos.md

Quais riscos **bloqueiam** merge e quais poderiam seguir com mitigação documentada?

Justifique com impacto operacional — não com preferência de estilo.
```

---

## 6. Comentário humano de risco

```
Escolha o risco mais crítico do PR.

Redija um comentário no GitHub no formato:

trecho → risco em produção → ação pedida ao autor.

Tom profissional; uma ação clara.
```

---

## 7. Síntese

```
@mapa_riscos.md

Em 4 bullets: o que aprendeu sobre **detecção** de riscos neste PR?

Inclua: risco mais crítico, lacuna de ferramenta, um falso alarme evitado e critério de bloqueio.
```

## Comandos úteis

```bash
cd aula-04
python example.py
```

**Git (caminho completo a partir da raiz do repositório):**

```bash
git add automacao-e-devops-inteligente/aula-04/
```

---

## Máxima da aula

**Risco não some porque o CI ficou verde — quem revisa o PR nomeia o impacto e decide o que bloqueia merge.**
