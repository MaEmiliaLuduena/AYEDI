"""
#### **Ejercicio 7.7**
Crear una programa con cuatro opciones:
1.  Crear un archivo en blanco, con el nombre que desee el usuario
2.  Escribir datos en el archivo sin pisar los existentes
3.  borrar los datos del archivo
4.  leer linea a linea el archivo (YA LO HICIMOS)
"""

import os
path = os.path.abspath(os.path.dirname(__file__))
path_archivo = path+"\\archivo.txt"
print(path)

def crear_archivo():
    nombre = input("Ingrese el nombre del archivo: ")
    path_archivo = path+ f"\\{nombre}.txt"
    try:
        fichero = open(path_archivo, 'x')
        fichero.close()
    except:
        print("ERROR.")

def escribir_en_archivo(palabra):
    try:
        fichero = open(path_archivo, 'a')
        fichero.write(palabra+"\n")
        fichero.close()
    except:
        print("Error")

def pedir_palabras():
    while True:
        palabra = input("Ingrese una palabra: (escriba exit para salir): ")
        if palabra == "exit":
            break
        else:
            escribir_en_archivo(palabra)

def borrar_archivo():
    try:
        fichero = open(path_archivo, 'w')
        fichero.close()
    except:
        print("Error")

def leer_archivo():
    try:
        archivo= open(path_archivo,'r')
        while True:
            linea = archivo.readline()
            if linea == "":
                break
            print(linea,end="")
        archivo.close()
    except:
        print("Error")


while True:
    opcion = input(
    """
-----------Menu principal-----------
Por favor ingrese una opcion:
    1. Crear un archivo
    2. Escribir datos
    3. Borrar los datos del archivo
    4. Leer archivo
    5. Salir
    Opcion: """
    )
    if (opcion=="1"):
        crear_archivo()
    elif (opcion=="2"):
        pedir_palabras()
    elif (opcion=="3"):
        borrar_archivo()
    elif (opcion=="4"):
        leer_archivo()    
    elif (opcion=="5"):
        break
    else:
        print("ninguna opción correcta")
