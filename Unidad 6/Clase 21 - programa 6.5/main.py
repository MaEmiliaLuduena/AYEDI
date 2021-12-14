"""

Ejercicio 6.5

Crear una clase padre Computadoras:
    * Constructor debe incluir los atributos (id_modelo,listaPerifericos,SO)
    * Crear metodos para esta clase de:
        - Presentarse (modelo,marca,precio)
        - Indicar tipo de Computadora (Clases heredadas)
        - Metodos que luego modificarán las clases hijas. agregar_perifericos,CambiarSO

Crear 2 clases que hereden de la clase padre Computadoras, con un atributo en particular para cada una
    - Escritorio
    - Notebbok

Crear clase GestorComputadora que cuente con las siguientes funciones para un menu
    - Crear Computadora, indicando tipo y guardar en una lista. Verificando marca y SO de una lista
    - Listar Computadoras (presentandolos), indicando tipo.
    - Cambiar SO de una Computadora, verificando una lista de SO disponibles
    - Listar perifericos

"""
import GestorComputadora as gc
gestor= gc.GestorComputadora()

while True:
    opcion=input(
    """
-----------Menu principal-----------
Por favor ingrese una opcion:
    1. Crear Computadora
    2. Listar Computadoras
    3. Cambiar SO de una Computadora
    4. Listar perisfericos
    5. Agregar perisfericos

    0. Salir 
    
    Opcion: """
    )
    if (opcion=="1"):
        gestor.crear_computadora()
    elif (opcion=="2"):
        gestor.listar_computadoras()
    elif (opcion=="3"):
        gestor.cambiar_sistema_operativo()
    elif (opcion=="4"):
        gestor.listar_perisfericos()
    elif (opcion=="5"):
        gestor.agregar_perisfericos()
    elif (opcion=="0"):
        break
    else:
        print("Opcion Incorrecta")


