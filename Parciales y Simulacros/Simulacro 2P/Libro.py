"""
El programa debe:
*   Contar con una Clase Libro con los atributos (Id(unico), Nombre, Autor y estado (alquilado o no))
*   Contar con dos Clases Hijas que use el constructor de la clase padre pero que tenga un atributo mas:
        - LibroNiños (Atributo: edad_minima (por defecto = 11))
        - LibroIdiomas (Atributo: idioma_libro)
        
*   Se deben crear 4 metodos para la clase padre Libro (que heredaran las clases hijas):
        1. Presentarse: Que indique el Nombre, autor, año del libro y su estado 
        2. Indicar tipo de libro (tipo de clases heredadas o padre)
        3. Alquilar (Cambiaran el estado del libro a ALQUILADO)
        4. Devolver_alqiuer (Cambiaran el estado del libro a No alquilado)
"""

class Libro:
    #CONSTRUCTOR
    def __init__(self, id, nombre, autor, estado = "no alquilado"):
        self.id = id
        self.nombre = nombre
        self.autor = autor
        self.estado = estado

    def tipo_objeto(self):
        print("Libro tipo: ", type(self).__name__)

    def get_id(self):
        return self.id

    def get_estado(self):
        return self.estado

    def set_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        
    def devolver_alquiler(self, nuevo_estado):
        self.estado = nuevo_estado

    def presentarse(self):
        print("")
        print(f" Id: {self.id} / Nombre del libro: {self.nombre} / Autor {self.autor} / Estado: {self.estado}")
        print("")

#Clase hija LibroNiños        
class LibroNiños(Libro):
        def __init__(self,id, nombre, autor, estado, edad_minima = 11):
            super().__init__(id, nombre, autor, estado = "no alquilado" )
            self.edad_minima = edad_minima

#Clase hija LibroIdiomas
class LibroIdiomas(Libro):
    def __init__(self,id, nombre, autor, estado, idioma):
        super().__init__(id, nombre, autor, estado = "no alquilado")
        self.idioma = idioma