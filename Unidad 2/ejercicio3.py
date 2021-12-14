#El programa debe:
#- pedir dos datos por consola
#- verificar que los dos datos sean numeros enteros
#- en caso verdadero imprimir la suma de ambos
#- en caso contrario imprimir error

try:
    dato1= int(input("Ingrese el primer número entero: "))
    dato2= int(input("Ingrese el segundo número entero: "))

    suma= dato1 + dato2
    print(suma)
except:
    print("Recuerda que debes ingresar un número entero")