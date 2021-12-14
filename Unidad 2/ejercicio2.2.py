"""
El programa debe:

Mostrar al usuario un menu
Permitir al usuario ingresar una opcion del menu
imprimir esa opcion
en caso de no escribir ninuna opcion del menu indicar ERROR
Condiciones:

imprimir (string)
1 (int)
2 (int)
salir (string)
Ayuda (como se comparan string y enteros cuidado con castear antes de verificar si el usuario ingreso str o int)
"""
while True:
    try:
        dato_1 = input("""Por favor ingrese una opcion
        - imprimir
        - 1
        - 2
        - salir
        ingreso : """)
        if dato_1.isalpha(): #si el dato es alfabetico
            if dato_1=="imprimir":
                print("ingresaste IMPRIMIR")
            elif dato_1=="salir":
                print("ingresaste SALIR")
                break
            else:
                print("no ingresaste una opcion alfanumerica correcta")
        elif dato_1.isdigit(): #si el dato es numerico
            if int(dato_1)==1:
                print("ingresaste 1")
            elif int(dato_1)==2:
                print("ingresaste 2")
            else:
                print("no ingresaste una opcion numerica correcta")
        else:
            print("no ingresaste numeros o letras muy mal")
    except:
        print("ERROR")