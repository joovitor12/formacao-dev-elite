# Crie um dataclass Investimento (Ticker, Valor Inicial, Taxa Anual, Meses).

from dataclasses import dataclass
@dataclass
class Investimento:
    ticker: str
    valor_inicial: float
    taxa_anual: float
    meses: int