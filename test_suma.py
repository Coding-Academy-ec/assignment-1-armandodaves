# 001 --- suma

from codigo import sumar

def test_suma():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0

# --- Factorial
    
from codigo import factorial

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1


# 003 --- 
    
def contar_vocales(cadena):
    vocales = 'aeiouAEIOU'
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
    return contador


# 004 ---

from codigo import es_palindromo

def test_es_palindromo():
    assert es_palindromo("radar") == True
    assert es_palindromo("oso") == True
    assert es_palindromo("Python") == False

# 005 ---
    
from codigo import suma_lista

def test_suma_lista():
    assert suma_lista([1, 2, 3, 4, 5]) == 15
    assert suma_lista([-1, -2, -3, -4, -5]) == -15
    assert suma_lista([0, 0, 0, 0, 0]) == 0
