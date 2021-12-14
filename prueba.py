
"""
##**Ejercicio 5.5**
Crear una funcion que debe:
*    Tener almacenado el abcedario en una lista
*    Pedir al usuario un numero (2 o 3) - VERIFICAR 
*    Elimina de la lista las letras que ocupen posiciones múltiplos de ese numero
*   Mostrar por pantalla la lista resultante.
*   No deben aparecer y se deben tener en cuenta todos los posibles errores
"""
"""
#código Joel
def abc():
	
	lista= []
	abcde= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',  'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	while True:
		try:
			numero= int(input("Ingrese un numero 2 o 3: "))
			if numero>=2 and numero<=3:
				break
			else:
					print("dato fuera de rango")			
		except:
			print("dato erroneo")
	if numero== 2:		
		for i in range(len(abcde)):
			if i % numero == 0:
				lista.append(i-1)
		lista.pop(0)
		print(lista)
		lista.reverse()
		for i in (lista):
			abcde.pop(i)
			
		print(f"el abecedario sin los multiplos de 2 son:\n{abcde}")
		
	if numero== 3:		
		for i in range(len(abcde)):
			if i % numero == 0:
				lista.append(i+2)
		print(lista)
		lista.reverse()
		for i in (lista):
			abcde.pop(i)
			
		print(f"el abecedario sin los multiplos de 3 son:\n{abcde}")
abc()		
"""
##
##def agregar_fruta_o_verdura(): #agrega al stock frutas o verduras según seleccione el usuario
##    while True:
##        opcion= input("\nIngrese 1 para agregar frutas, 2 para agregar verduras, o fin para salir: ") #pide al usuario que ingrese la opción que desea realizar
##        
##        if opcion == "1":
##            fruta= input("Ingrese la fruta que desea agregar: ")
##            if fruta.isalpha(): #verifica que el usuario ingrese dígitos que se encuentren en el alfabeto
##                if fruta not in lista_frutas: #verifica que no esté en la lista esa fruta para agregarla
##                    lista_frutas.append(fruta)
##                    print(f"Se agregó con éxito '{fruta}' en la lista Frutas")
##                    print(lista_frutas)
##                else:
##                    print("La fruta ingresada ya se encuentra")
##            else:
##                print("Debe ingresar una palabra válida")
##                
##        elif opcion == "2":
##            verdura= input("Ingrese la verdura que desea agregar: ")
##            if verdura.isalpha(): #verifica que el usuario ingrese dígitos que se encuentren en el alfabeto
##                if verdura not in lista_verduras: #verifica que no esté en la lista esa verdura para agregarla
##                    lista_verduras.append(verdura)
##                    print(f"Se agregó con éxito '{verdura}' en la lista Verduras")
##                    print(lista_verduras)
##                else:
##                    print("La verdura ingresada ya se encuentra")
##            else:
##                print("Debe ingresar una palabra válida")
##                
##        elif opcion == "fin": #sale de las opciones
##            break
##        else:
##            print("No ingresó una opción válida.")
##
##
##def stock_frutas_o_verduras(): #consulta el stock de frutas o verduras
##    while True:
##        consulta= input("\nIngrese 1 si desea consultar el stock de Frutas, 2 si desea consultar el stock de Verduras, o fin para salir: ") #pide al usuario que ingrese la opción que desea realizar
##        
##        if consulta == "1": 
##            fruta= input("Ingrese la fruta de la cual quiere consultar stock: ")
##            if fruta.isalpha():
##                if fruta not in lista_frutas: #verifica si la fruta no se encuentra en el stock
##                    print(f"'{fruta}' no se encuentra en el stock")
##                else:
##                    print(f"'{fruta}' si se encuentra en nuestro stock!") #verifica que la fruta se encuentra en el stock
##                    print(lista_frutas) #muestra la lista
##            else:
##                print("Debe ingresar una palabra válida")
##                
##        elif consulta == "2":
##            verdura= input("Ingrese la verdura de la cual quiere consultar stock: ")
##            if verdura.isalpha():
##                if verdura not in lista_verduras: #verifica si la verdura no se encuentra en el stock
##                    print(f"'{verdura}' no se encuentra en el stock")
##                else:
##                    print(f"'{verdura}' si se encuentra en nuestro stock!") #verifica que la verdura se encuentra en el stock
##                    print(lista_verduras) #muestra la lista
##            else:
##                print("Debe ingresar una palabra válida")
##                
##        elif consulta == "fin": #sale de las opciones
##            break
##        else:
##            print("El dato ingresado es incorrecto. Seleccione una de las opciones indicadas.")
##            
##
##def eliminar_fruta_o_verdura():
##    while True:
##        opcion= input("\nIngrese 1 si desea eliminar Frutas, 2 si desea eliminar Verduras, o fin para salir: ")
##        
##        if opcion == "1":
##            fruta_a_eliminar= input("Ingrese la fruta a eliminar: ")
##            if fruta_a_eliminar.isalpha(): #verifica que el usuario ingrese dígitos que se encuentren en el alfabeto
##                if fruta_a_eliminar not in lista_frutas:
##                    print("Este producto no se encuentra en el stock")
##                else:
##                    lista_frutas.remove(fruta_a_eliminar) #elimina la fruta de la lista
##                    print("Su producto ha sido eliminado con éxito!")
##                    print(f"Su stock ahora es: {lista_frutas}") #muestra como quedó su stock
##            else:
##                print("Debe ingresar una palabra válida")
##                
##        elif opcion == "2":
##            verdura_a_eliminar= input("Ingrese la fruta a eliminar: ")
##            if verdura_a_eliminar.isalpha():
##                if verdura_a_eliminar not in lista_verduras:
##                    print("Este producto no se encuentra en el stock")
##                else:
##                    lista_verduras.remove(verdura_a_eliminar) #elimina la verdura de la lista
##                    print("Su producto ha sido eliminado con éxito!")
##                    print(f"Su stock ahora es: {lista_verduras}") #muestra como quedó su stock
##            else:
##                print("Debe ingresar una palabra válida")
##
##        elif opcion == "fin": #sale de las opciones
##            break
##        
##        else:
##            print("Ingrese un valor correcto")
##
##
##
##lista_frutas= []
##lista_verduras= []
##
##while True:
##    
##    condicion=input( #le da a elegir opciones al usuario
##    """\nPor favor indica la acción que deseas realizar:
##        1. Agregar frutas o verduras al correspondiente stock
##        2. Consultar el stock de frutas o verduras
##        3. Eliminar un elemento del stock
##        4. Salir
##Recuerda que para realizar la opción 2 o 3 primero debes agregar stock a \ntu lista. De lo contrario no se encontrará el producto.
##Opcion: """)
##    if condicion=="1":
##        agregar_fruta_o_verdura()
##    elif condicion=="2":
##        stock_frutas_o_verduras()
##    elif condicion=="3":
##        eliminar_fruta_o_verdura()
##    elif condicion=="4":
##        print("Adiós!")
##        break #sale del programa
##    else:
##        print("No ha seleccionado una opción correcta.") #le avisa al usuario si eligió una opción incorrecta
##

