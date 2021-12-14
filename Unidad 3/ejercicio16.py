"""
El programa debe:
*   mostrar el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” 
que terminará.
*   si el usuario escribe "hola" o "chau" que no se haga el eco
"""

while True:
    palabra= input("Ingrese una palabra: ")
    if palabra == "salir":
        break
    elif palabra == "hola" or palabra == "chau":
        continue
    else:
        print(palabra)


