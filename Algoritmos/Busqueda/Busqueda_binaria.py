"""  
lista = [0, 2, 44, 23, 21, 5, 7, 6]
number = 5

def binary_search (lista, number):
    first = lista[0]
    last = lista[-1]
"""  
def tamaño_calculadora(lista_ordenada):
    contador = 0
    for i in lista_ordenada:
        contador += 1
    return contador

def binary_search(lista_ordenada, tamaño, valor_buscado):
    first = 0
    last = tamaño
    middle = 0

    while first + 1 < last:
        middle = (first + last) // 2
        if lista_ordenada[middle] > valor_buscado:
            last = middle
        else:
            first = middle

    if lista_ordenada[first] == valor_buscado:
        return print(f"valor encontrado en la posicion {first}")
    else:
        return print("no se ha encontrado el valor")




lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valor_buscado = 0
tamaño = tamaño_calculadora(lista_ordenada)
binary_search(lista_ordenada, tamaño, valor_buscado)