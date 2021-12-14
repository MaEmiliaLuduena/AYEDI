"""
El programa debe :
*   Almacenar una variable `contraseña` con una contraseña
*   Preguntar al usuario por la contraseña e imprimir por pantalla si la contraseña introducida por el usuario coincide o no con la variable
 **IMPORTANTE**: sin tener en cuenta mayúsculas y minúsculas.(metodos string)
*   no debe generar errores
"""
try:
    contraseña= "bienvenida"
    contra_usuario= input("Ingrese su contraseña: ")
    if contraseña == contra_usuario.lower():
        print("Su contraseña coincide con la variable")
    else:
        print("Su contraseña no coincide con la variable")
except:
    print("Ingresaste un valor erróneo")