# 🎯 Desafio: To-Do List com Performance "Vercel Standard"

**Objetivo:** Construir uma aplicação de tarefas usando Next.js, mas com um diferencial: todo o código será auditado por uma Skill de performance profissional.

### 🛠️ Stack & Ferramentas
- **Framework:** Next.js (App Router)
- **UI:** shadcn/ui
- **Skill Engine:** `skill.sh`
- **Skill:** `vercel-react-best-practices`

### 🚀 Requisitos do Exercício
1. **Instalação da Skill**: Usar o terminal para instalar a skill oficial da Vercel.
2. **Setup Assistido**: O agente deve criar a estrutura respeitando regras de `bundle-size` e `async-parallel`.
3. **Componentes shadcn**: Implementar a UI garantindo que não haja re-renders desnecessários (seguindo a regra `rerender-memo`).
4. **Persistência**: Criar um serviço de storage que siga a regra `client-localstorage-schema`.

### 🤖 Comando de Ativação
Você deverá rodar o comando de instalação e garantir que o agente aplique as regras durante a geração do código.