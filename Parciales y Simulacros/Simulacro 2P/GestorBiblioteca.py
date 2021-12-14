"""
 Se debe crear una clase GestorBiblioteca que cuente con las siguientes funciones para un menu:

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
import Libro as li
lista_libros = []

class GestorBiblioteca:
    
    def crear_libro(self):
        while True:
            condicion=input(
            """
        ---------------- CREAR LIBRO ----------------
        Por favor ingrese la opcion que desee utilizar
            1. Libro Genérico
            2. Libro de Niños
            3. Libro de Idiomas
        Número: """)

            if condicion == "1" or condicion == "2" or condicion == "3":
                break
            else:
                print("Opcion incorrecta")
     #self, id, nombre, autor, estado   
        while True: #pide id
            id = input("Ingrese el id del libro: ")
            if id.isdigit():
                flag_agregar = True
                for i in lista_libros:
                    if (id == i.get_id()):
                        print("El id debe ser único")
                        flag_agregar = False
                        break
                if(flag_agregar): #significa que el id es valido, puede salir del while
                    break
            else:
                print("El legajo debe se numerico")

        nombre = input("Ingrese el nombre del libro: ")  
        autor = input("Ingrese el nombre del autor: ")
        estado = "no alquilado"
#Agrega el idioma la objeto 3
        if condicion == "3":
          idiomas = {
          "IN":"ingles", 
          "AL": "aleman",
          "CH":  "chino"
          }
          print("""
               ---------------- IDIOMA ----------------
                    IN = ingles
                    AL = aleman
                    CH = chino
               """)
          idioma = input("Ingrese el idioma que desea:  ")
          valor = idiomas.get(idioma, "español")
          print(f"La opción {idioma} corresponde a {valor}.")

        if condicion == "1":
            nombre_instancia = li.Libro(id, nombre, autor, estado )
        elif condicion == "2":
            nombre_instancia = li.LibroNiños(id, nombre, autor, estado , edad_minima = 11)
        elif condicion == "3":
            nombre_instancia = li.LibroIdiomas(id, nombre, autor, estado, idioma)
        
        lista_libros.append(nombre_instancia)

#Escribe automaticamente en el archivo txt cuando se crea el objeto
        import os
        path = os.path.abspath(os.path.dirname(__file__))
        path_archivo = path+"\\libros.txt"
        try:
            fichero = open(path_archivo, 'a+')
            fichero.write(f"ID: {id}, Nombre: {nombre},Autor: {autor} \n")
            fichero.close()
        except:
            print("ERROR.")

#Imprime la lista de libros y que tipo de objetos son
    def imprimir_libros(self):
        for i in lista_libros:
            i.presentarse()
            i.tipo_objeto()

#Cambio el estado de ALQUILADO a NO ALQUILADO y viceversa 
    def cambiar_estado(self):
            if len(lista_libros) == 0: #Me aseguro que la lista no este vacia al iniciar 
                print("La lista de libros esta vacia. Por favor agregue libros. ")
            flag_principal = True #Me aseguro de romper el primer while al agregar este flag.
            while flag_principal: #En este while compuebo que el id exista
                num_id = input("Ingrese el numero del id del libro: ")
                if num_id.isdigit(): 
                    flag = True
                    for i in lista_libros:
                        if num_id == i.get_id():
                            flag = False
                    if flag == False:
                        print("Valido")
                        print(i.get_estado()) 
                        flag_principal = False
                    else:
                        print("Legajo invalido")    
                else:
                    print("El legajo debe se numerico")

            while True: #Con este while se cambia de estado al libro
                condicion=input(
                        """
                    ---------------- CAMBIAR ESTADO ----------------
                    Por favor ingrese la opcion que desee utilizar
                        1. Alquilar libro
                        2. Devolver libro
                        3. Salir
                    Número: """)
                if condicion == "1": 
                    i.set_estado(nuevo_estado = "ALQUILADO") 
                elif condicion == "2": 
                    i.devolver_alquiler(nuevo_estado = "NO ALQUILADO")
                elif condicion == "3":
                    break
                else:
                    print("Opcion incorrecta")
