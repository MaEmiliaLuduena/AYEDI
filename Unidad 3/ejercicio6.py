""""
El programa debe:

pedir al usuario que ingrese la cant de dinero que dispone.
verificar que la cantidad ingresada sea un numero y sino mostrar error
verificar la cantidad de ingresada e indicar que auto o autos puede comprar
Ford = 10000
Renault = 11000
Chevrolet = 15000
"""

ford = 10000
renault = 11000
chevrolet = 15000
try:
    dinero_cliente= int(input("Ingrese la cantidad de dinero que dispone: "))
    if dinero_cliente >= chevrolet:
        print("Te puedes comprar un Chevrolet!")
    elif dinero_cliente >= renault:
        print("Te puedes comprar un renault!")
    elif dinero_cliente >= ford:
        print("Te puedes comprar un ford!")
    else:
        print("No tienes suficiente dinero!")

except:
    print("No ingresó un valor numérico")