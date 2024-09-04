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

class Contact:
  def __init__(self, name, number):
    self.name = name
    self.number = number
  
  def __repr__(self):
    return f'\n##########\nNombre: {self.name}\nNumero de telefono: {self.number}\n'


class ContactList:
    def __init__(self):
      self.contacts = {}

    def show_contacts(self):
      for contact in self.contacts.values():
        print(contact)

    def add_contact(self, name):
      if name in self.contacts:
        return print("\n##########\nEl usuario ya existe\n##########\n")

      else:
        number = input("Ingresa el numero de telefono:")
        if verify_number(number):
          self.contacts[name] = Contact(name, number)
          return print("\n##########\nEl usuario se ha añadido con exito\n##########\n")
    
        else:
          return print("\n##########\nError: El numero de telefono no puede tener mas de 11 digitos y debe ser numerico\n##########\n")

    def search_contact(self, name):
      if name in self.contacts:
        return print(self.contacts[name])
   
      else:
        return print("\n##########\nEl usuario no existe\n##########\n")
   
    def delete_contact(self, name):
      if name in self.contacts:
        del self.contacts[name]
        return print("\n##########\nEl usuario ha sido eliminado correctamente\n##########\n")
    
      else:
        return print("\n##########\nEl usuario no existe\n##########\n")
    
    def modify_contact(self, name_original):
      if name_original in self.contacts:
        while True:
          print("\n--¿Que desea modificar?--")
          print("1. Nombre")
          print("2. Numero de telefono")
          print("3. Ambos")
          print("4. Cancelar operacion")

          opcion = input("Seleccione la operacion que desea realizar: ")

          match opcion:
            # Caso: Carga de contacto
            case "1":
              name = input("Ingrese el nuevo nombre del contacto:")
              contact = self.contacts.pop(name_original)
              self.contacts[name] = Contact(name, contact.number)
              return print("\n##########\nEl usuario se ha actualizado con exito\n##########\n")
            case "2":
              number = input("Ingresa el nuevo numero de telefono:")
              if verify_number(number):
                self.contacts[name_original] = Contact(name_original, number)
                return print("\n##########\nEl usuario se ha actualizado con exito\n##########\n")
              
              else:
                return print("\n##########\nError: El numero de telefono no puede tener mas de 11 digitos y debe ser numerico\n##########\n")
            case "3":
              name = input("Ingrese el nuevo nombre del contacto: ")
              number = input("Ingresa el nuevo numero de telefono: ")
              if verify_number(number):
                del self.contacts[name_original]
                self.contacts[name] = Contact(name, number)
                return print("\n##########\nEl usuario se ha actualizado con exito\n##########\n")
          
              else:
                return print("\n##########\nError: El numero de telefono no puede tener mas de 11 digitos y debe ser numerico\n##########\n")   
            case "4":
              print("\n##########\nCancelando la operación...\n##########\n")
              break
            case _:
              print("\n##########\nSeleccione una opción correcta\n##########\n")

      else:
        return print("\n##########\nEl usuario no existe\n##########\n")


def verify_number(number: str):
  return number.isdigit() and len(number) <= 11


contact_list = ContactList()

# do{
#   # Aca iria tu codigo
# } while(opcion != 6)

while True:
  print("\n--- Menú ---")
  print("1. Ver todos los usuarios")
  print("2. Agregar un nuevo usuario")
  print("3. Buscar un usuario")
  print("4. Eliminar un usuario")
  print("5. Modificar un usuario")
  print("6. Salir")
  print("------------")

  opcion = input("Seleccione la accion que desea realizar: ")
  
  match opcion:

    case "1":
      contact_list.show_contacts()

    case "2":
      name = input("Ingrese el nombre del contacto:")
      contact_list.add_contact(name)
  
    case "3":
      name = input("Ingrese el nombre del contacto a buscar:")
      contact_list.search_contact(name)

    case "4":
      name = input("Ingrese el nombre del contacto a eliminar:")
      contact_list.delete_contact(name)

    case "5":
      name = input("Ingrese el nombre del contacto a modificar:")
      contact_list.modify_contact(name)

    case "6":
      print("\n##########\nCerrando el sistema...\n##########\n")
      break
  
    case _:
      print("\n##########\nSeleccione una opción correcta\n##########\n")