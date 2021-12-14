"""
###**Ejercicio 4.1 (Calculadora)**
El programa debe:
*   Contar con 4 funciones (suma, resta, división y multiplicación)
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los dos numero para operar y devolver el resultado al usuario
*   Gestionar posibles errores
"""
def sumador(a,b):
    suma = float(a)+float(b)
    return suma

def restador(a,b):
    resta = float(a)-float(b)
    return resta

def divisor(a,b):
    division = float(a)/float(b)
    return division

def multiplicador(a,b):
    multiplicacion = float(a)*float(b)
    return multiplicacion

def pedir_numeros():
    while True:
        try:
            num1 = float(input("1° Argumento: "))
            num2 = float(input("2° Argumento: "))
            break
        except:
            print("argumentos incorrectos")

    return num1,num2


while True:
    condicion=input(
"""Por favor ingrese una opcion
        1. suma
        2. resta
        3. multiplicacion
        4. division
        5. Salir
Numero : """)
    if (condicion=="1"):
        a,b = pedir_numeros()
        print (f"La suma de {a} + {b} = {sumador(a,b)}")
    elif (condicion=="2"):
        a,b = pedir_numeros()
        print (f"La resta de {a} + {b} = {restador(a,b)}")
    elif (condicion=="3"):
        pass
    elif (condicion=="4"):
        pass
    elif (condicion=="5"):
        break
    else:
        print("ninguna opcion correcta")