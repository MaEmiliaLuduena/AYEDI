"""
El programa debe:
*    Pedir al usuario una cantidad de tramos de un viaje
*    Pedir al usuario la duración en minutos de cada tramo
*    Calcular el tiempo total de viaje
*    No deben generar errores
"""

tramos= int(input("Ingrese la cantidad de tramos de su viaje: "))
i= 1
acum= 0
while i <= tramos:
    try:
        duracion= int(input("Ingrese la duración en minutos de cada tramo: "))
        i +=1
        acum += duracion
    except:
        print("Error")
    
tiempo_total= acum / 60
print("El tiempo total del viaje fue de ", tiempo_total, "hs.")