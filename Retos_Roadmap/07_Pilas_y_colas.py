""" 
EJERCICIO:
Implementa los mecanismos de introducción y recuperación de elementos propios de las
pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
o lista (dependiendo de las posibilidades de tu lenguaje).
"""
"""
# Pilas
pila = []

pila.append(1)
pila.append(2)
pila.append(3)

pila.pop()
pila.pop()

print(pila)

# Colas
cola = []

cola.append(1)
cola.append(2)
cola.append(3)
cola.append(4)
cola.append(5)

cola.pop(0)
cola.pop(0)
print(cola)
"""


"""
DIFICULTAD EXTRA (opcional):
- Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
  de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
  que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
  Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
  el nombre de una nueva web.
"""
"""
def main():
    
    webs = []

    print("--------/ N A V E G A D O R /--------")
    print("Ingresa una pagina web o navega hacia 'atras' o 'adelante'. Para abandonar la ejecucion escriba 'salir'")

    while True:

        opcion = str(input(">>>>>").lower().strip())

        
        match opcion:
            case "adelante":
                pass

            case "atras":
                if len(webs) > 1:
                    webs.pop()
                    print(f"Has navegado hacia atras. La pagina actual es: {webs[-1]}")
                else:
                    print("Estas en la pagina de inicio")

            case "salir":
                break

            case _:
                webs.append(opcion)
                print(f"Estas en {webs[len(webs)-1]}")

main()
"""

"""
DIFICULTAD EXTRA (opcional):
- Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
  impresora compartida que recibe documentos y los imprime cuando así se le indica.
  La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
  interpretan como nombres de documentos.
"""

def main():

    docs = []

    print("--------/ I M P R E S O R A /--------")
    print("Añada archivos a la cola")
    print("'Imprimir' para imprimir")
    print("'lista' para ver la cola")

    while  True:

        opcion = str(input(">>>>>").lower().strip())

        
        match opcion:
            case "salir":
                break
            
            case "lista":
                id = 1
                for doc in docs:
                    print(f"{id}_{doc}")
                    id += 1

            case  "imprimir":
                if len(docs) > 0:
                    impreso = docs.pop(0)
                    print(f"Se ha impreso: {impreso}")
                else:
                    print("No hay documentos para imprimir")

            case _:
                docs.append(opcion)
                print(f"Se ha añadido {docs[len(docs)-1]} a la cola")


if  __name__ == "__main__":
    main()