'''
************************************************************
 MATERIA: Algoritmos y Estructuras de Datos 1
 EXAMEN: 2° Examen
 APELLIDO Y NOMBRE: Ludueña María Emilia
 DNI: 37093663
 CARRERA: Analista de Sistemas
 AÑO: 2021 
 Se envía mail con asunto: "[AYEDI 2021 - Apellido, Nombre - 2°Examen]" COMPRMIIR EN CARPETA [Apellido,Nombre 2_examen]
 ************************************************************
 Ítems a evaluar:
 1. Contenidos de la materia
 2. Requerimientos y comprensión de consignas
 3. Estructura (modularización), legibilidad y comentarios del código.

¡Cualquier duda con el enunciado consultar al docente!
************************************************************
ENUNCIADO: "Programa de Agenda"

Introducción: 
    El siguiente programa consiste en un software que simule una agenda personal.
    El programa debe permitir agregar y quitar Eventos al sistema, como también gestionar datos del evento (Fecha, Hora, Lugar).

Requerimientos:
El programa debe:
*   Contar con una Clase Evento con los atributos (nombre_evento (único), fecha, hora, lugar)
*   Contar con dos Clases Hijas que use el constructor de la clase padre pero que tenga un atributo más:
        - EventoPersonal (Atributo: organizador (nombre del grupo que organiza))
        - EventoLaboral (Atributo: obligatorio "True o False" (por defecto = True))
        
*   Se deben crear 4 métodos para la clase padre Evento (que heredaran las clases hijas):
        1. Mostrar información: Que indique el nombre_evento, fecha y lugar del evento 
        2. Obtener tipo de evento (tipo de clases heredadas o padre)
        3. Setear Fecha y Hora (Setearán la Fecha y Hora en una misma función)
        4. Setear lugar (Setear el lugar)

*   Se debe crear una clase GestorEvento que cuente con las siguientes funciones para un menu:

    1.  Crear instancias de un evento y guárdalos en una lista de eventos. 
        1.1) Se debe verificar que tipo de instancia de evento a crear y los parámetros. IMPORTANTE!: clase hijas verificar y pedir parámetros
             - nombre_evento: debe ser único
             - Fecha: formato (dd/mm/yyyy) -> únicamente verificar la longitud del string = 10 
             - Hora: formato (hh:mm) -> no es necesario verificar
             - Lugar: sin formato especifico, no es necesario verificar
        1.2) Al crear un evento es necesario logearlo (Escribir en una línea nueva: nombre_evento-Fecha-Hora-Lugar-Tipo_de_evento(tipo de clase)) 
             en un archivo llamado lista_eventos.txt (Crear función en el mismo gestor). IMPORTANTE!: verificar permisos
        1.3) En caso que la instancia del evento sea EventoPersonal.
             - Para el organizador, el usuario debe elegir a través de una clave (mostradas por el programa) 
                desde un diccionario de organizadores.
             - En caso que no exista el organizador deseado debe ser "incognito" (AYUDA: Funcion get de diccionarios)
    2.   Listar eventos disponibles, leyendo la lista_evetos.txt. IMPORTANTE!: recorrer el archivo, no la lista. 
    3.   Cambiar el lugar de un evento, seleccionando su nombre. (Hacer check correspondientes)
    
*   Se deben crear los métodos correspondientes para las funciones del menú en las clases correspondientes
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
'''
organizadores = {
    "FA":"familia", 
    "AM": "amigos",
    "PR": "propio"
    }

import GestorEvento as ge
gestor = ge.GestorEvento()

while True:
    opcion = input(
    """
-----------MENU PRINCIPAL-----------
Por favor ingrese una opcion:
    1. Crear un evento
    2. Listar eventos
    3. Cambiar lugar del evento
    4. Salir
Numero: """
    )
    if (opcion=="1"):
        gestor.crear_evento()
    elif (opcion=="2"):
        gestor.listar_eventos()
    elif (opcion=="3"):
        gestor.cambiar_lugar()
    elif (opcion=="4"):
        print("¡Adiós!")
        break