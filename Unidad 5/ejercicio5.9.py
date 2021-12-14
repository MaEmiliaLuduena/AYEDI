'''
##**Ejercicio 5.9 (Empresa de Taxis)**
El programa debe:
*   Simular una empresa de taxis que cuente con tres Autos con sus respectivos choferes
```
Taxis=[["auto_1","auto_2","auto_3"],["chofer_1","chofer_2","chofer_3"],[45,50,30]]
```
    *  Cada auto cuenta con un chofer y no hace recorridos mayores a lo q se le indica
*   Contar con 6 funciones disponibles en el menu:
    1. Preguntar al usuario el recorrido del viaje e indicar posibles autos y choferes (LISTO)
    2. Modificar nombre chofer segun el nombre del auto. (LISTO)
        auto_1 -> "federico"
    3. Modificar el recorrido segun el nombre del auto. (LISTO)
        auto_1 -> 60
    4. Agregar nuevo auto a la empresa de Taxis, indicando auto, nombre chofer y recorrido maximo -> (LISTO)
    5. Observar una lista de autos choferes y recorrido maximo con el siguiente formato: (LISTO)
    6. Observar informacion de un chofer, verificando su existencia previamente

```
AUTO    -    CHOFER    -   RECORRIDO
auto_1  -   chofer_1   -   45
auto_2  -   chofer_1   -   50
auto_3  -   chofer_3   -   30
```
    
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
'''

Taxis=[["auto_1","auto_2","auto_3"],["chofer_1","chofer_2","chofer_3"],[45,50,30]]

def recorrido_viaje():
    contador = 0
    while True:
        try:
            recorrido= int(input("Ingrese el recorrido (en números) de su viaje: "))
            if recorrido < 0:
                print("No puede ingresar un valor negativo")
            else:
                for i in range(len(Taxis[2])):
                    if i <= recorrido:
                        contador += 1
                        print(f"{contador}° coche y chofer disponible: {Taxis[0][i]} - {Taxis[1][i]} - {Taxis[2][i]}")
                        
                    else:
                        print("No disponemos de coches que realicen ese recorrido")
                break
        except:
            print("Dato erroneo.") 

def modificar_chofer():
    while True:
        nombre_auto= input("Ingresa a qué auto deseas cambiar el nombre del chofer o escribe fin para terminar: ")
        if nombre_auto == "fin":
            break
        elif nombre_auto == "auto_1":
            nombre_chofer= input("Ingresa el nombre que desees: ")
            Taxis[1][0]= nombre_chofer
            print(f"Se modifico con exito. Ahora el nuevo nombre del {nombre_auto} es {Taxis[1][0]}")
        elif nombre_auto == "auto_2":
            nombre_chofer= input("Ingresa el nombre que desees: ")
            Taxis[1][1]= nombre_chofer
            print(f"Se modifico con exito. Ahora el nuevo nombre del {nombre_auto} es {Taxis[1][1]}")
        elif nombre_auto == "auto_3":
            nombre_chofer= input("Ingresa el nombre que desees: ")
            Taxis[1][2]= nombre_chofer
            print(f"Se modifico con exito. Ahora el nuevo nombre del {nombre_auto} es {Taxis[1][2]}")
        else:
            print("No contamos con ese auto")

def modificar_recorrido():
    while True:
        try:
            nombre_auto= input("Ingresa a qué auto deseas cambiar el recorrido o escribe fin para terminar: ")
            if nombre_auto == "fin":
                break
            elif nombre_auto == "auto_1":
                while True:
                    try:
                        recorrido= int(input("Ingresa el recorrido nuevo: "))
                        if recorrido <= 0:
                            print("No puede ingresar valores negativos o nulos")
                        else:
                            Taxis[2][0]= recorrido
                            print(f"Se modifico con exito. Ahora el nuevo recorrido del {nombre_auto} es {Taxis[2][0]}")
                            break
                    except:
                        print("Dato Incorrecto")
            elif nombre_auto == "auto_2":
                while True:
                    try:
                        recorrido= int(input("Ingresa el recorrido nuevo: "))
                        if recorrido <= 0:
                            print("No puede ingresar valores negativos o nulos")
                        else:
                            Taxis[2][1]= recorrido
                            print(f"Se modifico con exito. Ahora el nuevo recorrido del {nombre_auto} es {Taxis[2][1]}")
                            break
                    except:
                        print("Dato Incorrecto")
            elif nombre_auto == "auto_3":
                while True:
                    try:
                        recorrido= int(input("Ingresa el recorrido nuevo: "))
                        if recorrido <= 0:
                            print("No puede ingresar valores negativos o nulos")
                        else:
                            Taxis[2][2]= recorrido
                            print(f"Se modifico con exito. Ahora el nuevo recorrido del {nombre_auto} es {Taxis[2][2]}")
                            break
                    except:
                        print("Dato Incorrecto")
            else:
                print("No contamos con ese auto")
        except:
            print("Dato invalido")

