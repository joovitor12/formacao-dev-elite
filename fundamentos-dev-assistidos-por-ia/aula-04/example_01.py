from dataclasses import dataclass
from datetime import date
from enum import Enum


class TipoAtivo(Enum):
    ACOES = "Acao"
    FII = "Fundo Imobiliario"
    RF = "Renda Fixa"


# Cria uma classe de dados para Invesimento que contenha:
# id (uuid), ticker (str), valor_compra(float), data_compra (date), tipo (TipoAtivo)
@dataclass
class Investimento:
    id: str
    ticker: str
    valor_compra: float
    data_compra: date
    tipo: TipoAtivo