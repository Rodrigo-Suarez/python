### Arrays ###

# A diferencia de las listas, no estan integradas en python, y solo admiten valores del mismo tipo

import array

my_array = array.array("i", [0, 10, 20, 30])
print(my_array)

# Array vacio
my_array = array.array("i")
print(my_array)

#Agregar elementos al array
my_array.append(40)
my_array.append(20)
my_array.append(30)
print(my_array)

#Eliminar elementos especificos en un array
my_array.pop(1)
print(my_array)


