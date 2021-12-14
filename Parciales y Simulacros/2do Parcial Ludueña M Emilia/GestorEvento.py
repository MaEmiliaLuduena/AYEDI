"""
*   Se debe crear una clase GestorEvento que cuente con las siguientes funciones para un menu:

    1.  Crear instancias de un evento y guárdalos en una lista de eventos. 
        1.1) Se debe verificar que tipo de instancia de evento a crear y los parámetros. IMPORTANTE!: clase hijas verificar y pedir parámetros
             - nombre_evento: debe ser único
             - Fecha: formato (dd/mm/yyyy) -> únicamente verificar la longitud del string = 10 
             - Hora: formato (hh:mm) -> no es necesario verificar
             - Lugar: sin formato especifico, no es necesario verificar
        1.2) Al crear un evento es necesario logearlo (Escribir en una línea nueva: nombre_evento-Fecha-Hora-Lugar-Tipo_de_evento(tipo de clase)) 
             en un archivo llamado lista_eventos.txt (Crear función en el mismo gestor). IMPORTANTE!: verificar permisos
        1.3) En caso que la instancia del evento sea EventoPersonal.
             - Para el organizador, el usuario debe elegir a través de una clave (mostradas por el programa) 
                desde un diccionario de organizadores.
             - En caso que no exista el organizador deseado debe ser "incognito" (AYUDA: Funcion get de diccionarios)
    2.   Listar eventos disponibles, leyendo la lista_evetos.txt. IMPORTANTE!: recorrer el archivo, no la lista. 
    3.   Cambiar el lugar de un evento, seleccionando su nombre. (Hacer check correspondientes)
"""

import Evento as ev
import os
path = os.path.abspath(os.path.dirname(__file__))
path_archivo = path+"\\evento.txt"
lista_eventos = []

class GestorEvento():
    def crear_evento(self):
        while True:
            condicion=input(
            """
        Por favor ingrese la opción que desee utilizar:
            1. Evento 
            2. Evento Personal
            3. Evento Laboral
        Número: """)

            if condicion == "1" or condicion == "2" or condicion == "3": #sale del bucle si ingresa una opción correcta
                break
            else:
                print("Opcion incorrecta")


        while True:
            nombre_evento = input("Ingrese el nombre del evento: ")

            flag=True #verifica que el nombre evento no se encuentre para que no se repita
            for evento in lista_eventos:
                if nombre_evento == evento.get_nombre_evento():
                    flag=False
            if not nombre_evento.isdigit() and flag: #si el nombre del evento no es un dígito/num y verifica que no se encuentre repetido corta el bucle
                break
            else:
                print("El Nombre Evento ya existe o es incorrecto.")
        
        #verifica la fecha
        while True:
            fecha = input("Ingrese la fecha del evento en formato (dd/mm/yyyy): ")
            if len(fecha) == 10:
                break
            else:
                print("La longitud debe ser como la especificada en el campo fecha") 

        hora = input("Ingrese la hora del evento en formato (hh:mm): ")
        lugar = input("Ingrese el lugar del evento: ").capitalize()

    
        if condicion == "2":
          organizadores = {
            "FA":"familia", 
            "AM": "amigos",
            "PR": "propio"
            }
          print("""
          \t ORGANIZADORES
                    FA = familia 
                    AM = amigos
                    PR = propio
               """)
          organizador = input("Ingrese el nombre del organizador:  ")
          valor = organizadores.get(organizador, "INCÓGNITO")
          print(f"La opción {organizador} corresponde a {valor}.")

        if condicion == "1":
            nombre_instancia = ev.Evento(nombre_evento, fecha, hora, lugar)
        elif condicion == "2":
            nombre_instancia = ev.EventoPersonal(nombre_evento, fecha, hora, lugar, organizador)
        elif condicion == "3":
            nombre_instancia = ev.EventoLaboral(nombre_evento, fecha, hora, lugar, obligatorio="True")
        lista_eventos.append(nombre_instancia)

        
        try:
            fichero = open(path_archivo, 'a+')
            fichero.write(f"Nombre_evento: {nombre_evento}, Fecha: {fecha}, Hora: {hora}, Lugar: {lugar}, Tipo_de_evento: {self.tipo_evento} \n")
            fichero.close()
        except:
            print("ERROR.")

    #Imprime la lista de eventos y que tipo de evento es
    def listar_eventos(self):
        for i in lista_eventos:
            i.mostrar_info()
            i.tipo_evento()

    def cambiar_lugar(self):
        if len(lista_eventos)==0: #valida que antes exista un evento
            print("Primero debe cargar un evento")
            return False
        flag=True #se valida el nombre del evento elegido
        while flag:
            self.mostrar_info()
            nombre_evento=input("\nIngrese el nombre del evento a modificar el lugar: ")
            for i in lista_eventos: #se analizan los eventos de la lista 1 por 1
                    if nombre_evento == i.get_nombre_evento(): #se verifica que el nombre del evento ingresado coincida con alguno de los eventos de la lista
                        nuevo_lugar = input("Ingrese el nuevo lugar del evento: ")
                        i.set_lugar(nuevo_lugar) #se llama a la funcion "set_lugar" pasandole por parametros el nuevo lugar del evento
                        flag=False

        

        