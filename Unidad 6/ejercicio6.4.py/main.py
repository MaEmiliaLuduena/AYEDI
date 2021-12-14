"""
###**Ejercicio 6.4**
Crear una clase padre Vehiculos:
*   Constructor debe incluir los atributos (patente,marca,año,origen)
*   Crear metodos para esta clase de:
    1.  Presentarse (patente,marca,año,origen)
    2.  Indicar tipos de vehiculo(Clases heredadas)
    3.  Metodos que luego modificarán las clases hijas. Acelerar, Retroceder, obtener_velocidad, setear_velocidad
 
Crear 3 clases que hereden de la clase padre Vehiculos, con un atributo en particular para cada una
1.   Particular
2.   PickUp
3.   Deportivo
 
Crear clase GestorAutos que cuente con las siguientes funciones para un menu
1.   Crear auto, indicando tipo de auto y guardar en una lista
2.   Listar autos (presentandolos), indicando tipo de Vehiculo.
3.   Cambiar velocidad de un Vehiculo
4.   Calcular tiempo de viaje de un Vehiculo en una cant de Km pasados por parametro (tiempo = Km / Velocidad)
"""

import Vehiculos as vh
import gestorDeVehiculos as gv

gestor = gv.gestorDeVehiculos()

while True:
    opcion = input(
    """
-----------Menu principal-----------
Por favor ingrese una opcion:
    1. Crear Vehiculos
    2. Listar Vehiculos
    3. Cambiar velocidad
    4. Calcular tiempo
    5. Salir
    Opcion: """
    )
    if (opcion=="1"):
        gestor.crear_vehiculo()
    elif (opcion=="2"):
        gestor.listar_vehiculos()
    elif (opcion=="3"):
        gestor.cambiar_velocidad()
    elif (opcion=="4"):
        gestor.calcular_tiempo()
    elif (opcion=="5"):
        break
    else:
        print("ninguna opcion correcta")




"""
lista =[]
vehiculo_1 = vh.Vehiculos_Particular("ABCPA","ford",2020,"arg",110)
vehiculo_2 = vh.Vehiculos_Deportivo("ABCDE","ford",2020,"arg",200)
vehiculo_3 = vh.Vehiculo("ABC","ford",2020,"arg")
lista.append(vehiculo_1)
lista.append(vehiculo_2)
lista.append(vehiculo_3)
for i in lista:
    i.acelerar()
    i.presentarse()
"""