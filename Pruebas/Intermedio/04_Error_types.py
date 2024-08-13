### TIPOS DE ERROR ###

#SINTAX-ERROR

#print "hola"   # Descomentar para ver el error
print("hola")


#NAME-ERROR

variable = "hola"   # Comentar para ver el error
print(variable)


#INDEX-ERROR

#list = [1, 2, 3, 4, 5]   # Descomentar para ver el error
print(list[5])


#MODULE-NOT-FOUND-ERROR

#import mathsss   # Descomentar para ver el error
import math


#ATRIBUTE-ERROR

#print(math.PI)   # Descomentar para ver el error
print(math.pi)


#KEY-ERROR

my_dict = {"Torneo":"Copa America", "Edición":2024, "Sede":"USA", "Campeon":"Argentina", "Sub-campeon":"Colombia"}
#print(my_dict["toneo"])   #Descomentar para ver el error
print(my_dict["Torneo"])


#TYPE-ERROR

list = [1, 2, 3, 4, 5]
#print(list["hola"])   #Descomentar para ver el error
print(list[1])


#IMPORT-ERROR

#from math import PI   #Descomentar para ver el error
from math import pi


#VALUE-ERROR

#variable = int("10 años")   #Descomentar para ver el error
variable = int("10")
print(variable)


#ZERO-DIVISION-ERROR

#print(4/0)   #Descomentar para ver el error
print(4/2)
