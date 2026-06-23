# Padrão de código — Entrega Profissional

Documento de referência do time. **Toda implementação com IA deve citar este arquivo** (`@padrao_codigo.md`) nos prompts.

## 1. Nomenclatura

- Módulos e funções: `snake_case` em português claro (`notificar_entrega`, `validar_payload`).
- Constantes de módulo: `UPPER_SNAKE_CASE` (`LIMITE_TENTATIVAS`, `CANAL_PADRAO`).
- Variáveis locais: `snake_case`; evitar abreviações obscuras (`qtd` → `quantidade`).
- Proibido: `camelCase`, prefixo húngaro (`strNome`), nomes de uma letra exceto em loops curtos.

## 2. Tipagem

- Funções públicas do módulo: **type hints** em parâmetros e retorno.
- Retorno de operações de negócio: `dict[str, Any]` no formato de contrato abaixo.
- Evitar `Any` em domínio quando um `TypedDict` ou union fechada for suficiente.

## 3. Contrato de retorno (API interna)

Funções que executam fluxo de entrega retornam:

```python
{"ok": bool, "avisos": list[str], ...campos opcionais}
```

- `ok=True` só quando a operação concluiu conforme regra.
- Falhas de validação preenchem `avisos` com mensagens curtas e acionáveis — **sem** exceção para fluxo esperado.

## 4. Docstrings

- Funções públicas: docstring de **uma linha** descrevendo efeito + entradas/saída quando não óbvio.
- Módulo: docstring no topo explicando responsabilidade.

## 5. Estrutura e tamanho

- Uma função = uma responsabilidade.
- Funções públicas: preferir **até 25 linhas**; extrair validação e formatação.
- Validação de entrada em função dedicada (`validar_*`) quando houver mais de duas regras.

## 6. Constantes e números mágicos

- Limites, timeouts e códigos repetidos viram constantes nomeadas no topo do módulo.
- Proibido literal “solto” com significado de negócio no meio da função.

## 7. Logging e efeitos colaterais

- Registrar eventos operacionais com `logging` (módulo `logger = logging.getLogger(__name__)`).
- Proibido `print` em caminho de produção/simulação de entrega.
- Não logar segredos, tokens ou PII completa.

## 8. Tratamento de erros

- Proibido `except:` ou `except Exception:` sem re-raise ou registro explícito.
- Erros esperados → `avisos` no retorno; erros inesperados → log + propagar ou encapsular com mensagem clara.

## 9. Testabilidade

- Funções puras de validação e formatação **sem** I/O quando possível.
- Efeitos (log, envio) isolados em funções pequenas chamadas pela orquestração.

## 10. Prompts com IA

Ao pedir código ao Copilot ou agente:

1. Anexar `**@padrao_codigo.md`** e o arquivo alvo.
2. Declarar: *“Siga estritamente padrao_codigo.md; não invente outro estilo de retorno ou nomenclatura.”*
3. Revisar diff contra este documento **antes** de aceitar.

