"""
1- Obtener titulos de cada columna (1° fila)
2- contar la cantidad de columnas
3- contar la cantidad de filas
"""
import os
path = os.path.abspath(os.path.dirname(__file__))
path_tabla = path+"\\tabla.csv"
print(path)

def leer_titulos():
    try:
        tabla= open(path_tabla,'r')
        titulos = tabla.readline()
        lista_titulos = titulos.split(',')
        print("Los titulos son: ",end="")
        cont = 0
        for i in lista_titulos:
            print(i,end="-")
            cont+=1
        print(f"La cantidad de columnas son: {cont}")
        tabla.close()
    except:
        print("error")



def contar_filas():
    try:
        tabla= open(path_tabla,'r')
        cont = 0
        while True:
            linea = tabla.readline()
            print(linea)
            
            if linea == "":
                break
            cont+=1
        print(f"La cantidad de filas son: {cont}")
        tabla.close()
    except:
        print("error")
