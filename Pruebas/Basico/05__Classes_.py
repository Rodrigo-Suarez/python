### Clases ###

class Person:
    def __init__(self, name, surname, age,):
        self.name = name
        self.surname = surname
        #self.__age = age
    
    #def get_name(self):
        #return self.__age
    
    def jump(self):
        print(f"{self.name} puede saltar")
    
    def walk(self):
        print(f"{self.name} puede caminar")

    def talk(self):
        print(f"{self.name} puede hablar")


my_person = Person("Rodrigo", "Suarez", "17")
print(my_person.name)
print(my_person.surname)
#my_person.get_name() #Revisar#
my_person.jump()
my_person.walk()
my_person.talk()