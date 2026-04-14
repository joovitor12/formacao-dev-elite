# Quiz: domínio de IDEs AI-native
## Questões

### 1. Em IDEs AI-native (ex.: Cursor), o uso de `@arquivo` ou anexos de contexto serve principalmente para…

- A) Aumentar o tamanho do repositório no disco.  
- B) Restringir e direcionar o que o modelo “vê”, melhorando precisão e reduzindo ruído.  
- C) Substituir o versionamento Git.  
- D) Desativar o linter do projeto.

---

### 2. Qual prática reduz risco ao pedir alterações grandes com IA?

- A) Pedir “refatore o projeto inteiro” em um único prompt.  
- B) Dividir em passos lógicos (ex.: schema → serviço → rota) e revisar cada etapa.  
- C) Desligar os testes para o diff aplicar mais rápido.  
- D) Aceitar o diff sem ler se o chat parece confiante.

---

### 3. Sobre dados sensíveis (tokens, senhas, PII) no chat da IDE com IA, a postura recomendada é…

- A) Colar `.env` completo para o modelo “entender melhor”.  
- B) Não expor segredos nem dados reais de clientes; usar exemplos fictícios ou trechos anonimizados.  
- C) Enviar só se a sessão for “privada”.  
- D) Confiar que o provedor nunca armazena nada.

---

### 4. “Alucinação” no contexto de assistentes de código refere-se a…

- A) Bug de syntax highlight.  
- B) O modelo produzir informação plausível porém incorreta ou inexistente (API, versão, comportamento).  
- C) Falha exclusiva de compilação C++.  
- D) Lentidão da rede na IDE.

---

### 5. Rodar testes e linter antes de aceitar um diff gerado por IA é importante porque…

- A) Valida comportamento e estilo; a IA pode introduzir regressões ou violar convenções.  
- B) Só importa em projetos sem Git.  
- C) Substitui a necessidade de code review humano.  
- D) É obrigatório apenas em linguagens dinâmicas.

---

### 6. Em fluxo profissional, quem permanece responsável por decisões de arquitetura e trade-offs de longo prazo?

- A) Somente o modelo, se o prompt for detalhado.  
- B) O time humano (desenvolvedores, tech lead, produto), com a IA como apoio.  
- C) O CI/CD, automaticamente.  
- D) O cliente final, via e-mail.

---

### 7. Instruções persistentes (ex.: rules, skills, AGENTS no repositório) ajudam a IA a…

- A) Ignorar o `pyproject.toml`.  
- B) Alinhar padrões do projeto (estilo, camadas, o que não fazer) sem repetir tudo em todo prompt.  
- C) Remover a necessidade de documentação oficial das bibliotecas.  
- D) Desativar testes automatizados.

---

### 8. Quando o código gerado é crítico (auth, pagamentos, criptografia), o uso de IA deve ser tratado como…

- A) Substituto de auditoria de segurança e threat modeling.  
- B) Ferramenta de rascunho/aceleração; revisão cuidadosa, referências oficiais e validação humana continuam essenciais.  
- C) Fonte única de verdade sem verificação.  
- D) Opcional apenas para juniors.

---

### 9. Pedir “só o mínimo de contexto” (arquivos estritamente necessários) tende a…

- A) Impedir o uso de `@`.  
- B) Melhorar foco da resposta e reduzir respostas genéricas ou inconsistentes com o restante do código.  
- C) Garantir que o modelo nunca erre.  
- D) Substituir o OpenAPI/Swagger.

---

### 10. Uma limitação recorrente de assistentes integrados à IDE é…

- A) Não conseguirem editar arquivos.  
- B) Não substituírem conhecimento de domínio do negócio, compliance e ambiente de produção específico da empresa.  
- C) Funcionarem apenas offline.  
- D) Proibirem o uso de Git.

---

## Gabarito

| # | Resposta correta |
|---|------------------|
| 1 | **B** |
| 2 | **B** |
| 3 | **B** |
| 4 | **B** |
| 5 | **A** |
| 6 | **B** |
| 7 | **B** |
| 8 | **B** |
| 9 | **B** |
| 10 | **B** |

---

## Justificativas

1. **B** — Contexto seletivo (`@`, pastas, trechos) limita o que entra no prompt: menos ruído, mais chance de a resposta respeitar o código real e o escopo pedido.

2. **B** — Alterações incrementais com revisão entre passos reduzem diffs gigantes difíceis de auditar e facilitam localizar erros.

3. **B** — Segredos e PII não devem ir para o chat; políticas de retenção e vazamento variam; o risco é sempre do lado de quem cola o dado.

4. **B** — Alucinação é conteúdo bem redigido porém falso ou impreciso em relação à realidade (docs, APIs, versões).

5. **A** — Testes e linter capturam quebras e desvios de convenção; a IA não garante correção lógica nem aderência ao time.

6. **B** — Arquitetura envolve restrições humanas e organizacionais que o modelo não conhece por completo; a IA sugere, o time decide.

7. **B** — Rules/skills documentam expectativas do projeto de forma reutilizável, aproximando respostas do padrão do time (sem eliminar revisão).

8. **B** — Áreas sensíveis exigem verificação rigorosa e fontes confiáveis; IA acelera rascunho, não substitui análise de risco.

9. **B** — Contexto excessivo dilui o sinal; o mínimo necessário foca o modelo no que importa para aquela mudança.

10. **B** — A IDE com IA não “sabe” regras internas da empresa, contratos, SLAs ou lei aplicável; isso continua com pessoas e processos.
