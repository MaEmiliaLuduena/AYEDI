"""
El programa debe:
*   Contar con una Clase Libro con los atributos (Id(unico), Nombre, Autor y estado (alquilado o no))
*   Contar con dos Clases Hijas que use el constructor de la clase padre pero que tenga un atributo mas:
        - LibroNiños (Atributo: edad_minima (por defecto = 11))
        - LibroIdiomas (Atributo: idioma_libro)

*   Se deben crear 4 metodos para la clase padre Libro (que heredaran las clases hijas):
        1. Presentarse: Que indique el Nombre, autor, id del libro y su estado 
        2. Indicar tipo de libro (tipo de clases heredadas o padre)
        3. Alquilar (Cambiaran el estado del libro a ALQUILADO)
        4. Devolver_alqiuer (Cambiaran el estado del libro a No alquilado)
"""

#CLASE PADRE
class Libro:
    def __init__(self, id, nombre, autor, estado): #CONSTRUCTOR
        self.id = id #unico
        self.nombre = nombre #del Libro
        self.autor = autor
        self.estado = estado #alquilado o no
        
    #para todas las clases  (padre e hijas)
    def presentarse(self):
        print(f"Soy un Libro con Nombre: {self.nombre}, del Autor: {self.autor}, con id: {self.id} y mi estado es: {self.estado}")
    
    #para todas las clases  (padre e hijas)
    def tipo_libro(self):
        print("Soy un Libro tipo", type(self).__name__)
    
    def alquilar_libro(self):
        self.estado = "Alquilado"

    def devolver_alquiler(self):
        self.estado = "No Alquilado"

#CLASES HIJAS
class LibroNiños(Libro):
    def __init__(self, id, nombre, autor, estado, edad_minima= 11):
        super().__init__(id, nombre, autor, estado)
        self.edad_minima = edad_minima
 
class LibroIdiomas(Libro):
    def __init__(self, id, nombre, autor, estado, idioma_libro):
        super().__init__(id, nombre, autor, estado)
        self.idioma_libro = idioma_libro
 
