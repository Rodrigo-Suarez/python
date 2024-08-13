"""

Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

"""

def inversor(text):
    
    text_len = len(text)
    inversed_text = ""

    for index in range(0, text_len):
        inversed_text += text[text_len - index - 1]
    return inversed_text


print(inversor("hola mi gente sigan viendo"))