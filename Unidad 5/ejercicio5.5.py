"""
##**Ejercicio 5.5**
Crear una funcion que debe:
*    Tener almacenado el abcedario en una lista
*    Pedir al usuario un numero (2 o 3) - VERIFICAR 
*    Elimina de la lista las letras que ocupen posiciones múltiplos de ese numero
*   Mostrar por pantalla la lista resultante.
*   No deben aparecer y se deben tener en cuenta todos los posibles errores
"""

def eliminar_multiplos_abc():
    abc = "abcdefghijklmnñopqrstuvwxyz"
    lista_abecedario = list(abc)
    
    while True:
        numero = input("Ingrese un num (2 o 3): ")
        if numero == "2" or numero == "3":
            break
    lista_a_eliminar = []
    for i in range(int(numero),len(lista_abecedario)+1,int(numero)):
        lista_a_eliminar.append(lista_abecedario[i-1])

    for i in lista_a_eliminar:
        if i in lista_abecedario:
            lista_abecedario.remove(i)

    print(f"El abcedario sin las letras multiplos de {numero} es:\n{lista_abecedario} ")
    
eliminar_multiplos_abc()