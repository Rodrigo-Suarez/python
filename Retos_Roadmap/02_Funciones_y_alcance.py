
#  DIFICULTAD EXTRA (opcional):
#
#  Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
#  - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#    - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#    - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#    - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#    - La función retorna el número de veces que se ha impreso el número en lugar de los textos.


def function(word1, word2):

    counter = 0

    for number in range(1, 101):

        if number%3 == 0 and number%5 == 0:
            print(word1 + word2)

        elif number%3 == 0:
            print(word1)
        
        elif number%5 == 0:
            print(word2)

        else:
            print(number)
            counter += 1
    
    return print(counter)
        

function("hola", "puto")

        