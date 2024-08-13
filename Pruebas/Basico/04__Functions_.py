### Funciones ###

#Funcion simple
def calculator_1():
    print("Esto es una funcion simple")

calculator_1()


#Función con argumentos/parametros
def calculator_2(number_1, number_2):
    result = number_1 + number_2
    return result

result = calculator_2(1,2)
print(result)


#Funcion con parametros por defecto
def calculator_3(name, surname, alias = "Sin alias" ):
    print(f"{name} {surname} {alias}")
    
calculator_3("Rodrigo", "Suarez")
calculator_3("Rodrigo", "Suarez", "Choi")