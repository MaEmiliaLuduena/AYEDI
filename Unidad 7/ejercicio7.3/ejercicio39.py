"""
#### **Ejercicio 7.3**
Crear una funcion para leer un archivo.txt.

Crear funciones para:
*   Contar la cantidad de letrar que tiene el archivo (letras no espacios ni puntos)
*   Contar la cantidad de palabras que tiene el archivo
"""

def leer_caracteres():
    try:
        fichero = open("archivo1.txt", 'r')
        contador = 0
        while True:
            letra = fichero.readline(1)
            if letra == "":
                break
            elif letra != " " and letra != ".":
                contador += 1
                
        fichero.close()
        print(f"Se encontraronn {contador} letras en el Archivo.")
        
    except:
        print("no existe el archivo")

leer_caracteres()