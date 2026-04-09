def calcular_juros_compostos_mensais(valor_inicial, taxa_anual, meses):
    """Calcula o montante final com juros compostos:
    1. Converte a taxa anual para mensal (taxa_anual / 12)
    2. Aplica a formula: M = P * (1 + i)** n
    3. Arredonda o resultado para 2 casas decimais
    4. Retorna um dicionario com o montante e o total de juros ganhos.
    """
    taxa_mensal = taxa_anual / 12
    montante = valor_inicial * (1 + taxa_mensal) ** meses
    montante = round(montante, 2)
    juros = round(montante - valor_inicial, 2)
    return {"montante": montante, "juros": juros}


# Exemplo de uso:
if __name__ == "__main__":
    valor_inicial = 1000.0
    taxa_anual = 0.12  # 12% ao ano
    meses = 24

    resultado = calcular_juros_compostos_mensais(valor_inicial, taxa_anual, meses)
    print(f"Montante final: R$ {resultado['montante']}")
    print(f"Juros ganhos: R$ {resultado['juros']}")