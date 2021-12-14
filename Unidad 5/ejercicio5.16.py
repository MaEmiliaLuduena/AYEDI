"""
Ejercicio 5.16
Crear una funcion que debe: (usar set)

Pedir al usuario determinados paises y guardarlos en un set
Cuando el usuario escriba "listo", se debe imprimir todos los paises sin repetir, y la cantidad total sin repetir.
"""



def paises():
    paises= set([]) #conjunto vacio
    while True:
        pais = input("Ingrese un pais o 'listo' para terminar: ").capitalize()
        if pais == "Listo":
            break
        paises.add(pais)

    for i in paises:
        print (i)
    print(f"En total se cargaron {len(paises)} diferentes")
    print(type(paises))

paises()