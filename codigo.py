"""
Ejercicio 1: Suma de Dos Números
Descripción: Este ejercicio consiste en crear una función que reciba dos números como argumentos y devuelva la suma de ambos.
"""

def sumar(a, b):
    # Escribe aqui el return de la suma de 2 numeros

"""
Ejercicio 2: Factorial de un Número
Descripción: En este ejercicio se requiere crear una función que calcule el factorial de un número dado. El factorial de un número nn se calcula como n!=n×(n−1)×(n−2)×…×1n!=n×(n−1)×(n−2)×…×1.
"""
    
def factorial(n):
    if n == 0:
        # Escribe aqui el return de la operacion anterior
    else:
        # Escribe aqui el return de la operacion contraria a la operacion anterior

"""
Ejercicio 3: Contar Vocales en una Cadena
Descripción: En este ejercicio se debe implementar una función que cuente el número de vocales (mayúsculas y minúsculas) en una cadena de texto dada.
"""
    
def contar_vocales(cadena):
    vocales = 'aeiouAEIOU'
    contador = 0
    for letra in cadena:
        if letra in vocales:
            # Escribe aqui el contador de vocales
    return contador

"""
Ejercicio 4: Verificar Palíndromo
Descripción: En este ejercicio se debe implementar una función que verifique si una cadena de texto dada es un palíndromo, es decir, si se lee igual de izquierda a derecha que de derecha a izquierda.
"""

def es_palindromo(cadena):
    # Escribe aqui el return de la cadena al reves con una funcion de python
    return cadena == cadena[::-1]

"""
Ejercicio 5: Suma de Elementos de una Lista
Descripción: En este ejercicio se debe crear una función que calcule la suma de todos los elementos de una lista dada.
"""

def suma_lista(lista):
    # Escribe aqui el return de la suma de todos los elementos de la lista
    for elemento in lista:
        suma += elemento
    return suma
