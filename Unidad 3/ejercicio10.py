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
condicion = input("""Por favor ingrese una opcion
- imprimir
- 1
- 2
- salir
ingreso : """)
if condicion.isalpha():
    if condicion == "imprimir":
        print("Eligió imprimir")
    elif condicion == "salir":
        print("Eligió salir")
    else:
        print("No ingresaste una ocpión alfanumérica correcta")
elif condicion.isdigit():
    if int(condicion) == 1:
        print("Eligió 1")
    elif int(condicion) == 2:
        print("Eligió 2")
    else:
        print("No ingresaste una opción mencionada")
else:
    print("ERROR")