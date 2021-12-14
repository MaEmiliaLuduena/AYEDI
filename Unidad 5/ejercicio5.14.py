"""
Ejercicio 5.14
Crear una funcion que debe: (usar diccionario)

Crear un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
Pida al usuario el dato a agregar (key) y el valor
Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""

persona= {}

def informacion_persona():
    while True:
      clave_diccionario= input("Ingrese el dato a agregar o 'fin' para terminar: ")
      if clave_diccionario == "fin":
        break
      else:
        valor_diccionario= input("Ingrese el valor del dato agregado: ")
        persona.update({clave_diccionario:valor_diccionario})
        for i, j in persona.items():
          print(f"Clave: {i} - Valor: {j}")
    print(f"Su diccionario quedó de la siguiente manera:\n {persona}")

informacion_persona()

"""
def agregar_informacion():
  while True:
    key = input("Ingrese la informacion que registrara o salir (para abandonar el programa): ")
    if key =="salir":
      break
    if key in personas:
      print("Ya existe el valor, ingrese uno diferente!!")
    else:
      valor = input(f"Por favor ingrese el valor de {key}: ")
      personas.setdefault(key,valor)
      print(personas)
"""