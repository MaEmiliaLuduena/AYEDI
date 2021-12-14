"""##**Ejercicio 5.6 (Programa de Inventario de verduleria)**
Crear un prgrama que debe:
*    Contar con un stock de frutas y otro de verduras (El stock indica si venden o no esa fruta o verdura, no la cantidad) - dos listas que inician vacias
*    Contar con un menu y 3 funciones

      1. Agregar frutas o verduras al correspondiente stock (verificando que sean nuevas)
      2. Consultar el stock de frutas o verduras
      3. Eliminar un elemento del stock"""


def agregar_fruta_o_verdura(): #agrega al stock frutas o verduras según seleccione el usuario
    while True:
        opcion= input("\nIngrese 1 para agregar frutas, 2 para agregar verduras, o fin para salir: ") #pide al usuario que ingrese la opción que desea realizar
        
        if opcion == "1":
            fruta= input("Ingrese la fruta que desea agregar: ")
            if fruta.isalpha(): #verifica que el usuario ingrese dígitos que se encuentren en el alfabeto
                if fruta not in lista_frutas: #verifica que no esté en la lista esa fruta para agregarla
                    lista_frutas.append(fruta)
                    print(f"Se agregó con éxito '{fruta}' en la lista Frutas")
                    print(lista_frutas)
                else:
                    print("La fruta ingresada ya se encuentra")
            else:
                print("Debe ingresar una palabra válida")
                
        elif opcion == "2":
            verdura= input("Ingrese la verdura que desea agregar: ")
            if verdura.isalpha(): #verifica que el usuario ingrese dígitos que se encuentren en el alfabeto
                if verdura not in lista_verduras: #verifica que no esté en la lista esa verdura para agregarla
                    lista_verduras.append(verdura)
                    print(f"Se agregó con éxito '{verdura}' en la lista Verduras")
                    print(lista_verduras)
                else:
                    print("La verdura ingresada ya se encuentra")
            else:
                print("Debe ingresar una palabra válida")
                
        elif opcion == "fin": #sale de las opciones
            break
        else:
            print("No ingresó una opción válida.")


def stock_frutas_o_verduras(): #consulta el stock de frutas o verduras
    while True:
        consulta= input("\nIngrese 1 si desea consultar el stock de Frutas, 2 si desea consultar el stock de Verduras, o fin para salir: ") #pide al usuario que ingrese la opción que desea realizar
        
        if consulta == "1": 
            fruta= input("Ingrese la fruta de la cual quiere consultar stock: ")
            if fruta.isalpha():
                if fruta not in lista_frutas: #verifica si la fruta no se encuentra en el stock
                    print(f"'{fruta}' no se encuentra en el stock")
                else:
                    print(f"'{fruta}' si se encuentra en nuestro stock!") #verifica que la fruta se encuentra en el stock
                    print(lista_frutas) #muestra la lista
            else:
                print("Debe ingresar una palabra válida")
                
        elif consulta == "2":
            verdura= input("Ingrese la verdura de la cual quiere consultar stock: ")
            if verdura.isalpha():
                if verdura not in lista_verduras: #verifica si la verdura no se encuentra en el stock
                    print(f"'{verdura}' no se encuentra en el stock")
                else:
                    print(f"'{verdura}' si se encuentra en nuestro stock!") #verifica que la verdura se encuentra en el stock
                    print(lista_verduras) #muestra la lista
            else:
                print("Debe ingresar una palabra válida")
                
        elif consulta == "fin": #sale de las opciones
            break
        else:
            print("El dato ingresado es incorrecto. Seleccione una de las opciones indicadas.")
            

def eliminar_fruta_o_verdura():
    while True:
        opcion= input("\nIngrese 1 si desea eliminar Frutas, 2 si desea eliminar Verduras, o fin para salir: ")
        
        if opcion == "1":
            fruta_a_eliminar= input("Ingrese la fruta a eliminar: ")
            if fruta_a_eliminar.isalpha(): #verifica que el usuario ingrese dígitos que se encuentren en el alfabeto
                if fruta_a_eliminar not in lista_frutas:
                    print("Este producto no se encuentra en el stock")
                else:
                    lista_frutas.remove(fruta_a_eliminar) #elimina la fruta de la lista
                    print("Su producto ha sido eliminado con éxito!")
                    print(f"Su stock ahora es: {lista_frutas}") #muestra como quedó su stock
            else:
                print("Debe ingresar una palabra válida")
                
        elif opcion == "2":
            verdura_a_eliminar= input("Ingrese la fruta a eliminar: ")
            if verdura_a_eliminar.isalpha():
                if verdura_a_eliminar not in lista_verduras:
                    print("Este producto no se encuentra en el stock")
                else:
                    lista_verduras.remove(verdura_a_eliminar) #elimina la verdura de la lista
                    print("Su producto ha sido eliminado con éxito!")
                    print(f"Su stock ahora es: {lista_verduras}") #muestra como quedó su stock
            else:
                print("Debe ingresar una palabra válida")

        elif opcion == "fin": #sale de las opciones
            break
        
        else:
            print("Ingrese un valor correcto")



lista_frutas= []
lista_verduras= []

while True:
    
    condicion=input( #le da a elegir opciones al usuario
    """\nPor favor indica la acción que deseas realizar:
        1. Agregar frutas o verduras al correspondiente stock
        2. Consultar el stock de frutas o verduras
        3. Eliminar un elemento del stock
        4. Salir
Recuerda que para realizar la opción 2 o 3 primero debes agregar stock a \ntu lista. De lo contrario no se encontrará el producto.
Opcion: """)
    if condicion=="1":
        agregar_fruta_o_verdura()
    elif condicion=="2":
        stock_frutas_o_verduras()
    elif condicion=="3":
        eliminar_fruta_o_verdura()
    elif condicion=="4":
        print("Adiós!")
        break #sale del programa
    else:
        print("No ha seleccionado una opción correcta.") #le avisa al usuario si eligió una opción incorrecta