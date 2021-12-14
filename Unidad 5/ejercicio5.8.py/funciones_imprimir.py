base_productos = [[1,2,3],["producto1","producto2","producto3"],[300,400,500],[5,4,7]]


def imprimir_matriz(base_productos):
      
  print(f"C - Producto - Pr - Stock")
  for i in range(len(base_productos)-1):
    print(f"{base_productos[0][i]} - {base_productos[1][i]} - {base_productos[2][i]} - {base_productos[3][i]}")
imprimir_matriz(base_productos)

def imprimir_matriz2(matriz):
  print(f"--------------PRODUCTOS--------------")
  print(f"C \t PRODUCTO \t Pr$ \tStock")
  for i in range(len(matriz)-1):
    if i !=0:
      print("")
    for j in range(len(matriz)):
      print(f"{matriz[j][i]}",end='\t')
  print("") 

def imprimir_codigo_producto(matriz):
  print(f"--------------PRODUCTOS--------------")
  print(f"C \t PRODUCTO")
  for i in range(len(matriz)-1):
    if i !=0:
      print("")
    for j in range(2):
      print(f"{matriz[j][i]}",end='\t')
  print("") 


