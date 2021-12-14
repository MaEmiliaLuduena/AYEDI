"""
El programa debe:
*   Contar con una Clase Evento con los atributos (nombre_evento (único), fecha, hora, lugar)
*   Contar con dos Clases Hijas que use el constructor de la clase padre pero que tenga un atributo más:
        - EventoPersonal (Atributo: organizador (nombre de la persona que organiza))
        - EventoLaboral (Atributo: obligatorio "True o False" (por defecto = True))
        
*   Se deben crear 4 métodos para la clase padre Evento (que heredaran las clases hijas):
        1. Mostrar información: Que indique el nombre_evento, fecha y lugar del evento 
        2. Obtener tipo de evento (tipo de clases heredadas o padre)
        3. Setear Fecha y Hora (Setearán la Fecha y Hora en una misma función)
        4. Setear lugar (Setear el lugar)
"""


#CLASE PADRE
class Evento:
    #CONSTRUCTOR
    def __init__(self, nombre_evento, fecha, hora, lugar): 
        self.nombre_evento = nombre_evento #unico
        self.fecha = fecha
        self.hora = hora
        self.lugar = lugar 

    def mostrar_info(self):
        print(f"Nombre del Evento: {self.nombre_evento} - Fecha y Hora: {self.fecha}{self.hora} - Lugar del evento: {self.lugar}")

    def get_nombre_evento(self): #me trae el nombre del evento
        return self.nombre_evento

    def tipo_evento(self):
        print("Soy un Evento del tipo", type(self).__name__)

    def set_fecha_hora(self,nueva_fecha, nueva_hora): #cambia la fecha y hora por los parámetros indicados
        self.fecha = nueva_fecha
        self.hora = nueva_hora
        print(f"Antes mi fecha era {self.fecha} y ahora es {nueva_fecha}. Y antes mi hora era {self.hora} y ahora es {nueva_hora}")

    def set_lugar(self, nuevo_lugar): #cambia el lugar por el del parámetro que se le pasa
        self.lugar = nuevo_lugar


#CLASES HIJAS
class EventoPersonal(Evento):
    def __init__(self, nombre_evento, fecha, hora, lugar, organizador):
        super().__init__(nombre_evento, fecha, hora, lugar) #super me trae los métodos de la clase padre para no tener que vovler a agregarlos, y sólo agregar el atributo que quiero agregar a la clase hija
        self.organizador = organizador #nombre de la persona que organiza
 
class EventoLaboral(Evento):
    def __init__(self, nombre_evento, fecha, hora, lugar, obligatorio="True"):
        super().__init__(nombre_evento, fecha, hora, lugar)
        self.obligatorio = obligatorio