class Pelicula:
    #constructor
    def __init__(self,nombre,año,genero,nacionalidad,puntuacion):
        self.nombre = nombre 
        self.año = año
        self.genero = genero
        self.nacionalidad = nacionalidad
        self.puntuacion = puntuacion
    
    def presentar_pelicula(self):
        print(f"La pelicula {self.nombre} de {self.genero} del {self.año} obtuvo una puntuacion de {self.puntuacion} y fue filmada en {self.nacionalidad}")

    def año_pelicula(self):
        try:
            año_pelicula= int(input("Ingrese el año de la película: "))
            if self.año > año_pelicula:
                print("El año es mayor al indicado por parámetro")
            elif self.año == año_pelicula:
                print("El año es igual al indicado por parámetro")
            elif self.año < año_pelicula:
                print("El año es menor al indicado por parámetro")
        except:
            print("Error en el ingreso del año")

    def cambiar_genero(self, nuevo_genero):
        self.genero= nuevo_genero
        print(f"Se cambió el género de {self.genero} a {nuevo_genero}")
    
    def modificar_puntuacion(self, nueva_puntuacion):
        self.puntuacion = nueva_puntuacion
        print(f"Se cambió la puntuación de {self.puntuacion} a {nueva_puntuacion}")