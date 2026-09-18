from calculadora import *

def test_somar():
    # 2 + 3 deve produzir 5
    assert somar(2, 3) == 5

def test_subtrair():
    # 5 - 3 deve produzir 2
    assert subtrair(5, 3) == 2

def test_multiplicar():
    # 4 * 3 deve produzir 12
    assert multiplicar(4, 3) == 12

def test_dividir():
    # 10 / 2 deve produzir 5
    assert dividir(10, 2) == 5


    
    ## ALUNO: FÁBIO LUIZ S POVITZKI  ^^ 