"""
*   Contar con 6 funciones disponibles en el menu **(estas funciones deben estar incluidas en una clase llamada GestorZoologico)**:
    1. Crear instancia de Empleados y guardarlos en una lista
        * Los empleados se les pueden asignar animales luego, los animales al crearlos en el sistema tienen q contar siosi con un encargado
    2. Crear instancias de animales (se puede elegir entre los tres sectores)  y guardarlos en una lista
    3. Asignar a un empleado un animal a cuidar
    4. Cambiar de encargado un animal
    5. imprmir lista de animales (con toda su informacions)
    6. imprimir lista de Empleados (con toda su informacions)
    """
import Empleado as em
lista_empleados = []

class GestorZoo:
    def crear_instancia_empleado(self):
        flag = True
        #flag2 = False (propuesta)
        while flag: #
            legajo = input("Ingrese el legajo: ")
            for i in lista_empleados:
                if (legajo == i.get_legajo()):
                    print("El legajo debe ser unico")
                    flag2 = True
            # if(flag2): PROPUESTA


        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el nombre: ")
        lista_empleados.append(em.Empleado(legajo,nombre,apellido))
    
    def imprimir_empleados(self):
        for i in lista_empleados:
            i.presentarse()