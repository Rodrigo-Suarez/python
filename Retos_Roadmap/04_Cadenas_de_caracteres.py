""" 
EJERCICIO:
Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
- Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
   interpolación, verificación...
""" 
""" 
s1 = "Pelota"
s2 = "pelota"
s3 = "pElOtA"
s4 = "Pelota de futbol"
s5 = "P\te\tl\to\tt\ta"
s6 = "tu {} vieja me {} la {}"
s7 = "tu {x} vieja me {y} la {z}"
s8 = "Pelota2"
s9 = " "
s10 = "PELOTA"
s11 = "     pelota     "
s12 = "pelota vieja"
s13 = "aaaaa"
s14 = "pelota goood nazi insta"

#convierte el primer caracter en mayuscula
print(s2.capitalize())

#convierte todo a minuscula
print(s3.casefold())

#Centra la cadena en la terminal con los espacios que nosotros le asignamos
print(s1.center(50))
print(s1.center(50, "-"))

#devuelve cuantas veces aparace el caracter en la cadena
print(s1.count("a"))

#encode
print(s1.encode())

#Comprueba si comienza o termina con el caracter buscado
print(s1.endswith("a"))
print(s1.startswith("P"))

#Establece el espaciado de cada Tab
print(s5.expandtabs())
print(s5.expandtabs(5))
print(s5.expandtabs(2))


#reemplaza los espacios formateados por los parametros que le pasemos
print(s6.format("puta", "chupa", "verdura"))
map = {"x": "puta", "y": "chupa", "z": "verdura"}
print(s7.format_map(map))

#Devuelve la posicion en la que se encuentra el caracter buscado
print(s1.find("a"))
print(s1.find("a", 1, 3))
print(s1.find("a", 4))
print(s13.find("a"))
print(s13.rfind("a"))
print(s13.index("a"))
print(s13.rindex("a"))

#Comprobaciones
print(s1.isalnum())
print(s8.isalpha())
print(s1.isascii())
print(s1.isdecimal())
print(s1.isdigit())
print(s1.isidentifier())
print(s2.islower())
print(s1.isprintable())
print(s9.isspace())
print(s4.istitle())
print(s10.isupper())

#pone una cadena al comienzo de cada letra de la cadena del parametro
print("-".join(s1))

#Parte una cadena en tres tomando el parametro como indicacion
print(s4.partition("e"))
print(s4.rpartition("e"))

#Agrega espacios para la isquierda o para la derecha
print(s1.ljust(10), s2)
print(s1.rjust(10), s2) 

#Convierte a todo mayusculas o todo minusculas
print(s1.lower())
print(s1.upper())

#Borra el espacio de la derecha o el de la isquiera
print(s11.strip())
print(s11.lstrip())
print(s11.rstrip())

#Maketrans crea un mapa con el elemento a reemplazar y su sustituto
txt = "Hi Sam!"
mytable = txt.maketrans("Sma", "Jap")
print(txt.translate(mytable))

#Borra lo que empieza o lo que termina
print(s1.removeprefix("Pe"))
print(s1.removesuffix("ta"))

#Reemplaza el primer parametro por el segundo
print(s4.replace("a", "HOLA"))

#Invierte las mayusculas y minusculas
print(s3.swapcase())

#Convierte los elementos de una cadena en elementos de una lista. El parametro determina cual es la separacion
print(s1.split())
print(s14.rsplit(" "))

#si el parametro supera la cantidad de letras de la cadena, rellena con ceros
print(s1.zfill(7))

#hace la primera letra de cada palabra mayuscula
print(s4.title())
""" 

"""  
DIFICULTAD EXTRA (opcional):
 Crea un programa que analice dos palabras diferentes y realice comprobaciones
 para descubrir si son:
 - Palíndromos
 - Anagramas
 - Isogramas
"""


def palindromos(w):
    if w == w[::-1]:
        print(f"la palabra '{w}' es un palindromo")
    else:
        print(f"la palabra '{w}' no es un palindromo")

def anagramas(w1, w2):
    word1 = sorted(w1)
    word2 = sorted(w2)

    if word1 == word2:
        print(f"Las palabras {w1} y {w2} son anagramas")
    else:
        print(f"Las palabras {w1} y {w2} no son anagramas")


def isogramas(w1):
    dictionary = {}
    for i in w1:
        word = i
        reps = w1.count(i) 
        dictionary[word] = reps
    
    for key in dictionary:
        if dictionary[key] == dictionary[word]:
            continue
        else: 
            return print(f"La palabra {w1} no es un anagrama")
        
    return print(f"La palabra {w1} es un anagrama")


w1 = str(input("Ingrese la primera palabra: "))
w2 = str(input("Ingrese la segunda palabra: "))

palindromos(w1.lower())
palindromos(w2.lower())
anagramas(w1.lower(), w2.lower())
isogramas(w1.lower())
isogramas(w2.lower())

