# 🛡️ Guia de Governança: GitHub Copilot (Ou outros plugins e agentes de IA para código)

Para atuar como um **Desenvolvedor de Elite**, você deve configurar seu ambiente para evitar riscos legais e de segurança.

### 🔧 Configurações Recomendadas (GitHub Settings)

1. **Filtro de Código Público:** - Opção: *Suggestions matching public code*.
   - **Status:** `Block`. 
   - **Por que?** Evita que o Copilot sugira trechos de código protegidos por licenças restritivas (GPL, etc).

2. **Privacidade de Telemetria:**
   - Opção: *Allow GitHub to use my code snippets for product improvements*.
   - **Status:** `Unchecked` (Desmarcado).
   - **Por que?** Garante que seu código proprietário não seja enviado para treinar os modelos globais da OpenAI/GitHub.

### 🚫 Limitações Técnicas do Copilot

* **Data Cutoff:** O modelo tem uma data de corte. Bibliotecas lançadas ou atualizadas recentemente podem ter sugestões erradas.
* **Contexto Limitado:** Ele lê o `@workspace`, mas pode se perder em projetos gigantescos, gerando inconsistências entre arquivos distantes.
* **Segurança Reativa:** Ele possui filtros para não sugerir segredos, mas não impede você de escrever práticas inseguras (como não validar inputs).

### 📋 Checklist de Segurança
- [ ] O `.env` está no `.gitignore`?
- [ ] O código gerado foi validado em um ambiente de testes?
- [ ] As bibliotecas sugeridas estão nas versões corretas do seu `requirements.txt`?
- [ ] O "Public Code Filter" está ativado?