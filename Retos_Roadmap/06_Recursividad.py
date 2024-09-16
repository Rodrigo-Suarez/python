"""
 EJERCICIO:
 Entiende el concepto de recursividad creando una función recursiva que imprima
 números del 100 al 0.
"""
"""
def recursion(n = 0):
    if n > 100:
        return print("La ejecucion a finalizado")
    else:
        print(n)
        recursion(n + 1)
    
recursion()
"""

"""
 DIFICULTAD EXTRA (opcional):
 Utiliza el concepto de recursividad para:
 - Calcular el factorial de un número concreto (la función recibe ese número).
 - Calcular el valor de un elemento concreto (según su posición) en la 
   sucesión de Fibonacci (la función recibe la posición).
"""  
"""
def factorial(n):
    if n == 1:
        return 1
    else: 
        return n * factorial(n - 1)

print(factorial(5))
"""

def fibonacci(n):
   if n <= 1:
       return n
   else:
       return fibonacci(n - 2) + fibonacci(n - 1)

print(fibonacci(119))