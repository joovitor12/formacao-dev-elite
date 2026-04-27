# 🎯 Desafio: Arquitetura e Integração de APIs Públicas

**Objetivo:** Evoluir um script simples para uma aplicação estruturada, integrando duas fontes de dados externas e aplicando padrões de projeto (Controllers e Services) via Prompt Inline.

### 📝 O Cenário
Você recebeu um protótipo funcional que consulta o preço do Bitcoin em Dólar. Sua missão é transformar esse protótipo em uma aplicação robusta que também consulta a cotação atualizada do Dólar para Real (BRL) e apresenta o valor convertido, seguindo uma arquitetura profissional.

### 🚀 APIs Utilizadas (Gratuitas e Abertas)
1.  **Mercado Bitcoin**: `https://www.mercadobitcoin.net/api/BTC/ticker/`
2.  **AwesomeAPI**: `https://economia.awesomeapi.com.br/json/last/USD-BRL`

### 🏗️ Requisitos do Desafio
1.  **Integração de Câmbio**: Criar uma nova funcionalidade para buscar a cotação de USD para BRL.
2.  **Lógica de Conversão**: Implementar o cálculo que transforma o valor de BTC (USD) para BRL.
3.  **Resiliência**: Adicionar tratamento de erro (`try/except`) com um valor de **fallback** (ex: 5.0) para o câmbio, caso a API falhe.
4.  **Padronização de Arquitetura**: Refatorar o código separando as responsabilidades (Utilizando algum framework web da sua escolha (ex: *FastAPI*)):
    * **Services**: Camada responsável pelas requisições HTTP e extração de dados brutos.
    * **Controllers**: Camada que orquestra os serviços, realiza os cálculos e formata os dados para o usuário.

### 🤖 Regras do Jogo
* Utilize o **Prompt Inline (Ctrl + I)** para realizar todas as refatorações e adições.
* Não escreva a estrutura de classes ou métodos manualmente; guie a IA através de comandos claros.

---

### 💻 Código Base (Exemplo em Python, também é liberado fazer em outra linguagem da sua escolha)

Crie um arquivo chamado `main.py`, cole o código abaixo e utilize-o como ponto de partida:

```python
import requests

def buscar_preco_btc_usd():
    """Busca o preço do Bitcoin em USD na API do Mercado Bitcoin"""
    url = "https://www.mercadobitcoin.net/api/BTC/ticker/"
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL" ## API de Pesquisa da cotação do dólar
    response = requests.get(url)
    dados = response.json()
    # O preço de venda (last) vem como string nesta API
    return float(dados['ticker']['last'])

if __name__ == "__main__":
    preco_usd = buscar_preco_btc_usd()
    print(f"Preço atual do BTC: $ {preco_usd}")