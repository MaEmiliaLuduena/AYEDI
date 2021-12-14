""" ##**Ejercicio 5.4**
Crear una funcion que debe:

*   Pedir al usuario una cantidad de tramos de un viaje
*   Pedir al usuario la duracion en minutos de cada tramo (usar listas)
*   Calcular el tiempo total de viaje (motrar en horas)
*   No deben aparecer y se deben tener en cuenta todos los posibles errores """

def viaje():
    duracion_de_tramo = []
    while True:
        try:
            cantidad_de_tramos=int(input("Por favor introduzca la cantidad de tramos del viaje: "))
            break
        except:
            print("Error, reintentar.")
    for i in range(cantidad_de_tramos):
        while True:
            try:
                tramo = int(input(f"Por favor ingresar la duración del tramo {i+1} en minutos: "))
                duracion_de_tramo.append(tramo)
                break
            except:
                print("Error, reintentar.")
    
    tiempo_total=0
    for i in duracion_de_tramo:
        tiempo_total += i
        
    horas,minutos = minutos_a_hora(tiempo_total)
    print(f"La duracion de todo el viaje es: {horas}hs: {minutos}min")

def minutos_a_hora(minutos):
    minutos_iniciales = minutos
    horas_finales = 0
    while  minutos > 60:
        minutos = minutos - 60
        horas_finales+=1

    #print(f"los {minutos_iniciales} son {horas_finales} hs:{minutos} min")
    return horas_finales,minutos

viaje()