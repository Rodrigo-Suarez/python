### Modulos ###

#Importar un modulo completo
import moduloUno
moduloUno.repetidor(5, 5)


#Importar un elemento especifico de un modulo
from moduloDos import caca
print(caca) #En este caso ya no hace falta llamar a moduloDos.caca


#Importar un elemento o modulo asignandole otro nombre
import moduloUno as funcion
funcion.repetidor(5, 5)

from moduloDos import caca as hola
print(hola)


#Importar funciones del sistema integradas en python
import math

print(math.pi)