# 🤝 Orquestração Humano + Agente (HITL)

O conceito de **Human-in-the-Loop** garante que a Inteligência Artificial trabalhe sob a supervisão e diretrizes de um especialista humano.

### As 3 Camadas de Controle do Desenvolvedor:

1. **Diretriz Estratégica (The Why):** O agente não sabe o contexto do negócio. Você define se o projeto precisa de performance extrema ou entrega rápida.
   
2. **Validação Técnica (The How):** O agente pode sugerir padrões genéricos. Você impõe o uso de `asyncio`, `Pydantic` ou a arquitetura `Service/Controller` que definimos nas Skills.

3. **Code Review Ativo (The Check):** Nunca aceite um "Apply" do agente sem ler. Verifique:
   - Tratamento de exceções.
   - Segurança de chaves e variáveis de ambiente.
   - Eficiência de loops.

### Comandos de Orquestração:
- **Interrupção:** "Pare o plano. Antes de seguir, verifique se a biblioteca X é compatível com nossa versão do Python."
- **Refinamento:** "Refatore o que você acabou de escrever, mas aplique o padrão SOLID no Service."
- **Contextualização (Mensagem pro agente, passando o contexto):** "Considere que este projeto rodará em um ambiente serverless."