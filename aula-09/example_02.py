# Funcao para classificar o risco de credito de um cliente baseado em dados demograficos
def classificar_risco_credito(dados_cliente):
    # exemplo de classificacao de risco de credito
    if dados_cliente["renda"] < 2000:
        return "alto risco"
    elif dados_cliente["renda"] < 5000:
        return "risco medio"
    else:
        return "baixo risco"