#El programa debe:
#- pedir en orden el Nombre, apellido, edad y numero de calzado
#- verificar que cada uno sea el tipo de variable correcto (IMPORTANTE)
#- en caso verdadero imprimir de la siguiente manera el resultado:
try:
    nombre= str(input("Ingrese su nombre: "))
    apellido= str(input("Ingrese su apellido: "))
    edad= int(input("Ingrese su edad: "))
    num_calzado= float(input("Ingrese su número de calzado: "))
    print(f"Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nNúmero de Calzado: {num_calzado}")
except:
    print("El valor ingresado es incorrecto")