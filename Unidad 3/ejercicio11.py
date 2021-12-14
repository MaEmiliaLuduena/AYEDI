try:
    print("""Hola! Elige dos de los siguientes colores para adivinar qué color se forma: 
    .Azul
    .Rojo
    .Verde
    """)

    primer= input("Ingrese el primer color: ")
    if primer.isalpha():
        if primer.lower() == "rojo":
            segundo= input("Ingrese el segundo color: ")
            if segundo.lower() == "azul":
                print("Formaste Morado!")
            else: #Eligió verde
                print("Formaste Amarillo!")
        else: #Eligió azul
            segundo= input("Ingrese el segundo color: ")
            if segundo.lower() == "verde":
                print("Formaste Cyan!")
            else: #Eligió rojo
                print("Formaste Morado!")
    else:
        print("Debes escribir el color")
except:
    print("ERROR")