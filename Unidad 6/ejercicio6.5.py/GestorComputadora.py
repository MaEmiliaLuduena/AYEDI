import Computadoras as cp

lista_computadoras=[]
lista_id_modelo=["Asus","Sony","Lenovo","Bangho","Hp","Samsung"]
lista_sistemaOperativo=["Windows","Ubuntu","Linux"]

class GestorComputadora:

    def __init__(self):
        pass

    def crear_computadora(self):
        while True:
            tipo_pc= input(
            """\n
        -----------Crear Computadora-----------
        Por favor ingrese una opción:
            1. Computadora de Escritorio
            2. Computadora Notebook
            
            0. Salir 
            
            Opcion: """
            )
            if (tipo_pc=="1" or tipo_pc=="2"):
                break
            else:
                print("Opcion Incorrecta")

        while True:
            try:
                numero_serie=int(input(f"\nIngrese el N° de Serie del equipo: "))
                break
            except:
                print("Datos erroneos")

        while True:
            print(lista_id_modelo)
            id_modelo=input(f"\nIngrese el modelo de su equipo: ").capitalize()
            if id_modelo in lista_id_modelo:
                break
            else:
                print("Modelo incorrecto, seleccione uno de la lista.\n")

        while True:
            print(lista_sistemaOperativo)
            Sistema_Operativo=input(f"\nIngrese el Sistema Operativo de su equipo: ").capitalize()
            if Sistema_Operativo in lista_sistemaOperativo:
                break
            else:
                print("Sistema Operativo incorrecto, seleccione uno de la lista.\n")
        
        if tipo_pc=="1":
            while True:
                opcion= input("""\nDesea agregar un color a su equipo?: 
                1. SI
                2. NO
                
                Opcion: """)
                if opcion == "1":
                    color = input("Ingrese el color del equipo: ").capitalize()
                    break
                elif opcion == "2":
                    #color=""
                    break
                else:
                    print("Opcion Incorrecta")
        else:
            while True:
                opcion=input("""\nDesea agregar el tamaño de pulgadas a su equipo?: 
                1. SI
                2. NO
                
                Opcion: """)
                if opcion == "1":
                    while True:
                        try:
                            pulgadas = float(input("Ingrese las Pulgadas de la Notebook: "))
                            break
                        except:
                            print("Datos incorrectos")
                    break
                elif opcion == "2":
                    #pulgadas=""
                    break
                else:
                    print("Opcion Incorrecta")                
        
        print(f"\nIngrese los periféricos del equipo, para finalizar escriba 'Salir' ")
        lista_perifericos=[]
        i=1
        while True:
            periferico = input(f"Periférico {i}: ").capitalize()
            i+=1
            if periferico == "Salir":
                break
            lista_perifericos.append(periferico)
        
        if tipo_pc == "1":
            nueva_computadora= cp.Escritorio(numero_serie,id_modelo,lista_perifericos,Sistema_Operativo,color)
        else:
            nueva_computadora= cp.Notebook(numero_serie,id_modelo,lista_perifericos,Sistema_Operativo,pulgadas)
        lista_computadoras.append(nueva_computadora)

    def listar_computadoras(self):
        for computadora in lista_computadoras:
            computadora.presentarse()
            computadora.tipo_computadora()
            print("")
    
    def cambiar_sistema_operativo(self):
        for computadora in lista_computadoras:
            print(computadora.numero_serie)   
        while True:
            try:
                numero_serie = int(input(f"\nIngrese el N° de Serie del equipo: "))
            except:
                print("ERROR - Ingrese un N° de serie de la Lista.")
            for computadora in lista_computadoras:
                if computadora.numero_serie == numero_serie:
                    while True:
                        print(lista_sistemaOperativo)
                        nuevo_sistema_operativo = input(f"\nIngrese el nuevo Sistema Operativo: ").capitalize()
                        if nuevo_sistema_operativo in lista_sistemaOperativo:
                            computadora.cambiar_sistema_operativo(nuevo_sistema_operativo)
                            return
                        else:
                            print("El S.O. ingresado NO se encuentra en la lista.")


    def listar_perifericos(self):
        for computadora in lista_computadoras:
            print(computadora.numero_serie) 
        while True:
            try:
                numero_serie = int(input(f"\nIngrese el N° de Serie del equipo que desea ver sus periféricos: "))
                for computadora in lista_computadoras:
                    if computadora.numero_serie == numero_serie:
                        print(computadora.listaPerifericos)
                        return
            except:
                print("ERROR - Ingrese un N° de serie de la Lista.")
    

    def agregar_perifericos(self):
        for computadora in lista_computadoras:
            print(computadora.numero_serie)
        while True:
            try:
                numero_serie = int(input(f"\nIngrese el N° de Serie del equipo: "))
                for computadora in lista_computadoras:
                    if computadora.numero_serie == numero_serie:
                        while True:
                            nuevo_periferico= input(f"\nIngrese los nuevos periféricos, para finalizar escriba 'Salir': ").capitalize()
                            if nuevo_periferico != "Salir":
                                lista=[]
                                lista= computadora.listaPerifericos
                                lista.append(nuevo_periferico)
                                computadora.listaPerifericos = lista
                            else:
                                break
                break
            except:
                print("ERROR - Ingrese un N° de serie de la Lista.")