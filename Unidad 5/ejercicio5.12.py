"""
Ejercicio 5.12
Crear una funcion que debe: (usar diccionario)

Preguntar al usuario su nombre, edad, dirección y teléfono y lo guardar en un diccionario.
Mostrar por pantalla el mensaje: "nombre" tiene "edad" años, vive en "direccion" y su número de teléfono es "telefono".
"""

datos_persona= {}

def pedir_datos():
    while True:
        try:
            nombre= input("Por favor ingrese su nombre: ").capitalize()
            if nombre.isalpha():
                datos_persona.update({"Nombre":nombre})
                break
            else:
                print("Debes ingresar un nombre válido")
        except:
            print("Error en el nombre ingresado")

    while True:
        try:    
            edad= int(input("Ingrese su edad: "))
            if edad > 0:
                datos_persona.update({"Edad":edad})
                break
            else:
                print("No puedes ingresar valores negativos") 
        except:
            print("Error en el campo edad")

    direccion= input("Ingrese su dirección: ").capitalize()
    datos_persona.update({"Direccion":direccion})

    while True:
        try:
            telefono= int(input("Ingrese su teléfono: "))
            if telefono > 100000: #Calcula la longitud real de un n° de teléfono
                datos_persona.update({"Telefono":telefono})
                break  
            else:
                print("Debes ingresar un teléfono válido")
        except:
            print("Error")

    print(f"{nombre} tiene {edad} años, vive en {direccion} y su número de teléfono es {telefono}.")                
    """ print(f"Su nuevo diccionario Persona es: ")
    for i, j in datos_persona.items():
        print(f" {i} : {j}") """

pedir_datos()