### Manejo de ficheros ###

#FICHERO TIPO ".txt"
import os

text_txt = open("Pruebas\Intermedio\My_text.txt", "w+")
text_txt.write("El que lee es puto\njajaja sos gay\ntodavia seguis leyendo\nque puto")

#print(text_txt.read())
print(text_txt.read(10))   #Escribe los primeros 10 caracteres
print(text_txt.readline())   #Escribe una linea
print(text_txt.readlines())   #Escribe todas las lineas y las transforma en una lista

for line in text_txt.readlines():
    print(line)

text_txt.write("\nque putoooo ajjaja")
print(text_txt.readline())

text_txt.close()

with open("Pruebas\Intermedio\My_text.txt", "r") as text_txt:
    for line in text_txt:
        print(line)

#os.remove("python\Pruebas\Intermedio\My_text.txt")


#FICHERO TIPO ".json"

import json

my_json = open("Pruebas\Intermedio\My_json.json", "w+" )

my_json_content = {
    "name" : "Rodrigo", 
    "surname" : "Suarez", 
    "age" : 17, 
    "lenguage" : "Python", 
    "work" : "Backend"
    }

json.dump(my_json_content, my_json, indent = 4)

my_json.close()                                                     #
                                                                    # CERRAR EL ARCHIVO UNA VEZ ESCRITO Y ABRIRLO DEVUELTA PARA PODER LEERLO
with open("Pruebas\Intermedio\My_json.json", "r" ) as my_json:      #
    for line in my_json:
        print(line)

#TRANSFORMAR EL .JSON EN UN DICT
my_dict_json = json.load(open("Pruebas\Intermedio\My_json.json"))
print(my_dict_json)
print(type(my_dict_json))
print(my_dict_json["name"])


#FICHERO TIPO ".csv"
import csv

my_csv = open("Pruebas\Intermedio\My_csv.csv", "w+")

my_csv_writer = csv.writer(my_csv)
my_csv_writer.writerow(["name", "surname", "age", "lenguage", "work"])
my_csv_writer.writerow(["Rodrigo", "Suarez", "17", "Python", "Backend"])
my_csv_writer.writerow(["Pedro", "Gonzalez", "88", "Indu", "Cura"])

my_csv.close()

with open("Pruebas\Intermedio\My_csv.csv") as My_csv:
    for date in My_csv:
        print(date)
