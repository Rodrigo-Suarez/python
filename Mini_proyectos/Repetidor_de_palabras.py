"""
### Repetidor de palabras
string = str(input("Escriba una palabra: "))
reps = int(input("¿Cuantas veces quiere que se repita?: "))
contador = 0

while string:
    print(string)
    contador += 1
    if contador == reps:
        break

print("Operación exitosa")
"""


def repetidor(word, reps):
    for rep in range(reps):
        print(word)

repetidor("pablo", 500)