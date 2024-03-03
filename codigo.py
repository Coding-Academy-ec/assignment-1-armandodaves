"""
Ejercicio 1: Suma de Dos Números
Descripción: Este ejercicio consiste en crear una función que reciba dos números como argumentos y devuelva la suma de ambos.
"""

def sumar(a, b):
    try:
        return a + b
    except ValueError:
        print('Error: No se ha ingresado números')

"""
Ejercicio 2: Factorial de un Número
Descripción: En este ejercicio se requiere crear una función que calcule el factorial de un número dado. El factorial de un número nn se calcula como n!=n×(n−1)×(n−2)×…×1n!=n×(n−1)×(n−2)×…×1.
"""
    
def factorial(n):
    numero = n
    lista = []
    resultado = 1
    
    if numero <= 0:
        print('No se puede sacar la factorial de cero o número menor a este, por ende se retornará 1')
        return 1
    
    else:
        while numero > 0:
            if numero not in lista or numero == 1:
                lista.append(numero)
            else:
                lista.append(numero - 1)
            numero -= 1
  
        lista.sort()
        
        for num in lista:
            resultado *= num
        
        print(f'El resultado de la factorial de {n} es: {resultado}')
        return resultado
                
            
"""
Ejercicio 3: Contar Vocales en una Cadena
Descripción: En este ejercicio se debe implementar una función que cuente el número de vocales (mayúsculas y minúsculas) en una cadena de texto dada.
"""
    
def contar_vocales(cadena):
    contador_vocales = 0
    for letra in cadena:
        if letra.lower() in ['a', 'e', 'i',' o', 'u']:
            contador_vocales += 1
    return contar_vocales()

"""
Ejercicio 4: Verificar Palíndromo
Descripción: En este ejercicio se debe implementar una función que verifique si una cadena de texto dada es un palíndromo, es decir, si se lee igual de izquierda a derecha que de derecha a izquierda.
"""

def es_palindromo(cadena):
    # Escribe aqui el return de la cadena al reves con una funcion de python
    caracteres_no_validos = ['.', ',', "'", ':', ';', '¨', '"', ' ']
    cadena_formateada = cadena.lower()
    for caracter in caracteres_no_validos:
        cadena_formateada = cadena_formateada.replace(caracter, '')
    cadena_formateada_reversa = cadena_formateada[::-1]
    
      
    if cadena_formateada == cadena_formateada_reversa:
        print('Si es palíndroma')
        return True
    else:
        print('No es palíndroma')
        return False

"""
Ejercicio 5: Suma de Elementos de una Lista
Descripción: En este ejercicio se debe crear una función que calcule la suma de todos los elementos de una lista dada.
"""

def suma_lista(lista):
    # Escribe aqui el return de la suma de todos los elementos de la lista
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma

