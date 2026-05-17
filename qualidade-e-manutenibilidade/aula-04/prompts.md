# Aula 04 — Separação de responsabilidades

**Objetivo:** reconhecer quando um módulo acumula papéis demais e **separar responsabilidades** em unidades menores, com orquestração fina e testes preservando o contrato público.

**Ferramenta:** GitHub Copilot Chat / Explorer (ou agente equivalente com `@workspace`).

**Material sugerido:**

| Caminho | Papel |
| -------- | ------ |
| `pre-changes/` | Ambiente de trabalho: `pedido_flow.py` monolítico + testes verdes. |
| `pedido_flow.py` (raiz) | Referência do baseline antes da separação. |
| `test_pedido_flow.py` | Contrato via `processar_pedido` — não quebre a assinatura. |

**Como usar:** trabalhe em **`pre-changes/`**. Extraia **uma responsabilidade por vez** (validação → preço → persistência → notificação). Mantenha `processar_pedido` como fachada fina no final.

---

## 1. Mapear responsabilidades no monólito

```
@pre-changes/pedido_flow.py

Liste cada responsabilidade distinta escondida em processar_pedido:

- validação de entrada
- cálculo de preço / desconto / taxa
- persistência
- notificação
- orquestração do fluxo

Para cada uma: trecho (função/bloco) e por que deveria ser outro módulo.

Não escreva código ainda.
```

---

## 2. Ordem segura de extração

```
@pre-changes/pedido_flow.py @pre-changes/test_pedido_flow.py

Sugira a ordem ideal para extrair módulos (4 passos) minimizando risco.

Para cada passo:
- arquivo novo sugerido;
- funções que saem;
- o que permanece em pedido_flow.py;
- qual teste rodar para validar.
```

---

## 3. Extrair validação (primeiro passo típico)

```
@pre-changes/pedido_flow.py

Proponha extrair APENAS validação para um arquivo validacao.py com função pura
(ex.: validar_pedido(payload) -> list[str] de erros).

processar_pedido deve continuar com a mesma assinatura e os testes devem passar.

Mostre esboço de código, não refatore o arquivo inteiro de uma vez.
```

---

## 4. Orquestrador fino

```
Após separar validação, preço, persistência e notificação, como deve ficar processar_pedido?

Descreva em pseudocódigo de 8–12 linhas: só coordena chamadas, sem regra de negócio inline.

@pre-changes/pedido_flow.py
```

---

## 5. IA como revisor de fronteiras

```
Revise a separação atual em pre-changes/:

- algum módulo ainda mistura duas responsabilidades?
- há dependência circular entre arquivos?
- processar_pedido ainda é a única entrada pública para os testes?

Responda em bullets com severidade (baixa/média/alta).

@pre-changes/
```

---

## 6. Contrato entre módulos

```
Sem implementar, defina contratos mínimos entre os módulos extraídos:

- entradas e saídas de cada função pública;
- o que NÃO pode vazar (ex.: print de notificação dentro do cálculo de preço).

Use linguagem natural + tipos Python quando ajudar.
```

---

## Comandos úteis

```bash
cd pre-changes
pytest -q
python example.py
```

---

## Máxima da aula

**Um módulo, um motivo para mudar.** Separação de responsabilidades reduz acoplamento e deixa cada parte testável — a orquestração só liga as peças.
