import requests


def buscar_preco_btc_usd_service():
    """Busca o preço do Bitcoin em USD na API do Mercado Bitcoin"""
    url = "https://www.mercadobitcoin.net/api/BTC/ticker/"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        dados = response.json()
        return float(dados['ticker']['last'])
    except Exception:
        # Valor de fallback caso a API falhe
        return 5.0


def usd_to_brl():
    """Integração de Câmbio: Criar uma nova funcionalidade para buscar a cotação de USD para BRL."""
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        dados = response.json()
        return float(dados['USDBRL']['bid'])
    except Exception:
        # Valor de fallback caso a API falhe
        return 5.0

# Lógica de Conversão: Implementar o cálculo que transforma o valor de BTC (USD) para BRL.
def btc_usd_to_brl():
    preco_btc_usd = buscar_preco_btc_usd_service()
    cotacao_usd_brl = usd_to_brl()
    preco_btc_brl = preco_btc_usd * cotacao_usd_brl
    return preco_btc_brl