"""  
*   Cuyo constructor debe inicializar los atributos nombre, apellido, edad, ciudad_de_residencia
*   Se deben crear dos metodos en la clase:
    1.  Presentarse que la persona indique: Soy {nombre} {apellido}, tengo {edad} años y vivo en 
        {ciudad de residencia}
    2.  Indique segun la edad de la persona si esta es: Niño (0 a 14), Adolescente (14 a 22),
         Joven (22 a 30), mayor(30 a 50)"""

class Persona:
    nacionalidad = "argentina"
    #constructor
    def __init__(self,dni,nombre,apellido,edad,residencia):
        self.dni = dni #unico
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.residencia = residencia
    
    def presentarse(self):
        print(f"""Soy {self.nombre} {self.apellido}, tengo {self.edad} años y vivo en {self.residencia}. Mi nacionalidad es {self.nacionalidad}""")
    
    def rango_edad(self):
        nombre_apellido = f"{self.nombre} {self.apellido}"
        if(self.edad > 0 and self.edad < 14):
            print(f"{nombre_apellido}  es niño")
        elif(self.edad >= 14 and self.edad <= 22):
            print(f"{nombre_apellido} es adolescente")
        elif(self.edad > 22 and self.edad < 30):
            print(f"{nombre_apellido} es joven")
        elif(self.edad >= 30 and self.edad <= 50):
            print(f"{nombre_apellido} es mayor")
        else:
            print(f"{nombre_apellido} es adulto mayor")