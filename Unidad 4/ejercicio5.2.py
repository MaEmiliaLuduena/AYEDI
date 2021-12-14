"""
##**Ejercicio 5.2**
Crear una funcion que debe:

*    Pedir al usuario una palabra o una frase
*    Indicar si esta se trata de un palindromo (reconocer, neuquen, amor a roma)
*    No deben aparecer y se deben tener en cuenta todos los posibles errores
"""

def es_palindromo():
  palabra_original = input("Ingrese una palabra: ")
  if not palabra_original.isalpha():
    print("la palabra no es correcta")
  else:
    palabra_original_lista = list(palabra_original)
    palabra_reversa = palabra_original_lista.copy()
    palabra_reversa.reverse()
    if palabra_original_lista == palabra_reversa:
      print("OK! es una palabra capicua")
    else:
      print("ERROR! No es una palabra capicua")

es_palindromo()