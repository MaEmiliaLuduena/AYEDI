"""
El programa debe:

pedir al usuario una palabra
pedir un numero al usuario
mostrar la palabra por pantalla la cantidad de veces que diga el numero
no debe generar errores
"""

i= 0
try:
    palabra= input("Ingrese una palabra: ")
    numero= int(input("Ingrese un número: "))
    while i<numero:
        i += 1
        print(palabra)
except:
    print("Error")