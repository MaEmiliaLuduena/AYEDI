"""
#### **Ejercicio 7.2**
Crear una funcion para leer un archivo.txt.
*   pedir al usuario una palabra y encontrar la cantidad de veces que aparece esa palabra en el archivo
"""

import os
#path actual
#path = os.path.abspath(os.path.dirname(__file__))#probar este 1°
path = os.path.abspath(os.path.dirname('__file__'))#probar este 2°
#path = os.path.dirname(os.path.abspath("__file__"))#probar este 3°
path_archivo = path+"\\archivo.txt"
print(path+"\\archivo.txt")##\\ por caracteres especiales

def leer_archivo():
    try:
        fichero = open("archivo1.txt", 'r')
        caracter = fichero.read()
        lista = caracter.split()
        contador = 0
        palabra= input("Ingrese la palabra a buscar: ")
        for i in lista:
            if i == palabra:
                contador += 1
                print(f"La palabra se encuentra {contador} veces en el Archivo.")
                caracter = fichero.read()
        fichero.close()
    except:
        print("no existe el archivo")


 

