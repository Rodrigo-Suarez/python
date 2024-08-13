### EXPRESIONES REGULARES ###

import re

# MATCH    // Busca solo al comienzo de la cadena  

my_string = "Holaa, me llamo Rodrigo y tengo 17 años"
my_other_string = "Hola, me llamo Pedro y tengo 62 años"

my_match = re.match("Holaa", my_string, re.I)   # "re.I" Hace que no importe si esta escrito en mayusculas o en minusculas
print(my_match)

start, end = my_match.span()
print(my_match.span())

print(my_string[start:end])


my_other_match = re.match("Hoa", my_other_string)
if my_other_match is not None:
    print(my_other_match)
    start, end = my_other_match.span()
    print(my_other_string[start:end])



#SEARCH    // Busca en cualquier lado de la cadena // Si la palabra se repite solo considerara la primera que aparece

my_string = "Holaa, me llamo Rodrigo y tengo 17 años"

search = re.search("llamo", my_string, re.I)
print(search)

start, end = search.span()
print(my_string[start:end])



#FINDALL // Busca en cualquier lado de la cadena y nos devuelve como lista // Si la palabra se repite nos la imprimira como cuantas veces aparezca

my_string = "Holaa, me llamo Rodrigo y tengo 17 años"

findall = re.findall("a", my_string, re.I)
print(findall)


#SPLIT // Utiliza un patron asignado para dividir la cadena de texto

my_string = "Holaa, me llamo Rodrigo y tengo 17 años"

my_split = re.split(",", my_string)
print(my_split)


#SUB // Reemplaza el texto quue nosotros elijamos 

my_string = "Holaa, me llamo Rodrigo y tengo 17 años"

my_sub = re.sub("Holaa", "Hola", my_string)
print(my_sub)


my_string = "Hola hola HOLA HoLa"

my_sub = re.sub("[H|h]ola", "chau", my_string)
print(my_sub)


my_string = "Hola hola HOLA HoLa"

my_sub = re.sub("Hola|hola|HOLA|HoLa", "chau", my_string)
print(my_sub)


#PATRONES

my_string = "Hola, me llamo Rodrigo y tengo 17 años"

my_pattern = r"[Hh]ola"
print(re.findall(my_pattern, my_string))

my_pattern = r"[Hh]ola|tengo"
print(re.findall(my_pattern, my_string))

my_pattern = r"[A-z]"
print(re.findall(my_pattern, my_string))

my_pattern = r"[0-9]"
print(re.findall(my_pattern, my_string))

my_pattern = r"\d"
print(re.findall(my_pattern, my_string))

my_pattern = r"\D"
print(re.findall(my_pattern, my_string))

my_pattern = r"[m].*"
print(re.findall(my_pattern, my_string))


#Verificacion de email con patron de expresion regular 
# Pagina para aprender expresiones regulares https://regex101.com

my_string = "ranaraniada@gmail.com"
my_pattern = r"^[a-zA-Z0-9-_.+-]+@[a-zA-Z]+.com"
print(re.findall(my_pattern, my_string))