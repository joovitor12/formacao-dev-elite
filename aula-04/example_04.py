# Crie uma função que recebe um texto de notícia financeira e:
# 1. Utilize a biblioteca 'langchain' para invocar o modelo GPT-4.
# 2. Use um System Message instruindo a IA a ser um analista sênior.
# 3. O output deve ser obrigatoriamente um JSON com as chaves 'sentimento' e 'impacto_mercado'.
def analisar_noticias(texto_noticia):
    import json
    from langchain_openai import ChatOpenAI
    from langchain_core.messages import SystemMessage, HumanMessage

    # Configura o modelo GPT-4
    modelo = ChatOpenAI(model="gpt-4", temperature=0.1)

    # Define a mensagem do sistema para instruir a IA
    system_message = SystemMessage(
        content="Você é um analista financeiro sênior. Analise a notícia financeira e forneça APENAS um JSON válido com as chaves 'sentimento' (positivo, negativo ou neutro) e 'impacto_mercado' (alto, médio ou baixo). Não inclua texto adicional, apenas o JSON."
    )

    # Cria a mensagem de entrada para o modelo
    human_message = HumanMessage(content=f"Notícia: {texto_noticia}")

    # Chama o modelo com as mensagens
    mensagens = [system_message, human_message]
    resposta = modelo.invoke(mensagens)

    try:
        # Tenta fazer parse do JSON da resposta
        resultado_json = json.loads(resposta.content)
        return resultado_json
    except json.JSONDecodeError:
        # Se não conseguir fazer parse, retorna a resposta bruta
        return {"erro": "Resposta não está em formato JSON válido", "resposta_bruta": resposta.content}


# Exemplo de uso:
if __name__ == "__main__":
    noticia = "A empresa XYZ anunciou um aumento significativo nos lucros do último trimestre, superando as expectativas dos analistas."
    try:
        resultado = analisar_noticias(noticia)
        print("Resultado da análise:")
        print(f"Sentimento: {resultado.get('sentimento', 'N/A')}")
        print(f"Impacto no mercado: {resultado.get('impacto_mercado', 'N/A')}")
        print("\nResposta completa:")
        print(resultado)
    except Exception as e:
        print(f"Erro ao analisar notícia: {e}")