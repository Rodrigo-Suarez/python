def repetidor(word, number):
    contador = 0
    while contador != number:
        print(word)
        contador += 1
    else:
        print(f"La palabra '{word}' fue impresa {number} veces")

