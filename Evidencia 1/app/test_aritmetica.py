from aritmetica import *

def test_sumar():
    assert sumar(1.11, 2.22) == 3.33
    assert sumar(-1.0, 1.0) == 0.00
    assert sumar(0.0, 0.0) == 0.00

def test_restar():
    assert restar(5.55, 2.22) == 3.33
    assert restar(0.0, 0.0) == 0.00
    assert restar(-2.2, -2.2) == 0.00

def test_dividir():
    assert dividir(5.0, 2.0) == 2.50
    assert dividir(5.0, 0.0) == "Error: División por cero no permitida."
    assert dividir(0.0, 2.0) == 0.00

def test_multiplicar():
    assert multiplicar(3.3, 3.3) == 10.89
    assert multiplicar(2.0, 0.0) == 0.00
    assert multiplicar(0.0, 0.0) == 0.00

def test_sumar_n():
    assert sumar_n(1.1, 2.2, 3.3) == 6.60
    assert sumar_n(0.0, 0.0, 0.0) == 0.00
    assert sumar_n(-1.1, 1.1) == 0.00

def test_promedio_n():
    assert promedio_n(1.0, 2.0, 3.0) == 2.00
    assert promedio_n(0.0, 0.0, 0.0) == 0.00
    assert promedio_n(5.0, 5.0) == 5.00

if __name__ == "__main__":
    test_sumar()
    test_restar()
    test_dividir()
    test_multiplicar()
    test_sumar_n()
    test_promedio_n()
    print("Todos los tests pasaron correctamente.")