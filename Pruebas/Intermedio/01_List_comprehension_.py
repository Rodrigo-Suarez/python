### LIST COMPREHENSION ###

#GENERAR UNA LISTA
my_normal_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_normal_list)

my_automatic_list = [i for i in range(11)]
print(my_automatic_list)

my_range_list = list(range(11))
print(my_range_list)


#LISTAS MODIFICADAS
my_automatic_list = [i * 5 for i in range(11)]
print(my_automatic_list)