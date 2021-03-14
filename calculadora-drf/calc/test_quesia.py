import pytest
from .tools import NumeroInvalido, somar, dividir

@pytest.mark.parametrize("n1, n2, result", [(5, 7, 12),(3, 3, 6), (7, 4, 11)])
def test_somar_numero_inteiro(n1, n2, result):
    # numero1 = 5
    # numero2 = 7
    # somar = (numero1 + numero2)
    assert somar(n1, n2) == result

def test_mal():
    numero1 = 5
    numero2 = "Quésia"
    # somar = (numero1 + numero2)
    with pytest.raises(NumeroInvalido):   
        somar(numero1, numero2)

def test_float():
    numero1 = 3.5
    numero2 = 6.5
    assert somar(numero1, numero2) == 10

def test_dividir_without_result():
    numero1 = 100
    numero2 = 14
    assert dividir(numero1, numero2)

def test_dividir_with_result():
    numero1 = 3.0
    numero2 = 4
    assert dividir(numero1, numero2) == 0.75

def test_dividir_with_zero_error():
    numero1 = 4.0
    numero2 = 0
    with pytest.raises(ZeroDivisionError):
        dividir(numero1, numero2)

# 1 chamei função
# 2 fiz a conta
# 3 retornei o valor
# 4 
