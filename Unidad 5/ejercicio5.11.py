"""
Ejercicio 5.11
Crear una funcion que debe: (usar diccionario)

Contener un diccionario con distintas monedas de paises, siendo: La key el nombre de la moneda y el valor el simbolo.
Preguntar al usuario que tipo de moneda desea y mostrar el simbolo si existe en el diccionario, caso contrario indicar que no existe.
"""

monedas = {
  "Peso":"$", 
  "Dolar": "USD",
  "Euro":  "€"
  }

def obtener_simbolo():

  #imprime los key
  print("---------------Keys---------------")
  for i in monedas:
    print(i)

  moneda= input("\nIngrese qué tipo de moneda desea: ").capitalize()
  valor = monedas.get(moneda,"No existe esa moneda")

  print(f"El símbolo de {moneda} : {valor}")

obtener_simbolo()
