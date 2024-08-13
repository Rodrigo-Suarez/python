### FUNCIONES DE ORDEN SUPERIOR###

#USAR UNA FUNCION COMO ARGUMENTO PARA OTRA FUNCION

# Ejemplo-1
def first_function(value):
    return value + 1

def second_function(number_1, number_2):
    return number_1 + number_2

print(second_function(1, first_function(1)))


#Ejemplo-2
def first_function(value):
    return value + 1

def second_function(number_1, number_2, number_3):
    return number_3(number_1 + number_2)

print(second_function(1, 1, first_function))


### CLOSURES ###  // FUNCION CON UNA FUNCION DENTRO
def first_function():

    def second_function(value):
        return value + 1
    
    return second_function

funcion = first_function()
print(funcion(4))


### BUILT-IN HIGH ORDER FUNCTIONS ###

# MAP // Recorre los valores para saber como modificarlos en base a una funcion  // Nos ahorra usar um loop "for"

numbers = [1, 3, 6, 2, 77, 5]

def function(value):
    return value + 1

print(list(map(function, numbers)))
print(list(map(lambda value: value + 1, numbers))) #En lugar de usar una funcion utilizamos una lambda ya que en este caso es mas simple y conveniente


# FILTER // Recorre los valores y devuelve TRUE o FALSE para saber que filtrar

numbers = [1, 3, 6, 2, 77, 5]

def function(value):
    if value % 2 == 0:
        return True
    return False

print(list(filter(function, numbers)))
print(list(filter(lambda value: value % 2 == 0, numbers)))


# REDUCE // Opera con un valor mas el acumulado

from functools import reduce

numbers = [1, 3, 6, 2, 77, 5]

def function(numero_1, numero_2):
    return numero_1 + numero_2

print(reduce(function, numbers))
print(reduce(lambda numero_1, numero_2: numero_1 + numero_2, numbers))