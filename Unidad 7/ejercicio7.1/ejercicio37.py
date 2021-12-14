"""
#### **Ejercicio 7.1**
Crear una funcion para leer el un archivo.txt hasta encontrar un punto.
"""

try:
    fichero = open("archivo.txt", 'r')
    caracter = fichero.readline(1) #para leer caracter por caracter
    while caracter != ".":
      print(caracter,end="")
      caracter = fichero.readline(1)
    fichero.close()
except:
    print("no existe el archivo")
####################################################

import os
path = os.path.abspath(os.path.dirname(__file__))#probar este 1°
print(path)
#path = os.path.abspath(os.path.dirname('__file__'))#probar este 2°
#path = os.path.dirname(os.path.abspath("__file__"))#probar este 3°
def imprimir_hasta_punto_while():
    try:
        fichero = open(path+"\\archivo.txt", 'r')
        while True:
            caracter = fichero.readline(1)
            print(caracter,end="")
            if(caracter=="."):
                break
        fichero.close()
    except:
        print("no existe el archivo")