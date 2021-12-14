"""
flag= True
while True:#DESPUES VEMOS COMO SALIR
  try:
    numero_inicial=int(input("Ingrese un numero incial: "))
    numero_limite=int(input("Ingrese un numero limite: "))
  except:
    print("dije un numero")
  if (numero_inicial<numero_limite):
    while numero_inicial<=numero_limite:
      print(numero_inicial)
      numero_inicial+=1
    flag= False
  else:
    print("el numero incial debe ser menor que el limite")
"""

"""
flag = True # mi flag
while flag:
  contraseña = input("ingrese la contraseña: ")
  if contraseña =="1234":
    flag = False
    print("contraseña CORRECTA")
  else:
    print("contraseña incorrecta")
"""

"""
El programa debe:
*  pedir al usuario 5 datos numericos
*  verificar que sean enteros y sino pedir nuevamente los 5
*  cuando se tenga los 5 datos el programa debe devolver el promedio
*  no deben aparecer errores.
"""

i = 1
acum = 0
while i<=5:
    try:
        numero=float(input("ingrese un número"))
        i+=1
        acum+=numero
    except:
        print("no es un número válido")
        i=i
promedio = acum/5
print(f"El promedio de los cinco números ingresados es {promedio}")