### Bucles ###

#Bucle while
number = 0

while number <=5:
    print("El numero es:",number )
    number += 1
else:
    print("El numero es mayor a 5")

print("Fin del bucle")


#Bucle for
my_list = ["Argentina", "Bolivia", "Peru", "Paraguay", "Brasil", "Uruguay"]
contador = 0

for countries in my_list:
    while countries == my_list[contador]:
        print(countries, ": Sudamerica")
        contador += 1
        if contador == len(my_list):
            break
