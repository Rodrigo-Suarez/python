
def invert(lst):
    lista = []
    for n in range(len(lst)):
        lista.append(lst[n]*-1)
    return lista
lista = [1, -2, 3, -4, 5]
print(invert(lista))

print(lista)
