"""

Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
 - La serie Fibonacci se compone por una sucesión de números en
   la que el siguiente siempre es la suma de los dos anteriores.
   0, 1, 1, 2, 3, 5, 8, 13...

"""

def fibonacci():
    prev = 0
    next = 1

    for index in range(0, 51):
        print(prev) #imprime el numero fibonacci
        
        fib = prev + next # Crea el numero fibonacci
        prev = next # Guarda el valor 2 como valor 1
        next = fib # Asigna al valor 2 el nuevo numero


fibonacci()
