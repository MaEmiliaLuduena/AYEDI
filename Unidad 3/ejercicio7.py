"""
El programa debe :
*    Pedir al usuario un string
*    Determinar si una cadena esta en minusculas o mayusculas
"""
try:
    palabra= input("Ingrese una palabra o cadena de caracteres: ")
    if palabra.islower():
        print("Tu cadena de caracteres está en minúscula")
    else:
        print("Tu cadena de caracteres no está en minúscula en su totalidad")
except:
    print("Ingresaste un valor erróneo")