"""
Crear una clase padre Computadoras:
*   Constructor debe incluir los atributos (id_modelo,listaPerifericos,SO)
*   Crear metodos para esta clase de:
    1.  Presentarse (id_modelo,listaPerifericos,SO)
    2.  Indicar tipo de Computadora (Clases heredadas)
    3.  Metodos que luego modificarán las clases hijas. agregar_perifericos,CambiarSO
Crear 2 clases que hereden de la clase padre Computadoras, con un atributo en particular para cada una
1.   Escritorio
2.   Notebbok
"""
listaPerifericos=[]
class Computadoras:
    #constructor
    def __init__(self,id_modelo,listaPerifericos,SO):
        self.id_modelo = id_modelo #unico
        self.listaPerifericos = listaPerifericos
        self.SO = SO

    def presentarse(self):
        print(f"""Soy una computadora con id {self.id_modelo}, con los periféricos {self.listaPerifericos} 
        y con Sistema Operativo {self.SO}""")

    def tipo_computadora(self):
        print ("Computadora tipo: ", type(self).__name__)

    def agregar_perifericos(self):
        """ print (f"Se ha agregado {periferico} a la lista {self.listaPerifericos}")
        self.listaPerifericos.append(periferico) """
        pass

    def CambiarSO(self):
        pass
    
class Escritorio(Computadoras):
    def __init__(self,id_modelo,listaPerifericos,SO, marca = "Samsung"):
        super().__init__(id_modelo,listaPerifericos,SO)
        self.marca = marca

    def agregar_perifericos(self,nuevo_periferico):
        print (f"Los periféricos que tiene la Computadora de Escritorio son {self.listaPerifericos}")
        self.listaPerifericos.append(nuevo_periferico)

 
    def CambiarSO(self,nuevo_SO):
        print (f"El SO de la computadora Escritorio era {self.SO} y ahora es {nuevo_SO}")
        self.SO = nuevo_SO

class Notebook(Computadoras):
    def __init__(self,id_modelo,listaPerifericos,SO, marca = "LG"):
        super().__init__(id_modelo,listaPerifericos,SO)
        self.marca = marca
 
    def agregar_perifericos(self,nuevo_periferico):
        print (f"Los periféricos que tiene la Computadora de Escritorio son {self.listaPerifericos}")
        self.listaPerifericos.append(nuevo_periferico)

    def CambiarSO(self,nuevo_SO):
        print (f"El SO de la computadora Notebook era {self.SO} y ahora es {nuevo_SO}")
        self.SO = nuevo_SO          

