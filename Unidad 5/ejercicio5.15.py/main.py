"""
##**Ejercicio 5.15 (Base de peliculas)**
El programa debe:
*   Simular una base de datos de peliculas y series con la capacidad de agregar, buscar, eliminar y filtrar peliculas y series.
*   Debe comenzar con las siguientes peliculas y series en un diccionario:

```
base = {
    "peliculas" : ["El hombre araña", "Los vengadores" , "Los vengadores 2"],
    "series" : ["prision break", "la casa de papel" , "los simpsons"]
        }
```

*   Contar con 5 funciones disponibles en el menu:
    1. Mostrar por pantalla en formato vertical la lista de peliculas o series disponibles.
    2. Agregar nuevas peliculas o series (que no esten) en la base.
    3. Eliminar peliculas o series de la base.
    4. Mostrar segun requiera el usuario la lista de peliculas desde un punto a otro (ej el usuario quiere 
    ver de la 2° a la 4° una lista ).
    lista = [1,2,3,4]
    print(lista[])
    5. Buscar peliculas o series que contengan una palabra requerida por el usuario. (ej. input("el"), 
        se liste las peliculas que contengan la palabra "el").
"""
import funciones as fn
while True:
    opcion=input(
    """
-----------Menu principal-----------
Por favor ingrese una opcion:
    1. Mostrar bases
    2. Agregar series o peliculas
    3. Elimnar series o peliculas
    4. Mostrar de a a b
    5. Mostrar palabra requerida por el usuario
    Opcion: """
    )
    if (opcion=="1"):
        fn.mostrar_bases() 
    elif (opcion=="2"):
        fn.agregar_peliculas_series()
    elif (opcion=="3"):
        fn.eliminar_peliculas_series()
    elif (opcion=="4"):
        fn.lista_desde_un_punto_a_otro()
    elif (opcion=="5"):
        fn.palabra_requerida()
    elif (opcion=="6"):
        break
    else:
        print("Ninguna opción es correcta")
