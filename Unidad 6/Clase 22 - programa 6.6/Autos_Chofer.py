

#CLASE DE OBJETOS CHOFER
class Chofer:

    def __init__(self,nombre,apellido,dni,fecha_nacimiento,residencia): #Constructor de Objetos "CHOFERES"
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.residencia = residencia
    
    def get_dni(self): #me devuelve un dni
        return self.dni

    def get_residencia(self): #me devuelve la residencia de un chofer
        return self.residencia
    
    def set_residencia(self,nueva_residencia): #modifica la residencia de un chofer en particular
        self.residencia = nueva_residencia
        print(f"La nueva residencia es {self.residencia}")

    def imprimir_informacion_chofer(self): #imprime los datos de un chofer
        print(f"""\nNombre: {self.get_nombre()} - Apellido {self.apellido} - Dni: {self.dni} - Fecha de Nacimiento: {self.fecha_nacimiento} - Residencia: {self.residencia}""")

#CLASE DE OBJETOS AUTO
class Autos:

    def __init__(self,patente,modelo,año,marca,dni_chofer): #Constructor de Objetos "AUTOS"
        self.patente = patente
        self.modelo = modelo
        self.año = año
        self.marca = marca
        self.dni_chofer = dni_chofer
    
    def get_patente(self): #me devuelve una patente
        return self.patente

    def get_chofer(self): #me devuelve el dni de un chofer que este cargado en un auto
        return self.dni_chofer

    def set_chofer(self, nuevo_dni): #Modifica le dni de un auto solicitado
        self.dni_chofer = nuevo_dni
        print("Chofer Modificado con Exito!")

    def imprimir_informacion_auto(self): #imprime los datos de un auto
        print(f"""\nPatente: {self.patente} - Año {self.año} - Marca y Modelo: {self.modelo}/{self.modelo} - Chofer DNI: {self.dni_chofer}""")



