"""
*   Se debe crear una clase GestorBiblioteca que cuente con las siguientes funciones para un menu:

    1.  Crear instancias de libros y guardalos en una lista de libros. 
        1.1) Se debe verificar que tipo de instancia de libro crear y los parametros
             - Id debe ser unico, se comienza del 1
             - Nombre y autor no es necesario
             - estado debe comenzar "No alquilado"
        1.2) Al crear un libro es necesario logearlo (Escribir en una linea nueva: id-nombre-autor) 
             en un archivo llamado libros.txt (Crear funcion en el mismo gestor)
        1.3) En caso que la instancia del libro sea LibroIdiomas.
             - El usuario  debe elegir a travez de una clave (mostradas por el programa) desde un diccionario de idiomas.
             - En caso que no exista el idioma deseado debe ser en idioma "español" (AYUDA: Funcion get de diccionarios)
    2.   Listar libros disponibles (recorrer la lista, no el archivo)
    3.   Cambiar el estado (Alquilar o devolver) de un libro, seleccionando su id. (Hacer check correspondientes)
"""

import Libro as lb

lista_libros= [id, nombre, autor, estado="No alquilado"]

def instancia_libros():
    while True:
        try:
            id_libro= int(input("Ingrese el id del libro: "))
            for id_libro in lista_libros:
                if id_libro not in lista_libros:
                    lista_libros.append(id_libro)
                    break
                else:
                    print("Ya se encuentra ese id en otro libro")
        except:
            print("Error en el campo id")        
        
        nombre= input("Ingrese el nombre del libro")
        lista_libros.append(nombre)

        try:
            autor= input("Ingrese el autor del libro: ")
            if autor.isdigit():
                print("No puedes ingresar números o símbolos")
            else:
                lista_libros.append(autor)
        except:
            print("Error en el campo autor")

        
            

