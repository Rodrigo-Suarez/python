'''

 * Escribe una función que reciba dos palabras (String) y retorne
   verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
     las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.

'''

#SOLUCION MOURE DEV (era facil pero no conocia el concepto de sorted, por eso no lo pude hacer)

def anagrama(word_1, word_2):
    if word_1.lower() == word_2.lower():
        return False
    
    return sorted(word_1.lower()) == sorted(word_2.lower())

print(anagrama("hola", "alho"))