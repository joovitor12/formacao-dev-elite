# Gera um codigo onde eh usado aspas simples para retornar dados
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Acessa a variável de ambiente
api_key = os.getenv("api_key")
# Exibe a chave da API usando aspas simples
print("A chave da API é:", api_key)
