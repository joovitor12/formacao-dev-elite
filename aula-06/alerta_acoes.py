"""
Módulo de Monitoramento de Ativos Financeiros.
Objetivo: Comparar preços atuais com preços teto e disparar alertas.
"""

from dataclasses import dataclass

@dataclass
class AtivoFinanceiro:
    ticker: str
    preco_atual: float
    preco_teto: float


class MonitorPrecos:
    def __init__(self, lista_ativos: list[AtivoFinanceiro]):
        self.lista_ativos = lista_ativos

    def verificar_oportunidades(self):
        for ativo in self.lista_ativos:
            if ativo.preco_atual < ativo.preco_teto:
                print(f"Oportunidade: {ativo.ticker} está abaixo do teto! Preço atual: {ativo.preco_atual}, Teto: {ativo.preco_teto}")


# Exemplo de uso
if __name__ == "__main__":
    ativos = [
        AtivoFinanceiro(ticker="AAPL", preco_atual=150.0, preco_teto=155.0),
        AtivoFinanceiro(ticker="GOOGL", preco_atual=2800.0, preco_teto=2750.0),
        AtivoFinanceiro(ticker="AMZN", preco_atual=3400.0, preco_teto=3500.0)
    ]

    monitor = MonitorPrecos(lista_ativos=ativos)
    monitor.verificar_oportunidades()

