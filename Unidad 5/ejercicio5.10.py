"""
##**Ejercicio 5.10 (Conversión de alfabeto)**
El programa debe:
*   Simular la conversion de un alfabeto a otro: Por ejemplo el moorse 
    (NO ES ESTRICTAMENTE NECESARIO USAR ESTE ALFABETO, PUEDE SER INVENTADO)

```
 alfabeto_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 alfabeto_b = ['.-' ,'-...' , '-.-.' ,'-..' ,'.', '..-.','--.', '....','..' ,'.---' , '-.-', '.-..','--' ,'-.' ,'---' ,'.--.','--.-' , '.-.' ,'...' ,'-','..-' ,'...-','.--','-..-' , '-.--' , '--..' ]
```

*   Contar con 6 funciones disponibles en el menu:
    1. Mostrar el alfabeto A (LISTO)
    2. Mostrar el alfabeto B (LISTO)
    3. Modificar una letra del Alfabeto A y el alfabeto B (debe ser la misma) (LISTO)
    4. Conversion de alfabeto A a alfabeto B: ejemplo **abc --> .--...-.-.**
    5. Conversion de alfabeto B a alfabeto A: ejemplo **.--...-.-. --> abc**
    6. Verificacion de existencia de una letra del alfabeto (debe seleccionar A o B) (LISTO)

*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
    """

alfabeto_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alfabeto_b = ['.-' ,'-...' , '-.-.' ,'-..' ,'.', '..-.','--.', '....','..' ,'.---' , '-.-', '.-..','--' ,'-.' ,'---' ,'.--.','--.-' , '.-.' ,'...' ,'-','..-' ,'...-','.--','-..-' , '-.--' , '--..' ]

def muestra_alfabeto_a():
    return alfabeto_a

def muestra_alfabeto_b():
    return alfabeto_b

def modificar_letra_alfabetos():
    while True:
        letra_a= input("Indique la letra del alfabeto_a que desea modificar: ")
        if letra_a in alfabeto_a:
            indice= alfabeto_a.index(letra_a)
            alfabeto_a[indice]= input("Ingrese la letra nueva: ") 
            alfabeto_b[indice]= input("Indique la letra del alfabeto_b que modificará en la misma posición: ")
            print(f"Los alfabetos ahora quedaron de esta manera:\ alfabeto_a= {alfabeto_a}\n alfabeto_b= {alfabeto_b} ")
            break

        elif letra_a in alfabeto_b:
            indice= alfabeto_b.index(letra_a)
            alfabeto_b[indice] = input("Ingrese la nueva letra: ")
            alfabeto_a[indice]= input("Indique la letra del alfabeto_a que modificará en la misma posición: ")
            print(f"Los alfabetos ahora quedaron de esta manera:\ alfabeto_a= {alfabeto_a}\n alfabeto_b= {alfabeto_b} ")
            break
        else:
            print("No se encuentra esa letra en el alfabeto")

def conversion_alfabetoA_a_alfabetoB():
    palabra = input("introduzca su palabra del alfabeto tipo A que desea convertir en el alfabeto tipo B: ")
    lista_palabra = list(palabra)
    for i in lista_palabra:
        if i in alfabeto_a:
            indice = alfabeto_a.index(i)
            print(alfabeto_b[indice],end="")
        else:
            print(f"\nCuidado, la letra {i} no pertece al alfabeto A") #Por si ingresa un valor que no pertenece a la lista
    return

    """ while True:
        palabra_letra= input("Ingrese la palabra o letra a convertir: ")
        if palabra_letra in alfabeto_a:
            indice= alfabeto_a.index(palabra_letra)
            print(f"{palabra_letra} en el alfabeto_b significa: {alfabeto_b[indice]}")
            break
        else:
            print(f"El abecedario no cuenta con {palabra_letra}")
            break """


def conversion_alfabetoB_a_alfabetoA():
    while True:
        palabra_letra= input("Ingrese la palabra o letra a convertir: ")
        if palabra_letra in alfabeto_b:
            indice= alfabeto_b.index(palabra_letra)
            print(f"{palabra_letra} en el alfabeto_b significa: {alfabeto_a[indice]}")
            break
        else:
            print(f"El abecedario no cuenta con {palabra_letra}")
            break
        """
        simbolos = input("Ingrese las letras del alfabeto B a convertir al alfabeto A: ")
        lista_simbolos = simbolos.split()
        for i in lista_simbolos:
            if i in alfabeto_b:
                indice = alfabeto_b.index(i)
                print(alfabeto_a[indice],end="")
            else:
                print(f"\nCuidado, la letra {i} no pertece al alfabeto B") #Por si ingresa un valor que no pertenece a la lista
        return
        """

def verificacion_letra():
    while True:
        alfabeto= input("""Ingrese 1 para verificar existencia de letra en alfabeto_a, 
                            2 para verificar existencia de letra en alfabeto_b, 
                            o 3 para salir: """)
        if alfabeto == "1":
            letra= input("Ingrese la letra a verificar: ")
            if letra in alfabeto_a:
                print(f"{letra} se encuentra en el alfabeto_a")
            else:
                print(f"{letra} No se encuentra en el alfabeto_a")
        elif alfabeto == "2":
            letra= input("Ingrese la letra a verificar: ")
            if letra in alfabeto_b:
                print(f"{letra} se encuentra en el alfabeto_b")
            else:
                print(f"{letra} No se encuentra en el alfabeto_b")
        elif alfabeto == "3":
            break
        else:
            print("Dato erroneo")
    

while True:
    condicion=input( #le da a elegir opciones al usuario
    """\nPor favor indica la acción que deseas realizar:
        1.  Mostrar el alfabeto A
        2.  Mostrar el alfabeto B
        3.  Modificar una letra del Alfabeto A y el alfabeto B
        4.  Conversion de alfabeto A a alfabeto B
        5.  Conversion de alfabeto B a alfabeto A
        6.  Verificacion de existencia de una letra del alfabeto
        7.  Salir
    Opcion: """)

    if condicion=="1":
            print(f"El alfabeto_a es: {muestra_alfabeto_a()}")
    elif condicion=="2":
        print(f"El alfabeto_b es: {muestra_alfabeto_b()}")
    elif condicion=="3":
        modificar_letra_alfabetos()
    elif condicion=="4":
        conversion_alfabetoA_a_alfabetoB()
    elif condicion == "5":
        conversion_alfabetoB_a_alfabetoA()
    elif condicion == "6":
        verificacion_letra()
    elif condicion == "7":
        print("Adiós!")
        break #sale del programa
    else:
        print("No ha seleccionado una opción correcta.") #le avisa al usuario si eligió una opción incorrecta
