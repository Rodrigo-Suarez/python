### Condicionales ###

#Condicional basico
number = 20

if number == 10:
    print("El numero es igual a 10")
else: #Si no se cumple la condicion
    print("El numero no es igual 10")


#Condicional con segunda condicion en caso de que la primera falle
number_2 = 20

if number_2 == 10:
    print("El numero 2 es igual a 10")
elif number_2 == 20: #Segunda condicion en caso de que la primera no se cumpla
    print("El numero 2 es igual a 20")
else: 
    print("El numero 2 no es igual 10")


#Condicional con mas de 1 condicion
number_3 = 15

if number_3 > 10 and number_3 < 20:
    print("El numero 3 es mayor que 10 y menor que 20")
elif number_3 == 1:
    print("El numero 3 es igual 1")
else:
    print("El numero 3 no es mayor que 10 ni menor que 20 y distinto de 1")


#Condicionales negativos
string = ""

if not string:
    print("Este string esta vacio")

number = 15

if not number==10:
    print("El numero no es igual a 10")