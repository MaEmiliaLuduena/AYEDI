"""
###**Ejercicio 6.4**
Crear una clase padre Vehiculos:
*   Constructor debe incluir los atributos (patente,marca,año,origen)
*   Crear metodos para esta clase de:
    1.  Presentarse (patente,marca,año,origen)
    2.  Indicar tipos de vehiculo(Clases heredadas)
    3.  Metodos que luego modificarán las clases hijas. Acelerar, Retroceder, obtener_velocidad, setear_velocidad
"""
class Vehiculo:
    def __init__(self,patente,marca,anio,origen):
        self.patente = patente
        self.marca = marca
        self.anio = anio
        self.origen = origen
    
    #para todas las clases  (padre e hijas)
    def presentarse(self):
        print(f"soy un vehiculo con patente {self.patente}, marca {self.marca}, del año {self.anio} y origen {self.origen}")
    
    #para todas las clases  (padre e hijas)
    def tipo_vehiculo(self):
        print("Soy un vehículo tipo", type(self).__name__) #me dice el tipo de la clase heredada

    def acelerar(self):
        pass

    def retroceder(self):
        pass

    def obtener_velocidad_max(self):
        pass

    def setear_velocidad_max(self):
        pass

class Vehiculos_Particular(Vehiculo):
    def __init__(self, patente, marca, anio, origen, velocidad_max = 130): #Velocidad por defecto
        super().__init__(patente, marca, anio, origen)
        self.velocidad_max = velocidad_max
 
    def acelerar(self):
        print("Estoy acelerando soy un Vehículo Particular")
 
    def retroceder(self):
        print("Estoy retrocediendo soy un Vehículo Particular")
 
    def obtener_velocidad_max(self):
        print(f"La velocidad máxima es {self.velocidad_max} - soy un Vehículo Particular")
 
    def setear_velocidad_max(self, velocidad_max_nueva):
        print (f"La velocidad máxima era {self.velocidad_max} y ahora es {velocidad_max_nueva} - soy un Vehículo Particular")
        self.velocidad_max = velocidad_max_nueva
 
class Vehiculos_PickUp(Vehiculo):
    def __init__(self, patente, marca, anio, origen, velocidad_max = 100): #Velocidad por defecto
        super().__init__(patente, marca, anio, origen)
        self.velocidad_max = velocidad_max
 
    def acelerar(self):
        print("Estoy acelerando soy VPU")
 
    def retroceder(self):
        print("Estoy retrocediendo soy VPU")
 
    def obtener_velocidad_max(self):
        print(f"La velocidad maxima es {self.velocidad_max} - soy un VPU")
 
    def setear_velocidad_max(self, velocidad_max_nueva):
        print (f"La velocidad maxima era {self.velocidad_max} y ahora es {velocidad_max_nueva} - soy un VPU")
        self.velocidad_max = velocidad_max_nueva
 
class Vehiculos_Deportivo(Vehiculo):
    def __init__(self, patente, marca, anio, origen, velocidad_max = 200): #Velocidad por defecto
        super().__init__(patente, marca, anio, origen)
        self.velocidad_max = velocidad_max
 
    def acelerar(self):
        print("Estoy acelerando soy VD")
 
    def retroceder(self):
        print("Estoy retrocediendo soy VD")
 
    def obtener_velocidad_max(self):
        print(f"La velocidad maxima es {self.velocidad_max}  - soy un VD")
 
    def setear_velocidad_max(self, velocidad_max_nueva):
        print (f"La velocidad maxima era {self.velocidad_max} y ahora es {velocidad_max_nueva}  - soy un VD")
        self.velocidad_max = velocidad_max_nueva