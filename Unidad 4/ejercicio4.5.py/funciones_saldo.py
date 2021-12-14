"""2.Ingresa dinero al sistema y actualiza el saldo"""
def ingresar_y_actualizar(dinero_disponible):
    while True:
        try:
            dinero_ingresar = float(input("Ingrese dinero a depositar: "))
        except:
            print("Error en los parametros")
        if dinero_ingresar > 0 :
            break
        else:
            print("Por favor ingrese una suma positiva")
    dinero_disponible+=dinero_ingresar
    return dinero_disponible

def retirar_y_actualizar(dinero_disponible):
    while True:
        try:
            dinero_retirar= float(input("Ingrese el dinero a retirar: "))
        except:
            print("Error en los parametros")
        if dinero_retirar > 0:
            break
        else:
            print("Por favor ingrese una suma positiva")
    dinero_disponible -= dinero_retirar
    return dinero_disponible

def consultar_saldo(dinero_disponible):
    print(f"El dinero disponible es: {dinero_disponible}")
