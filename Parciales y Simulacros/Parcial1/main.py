'''
************************************************************
 MATERIA: Algoritmos y Estructuras de Datos 1
 EXAMEN: 1° Examen
 APELLIDO Y NOMBRE: Ludueña María Emilia
 DNI: 37093663
 CARRERA: Analista en Sistemas
 AÑO: 2021 
 Se envia mail con asunto: "[AYEDI 2021 - Apellido, Nombre - 1°Examen]"
 ************************************************************
 Items a evaluar:
 1. Requerimientos y comprension de consignas
 2. Estructura (modularización), legibilidad y comentarios del codigo.

¡Cualquier duda con el enunciado consultar al docente!
************************************************************
ENUNCIADO: "Programa de Gestión de alumnos y Materias"

Introduccion: 
    El siguiente programa consiste en un software de gestion de alumnos y gestion de materias
    de una institucion educativa.
    El programa debe permitir agregar alumnos al sistema junto con su informacion personal: 
    Nombre, Edad y mail.
    El programa debe permitir agregar Materias al sistema.

Requerimientos:
El programa debe:
*   Contar con un menu donde permita al usuario elegir entre las siguientes funciones:
    1. Ver lista de alumnos (Formato: nombre_usuario - Edad - Mail) (LISTO)
    2. Permitir al usuario del programa agregar un nuevo alumno (Indicando: nombre_usuario - Edad - Mail)
       Verificando: Que el nombre_usuario no exista previamente, la edad entre 10 y 18 años y que el mail cuente con un @.
       (Ayuda: metodo in de list sirve tambien para strings)
    3. Editar la edad de un alumno verificando que este entre 10 y 18 años, se edita mediante el nombre.
    4. Ver lista de materias (Formato: Materias) (LISTO)
    5. Agregar materias al sistema (verificando que no exista previamente) (LISTO)
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
'''
import funciones as fn

Alumnos= [["maria", "camila"],[20, 18],["maria@ejemplo.com", "camila@ejemplo.com"]]
Materias= ["Química", "Física", "Matemática", "Lengua"]

while True:
    condicion=input( #le da a elegir opciones al usuario
    """\nPor favor indica la acción que deseas realizar:
        1.  Ver lista de alumnos
        2.  Agregar alumno
        3.  Editar la edad de un alumno
        4.  Ver lista de materias
        5.  Agregar materias al sistema
        6.  Salir
    Opcion: """)

    if condicion=="1":
        fn.lista_alumnos(Alumnos)
    elif condicion=="2":
        fn.agregar_alumno()
    elif condicion=="3":
        fn.editar_edad()
    elif condicion=="4":
        fn.lista_materias()
    elif condicion == "5":
        fn.agregar_materias()
    elif condicion == "6":
        print("\t Adiós!")
        break #sale del programa
    else:
        print("No ha seleccionado una opción correcta.") #le avisa al usuario si eligió una opción incorrecta
