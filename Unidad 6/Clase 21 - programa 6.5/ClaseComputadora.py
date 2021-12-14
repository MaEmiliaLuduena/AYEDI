

listaPerifericos=[]
class Computadoras:
    def __init__(self,numero_serie,id_modelo,listaPerifericos,sistemaOperativo):
        self.numero_serie = numero_serie
        self.id_modelo = id_modelo
        self.listaPerifericos = listaPerifericos
        self.sistemaOperativo = sistemaOperativo
    
    def presentarse(self):
        print(f"Soy una Computadora modelo {self.id_modelo}, con perisfericos {self.listaPerifericos} y con SO {self.sistemaOperativo}")
    
    def tipo_computadora(self):
        print("Soy una Computadora tipo", type(self).__name__)

    def agregar_perifericos(self):
        pass

    def CambiarSO(self):
        pass

class Escritorio(Computadoras):
    def __init__(self,numero_serie,id_modelo,listaPerifericos,sistemaOperativo,color = "negra"): #color por defecto
        super().__init__(numero_serie,id_modelo,listaPerifericos,sistemaOperativo)
        self.color = color
    
    def agregar_perifericos(self,nuevo_periferico):
        self.listaPerifericos.append(nuevo_periferico)
        print(f"Los nuevos perisfericos del equipo son: {self.listaPerifericos}")

    def cambiar_sistema_operativo(self,sistemaOperativo):
        self.sistemaOperativo = sistemaOperativo
        print(f"El nuevo SO del equipo es: {self.sistemaOperativo}")

class Notebook(Computadoras):
    def __init__(self,numero_serie,id_modelo,listaPerifericos,sistemaOperativo,pulgadas = 15.6): #pulgadas por defecto
        super().__init__(numero_serie,id_modelo,listaPerifericos,sistemaOperativo)
        self.pulgadas = pulgadas

    def agregar_perifericos(self,nuevo_periferico):
        self.listaPerifericos.append(nuevo_periferico)
        print(f"Los nuevos perisfericos del equipo son: {self.listaPerifericos}")

    def cambiar_sistema_operativo(self,sistemaOperativo):
        self.sistemaOperativo = sistemaOperativo
        print(f"El nuevo SO del equipo es: {self.sistemaOperativo}")
        

