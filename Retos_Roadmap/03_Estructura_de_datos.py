"""
EJERCICIO:
 - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
   en tu lenguaje.
 - Utiliza operaciones de inserción, borrado, actualización y ordenación.
"""
# Listas
"""
my_list = [1, 2, 3, 4, 5]
print(my_list)

my_list.append(6)
print(my_list)

my_list.pop(0)
print(my_list)

#my_list.clear()
#print(my_list)

my_copy_list = my_list.copy()
my_copy_list[0] = 9
print(my_list)
print(my_copy_list)

my_count_list = my_list.count(2)
print(my_count_list)

my_list.extend("holaa")
print(my_list)

my_index_list = my_list.index(2)
print(my_index_list)

my_list.insert(1, 1111)
print(my_list)

my_list.remove("a")
print(my_list)

my_list.reverse()
print(my_list)

my_list = [1, 2, 4, 6, 1]
my_list.sort()
print(my_list)



#Tuplas
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

my_count_tuple = my_tuple.count(2)
print(my_count_tuple)

my_index_tuple = my_tuple.index(1)
print(my_index_tuple)



#Diccionarios
my_dict = {"pais": "Argentina", "Capital": "Buenos Aires"}
print(my_dict)

#my_dict.clear()
print(my_dict)

my_copy_dict = my_dict.copy()
print(my_copy_dict)

keys = ["Name", "Age", "Sex"]
my_dict = dict.fromkeys(keys, 1)
print(my_dict)

my_get_dict = my_dict.get("Name")
print(my_get_dict)

my_items_dict = my_dict.items()
print(my_items_dict)

my_keys_dict = my_dict.keys()
print(my_keys_dict)

my_dict.pop("Name")
print(my_dict)

my_popitem_dict = my_dict.popitem()
print(my_dict)
print(my_popitem_dict)

my_dict.setdefault("Name", 1)
print(my_dict)

my_dict = {"pais": "Argentina", "Capital": "Buenos Aires"}
my_other_dict = {"Capital": "Santa Fe", "Region": "America"}
my_dict.update(my_other_dict)
print(my_dict)

my_dict_values = my_dict.values()
print(my_dict_values)


#SETs
my_set = {"agua","tierra", "fuego", "aire"}
my_set.add("luna")
print(my_set)

#my_set.clear()
print(my_set)

my_set_2 = my_set.copy()
print(my_set_2)

my_set = {"agua","tierra", "fuego", "aire"}
my_set_2  = {"agua", "sol", "pasto", "piedra"}
my_set_3 = my_set.difference(my_set_2)
print(my_set_3)

my_set.difference_update(my_set_2)
print(my_set)

my_set = {"agua", "tierra", "fuego", "aire"}
my_set.discard("agua")
print(my_set)

my_set = {"agua","tierra", "fuego", "aire"}
my_set_2  = {"agua", "sol", "pasto", "piedra"}
my_set_3 = my_set.intersection(my_set_2)
print(my_set_3)

my_set = {"agua","tierra", "fuego", "aire"}
my_set_2  = {"agua", "sol", "pasto", "piedra"}
my_set.intersection_update(my_set_2)
print(my_set)

my_set_3 = my_set.isdisjoint(my_set_2)
print(my_set_3)

my_set = {"agua","tierra", "fuego", "aire"}
my_set_2  = {"agua", "sol", "pasto", "piedra"}
my_set_3 = my_set.issubset(my_set_2)
print(my_set_3)

my_set = {"agua","tierra", "fuego", "aire"}
my_set_2  = {"agua", "sol", "pasto", "piedra"}
my_set_3 = my_set.issuperset(my_set_2)
print(my_set_3)

my_set_2 = my_set.pop()
print(my_set_2)

my_set = {"agua","tierra", "fuego", "aire"}
my_set.pop()
print(my_set)

my_set = {"agua","tierra", "fuego", "aire"}
my_set.remove("agua")
print(my_set)

my_set = {"agua","tierra", "fuego", "aire"}
my_set_2  = {"agua", "sol", "pasto", "piedra"}
my_set_3 = my_set.union(my_set_2)
print(my_set_3)

my_set = {"agua","tierra", "fuego", "aire"}
my_set_2  = {"agua", "sol", "pasto", "piedra"}
my_set.update(my_set_2)
print(my_set)

my_set = {"agua","tierra", "fuego", "aire"}
my_set_2  = {"agua", "sol", "pasto", "piedra"}
my_set_3 = my_set.symmetric_difference(my_set_2)
print(my_set_3)

my_set = {"agua","tierra", "fuego", "aire"}
my_set_2  = {"agua", "sol", "pasto", "piedra"}
my_set.symmetric_difference_update(my_set_2)
print(my_set)
"""


"""
 DIFICULTAD EXTRA (opcional):
 Crea una agenda de contactos por terminal.
 - Debes implementar funcionalidades de búsqueda, inserción, actualización
   y eliminación de contactos.
 - Cada contacto debe tener un nombre y un número de teléfono.
 - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
   y a continuación los datos necesarios para llevarla a cabo.
 - El programa no puede dejar introducir números de teléfono no númericos y con más
   de 11 dígitos (o el número de dígitos que quieras).
 - También se debe proponer una operación de finalización del programa.
 """

class contact:
  def __init__(self, name, number, id):
      self.name = name
      self.number = number
      self.id = id

  def __str__(self):
     return f"##########\nID: {self.id}\nNombre: {self.name}\nNúmero: {self.number}\n##########"
  
      
contact_list = []


def add_contact(name, number):
    
    if len(str(number)) > 11:
      return print("~~El numero de telefono no puede tener mas de 11 digitos~~")

    else:
      contact_id = len(contact_list)
      user = contact(name, number, contact_id)
      contact_list.append(user)

    return print("El usuario se ha añadido con exito")
     

while True:
  print("\n--- Menú ---")
  print("1. Agregar un nuevo usuario")
  print("2. Ver todos los usuarios")
  print("3. Salir")
  print("------------") 
  add_contact(str(input("Ingrese el nombre:")), int(input("Ingresa el numero de telefono:")))
  for user in contact_list:
    print(user)