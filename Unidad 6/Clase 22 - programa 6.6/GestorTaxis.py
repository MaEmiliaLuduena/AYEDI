

import Autos_Chofer as ac

lista_choferes=[]
lista_autos=[]

#CLASE DE OBJETOS gestorTaxis - Esta clase solo almacena las funciones que me gestionaran el sistema
class GestorTaxis:

    def crear_chofer(self): #crear chofer
        while True:
            dni = input("Ingrese el dni del chofer: ")

            flag=True #en el siguiente segmento se valida que el DNI NO se encuentre cargado
            for chofer in lista_choferes:
                if dni== chofer.get_dni():
                    flag=False
            if dni.isdigit() and len(dni) == 8 and flag:
                break
            else:
                print("El DNI ya existe o es incorrecto.")

        nombre = input("Ingrese el nombre del chofer: ").capitalize()
        apellido = input("Ingrese el apellido del chofer: ").capitalize()
        fecha_nacimiento = input("Ingrese la Fecha de Nacimiento del chofer: ")
        residencia = input("Ingrese la residencia del chofer: ").capitalize()

        #se crea el objeto CHOFER y se almacena en la lista
        lista_choferes.append(ac.Chofer(nombre, apellido, dni, fecha_nacimiento, residencia))
        print("\nChofer cargado con Exito!")


    def crear_auto(self): #crear auto
        if (len (lista_choferes)==0): #valida que antes exista un chofer
            print("\nPrimero Cargue un Chofer!")
            return False

        while True:
            patente = input("""\n------Formatos Validos------
                Patente Vieja: AAA 123
                Patente Nueva: AA 123 BB\n\nIngrese la patente: """)
            
            #en este segmento se contabilizan las letras y numeros de la patente ingresada para verificar que sea correcta
            cont_letras = 0
            cont_numeros = 0
            for i in patente:
                if i.isdigit():
                    cont_numeros+=1
                elif i.isalpha():
                    cont_letras+=1
            if cont_letras>=3 and cont_letras<=4 and cont_numeros==3:
                break
            else:
                print("\nPatente Incorrecta.")

        marca = input("Ingrese la marca del Auto: ")
        modelo = input("Ingrese el modelo del Auto: ")

        while True:
            try:
                año = int(input("Ingrese el año del Auto: "))
                break
            except:
                print("Año Incorrecto, Ingrese solo Numeros.")

        self.imprimir_info_choferes() #se imprime la info de los choferes actuales para la eleccion de uno mendiante el DNI

        flag=True #en este segmento se valida el DNI del chofer elegido
        while flag:
            dni_chofer = input("\nIngrese el DNI del chofer a elegir: ")
            for chofer in lista_choferes:
                    if dni_chofer == chofer.get_dni():
                        lista_autos.append(ac.Autos(patente,modelo,año,marca,dni_chofer)) #se crea el objeto AUTO y se almacena en la lista
                        flag=False
            
        print("\nTaxi cargado con éxito!")
            

    def imprimir_info_choferes(self):
        if (len (lista_choferes)==0): #valida que antes exista un chofer
            print("\nPrimero Cargue un Chofer!")
            return False

        print("\n----- Choferes Disponibles-----")
        for i in lista_choferes:
            i.imprimir_informacion_chofer()
    

    def imprimir_info_autos(self):
        print("\n----- Taxis Habilitados-----")
        for i in lista_autos:
            i.imprimir_informacion_auto()


    def modificar_chofer_auto(self):
        if (len (lista_choferes)==0): #valida que antes exista un chofer
            print("Primero Cargue un Chofer!")
            return False

        flag=True #en este segmento se valida el la PATENTE del Auto elegido
        while flag:
            self.imprimir_info_autos()
            patente=input("\nIngrese la Patente del Autor que desea cambiarle el chofer: ")
            for auto in lista_autos: #se analizan los autos de la lista 1 por 1
                    if patente == auto.get_patente(): #se verifica que la patente ingresada coincida con alguno de los autos de la lista
                        nuevo_dni = input("Ingrese el DNI del Nuevo Chofer: ")
                        auto.set_chofer(nuevo_dni) #se llama a la funcion "set_chofer" pasandole por parametros el DNI del nuevo chofer
                        flag=False


    def modificar_residencia_chofer(self):
        if (len (lista_choferes)==0): #valida que antes exista un chofer
            print("\nPrimero Cargue un Chofer!")
            return False

        flag=True #en este segmento se valida el DNI del Chofer elegido
        while flag:
            self.imprimir_info_choferes()
            dni_chofer=input("\nIngrese el DNI del chofer a modificar: ")
            for chofer in lista_choferes: #se analizan los choferes de la lista 1 por 1
                    if dni_chofer == chofer.get_dni(): #se verifica que el DNI ingresado coincida con alguno de los Choferes de la lista
                        nueva_residencia = input("Ingrese la nueva residencia del chofer: ")
                        chofer.set_residencia(nueva_residencia) #se llama a la funcion "set_residencia" pasandole por parametros la nueva residencia del chofer
                        flag=False
