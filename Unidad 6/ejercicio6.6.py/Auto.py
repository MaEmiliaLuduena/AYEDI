"""
*   La Clase auto tiene los atributos (patente, modelo, año, marca, nombre_Chofer (objeto clase Choferes))
    2. Crear instancias de Autos (verificando que haya choferes para ese auto) y guardarlos en una lista de autos
    3. Modificar el chofer de un auto
    6. imprimir lista de autos (con toda su informacions)
"""

""" class Auto:
    #CONSTRUCTOR
    def _init_(self, patente,modelo, año, marca, nombre_chofer):
        self.patente = patente
        self.modelo = modelo
        self.año = año
        self.marca = marca
        self.nombre_chofer = nombre_chofer

    def get_chofer(self):
        return self.nombre_chofer

    def set_chofer(self,nuevo_nombre):
        self.nombre_chofer =  nuevo_nombre

    def imprimir_informacion(self):
        print(f"Patente:{self.patente} - Año{self.año} - Marca/Modelo {self.marca}/{self.modelo} - Chofer {self.nombre_chofer}") """


class Auto:
    def __init__(self,patente,modelo,anio,marca,dni_chofer):
        self.patente = patente
        self.modelo = modelo
        self.anio = anio
        self.marca = marca
        self.dni_chofer = dni_chofer
    
    def get_chofer(self):
        return self.dni_chofer

    def get_patente(self):
        return self.patente
    
    def set_chofer(self,dni_chofer):
        self.dni_chofer = dni_chofer
    
    def imprimir_info(self):
        print(f"Patente: {self.patente} - año: {self.anio} - Marca/Modelo: {self.marca}/{self.modelo} - Chofer: {self.dni_chofer}")