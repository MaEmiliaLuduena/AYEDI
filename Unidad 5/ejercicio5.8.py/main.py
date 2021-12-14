'''
##**Ejercicio 5.8 (Programa de ventas)**
El programa debe:
*   Simular un programa que venda 3 productos
Codigo      Nombre     Precio Stock
    1     & producto1  & 300   & 5
    2     & producto2  & 400   & 4
    3     & producto3  & 500   & 7

*   El menu debe mostrar los productos a comprar. ->LISTO
*   Luego se debe contar con un menu de si se pagara en efectivo o tarjeta credito o debito -> LISTO
*   Contar con 7 funciones disponibles en el menu:
  1.  Ver menu de productos (Formato: codigo - producto) ->LISTO
  2.  Pagar con tarjeta credito (Se debe cobrar 10% mas y se debe descontar el stock) -> LISTO
  3.  Pagar con tarjeta debito (se debe descontar el stock) -> LISTO
  4.  Pagar con efectivo (Se debe cobrar 10% menos y se debe descontar el stock) -> LISTO
  5.  Consultar productos y stock -> LISTO
  6.  Agregar stock a los productos -> LISTO
  7.  Cambiar el precio a los productos -> LISTO
  
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
'''
import funciones_imprimir as fi

base_productos = [[1,2,3],["producto1","producto2","producto3"],[300,400,500],[5,4,7]]

def imprimir_matriz(base_productos):    
  print(f"C - Producto - Pr - Stock")
  for i in range(len(base_productos)-1):
    print(f"{base_productos[0][i]} - {base_productos[1][i]} - {base_productos[2][i]} - {base_productos[3][i]}")

def forma_pago():
  while True:
    forma_pago = input("""Por favor ingrese su forma de pago:
      1. Credito
      2. Debito
      3. Efectivo
      Opcion: """)
    if forma_pago =="1":
      return pago_con_credito()
    elif forma_pago =="2":
      return pago_con_debito()
    elif forma_pago =="3":
      return pago_con_efectivo()
    else:
      print("Opcion incorrecta")

def pago_con_credito():
  #fi.imprimir_codigo_producto(base_productos)
  print(f"--------------PAGO CON CREDITO--------------")
  while True:
    print(f"¿Qué producto desea vender?: ")
    for i in range(len(base_productos[1])):
      print(f"{base_productos[0][i]}  {base_productos[1][i]}")
    producto=input("--> ")
    if producto =="1":
      if(base_productos[3][0]>0):
        base_productos[3][0] = base_productos[3][0]-1 #resto stock
        print(f"El comprador debe pagar: {base_productos[2][0]*1.1}")
        return
      else:
        print("no hay stock")
    elif producto =="2":
      if(base_productos[3][1]>0):
        base_productos[3][1] = base_productos[3][1]-1 #resto stock
        print(f"El comprador debe pagar: {base_productos[2][1]*1.1}")
        return
      else:
        print("no hay stock")
    elif producto =="3":
      if(base_productos[3][2]>0):
        base_productos[3][2] = base_productos[3][2]-1 #resto stock
        print(f"El comprador debe pagar: {base_productos[2][2]*1.1}")
        return
      else:
        print("no hay stock")
    else:
      print("Opcion incorrecta")

def pago_con_debito():
  print(f"--------------PAGO CON DÉBITO--------------")
  while True:
    print(f"¿Qué producto desea vender?: ")
    for i in range(len(base_productos[1])):
      print(f"{base_productos[0][i]}  {base_productos[1][i]}")
    producto=input("--> ")
    if producto =="1":
      if(base_productos[3][0]>0):
        base_productos[3][0] = base_productos[3][0]-1 #resto stock
        print(f"El comprador debe pagar: {base_productos[2][0]}")
        return
      else:
        print("no hay stock")
    elif producto =="2":
      if(base_productos[3][1]>0):
        base_productos[3][1] = base_productos[3][1]-1 #resto stock
        print(f"El comprador debe pagar: {base_productos[2][1]}")
        return
      else:
        print("no hay stock")
    elif producto =="3":
      if(base_productos[3][2]>0):
        base_productos[3][2] = base_productos[3][2]-1 #resto stock
        print(f"El comprador debe pagar: {base_productos[2][2]}")
        return
      else:
        print("no hay stock")
    else:
      print("Opcion incorrecta")

def pago_con_efectivo():
  print(f"--------------PAGO CON EFECTIVO--------------")
  while True:
    print(f"¿Qué producto desea vender?: ")
    for i in range(len(base_productos[1])):
      print(f"{base_productos[0][i]}  {base_productos[1][i]}")
    producto=input("--> ")
    if producto =="1":
      if(base_productos[3][0]>0):
        base_productos[3][0] = base_productos[3][0]-1 #resto stock
        base_productos[2][0] -= base_productos[2][0]*0.1
        print(f"El comprador debe pagar: {base_productos[2][0]}")
        return
      else:
        print("no hay stock")
    elif producto =="2":
      if(base_productos[3][1]>0):
        base_productos[3][1] = base_productos[3][1]-1 #resto stock
        base_productos[2][1] -= base_productos[2][1]*0.1
        print(f"El comprador debe pagar: {base_productos[2][1]}")
        return
      else:
        print("no hay stock")
    elif producto =="3":
      if(base_productos[3][2]>0):
        base_productos[3][2] = base_productos[3][2]-1 #resto stock
        base_productos[2][2] -= base_productos[2][2]*0.1
        print(f"El comprador debe pagar: {base_productos[2][2]}")
        return
      else:
        print("no hay stock")
    else:
      print("Opcion incorrecta")

