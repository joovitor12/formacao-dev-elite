from models import Investimento

def calcular_juros_com_taxa(investimento: Investimento, taxa: float) -> float:
    """
    Calcula o valor do investimento após aplicar juros compostos mensais.

    Args:
        investimento (Investimento): O investimento para o qual calcular os juros.
        taxa (float): A taxa de juros mensal a ser aplicada (em percentual).

    Returns:
        float: O valor do investimento após aplicar os juros.
    """

    if not isinstance(investimento.valor_inicial, (int, float)):
        raise TypeError("O valor do investimento deve ser numérico.")
    if investimento.valor_inicial == 0:
        raise ValueError("O valor principal do investimento não pode ser zero.")

    meses = investimento.meses
    if not isinstance(meses, int) or meses < 0:
        raise ValueError("O número de meses deve ser um inteiro não negativo.")

    # Juros compostos mensais
    montante = investimento.valor_inicial * ((1 + taxa / 100) ** meses)
    return montante


# Função para descontar IR sobre o lucro
def descontar_ir(valor_inicial: float, valor_final: float, meses: int) -> float:
    """
    Desconta o imposto de renda sobre o lucro do investimento.
    15% sobre o lucro se tempo > 12 meses, 20% se <= 12 meses.
    """
    lucro = valor_final - valor_inicial
    if lucro <= 0:
        return valor_final
    if meses > 12:
        ir = 0.15 * lucro
    else:
        ir = 0.20 * lucro
    return valor_final - ir

## Exemplo de uso

# Testes unitários
import unittest

class DummyInvestimento:
    def __init__(self, valor_inicial, meses, taxa_anual=0, ticker="TEST"):
        self.valor_inicial = valor_inicial
        self.meses = meses
        self.taxa_anual = taxa_anual
        self.ticker = ticker

class TestEngine(unittest.TestCase):
    def test_calcular_juros_com_taxa_basico(self):
        investimento = DummyInvestimento(1000, 12)
        taxa = 1 # 1% ao mês
        esperado = 1000 * ((1 + 0.01) ** 12)
        resultado = calcular_juros_com_taxa(investimento, taxa)
        self.assertAlmostEqual(resultado, esperado, places=2)

    def test_calcular_juros_com_taxa_zero(self):
        investimento = DummyInvestimento(1000, 0)
        taxa = 1
        esperado = 1000
        resultado = calcular_juros_com_taxa(investimento, taxa)
        self.assertEqual(resultado, esperado)

    def test_calcular_juros_com_taxa_valor_inicial_zero(self):
        investimento = DummyInvestimento(0, 12)
        with self.assertRaises(ValueError):
            calcular_juros_com_taxa(investimento, 1)

    def test_calcular_juros_com_taxa_tipo_invalido(self):
        investimento = DummyInvestimento("mil", 12)
        with self.assertRaises(TypeError):
            calcular_juros_com_taxa(investimento, 1)

    def test_calcular_juros_com_taxa_meses_negativo(self):
        investimento = DummyInvestimento(1000, -1)
        with self.assertRaises(ValueError):
            calcular_juros_com_taxa(investimento, 1)

    def test_descontar_ir_maior_12_meses(self):
        valor_inicial = 1000
        valor_final = 2000
        meses = 13
        lucro = valor_final - valor_inicial
        esperado = valor_final - 0.15 * lucro
        resultado = descontar_ir(valor_inicial, valor_final, meses)
        self.assertAlmostEqual(resultado, esperado, places=2)

    def test_descontar_ir_menor_igual_12_meses(self):
        valor_inicial = 1000
        valor_final = 2000
        meses = 12
        lucro = valor_final - valor_inicial
        esperado = valor_final - 0.20 * lucro
        resultado = descontar_ir(valor_inicial, valor_final, meses)
        self.assertAlmostEqual(resultado, esperado, places=2)

    def test_descontar_ir_sem_lucro(self):
        valor_inicial = 1000
        valor_final = 900
        meses = 10
        resultado = descontar_ir(valor_inicial, valor_final, meses)
        self.assertEqual(resultado, valor_final)

if __name__ == "__main__":
    unittest.main()