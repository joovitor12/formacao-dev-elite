def aplicar_desconto(valor: float, taxa: float) -> float:
    if taxa < 0 or taxa > 1:
        raise ValueError("A taxa deve estar entre 0 e 1")
    return valor * (1 - taxa)


import pytest

def test_aplicar_desconto_sucesso():
    assert aplicar_desconto(100.0, 0.2) == 80.0

def test_aplicar_desconto_taxa_zero():
    assert aplicar_desconto(50.0, 0.0) == 50.0

def test_aplicar_desconto_taxa_negativa():
    with pytest.raises(ValueError):
        aplicar_desconto(100.0, -0.1)