"""
El programa debe:

- pedir el ingreso de un número positivos al usuario y almacenar la respuesta en la variable numero.
- Verificar que se trate de un numero entero y sino mostrar un error
- Comprobar si el número es negativo. Si lo es, el programa debe avisa que no era eso lo que se había pedido. (si no hay error)
- Finalmente imprimir siempre el valor introducido por el usuario.(si no hay error)
"""
try:    
    numero= int(input("Ingrese un número positivo: "))
    if numero < 0:
        print("Se pidio un número positivo. Ingresaste un número negativo.")
    print(f"El número que ingresaste fue: {numero}")
except:
    print("No ingresó un número entero")
