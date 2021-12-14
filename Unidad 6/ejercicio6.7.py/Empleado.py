"""
*   La Clase Empleados tiene los atributos (legajo, nombre, apellido, lista_animales_a_cuidar(clase animal))
      *  un empleado puede cuidar animales de diferentes sectores
"""
class Empleado:
    def __init__(self,legajo, nombre, apellido, lista_animales_a_cuidar = []):
        self.legajo = legajo
        self.nombre = nombre
        self.apellido = apellido
        self.lista_animales_a_cuidar = lista_animales_a_cuidar
    
    def asignar_animales(self,nuevo_animal):
        self.lista_animales_a_cuidar.append(nuevo_animal)
    
    def presentarse(self):
        print(f"{self.legajo} - {self.nombre} {self.apellido}")
        print("Cuida los siguientes animales")
        for i in self.lista_animales_a_cuidar:
            i.presentarse()

    def get_legajo(self):
        return self.legajo