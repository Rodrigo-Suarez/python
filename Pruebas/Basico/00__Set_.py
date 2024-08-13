
#Dar vuelta un set
my_set = {1, 2, 3, 4, 5} #Creo un set
my_set = list(my_set) #Convierto el set en lista
my_set.reverse() #Doy vuelta la lista
print(my_set)

#Union de sets
my_set_1 = {1, 2, 3, 4, 5}
my_set_2 = {6, 7, 8, 9, 10}
my_union_set = my_set_1.union(my_set_2) #Uno ambos sets
print(my_union_set)