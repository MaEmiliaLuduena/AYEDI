"""
Crear una funcion que debe: (usar diccionario)

Preguntar al usuario su nombre, edad, dirección y teléfono y lo guardar en un diccionario.
Mostrar por pantalla el mensaje: "nombre" tiene "edad" años, vive en "direccion" y su número de teléfono es "telefono".
"""

datos_persona= {}

def pedir_datos():
    while True:
        try:
            nombre = input("Ingrese su nombre: ").capitalize
            if nombre.isalpha():
                datos_persona.update({"Nombre":nombre})
                break
            else:
                print("No puedes ingresar números")
        except:
            print("Error en el campo nombre")

    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad.isalpha():
                print("Debes ingresar números")
                
            else:
                datos_persona.update({"Edad" : edad})
                break
        except:
            print("Error en el campo edad")


    direccion = input("Ingrese su dirección: ").capitalize
    datos_persona.update({"Direccion" : direccion})

    while True:
        try:
            telefono = int(input("Ingrese su teléfono: "))
            if telefono.isalpha():
                print("Debes ingresar números") 
            else:
                datos_persona.update({"Telefono" : telefono})
                break        
        except:
            print("Error en el campo teléfono")
        
        nombre_1= "Nombre"
        edad_1 = "Edad"
        direccion_1 = "Direccion"
        telefono_1 = "Telefono"

    print(f"{nombre_1} tiene {edad_1}, vive en {direccion_1} y su número de teléfono es {telefono_1}")
pedir_datos()