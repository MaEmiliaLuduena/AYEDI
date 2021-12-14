"""
###**Ejercicio 4.2 (Mediciones)**
El programa debe:
*   Contar con 4 funciones (calcular Area (cuadrado), calcular Perimetro(cuadrado),
    calcular Area (circulo), calcular Perimetro(circulo))
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los parametros y devolver el resultado al usuario
*   Gestionar posibles errores
"""
import math as mt

def perimetro_circulo():
    while True:
        try:
            radio = float(input("Ingrese el radio del circulo: "))
            if(radio<=0):
                print("El radio debe ser mayor que cero")
            else:
                break
        except:
            print("datos erroneos")

    print(f"El perimetro del circulo es{round(2*mt.pi*radio,0)}")

def area_cuadrado():
    while True:
        try:
            lado=float(input("Ingrese el lado del cuadrado: "))
            if lado<=0:
                print("El lado de un cuadrado no puede ser negativo, reitentar.")
            else:
                break
        except:
            print("Dato erroeo. Reintentar")

    print(f"El area del cuadrado es: {lado*lado}")

def area_circulo():
    while True:
        try:
            radio=float(input("Ingrese el radio del circulo: "))
            if radio<=0:
                print("El radio debe ser mayor que 0. Reintentar")
            else:
                break
        except:
            print("Dato erroneo. Reintentar")
    print(f"El area del circulo es {round(mt.pi*(radio*radio),2)}")

def perimetro_cuadrado():
    while True:
        try:
            lado_cuadrado= float(input("Ingrese cuanto mide un lado del cuadrado: "))
            if (lado_cuadrado <= 0):
                print("Ingrese un numero mayor o distinto de cero")
            else:
                break 
        except:
            print("ERROR. Datos erroneos")
    print(f"El perimetro del cuadrado es: {lado_cuadrado*4 }")

while True:
    condicion=input(
    """Por favor ingrese una opcion:
        1. Calcular area cuadrado
        2. Calcular perimetro cuadrado
        3. Calcular area circulo
        4. Calcular perimetro circulo
        5. Salir
    Opcion: """)
    if condicion=="1":
        area_cuadrado()
    elif condicion=="2":
        perimetro_cuadrado()
    elif condicion=="3":
       area_circulo() 
    elif condicion=="4":
        perimetro_circulo()
    elif condicion=="5":
        break
    else:
        print("No ha seleccionado una opción correcta.")