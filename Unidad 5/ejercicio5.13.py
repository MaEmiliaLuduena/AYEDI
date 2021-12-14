"""##**Ejercicio 5.13**
Crear una funcion que debe: (usar diccionario)
*   Guardar en un diccionario los precios de las frutas de la tabla.
*   Preguntar al usuario por una fruta, un número de kilos y mostrar por pantalla el precio de ese número de kilos de fruta. 
*   Si la fruta no está en el diccionario debe mostrar un mensaje informando ERROR."""

frutas= {
    "banana": 50,
    "manzana": 80,
    "pera": 100,
    "naranja": 30
    }

def precios_frutas():
    while True:
        try:
            fruta= input("Ingrese la fruta que desea consultar o 'fin' para salir : ")
            if fruta.isalpha():
                if fruta == "fin":
                    print("Adiós")
                    break
                elif fruta in frutas:
                    while True:
                        try:
                            kilos= float(input("Ingrese los kilos: "))
                            valor= frutas.get(fruta, "Error. No tenemos esa fruta")
                            precio_final= valor * kilos
                            print(f"El precio de {fruta} por {kilos} kilos es {precio_final} pesos")
                            break
                        except:
                            print("Error")
                else:
                    print("Error. No tenemos esa fruta")
            else:
                print("No puedes ingresar números ni símbolos")
            
        except:
            print("Error")

""" def precios_frutas():
    while True:
        fruta= input("Ingrese la fruta nueva: ")
        if fruta in frutas:
            valor = frutas.get(fruta,"No existe esa fruta en la lista")
            while True:
                try:
                    kilos= float("Ingrese los kilos de esa fruta: ")
                    precio= valor * kilos
                    print(f"El precio en esa cantidad de kilos de {fruta} es {precio}")
                    break
                except:
                    print("Error")
                break """
        
precios_frutas()
