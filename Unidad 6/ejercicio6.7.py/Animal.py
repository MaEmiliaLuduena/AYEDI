"""
*   La Clase Animales tiene los atributos (nombre, tipo_animal, fecha_nacimiento, 
    encargado_cuidar (LEGAJO de objeto empleado))
    *   Crear 3 clases que hereden de animal segun su sector del zoologico)
        1. AnimalesEnjaulados.
        2. AnimalesSueltos.
        3. AnimalesAcuaticos
"""
class Animal:
        #CONSTRUCTOR
    def __init__(self, nombre, tipo_animal, fecha_nacimiento, encargado_cuidar):
        self.nombre = nombre
        self.tipo_animal = tipo_animal
        self.fecha_nacimiento = fecha_nacimiento
        self.encargado_cuidar = encargado_cuidar

    def tipo_objeto(self):
        print("Soy un animal tipo", type(self).__name__)
    
    def set_empleado(self,encargado_cuidar):
        self.encargado_cuidar = encargado_cuidar

    def presentarse(self):
        print(f"Clase: {type(self).__name__} - Nombre: {self.nombre} - Nacimiento {self.fecha_nacimiento}")
 
class AnimalesEnjaulados(Animal):
    pass
 
class AnimalesSueltos(Animal):
    pass
 
class AnimalesAcuaticos(Animal):
    pass
"""
animal = Animal("ani1","felino","1/1/2010","pedro")
animal_marino = AnimalesAcuaticos("ani2","felino","9/1/2010","pedro")
animal_jaula = AnimalesEnjaulados("ani3","felino","8/1/2010","pedro")
animal_suelto = AnimalesSueltos("ani4","felino","7/1/2010","pedro")
animal.tipo_objeto()
animal_marino.tipo_objeto()
animal_jaula.tipo_objeto()
animal_suelto.tipo_objeto()"""