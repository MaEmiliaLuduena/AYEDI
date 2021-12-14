###**Ejercicio (Ahora con flag)**
"""El programa debe:
*  pedir un dato al usuario
*  solo en caso que este escriba la palabra clave "python" imprimir por pantalla "Correcto", en caso contrario debe seguir pidiendo el dato
*  no deben aparecer errores."""

flag = True
while flag:
    dato= input("Ingrese el dato clave: ")
    if dato == "Python":
        print("Correcto!")
        flag= False
    else:
        print("Dato clave incorrecto")