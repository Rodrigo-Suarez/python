"""  
EJERCICIO:
 -Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
  su tipo de dato.
 -Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas(Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 
"""
""" 
# Por valor

a = 10
b = a
b= 20
print(a)
print(b)

def funcion(number):
    number += 20
    print(number)

n = 10
funcion(n)
print(n)


# Por referencia

lista_a = [1, 2, 3, 4, 5]
lista_b = lista_a
lista_b.append(10)
print(lista_a)
print(lista_b)

def funcion_2(lista):
    lista.append(10000)
    lista_2 = lista
    lista_2.append(1)
    print(lista)
    print(lista_2)

lista = [10, 20, 30, 50, 100]
funcion_2(lista)
print(lista)
"""

""""
DIFICULTAD EXTRA (opcional):
 Crea dos programas que reciban dos parámetros (cada uno) definidos como
 variables anteriormente.
 - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
   se asigna a dos variables diferentes a las originales. A continuación, imprime
   el valor de las variables originales y las nuevas, comprobando que se ha invertido
   su valor en las segundas.
   Comprueba también que se ha conservado el valor original en las primeras.
"""

def programa_valor(param_1, param_2):
    a = param_2
    b = param_1
    param_1 = a
    param_2 = b

    return param_1 , param_2

a = 5
b = 10
c, d = programa_valor(a, b)
print(f"Originales: {a} - {b}")
print(f"Intercambiados: {c} - {d}")


def programa_referencia(param_1, param_2):
    a = param_2
    b = param_1
    param_1 = a
    param_2 = b
    
    return param_1 , param_2


aa = [1, 2]
bb = [300, 400]
cc, dd = programa_referencia(aa, bb)
print(f"Originales: {aa} - {bb}")
print(f"Intercambiados: {cc} - {dd}")