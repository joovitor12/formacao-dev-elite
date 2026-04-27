# integra o langfuse aqui para monitorar o desempenho do modelo
from langfuse import Langfuse
# inicializa o Langfuse com a chave de API
langfuse = Langfuse(api_key="sua_chave_de_api_aqui")
# exemplo de função que utiliza o Langfuse para monitorar o desempenho do modelo
def exemplo_funcao():
    # inicia o monitoramento do desempenho do modelo
    with langfuse.monitor("exemplo_funcao"):
        # código da função que utiliza o modelo de linguagem
        resultado = "resultado do modelo de linguagem"
        return resultado