"""
###**Ejercicio 6.2**
Crear una clase de FiguraGeometrica:
*   Cuyo constructutor debe inicializar los atributos tipo_de_figura, color, y tamaño 
    (por defecto "pequeño")
*   Se deben crear 3 metodos en la clase:
    1.  Presentar la figura: Un {tipo_de_figura} de color {color} y tamaño {tamaño}
    2.  Cambiar color de figura e indicar nuevo color
    3.  verificar si la figura es tamaño pequeño, agrandar a tamaño grande
    """

class FiguraGeometrica:
    #constructor
    def __init__(self,tipo_de_figura,color,tamaño="pequeño"):
        self.tipo_de_figura = tipo_de_figura 
        self.color = color
        self.tamaño = tamaño

#figura_1= FiguraGeometrica("triangulo", "blanco")
#print(figura_1.tamaño)

    def presentar_figura(self):
        print(f"Un {self.tipo_de_figura} de color {self.color} y tamaño {self.tamaño}")
#figura_1= FiguraGeometrica("triangulo", "blanco")
#figura_1.presentar_figura()

    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        print(f"Cambie del color {self.color} al color {nuevo_color}")
        
        #figura_1= FiguraGeometrica("triangulo", nuevo_color)
        #figura_1.cambiar_color(nuevo_color)

    def verificar_tamaño(self): #ver en colab como llamar el método
        if self.tamaño == "pequeño":
            self.tamaño = "grande"
        print(f"El tamaño de {self.tipo_de_figura} ahora es {self.tamaño}")


figura_1=FiguraGeometrica("triangulo","blanco")
figura_1.presentar_figura()
figura_1.verificar_tamaño()

nuevo_color = input("Indique el nuevo color de la figura: ")
if(figura_1.color == nuevo_color):
    print("ya tiene ese color no es necesario cambiarlo")
else:
    figura_1.cambiar_color(nuevo_color)
