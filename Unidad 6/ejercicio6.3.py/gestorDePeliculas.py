    """El programa debe: gestorDePeliculas
*   Tener un menu con 7 opciones:
    1. Crear una pelicula y guardar su nombre (instancia) en una lista de peliculas.
    2. Verificar si la pelicula deseada existe en la lista de peliculas (a partir del nombre).
    3. Pedir a la lista de peliculas, todas las de un año.
    4. Presentar una pelicula de la lista
    5. Cambiar el genero de una pelicula
    6. Verificar el año de la pelicula
    7  Modificar puntuacion de la pelicula (entre 1 y 10)
    """
import ClasePelicula as pl
lista_peliculas = [] #empieza vacia
lista_generos=["Comedia","Accion","Drama","Terror","Suspenso","Ciencia ficcion","Infantil"]

class GestorDePeliculas:
    def __init__(self):
        pass

    def crear_peliculas(self):
        #Verifico el nombre
        while True:
            nombre = input("Ingrese el nombre de la pelicula: ").capitalize()
            if self.verificar_pelicula(nombre) == False: #True -> la pelicula existe , False -> No existe
                break

        #Verifico el año
        while True:
            try:
                año = int(input("Por favor ingrese el año: "))
                break
            except:
                print("El año es numerico")

        #Verifico el genero
        while True:
            genero = input("Ingrese el genero de la pelicula: ")
            if genero in lista_generos:
                break
            else:
                print("Reintentar, el genero no se encuentra registrado en el sistema.")
                print(lista_generos)
        #Pedimos la nacionalidad
        while True:
            nacionalidad = input("Ingrese la nacionalidad: ").capitalize()
            if nacionalidad.isalpha():
                break
            else:
                print("La nacionalidad no puede tener simbolos")
        #Verificar la puntuacion
        while True:
            try:
                puntuacion=int(input("Ingrese la puntuacion: "))
                if puntuacion > 0 and puntuacion <= 10:
                    break
                else:
                    print("La puntuacion debe estar entre 1 y 10")
            except:
                print("Error en los argumentos")

        nombre_intancia = pl.Pelicula(nombre,año,genero,nacionalidad,puntuacion)
        
        lista_peliculas.append(nombre_intancia)   


    def imprimir_lista(self):
        #print(f"la longitud de la lista es de {len(lista_peliculas)}")
        cont = 1
        for peliculas in lista_peliculas: #Enumera las películas con el contador
            print(f"{cont}. ", end ="")
            peliculas.presentar_pelicula()
            cont+=1

    #Verifica si la pelicula deseada existe en la lista de peliculas
    def verificar_pelicula(self,nombre_pelicula = "null"):
        while True:
            if nombre_pelicula == "null":
                nombre_pelicula = input("Ingrese el nombre de la pelicula a verificar: ").capitalize()

            for peliculas in lista_peliculas:
                if nombre_pelicula == peliculas.nombre:
                    print("Esta pelicula ya existe")
                    return True

            print("Esta pelicula no existe")
            return False

    #Pedir a la lista de peliculas, todas las de un año.
    def peliculas_año(self):
        while True:
            try:
                año = int(input("Por favor ingrese el año: "))
                break
            except:
                print("El año es numérico")
        cont = 1        
        flag = False
        for peliculas in lista_peliculas:
                if peliculas.año == año:
                    print(f"{cont}. {peliculas.nombre}")
                    cont+=1 #Suma la cantidad de películas de un mismo año
                    flag = True
        
        if flag == False:
            print("No existe ninguna película en ese año")
                    

    #5. Cambiar el genero de una pelicula
    def nuevo_genero(self):
        while True:
            self.imprimir_lista()
            nuevo_nombre = input("Por favor ingrese el NOMBRE de la pelicula o 0 para salir: ").capitalize()
            #si el usuario ingresó cero me voy del método
            if nuevo_nombre == "0":
                return

            for pelicula in lista_peliculas: #reocorro la lista de peliculas
                print(f"Nombre pelicula en la lista {pelicula.nombre} vs {nuevo_nombre}")
                if pelicula.nombre == nuevo_nombre:
                    while True:
                        nuevo_genero = input("Ingrese el nuevo Genero de la Pelicula: ").capitalize()
                        if nuevo_genero in lista_generos: #verificamos que el genero este dentro de la lista
                            if pelicula.genero == nuevo_genero: #se fija si el genero es el mismo que estaba antes
                                print("La pelicula ya posee ese genero")
                            else:
                                pelicula.cambiar_genero(nuevo_genero)   #actualiza el nombre del género
                            return
                        else:
                            print("Por favor ingrese un género de la lista")
                            print(lista_generos)