def sumar(a, b):
    return round(a + b, 2)

def restar(a, b):
    return round(a - b, 2)

def dividir(a, b):
    try:
        return round(a / b, 2)
    except ZeroDivisionError:
        return "Error: División por cero no permitida."

def multiplicar(a, b):
    return round(a * b, 2)

def sumar_n(*args):
    return round(sum(args), 2)

def promedio_n(*args):
    return round(sum(args) / len(args), 2)