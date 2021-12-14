"""
El programa debe:
*     Preguntar al usuario una cantidad a invertir
*     Preguntar al usuario el interés anual y el número de años
*     Mostrar por pantalla el capital obtenido en la inversión cada año que dura la inversión
"""

cant_invertir= int(input("Ingrese la cantidad a invertir: "))
interes= float(input("Ingrese el interés anual: "))
años= int(input("Ingrese la cantidad de años de la inversión: "))

for i in range(1, años+1):
    capital = (cant_invertir * interes / 100) * años
    print("El capital obtenido en ", años, " año/s es de $ ", capital)
