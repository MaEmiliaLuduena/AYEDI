"""
###**Ejercicio 4.3 (Palabras)**
El programa debe:
*   Contar con 3 funciones:
    1. Contador de letras (letra,palabra): Debe contar la cantidad de la letra del parametro que tiene una palabra o 
    frase (letra y frase deben Ambos parametros)
    2. Comparador de palabras (palabra1 vs palabra2): debe comparar que palabra tiene mas letra.
    IMPORANTE: deben ser palabras y no frases (verificar)
    3. Quitador de vocales (palabra a retirar las vocales): debe recibir una palabra o frase y 
    quitar todas las vocales
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los parametros y devolver el resultado al usuario
*   Gestionar posibles errores
"""
def contador_de_letras(letra,palabra_o_frase):
    contador=0
    for i in palabra_o_frase:
        if i == letra:
            contador +=1
    return contador

def comparador_de_palabras(palabra_1,palabra_2):
    contador_1=0
    contador_2=0
    for i in palabra_1:
        if i != " ":
            contador_1+=1
        else:
            contador_1 = -1
            break

    for i in palabra_2:
        if i!=" ":
            contador_2+=1
        else:
            contador_2=-1
            break  
    if contador_1 == -1 or contador_2 == -1:
        print("Se ha ingresado una frase")
    elif contador_1>contador_2:
        print("La palabra 1 tiene más letras")
    elif contador_1==contador_2:
        print("Las palabras tienen la misma cantidad de letras")
    else:
        print("La palabra 2 tiene más letras")

""" def quitador_vocales(palabra_o_frase):
    palabra_auxiliar=""
    for i in palabra_o_frase:
        if i != "a" or i !="e" or i != "i" or i !="o" or i !="u":
            palabra_auxiliar = palabra_auxiliar + i
    
    return palabra_auxiliar """

def quitar_vocales2():
    vocales = ["a","e","i","o","u","A","E","I","O","U"]
    palabra_1=input("Ingrese una palabra o frase: ")
    palabra_2=input("Ingrese otra palabra o frase: ")
    nueva_palabra1=""
    nueva_palabra2=""
    for i in palabra_1:
        if i not in vocales:
            nueva_palabra1 +="".join(i)
        else:
            pass
    for i in palabra_2:
        if i not in vocales:
            nueva_palabra2 +="".join(i)
        else:
            pass
    print(f""" 
    #1° Palabra: {nueva_palabra1}
    #2° Palabra: {nueva_palabra2}
    #Son las palabras sin vocales.""")

while True:
    condicion=input(
    """
    Por favor ingrese una opcion:
    1. Contador de letras
    2. Comparador de palabras
    3. Quitador de vocales
    4. Salir
    Ingrese: """)
    if condicion=="1":
        while True:
            letra = input("Ingrese una letra: ")
            if letra.isalpha():
                if len(letra)==1:
                    break
        while True:
            palabra = input("ingrese una palabra o frase: ")
            if len(palabra)>3:
                break 
        print(f"La cantidad de letras {letra} en {palabra} es: {contador_de_letras(letra,palabra)}")
    elif condicion=="2":
        while True:
            palabra_1= input("Ingrese la primer palabra: ")
            if palabra_1.isalpha():
                break
            else:
                print("Debe ingresar una palabra")
        while True:
            palabra_2= input("Ingrese la segunda palabra: ")
            if palabra_2.isalpha():
                break
            else:
                print("Debe ingresar una palabra")
        comparador_de_palabras(palabra_1,palabra_2)
        
    elif condicion=="3":
       quitar_vocales2()

    elif condicion=="4":
        print("Adiós!")
        break
    else:
        print("Opcion Incorrecta.")
#letras = quitador_vocales("hola buen dia")
#print(f"Palabra sin vocales: {letras}")