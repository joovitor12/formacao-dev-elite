Checklist Dev de Elite:

1. Compliance e Regras de Negócio: A IA nao reconhece LGPD ou as regras de negocio da sua empresa ou time, como desenvolvedor, voce precisa dominar essas regras e delegar o que for tecnico para o seu agente
2. Arquitetura de Longo Prazo: A IA sugere o "padrão médio" da internet. Decisões entre Monólito vs. Microserviços exigem visão de futuro que o modelo não possui.
3. Segurança (Secrets): Jamais forneça chaves de API, tokens ou dados reais de usuários no contexto. Use sempre dados fictícios.
4. Código "Caixa Preta": Se você não consegue explicar o diff gerado, você não deve aceitá-lo. O "verde" no teste não garante que a lógica está correta para o negócio.
5. Domínios Obscuros ou Legados: Em bibliotecas muito antigas ou nichadas, o Cursor tende a alucinar métodos que não existem. Sempre valide na documentação oficial.
6. Performance de Produção: A IA foca em "fazer funcionar". Profiling de memória, timeouts e limites de concorrência continuam sendo trabalho humano.
7. Consistência de Estilo: Sem diretrizes (.cursor/rules), a IA pode refatorar arquivos inteiros desnecessariamente. Mantenha o escopo curto.