"""
El programa debe ser capaz de:
- solicitar 2 argumentos al usuario
- imprimir por pantalla el resultado de la suma de ambos argumentos.
"""

##def suma(a,b):
##  resultado = int(a)+int(b)
##  print (f"la suma de {a} y {b} es igual a: {resultado}")
##
##print("Se sumaran dos argumentos")
##print("Indique el argumento A")
##a = input()
##print("Indique el argumento B")
##b = input()
##suma(a,b)

##abc = "abcdefghijklmnñopqrstuvwxyz"
##lista_abecedario = list(abc)
##for i in range(len(lista_abecedario)):
##    print(lista_abecedario[i+1])


'''
##**Ejercicio 5.9 (Empresa de Taxis)**
El programa debe:
*   Simular una empresa de taxis que cuente con tres Autos con sus respectivos cheferes
```
Taxis=[["auto_1","auto_2","auto_3"],["chofer_1","chofer_2","chofer_3"],[45,50,30]]
```
    *  Cada auto cuenta con un chofer y no hace recorridos mayores a lo q se le indica
*   Contar con 6 funciones disponibles en el menu:
    1. Preguntar al usuario el recorrido del viaje e indicar posibles autos y choferes
    2. Modificar nombre chofer segun el nombre del auto.
        auto_1 -> "federico"
    3. Modificar el recorrido segun el nombre del auto.
        auto_1 -> 60
    4. Agregar nuevo auto a la empresa de Taxis, indicando auto, nombre chofer y recorrido maximo -> ULTIMO
    5. Observar una lista de autos choferes y recorrido maximo con el siguiente formato:
    6. Observar informacion de un chofer, verificando su existencia previamente

```
AUTO    -    CHOFER    -   RECORRIDO
auto_1  -   chofer_1   -   45
auto_2  -   chofer_2   -   50
auto_3  -   chofer_3   -   50
```
    
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
'''
##Taxis=[["auto_1","auto_2","auto_3"],["chofera","choferb","choferc"],[10,30,50]]
##def listar():
##    print("AUTO    -    CHOFER    -   RECORRIDO")
##    for i in range(len(Taxis[0])):
##        print(f"{Taxis[0][i]} - {Taxis[1][i]} - {Taxis[2][i]}")
##
##def modificar_nombre_chofer():
##    listar()
##    while True:
##        indicar_auto = input("Nombre del auto a modificar: ")
##        if indicar_auto in Taxis[0]:
##            Taxis[1][Taxis[0].index(indicar_auto)] = input("Nuevo nombre del chofer: ")
##            listar()
##            break
##        else:
##            print("no existe ese auto")
##
##def nuevo_viaje():
##    while True:
##        try:
##            while True:
##                distancia = float(input("Ingrese la distancia del viaje:"))
##                if(distancia <= 0):
##                    print("La distancia debe ser mayor que cero")
##                else:
##                    print("Posibles autos que podrían realizar el viaje:")
##                    for columnas in range(len(Taxis[2])):
##                        if(distancia <= Taxis[2][columnas]):
##                            print(f"Auto: {Taxis[0][columnas]} - Chofer: {Taxis[1][columnas]}")
##                    return
##        except:
##            print("Debe ingresar una distancia válida")
##
##def informacion_chofer():
##    chofer = input("Por favor ingrese el nombre del chofer: ")
##    if chofer.isalpha():
##        if chofer in Taxis[1]:
##            print (f"El chofer maneja el {Taxis[0][Taxis[1].index(chofer)]} y hace {Taxis[2][Taxis[1].index(chofer)]} kilómetros.")
##        else:
##            print("Este chofer no trabaja en esta empresa")
##
##informacion_chofer()



