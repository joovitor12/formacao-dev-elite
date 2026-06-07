# Aula 01 — O papel do code review moderno

**Objetivo:** entender o papel da **revisão de PR com IA** — abrir um PR real sobre `deploy_notifier.py`, rodar **GitHub Copilot Code Review** e complementar com julgamento humano.

**Ferramenta:** GitHub (PR + Copilot Code Review).

**Material:**

| Arquivo | Papel |
| -------- | ------ |
| `deploy_notifier.py` | Código simples com code smells para revisar em PR. |
| `registro_revisao.md` | Registrar achados e veredito após o Copilot. |
| `example.py` | Executar comportamento atual. |

**Fluxo em sala:**

1. Abrir branch e PR com mudança em `deploy_notifier.py` (correção, feature ou refactor — o diff é o material).
2. Ativar **Copilot Code Review** no PR.
3. Preencher `registro_revisao.md` cruzando sugestões do Copilot com sua análise.
4. Discutir: o que aprovar, pedir mudança ou classificar como nit/falso positivo.

---

## 1. Inventário de smells (preparação ao diff)

```
@deploy_notifier.py

Liste code smells e riscos (segurança, operação, manutenção).

Formato: smell → trecho → risco → severidade sugerida.

Não proponha refatoração completa ainda.
```

---

## 2. Depois do Copilot Code Review no PR

```
Cole aqui os comentários/sugestões que o Copilot gerou no PR.

Para cada achado do Copilot:
- concordo / discordo / parcial;
- severidade final (bloqueante / deve / sugestão / nit);
- comentário que você deixaria no GitHub.

Não implemente código.
```

---

## 3. Comentários acionáveis

```
Com base no diff do PR e no Copilot:

Redija 3 comentários no estilo GitHub review (tom profissional).

Cada um: trecho → risco → ação pedida ao autor.
```

---

## 4. Veredito humano

```
@registro_revisao.md

Sugira veredito final do PR e top 2 pontos bloqueantes (se houver).

Há sugestão do Copilot que você trataria como falso positivo?
```

---

## 5. Armadilha: CI verde = PR aprovado?

```
O PR passou no CI mas o Copilot (ou você) apontou token em log e notificação sempre ativa.

Por que "build verde" não basta para merge?

Resposta em bullets — sem código.
```

## Comandos úteis

```bash
cd aula-01
python example.py
```

---

## Máxima da aula

**Copilot acelera a leitura do diff — o revisor humano prioriza riscos e decide o merge.**
