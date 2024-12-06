import csv

preguntas = {}
#Abrir el archivo CSV
with open("datoschat.csv", "r") as archivo: 
    lector = csv.DictReader(archivo)
    for fila in lector:
        fila["preguntas"]
        fila["respuestas"]
        preguntas[fila["preguntas"]] =  fila["respuestas"]