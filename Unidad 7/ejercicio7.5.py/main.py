"""#### **Ejercicio 7.5 (FALTA)**
Crear una clase para leer archivos (lectorDeArchivos).
Crear funciones para:
*   Leer el archivo e imprimir todo su contenido
*   Encontrar la cantidad de comas en el archivo.
*   Contar la cantidad de palabras de 3 letras y guardarlas en un lista
*   Especificar una palabra a quitar e imprimir el contenido sin esta palabra"""
import os
path = os.path.abspath(os.path.dirname(__file__))#probar este 1°

class LectorDeArchivos:
    def leer_archivo(self):
        archivo = input("Ingrese el nombre del archivo a leer (con su formato): ")
        path_archivo = path + "\\" + archivo
        print(path_archivo)
        try:
            fichero = open(path_archivo, 'r')
            print(fichero.read())
            fichero.close()
        except:
            print("error con el archivo")
    
    def encontrar_cant_comas(self):
        archivo = input("Ingrese el nombre del archivo a leer (con su formato): ")
        path_archivo = path + "\\" + archivo
        #print(path_archivo)
        try:
            fichero = open(path_archivo, 'r')
            archivo_text = fichero.read()
            cont = 0
            for i in archivo_text:
                if(i == ","):
                    cont+=1
            fichero.close()
            print(f"El texto tiene {cont} comas")
        except:
            print("error con el archivo")
    
    def encontrar_cant_comas_2(self):
        archivo = input("Ingrese el nombre del archivo a leer (con su formato): ")
        path_archivo = path + "\\" + archivo
        #print(path_archivo)
        try:
            fichero = open(path_archivo, 'r')
            cont = 0  
            caracter = fichero.readline(1)
            while caracter != "":
                if (caracter == ","):
                    cont+=1
                caracter = fichero.readline(1)
                
            fichero.close()
            print(f"El texto tiene {cont} comas")
        except:
            print("error con el archivo")

lector = LectorDeArchivos()
#lector.leer_archivo()
lector.encontrar_cant_comas_2()