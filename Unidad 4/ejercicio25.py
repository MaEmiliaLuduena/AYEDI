"""
El programa debe:
*   Contar con 4 funciones:
  1.  Conversor de Grados Celcius a Fahrenheit(temperatura en °C).(buscar regla)
  2.  Conversor de cm3 a litros (cantidad de cm3)
  3.  Conversor de litros a cm3 (cantidad de litros)
  4.  Pesos a Dolares (pesos)
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los parametros y devolver el resultado al usuario
*   Gestionar posibles errores
"""
def conversor_celcius_fahrenheit(temperatura_en_C):
    try:
        grado_fahrenheit= (temperatura_en_C * 1.8) + 32
        print(f"Usted tiene {grado_fahrenheit} grados Fahrenheit")
    except:
        print("Dato erróneo. Reintentar")

def conversor_cm3_litros(cant_cm3):
    try:
        litros= cant_cm3 * 0.001
        print(f"Usted tiene {round(litros,2)} litros")
    except:
        print("Dato erróneo. Reintentar")

def conversor_litros_cm3(cant_litros):
    try:
        cm3= cant_litros / 0.001
        print(f"Usted tiene {cm3} cm3") 
    except:
        print("Dato erróneo. Reintentar")

def convertir_pesos_dolares(pesos):
    try:
        dolares= pesos / 180
        print(f"Usted tiene {round(dolares,2)} dolares")
    except:
        print("Dato erróneo. Reintentar")


while True:
    condicion=input(
    """Por favor ingrese una opcion:
        1. Convertir de Grados Celcius a Fahrenheit
        2. Convertir de cm3 a litros
        3. Convertir de litros a cm3
        4. Convertir Pesos a Dolares
        5. Salir
    Opcion: """)
    if condicion=="1":
        temperatura_en_C= float(input("Ingrese la temperatura en °C: "))
        conversor_celcius_fahrenheit(temperatura_en_C)
    elif condicion=="2":
        cant_cm3= float(input("Ingrese la cantidad de cm3: "))
        conversor_cm3_litros(cant_cm3)
    elif condicion=="3":
        cant_litros= float(input("Ingrese la cantidad de litros: "))
        conversor_litros_cm3(cant_litros)
    elif condicion=="4":
        pesos= float(input("Ingrese la cantidad de pesos a convertir: "))
        convertir_pesos_dolares(pesos)
    elif condicion=="5":
        print("Adiós!")
        break
    else:
        print("No ha seleccionado una opción correcta.")