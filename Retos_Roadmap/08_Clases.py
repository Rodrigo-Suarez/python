"""  
EJERCICIO:
Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
atributos y una función que los imprima (teniendo en cuenta las posibilidades
de tu lenguaje).
Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
utilizando su función.
"""

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"{self.name} {self.surname}, {self.age} años"

pedro = Person("Pedro", "Castillo", 19)
andrea = Person("Andrea", "Pelayes", 59)
juan = Person("Juan", "Romero", 45)
agustin = Person("Agustin", "Gil", 21)
print(pedro)
print(andrea)
print(juan)
print(agustin)

pedro.age = 99
print(pedro)






"""
DIFICULTAD EXTRA (opcional):
Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
en el ejercicio número 7 de la ruta de estudio)
- Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
  retornar el número de elementos e imprimir todo su contenido.
"""