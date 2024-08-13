"""

Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.

"""

def primos():

    for number in range(1, 101):

        if number >= 2:
             
            is_divisible = False

            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break
                    
            if not is_divisible:
                print(number)

primos()
