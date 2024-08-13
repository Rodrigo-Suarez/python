### Diccionario ###
my_dict = {"Torneo":"Copa America", "Edición":2024, "Sede":"USA", "Campeon":"Argentina", "Sub-campeon":"Colombia"}
print(my_dict)


# Modificar una key
my_dict["Torneo"] = "Eurocopa"
print(my_dict)


# Borrar una key
del my_dict["Edición"]
print(my_dict)


# Añadir una key
my_dict["Tercer puesto"] = "Uruguay"
print(my_dict)


# Funciones
print(my_dict.items()) # Imprime las keys y sus values como items
print(my_dict.keys()) # Imprime las key 
print(my_dict.values()) # Imprime los values


# Crear un dict vacio usando las keys de otro dict
my_empty_dict = dict.fromkeys(my_dict)
print(my_empty_dict)


# Crear un dict vacio asignandole nosotros mismos las key y sus valores (*el valor se aplica para todas las key, *darle un valor es opcional)
my_empty_dict = dict.fromkeys(("key_1", "key_2", "key_3"), ("valor"))
print(my_empty_dict)


# Crear un dict vacio usando una lista 
my_list = ["key_1", "key_2", "key_3"]
my_empty_dict = dict.fromkeys(my_list)
print(my_empty_dict)