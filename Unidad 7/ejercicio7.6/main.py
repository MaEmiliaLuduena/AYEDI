"""
#### **Ejercicio 7.6**
Crear una funcion que lo que le pida palabras al usuario 
y que las vaya escribiendo en un archivo txt cada palabra una bajo la otra."""

import os
path = os.path.abspath(os.path.dirname(__file__))
path_archivo = path+"\\archivo.txt"

def escribir_en_archivo(palabra):
    try:
        fichero = open(path_archivo, 'a')
        fichero.write(palabra+"\n")
        fichero.close()
    except:
        print("Error")

#escribir_en_archivo("hola")

def pedir_palabras():
    while True:
        palabra = input("Ingrese una palabra: (escriba exit para salir): ")
        if palabra == "exit":
            break
        else:
            escribir_en_archivo(palabra)

pedir_palabras()