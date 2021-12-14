base = {
    "peliculas" : ["El hombre araña", "Los vengadores el" , "Los vengadores 2"],
    "series" : ["prision break", "la casa de papel" , "los simpsons"]
        }

def mostrar_bases():
    while True:
        base_mostrar = input(
        """
-----------Menu BASES-----------
Ingrese si requiere ver:
1. la lista de peliculas
2. la lista de series
3. Salir
opcion: 
        """)
        if base_mostrar =="1":
            print(f"---------Peliculas---------")
            for i in range(len(base.get("peliculas"))):
                print(base.get("peliculas")[i])
        elif base_mostrar == "2":
            print(f"---------Series---------")
            for i in range(len(base.get("series"))):
                print(base.get("series")[i])
        elif base_mostrar == "3":
            break
        else:
            print("Opcion incorrecta")

def agregar_peliculas_series():
    while True:
        base_mostrar = input(
        """
-----------Menu AGREGAR-----------
Ingrese si requiere agregar:
1. Peliculas
2. Series
3. Salir
opcion: 
        """)
        if base_mostrar =="1":
            nombre_pelicula = input("Ingrese el nombre de la nueva pelicula: ")
            if nombre_pelicula not in base.get("peliculas"):
                base.get("peliculas").append(nombre_pelicula.capitalize())
            else:
                print("Esa película ya se encuentra")
        elif base_mostrar == "2":
            nombre_series = input("Ingrese el nombre de la nueva serie: ")
            if nombre_series not in base.get("series"):
                base.get("series").append(nombre_series.capitalize())
            else:
                print("Esa serie ya se encuentra")
        elif base_mostrar == "3":
                break
        else:
                print("Opcion incorrecta")

def eliminar_peliculas_series():
    while True:
        base_mostrar = input(
        """
-----------Menu ELIMINAR-----------
Ingrese si requiere eliminar:
1. Peliculas
2. Series
3. Salir
opcion: 
        """)
        if base_mostrar =="1":
            lista_peliculas = base.get("peliculas")
            print(lista_peliculas)
            nombre_pelicula = input("Ingrese el nombre de la pelicula que desea eliminar: ")
            if nombre_pelicula in lista_peliculas:
                base.get("peliculas").remove(nombre_pelicula)
            else:
                print("ese nombre no existe")
        elif base_mostrar == "2":
            lista_series = base.get("series")
            print(lista_series)
            nombre_series = input("Ingrese el nombre de la pelicula a eliminar: ")
            if nombre_series in lista_series:
                base.get("series").remove(nombre_series)
            else:
                print("ese nombre no existe")
        elif base_mostrar == "3":
            break
        else:
            print("Opcion incorrecta")

def lista_desde_un_punto_a_otro():
    while True:
        base_mostrar = input(
        """
-----------Menu MOSTRAR-----------
Ingrese si requiere mostrar:
1. Peliculas
2. Series
3. Salir
opcion: 
        """)
        if base_mostrar =="1":
            while True:
                try:
                    lista_pelicula= base.get("peliculas")
                    inicio= int(input("Ingrese a partir de qué posición quiere ver: "))
                    fin= int(input("Ingrese hasta qué posición quiere ver: "))
                    break        
                except:
                    print("Debe agregar números")
            for i in range(inicio-1,fin):
                print(lista_pelicula[i])
        elif base_mostrar == "2":
            while True:
                try:
                    lista_series= base.get("series")
                    inicio= int(input("Ingrese a partir de qué posición quiere ver: "))
                    fin= int(input("Ingrese hasta qué posición quiere ver: "))
                    break        
                except:
                    print("Debe agregar números")
            for i in range(inicio-1,fin):
                print(lista_series[i])
        elif base_mostrar == "3":
            break
        else:
            print("Opcion incorrecta")

def palabra_requerida(): #Revisar función, no anda bien
    while True:
        base_mostrar = input(
        """
-----------Menu MOSTRAR-----------
Ingrese si requiere buscar:
1. Peliculas
2. Series
3. Salir
opcion: 
        """)
        if base_mostrar =="1":
            lista_pelicula = base.get("peliculas")
            palabra= input("Ingrese la palabra a buscar: ")
            for pelicula in lista_pelicula:
                if palabra in pelicula:
                    print(f"La palabra '{palabra}' esta en {pelicula}")

        elif base_mostrar =="2":
            lista_series = base.get("series")
            palabra= input("Ingrese la palabra a buscar: ")
            for serie in lista_series:
                if palabra in serie:
                    print(f"La palabra '{palabra}' esta en {serie}")

        elif base_mostrar == "3":
            break
        else:
            print("Opcion incorrecta")       

