# Checklist de Uso Profissional com Cursor

- **Seleção de contexto:**  
  Anexar apenas os arquivos estritamente necessários (`@items.py`).

- **Fluxo incremental:**  
  Pedir alterações em passos lógicos (*Schema → Service → Rota*).

- **Consistência de padrão:**  
  Exigir que a IA respeite o estilo de código existente (`ruff`, `flake8`, `black`).  
  Tanto via skill do seu agente quanto manualmente no prompt.

- **Loop de correção:**  
  Sempre rodar os testes antes de aceitar o *diff* final.