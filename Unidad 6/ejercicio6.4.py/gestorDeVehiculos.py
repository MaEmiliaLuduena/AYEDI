"""
Crear clase GestorAutos que cuente con las siguientes funciones para un menu
1.   Crear auto, indicando tipo de auto y guardar en una lista
2.   Listar autos (presentandolos), indicando tipo de Vehiculo.
3.   Cambiar velocidad de un Vehiculo
4.   Calcular tiempo de viaje de un Vehiculo en una cant de Km pasados por parametro (tiempo = Km / Velocidad)
"""
import Vehiculos as vh
lista_vehiculos = []
class gestorDeVehiculos:

    def __init__(self):
        pass
    
    def crear_vehiculo(self):
        while True:
            tipo_auto = input(
        """
    -----------Crear Vehiculo-----------
    Por favor ingrese el Vehiculos que quiere crear:
        1. Vehiculo Generico
        2. Vehiculo Particular
        3. Vehiculo Deportivo
        4. Vehiculo PickUp
        Opcion: """
        )
            if (tipo_auto == "1" or tipo_auto =="2" or tipo_auto =="3" or tipo_auto =="4"):
                break
            else:
                print("opcion incorrecta")
        #marca, ano, origen
        patente = input("Ingrese la patente del vehiculo: ")
        marca = input("Ingrese la marca del vehiculo: ")
        origen = input("Ingrese el origen del vehiculo: ")
        
        while True:
            try:
                año_vehiculo = int(input("Ingrese el año del vehiculo: "))
                break
            except:
                print("Incorrecto")

        if(tipo_auto =="2" or tipo_auto =="3" or tipo_auto =="4"):
            while True:
                try:
                    vel_max = int(input("Ingrese la velocidad máxima: "))
                    break
                except:
                    print("Incorrecto")

        if tipo_auto=="1":
            nombre_instancia = vh.Vehiculo(patente,marca,año_vehiculo,origen)
        elif tipo_auto=="2":
            nombre_instancia = vh.Vehiculos_Particular(patente,marca,año_vehiculo,origen,vel_max)
        elif tipo_auto=="3":
            nombre_instancia = vh.Vehiculos_Deportivo(patente,marca,año_vehiculo,origen,vel_max)
        elif tipo_auto=="4":
            nombre_instancia = vh.Vehiculos_PickUp(patente,marca,año_vehiculo,origen,vel_max)

        lista_vehiculos.append(nombre_instancia)
    
    #listar vehículos    
    def listar_vehiculos(self):
        for vehiculo in lista_vehiculos:
            vehiculo.presentarse()
            vehiculo.tipo_vehiculo()
    
    #cambia velocidades
    def cambiar_velocidad(self):
        for vehiculo in lista_vehiculos:
            print(vehiculo.patente)

       
        while True: #SI NO ANDA SACAR ESTE WHILE Y BORRAR UN ESPACIO   
            patente = input("Ingrese la patente del vehiculo a cambiarle la velocidad: ")
            for vehiculo in lista_vehiculos:
                if vehiculo.patente == patente:
                    if type(vehiculo).__name__!="Vehiculo":
                        while True:
                            try:
                                vel_max2 = int(input("Ingrese la velocidad máxima: "))
                                break
                            except:
                                print("Incorrecto")
                        vehiculo.setear_velocidad_max(vel_max2)
                        break
                    else:
                        print("El vehiculo generico no tiene velocidad max")

    #Calcular tiempo de viaje de un Vehiculo en una cant de Km pasados por parametro (tiempo = Km / Velocidad)
    def calcular_tiempo(self):
        for vehiculo in lista_vehiculos:
            print(vehiculo.patente)

        #falta u while para que no salga si la patente esta mal HACER
        while True:
            patente = input("Ingrese la patente del vehiculo a cambiarle la velocidad: ")
            for vehiculo in lista_vehiculos:
                if(vehiculo.patente == patente):
                    if(type(vehiculo).__name__!="Vehiculo"):
                        while True:
                            try:
                                km = int(input("Ingrese el km: "))
                                print(f"El tiempo en recorrer los {km} km = {km/vehiculo.velocidad_max} hs min")
                                break
                            except:
                                print("Incorrecto")
                    else:
                        print("El vehículo genérico no tiene velocidad max")