def consultar_productos_y_stock():
  while True:
    producto= input("Ingrese el producto a consultar o escriba fin para terminar la consulta: ")
    if producto == "fin":
      break

    elif producto == "producto1":
      stock= base_productos[3][0]
      print(f"El stock de este producto es: {stock}")
      
    elif producto == "producto2":
      stock= base_productos[3][1]
      print(f"El stock de este producto es: {stock}")

    elif producto == "producto3":
      stock= base_productos[3][2]
      print(f"El stock de este producto es: {stock}")

    else:
      print("No contamos con el producto indicado")

def agregar_stock():
  while True:
    try:
      producto_stock= input("Indique el producto al que desea agregar stock o escriba fin para terminar: ")

      if producto_stock == "fin":
        break

      elif producto_stock == "producto1":
        stock_nuevo= int(input("Ingrese el stock nuevo: "))
        if stock_nuevo < 0:
          print("No puede ingresar valores negativos")
        else:
          base_productos[3][0]= stock_nuevo
          print(f"Se modifico con exito. Ahora su stock del {producto_stock} es {base_productos[3][0]}")
      
      elif producto_stock == "producto2":
        stock_nuevo= int(input("Ingrese el stock nuevo: "))
        if stock_nuevo < 0:
          print("No puede ingresar valores negativos")
        else:
          base_productos[3][1]= stock_nuevo
          print(f"Se modifico con exito. Ahora su stock del {producto_stock} es {base_productos[3][1]}")
      
      elif producto_stock == "producto3":
        stock_nuevo= int(input("Ingrese el stock nuevo: "))
        if stock_nuevo < 0:
          print("No puede ingresar valores negativos")
        else:
          base_productos[3][2]= stock_nuevo
          print(f"Se modifico con exito. Ahora su stock del {producto_stock} es {base_productos[3][2]}")

      else:
        print("Lo sentimos. No contamos con ese producto actualmente")
    except:
      print("Dato erroneo")

def cambiar_precio():
  while True:
    try:
      producto= input("Ingrese el producto al que le quiere cambiar el precio o escriba fin para terminar: ")
      if producto == "fin":
        break
      elif producto == "producto1":
        while True:
          precio_nuevo= float(input("Ingrese el precio nuevo: "))
          if precio_nuevo < 0:
            print("No puede ingresar valores negativos")
          else:
            base_productos[2][0]= precio_nuevo
            print(f"Se modifico con exito. Ahora el nuevo precio del {producto} es {base_productos[2][0]}")
            break
          
      elif producto == "producto2":
        while True:
          precio_nuevo= float(input("Ingrese el precio nuevo: "))
          if precio_nuevo < 0:
            print("No puede ingresar valores negativos")
          else:
            base_productos[2][1]= precio_nuevo
            print(f"Se modifico con exito. Ahora el nuevo precio del {producto} es {base_productos[2][1]}")
            break

      elif producto == "producto3":
        while True:
          precio_nuevo= float(input("Ingrese el precio nuevo: "))
          if precio_nuevo < 0:
            print("No puede ingresar valores negativos")
          else:
            base_productos[2][2]= precio_nuevo
            print(f"Se modifico con exito. Ahora el nuevo precio del {producto} es {base_productos[2][2]}")
            break
      else:
        print("Lo sentimos. No contamos con ese producto actualmente")

    except:
      print("Dato erroneo")

while True:
  condicion=input( #le da a elegir opciones al usuario
    """\nPor favor indica la acción que deseas realizar:
        1.  Ver menu de productos (Formato: codigo - producto)
        2.  Indicar forma de pago: Pagar con tarjeta credito, Pagar con tarjeta debito, Pagar con efectivo 
        3.  Consultar productos y stock 
        4.  Agregar stock a los productos 
        5.  Cambiar el precio a los productos
        6.  Salir
Opcion: """)

  if condicion=="1":
      imprimir_matriz(base_productos)
  elif condicion=="2":
      forma_pago()
  elif condicion=="3":
      consultar_productos_y_stock()
  elif condicion=="4":
    agregar_stock()
  elif condicion == "5":
    cambiar_precio()
  elif condicion == "6":
    print("Adiós!")
    break #sale del programa
  else:
      print("No ha seleccionado una opción correcta.") #le avisa al usuario si eligió una opción incorrecta



fi.imprimir_matriz(base_productos)
#fi.imprimir_matriz2(base_productos)
#fi.imprimir_codigo_producto(base_productos)
#forma_pago()

