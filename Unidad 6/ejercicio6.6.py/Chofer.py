"""
*   La Clase Chofer tiene los atributos (nombre, apellido, dni, fecha nacimiento, Residencia)
    4. Modificar el lugar de residencia del chofer indicando su nombre
    5. imprmiir lista de choferes (con toda su informacion)
"""

class Chofer:
    def __init__(self,nombre, apellido, dni, fecha_nacimiento, residencia):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.residencia = residencia
       
    def set_nombre(self,nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_nombre(self):
        return self.nombre
    
    def get_dni(self):
        return self.dni
 
    def set_residencia(self, nueva_residencia):
        self.residencia = nueva_residencia
 
    def imprimir_info(self):
        print(f"Nombre: {self.get_nombre()} - Apellido: {self.apellido} - DNI: {self.dni} - Fecha nacimiento: {self.fecha_nacimiento} - Residencia: {self.residencia}")