Cole o texto abaixo no chat para gerar uma skill de arquitetura:

```
$skillcreator crie uma skill que faz exatamente isso:

Sempre que esta skill for ativada, siga rigorosamente estas instruções:

1. **Separação de Camadas**: 
   - Lógica de infraestrutura e chamadas de rede ficam em services/.
   - Lógica de orquestração e retorno de dados ficam em controllers/.
2. **Estilo de Código**:
   - Utilize obrigatoriamente Python Type Hints em todas as funções.
   - Não utilize "Magic Numbers"; defina constantes no topo do arquivo.
3. **Tratamento de Erros**:
   - Toda função de rede deve ter um bloco try/except.
   - Utilize logging em vez de print para mensagens de erro.

O nome dela eh core-architect
4. **Resiliência**:
   - Sempre proponha um valor de fallback para chamadas de API externas.

# Exemplo de Fluxo:
Usuário: "Quero buscar dados de clima."
Agente: Criar WeatherService para o fetch e WeatherController para processar o dado.
```