### Exceptions ###

#Excepción
number_one = 1
number_two = "1"

try:
    print(number_one + number_two)

except:
    print("Error")


#Excepciones con else y finally(opcionales)
number_one = 1
number_two = "1"

try:
    print(number_one + number_two)

except:
    print("Error")

else: #Se ejecuta si la operacion no da error // *OPCIONAL
    print("La ejecución fue exitosa")

finally: #Se ejecuta siempre // *OPCIONAL
    print("La ejecucion continua")


#Exceptions que reconocen el error y lo imprimen(opcional)
number_one = 1
number_two = "1"

try:
    print(number_one + number_two)

except ValueError: #Erro incorrecto 
    print("Error")

except TypeError as error:
    print(error)

finally: 
    print("La ejecucion continua")
