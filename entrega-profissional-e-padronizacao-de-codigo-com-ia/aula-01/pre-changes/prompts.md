# Aula 01 — Importância do padrão de código

**Objetivo:** entender **por que** um padrão de código existe e como usá-lo como **contrato** ao implementar com IA — a IA acelera o código; o padrão define o que é aceitável no time.

**Enquadramento:** sem padrão explícito, cada prompt gera estilo diferente (nomes, retornos, logging, erros). Documentar o padrão e **referenciá-lo em todo prompt** reduz retrabalho e review surpresa.

**Ferramentas:** Copilot Chat / agente com `@workspace`.

**Material:**

| Arquivo | Papel |
| -------- | ------ |
| `padrao_codigo.md` | **Padrão oficial** do time — anexar em prompts de implementação. |
| `notificacao_entrega.py` | Baseline com **desvios intencionais** do padrão. |
| `registro_padrao_codigo.md` | Auditoria, prompt à IA e conformidade final. |
| `example.py` | Smoke test do baseline. |

**Fluxo em sala:**

1. Ler `padrao_codigo.md` e discutir por que padrão importa.
2. Auditar baseline vs padrão → `registro_padrao_codigo.md` §2.
3. Pedir implementação/refatoração à IA **com** `@padrao_codigo.md` → §3.
4. Revisar diff contra padrão; corrigir desvios → §4.
5. Rodar `python example.py` (ajustar teste se contrato mudar para `ok`/`avisos`).

---

## 1. Por que padrão de código

```
Antes de abrir código, responda em bullets:

- três problemas que aparecem quando cada dev (ou cada prompt de IA) usa estilo próprio;
- diferença entre "código que roda" e "código entregável no padrão do time";
- por que o padrão deve ir **no prompt**, não só no README esquecido.

Não analise notificacao_entrega.py ainda.
```

---

## 2. Ler o padrão

```
@padrao_codigo.md

Resuma em 5 bullets as regras que mais impactam review diário.

Destaque: nomenclatura, contrato de retorno, logging, type hints, tratamento de erros.
```

---

## 3. Auditar baseline

```
@notificacao_entrega.py @padrao_codigo.md @registro_padrao_codigo.md

Compare o baseline ao padrão.

Para cada desvio: trecho → regra (§) → severidade.

Preencha a tabela da seção 2 do registro.

Não refatore ainda.
```

---

## 4. Implementar com IA seguindo o padrão

```
@padrao_codigo.md @notificacao_entrega.py

Refatore notificacao_entrega.py para conformidade com padrao_codigo.md:

- renomear NotificarEntrega → notificar_entrega;
- contrato {"ok", "avisos"} em vez de success/msg;
- type hints, logging, constantes, validar_payload dedicada;
- remover print, bare except e token em log.

Siga ESTRITAMENTE padrao_codigo.md — não invente outro estilo.

Registre prompt e desvios da IA na seção 3 do registro.
```

---

## 5. Revisar conformidade

```
@notificacao_entrega.py @padrao_codigo.md @registro_padrao_codigo.md

Checklist linha a linha contra o padrão.

Preencha seção 4 e marque checklist de entrega.

Ajuste manualmente o que a IA errou.
```

---

## 6. Validar execução

```
Atualize example.py se o contrato mudou para ok/avisos.

python example.py

Registre resultado no registro.
```

---

## 7. Síntese

```
@registro_padrao_codigo.md

Complete o resumo final (3 perguntas).

Em 1 frase: como você vai citar o padrão nos próximos prompts de IA?
```

---

## Comandos úteis

```bash
cd entrega-profissional-e-padronizacao-de-codigo-com-ia/aula-01
python example.py
```

---

## Máxima da aula

**IA gera rápido — padrão explícito no prompt define o que o time aceita entregar.**
