# Aula 05 — Visão geral do projeto

**Objetivo:** alinhar **escopo, arquitetura e mapa das trilhas** do MVP Chatbot (Parlant + OpenRouter `openrouter/owl-alpha`) antes de implementar.

**Enquadramento:** o projeto final **reutiliza** práticas de fundamentos, qualidade, automação/DevOps, entrega profissional e resolução de problemas — sem reimplementar cada trilha do zero. Esta aula fixa a visão; código do servidor vem nas entregas seguintes.

**Ferramentas:** Copilot Chat / agente com `@workspace`, documentação Parlant, conta OpenRouter.

**Material:**


| Arquivo | Papel |
|---------|--------|
| `visao_geral_projeto.md` | Problema, stack, persona, fluxo — **leitura obrigatória**. |
| `mapa_disciplinas.md` | Como cada trilha do curso se aplica ao MVP. |
| `arquitetura_mvp.md` | Componentes, runtime, OpenRouter, estrutura alvo. |
| `escopo_mvp.md` | Must have / won't have / Definition of Done. |
| `padrao_projeto_mvp.md` | Contrato de código do MVP — anexar em prompts futuros. |
| `registro_visao_geral.md` | Entregável: síntese, riscos, perguntas de teste. |
| `.env.example` | Template de variáveis (OpenRouter). |
| `example.py` | Smoke: documentação base presente. |


**Fluxo em sala:**

1. Ler `visao_geral_projeto.md` e discutir persona + limites do agente.
2. Cruzar trilhas em `mapa_disciplinas.md` → `registro_visao_geral.md` §2.
3. Validar escopo e arquitetura → §3 e §4.
4. Configurar `.env` (local) e registrar riscos → §5.
5. Rodar `python example.py`.

---

## 1. Ler a visão geral

```
@visao_geral_projeto.md

Resuma em 5 bullets: problema, Parlant, OpenRouter/owl-alpha, persona, próximo passo.

Destaque o que diferencia Parlant de “só um prompt no ChatGPT”.
```

---

## 2. Mapa das trilhas

```
@mapa_disciplinas.md @registro_visao_geral.md

Para cada disciplina do curso:

- qual artefato do MVP ela impacta?
- uma pergunta-guia que você faria no review.

Preencha a tabela da seção 2 do registro.

Não escreva código ainda.
```

---

## 3. Escopo e arquitetura

```
@escopo_mvp.md @arquitetura_mvp.md

Liste 3 itens must-have que você priorizaria na primeira sprint.

Desenhe (texto ou mermaid) o caminho: usuário → Parlant → OpenRouter.

Registre na seção 3 do dossiê.

Identifique 2 riscos (segurança, operação, alucinação).
```

---

## 4. Padrão do MVP

```
@padrao_projeto_mvp.md

Quais 4 regras deste padrão você já aplicaria no primeiro commit do servidor?

Compare com o que você lembra da trilha de entrega profissional (padrão, lint, pipeline).

Preencha seção 4 do registro.
```

---

## 5. Preparar ambiente OpenRouter

```
@.env.example

Explique como obter OPENROUTER_API_KEY sem expor a chave no chat.

Copie .env.example → .env localmente (não commitar).

Opcional — validar provider fora do Parlant:

curl https://openrouter.ai/api/v1/models -H "Authorization: Bearer $OPENROUTER_API_KEY"

Registre na seção 5 do registro se a chave está configurada (sim/não — sem colar a key).
```

---

## 6. Síntese com IA

```
@visao_geral_projeto.md @escopo_mvp.md @mapa_disciplinas.md

Proponha 5 perguntas de teste para o sandbox (onboarding da formação).

Formato: pergunta → resposta esperada (comportamento, não texto literal).

Preencha seção 6 do registro.
```

---

## Comandos úteis

```bash
cd entrega-profissional-e-padronizacao-de-codigo-com-ia/aula-05
cp .env.example .env   # editar localmente
python example.py
```

Documentação Parlant: https://parlant.io/docs/quickstart/installation

---

## Máxima da aula

**Visão alinhada antes de código — o MVP integra trilhas; Parlant governa comportamento; OpenRouter fornece inferência.**
