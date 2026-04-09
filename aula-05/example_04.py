
import requests
import logging
from requests.exceptions import RequestException

def buscar_cotacao(ticker):
    url = f"https://api.exemplo.com/quote/{ticker}"
    for tentativa in range(2):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            logging.error(f"Erro ao buscar cotação para {ticker} (tentativa {tentativa+1}): {e}")
            if tentativa == 1:
                return None