def agregar_auto():
    while True:
        try:
            while True:
                nombre_auto= input("Ingrese el nombre del Auto que desea agregar o escriba fin para terminar: ")
                if nombre_auto == "fin":
                    break
                elif nombre_auto == "auto_1" or nombre_auto == "auto_2" or nombre_auto == "auto_3":
                    print("Ese nombre ya existe.")
                else:
                    Taxis[0].append(nombre_auto)
                    break

            while True:
                nombre_chofer= input("Ingrese el nombre del Chofer: ")
                if nombre_chofer == "chofer_1" or nombre_chofer == "chofer_2" or nombre_chofer == "chofer_3":
                    print("Ese nombre ya existe.")
                else:
                    Taxis[1].append(nombre_chofer)
                    break

            recorrido_maximo= float(input("Ingrese el Recorrido maximo: "))
            if recorrido_maximo <= 0:
                print("No puede ingresar valores negativos o nulos")
            else:
                Taxis[2].append(recorrido_maximo)
                break
        except:
            print("Error")

    print(f"Se ha agregado {nombre_auto} con su chofer {nombre_chofer}, y el reccorrido {recorrido_maximo} a la lista Taxis")
    print(f"Su lista de ahora ahora es: {Taxis}")

def imprimir_matriz(Taxis):
    print("--------------------------------")
    print(f"| Auto  |  Chofer  | Recorrido |")
    print("--------------------------------")
    for i in range(len(Taxis[0])):
        print(f"{Taxis[0][i]} - {Taxis[1][i]} - {Taxis[2][i]}")

def info_chofer():
    while True:
        chofer= input("Ingrese el chofer del cual quiere saber información o escriba fin para terminar: ")
        if chofer in Taxis[1]:
            """ print("--------------------------------")
            print(f"| Auto  |  Chofer  | Recorrido |")
            print("--------------------------------")
            for i in range(len(Taxis)):
                print(f"{Taxis[0][i]} - {Taxis[1][i]} - {Taxis[2][i]}") """
            print (f"El chofer maneja el {Taxis[0][Taxis[1].index(chofer)]} y hace {Taxis[2][Taxis[1].index(chofer)]} kilómetros.")
        elif chofer == "fin":
            break
        else:
            print("No encontramos el chofer indicado")
    

while True:
    condicion=input( #le da a elegir opciones al usuario
    """\nPor favor indica la acción que deseas realizar:
        1.  Recorrido del viaje e indicar posibles autos y choferes
        2.  Modificar nombre chofer segun el nombre del auto
        3.  Modificar el recorrido segun el nombre del auto
        4.  Agregar nuevo auto a la empresa de Taxis
        5.  Observar una lista de autos choferes y recorrido maximo
        6.  Observar informacion de un chofer
        7.  Salir
    Opcion: """)

    if condicion=="1":
        recorrido_viaje()
    elif condicion=="2":
        modificar_chofer()
    elif condicion=="3":
        modificar_recorrido()
    elif condicion=="4":
        agregar_auto()
    elif condicion == "5":
        imprimir_matriz(Taxis)
    elif condicion == "6":
        info_chofer()
    elif condicion == "7":
        print("Adiós!")
        break #sale del programa
    else:
        print("No ha seleccionado una opción correcta.") #le avisa al usuario si eligió una opción incorrecta
