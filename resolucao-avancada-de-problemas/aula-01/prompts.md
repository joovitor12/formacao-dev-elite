# Aula 36 — Prompts para colar no chat do agente (Copilot, Cursor, etc.)

**Como usar:** copie o bloco que fizer sentido no momento, cole no chat, e **complete** entre colchetes `[]` com o erro, arquivo ou trecho real do seu projeto.

---

## 1. Antes de pedir correção (causa raiz)

```
Não quero que você corrija o código agora. Com base no contexto do meu workspace/projeto, explique a causa raiz deste erro e o caminho lógico que leva até ele.

Erro (mensagem completa / stack trace):
[cole aqui]

Trecho relevante (ou arquivo @arquivo):
[cole ou referencie]
```

---

## 2. Ciclo: Observação → Interrogação → Reflexão

### Interrogação (em vez de “conserta para mim”)

```
O estado atual do sistema (código + erro abaixo) o que indica sobre a origem deste problema? Liste hipóteses ordenadas da mais provável para a menos provável e diga o que eu deveria verificar em cada uma.

Erro:
[cole aqui]

Contexto:
[cole trecho ou @arquivo]
```

### Reflexão (alinhar com regra de negócio)

```
Sua sugestão faz sentido para a regra de negócio a seguir?
[descreva em 2–5 frases o comportamento esperado]

Se houver trade-offs (performance, segurança, consistência), liste-os antes de recomendar uma mudança.
```

---

## 3. Técnicas de investigação (extrair inteligência, não só código)

### Explicação de fluxo (onde o dado nasce, onde pode corromper)

```
@workspace Explique como o dado [NOME_DO_CAMPO_OU_VARIÁVEL] chega até [NOME_DA_FUNÇÃO_OU_ARQUIVO] e em quais pontos do caminho ele pode estar sendo alterado, perdido ou mal tipado. Cite arquivos/funções específicos do projeto quando possível.
```

### Análise de mudança recente (ex.: schema Pydantic)

```
Recentemente alterei [O_QUE_MUDOU — ex.: schema Pydantic / contrato de API / modelo de dados]. Como essa mudança pode explicar o erro de validação (ou comportamento) abaixo? Relacione campos, tipos opcionais/obrigatórios e valores default.

Erro:
[cole aqui]

Trecho do schema/modelo atual:
[cole ou @arquivo]
```

### Verificação de invariantes (ex.: função assíncrona + estrutura mutável)

```
Nesta função assíncrona [NOME], quais condições devem ser sempre verdadeiras para que [estrutura — ex.: “este dicionário não mude de tamanho de forma inesperada” / “esta lista não tenha duplicatas”]?

Aponte race conditions ou uso compartilhado de estado que possam violar essas invariantes.
```

---

## 4. Checklist rápido (“filtro de elite”) antes de aceitar patch da IA

- A correção **elimina o sintoma** ou **corrige a causa**?
- Introduz **risco de segurança** (dados sensíveis, validação fraca, `eval`, SQL, permissões)?
- Mantém **compatibilidade** com o restante do sistema (API, banco, filas)?
- Existe um **teste mínimo** ou cenário manual que prova o comportamento certo?

---

## Máxima da aula

**A IA acelera o diagnóstico, mas a responsabilidade do tratamento é do engenheiro.**
