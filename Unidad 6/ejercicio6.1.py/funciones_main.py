import Persona as pn
lista_personas = []

def crear_personas():
    while True: 
        dni = input("Por favor ingrese el dni: ") #pide dni
        if dni.isdigit():
            flag_agregar = True
            for persona in lista_personas:
                if dni == persona.dni:
                    print("ese dni ya existe")
                    flag_agregar = False
                    break
            if(flag_agregar): #significa que el dni es valido, puedo salir de su while
               break 
        else:
            print("El dni debe ser numérico")
    #nombre
    while True:
        nombre = input("Por favor ingrese el nombre: ").capitalize()
        if not nombre.isalpha():
            print("Un nombre no puede tener símbolos")
        else:
            break
    #apellido
    while True:
        apellido = input("Por favor ingrese el apellido: ").capitalize()
        if not apellido.isalpha():
            print("Un apellido no puede tener símbolos")
        else:
            break
    #edad
    while True:
        try:
            edad = int(input("Por favor ingrese la edad: "))
            if edad <= 0:
                print("La edad debe ser mayor a cero")
            else:
                break
        except:
            print("Error de argumentos")

    #residencia
    residencia = input("Por favor ingrese la residencia: ").capitalize()
    nombre_instancia = dni + nombre
    #instanciando o creando un objeto de persona
    nombre_instancia = pn.Persona(dni,nombre,apellido,edad,residencia)
    lista_personas.append(nombre_instancia)

def listar_personas():
    for persona in lista_personas:
        persona.presentarse()

def consultar_rango():
    print("------ Lista de personas------")
    for persona in lista_personas:
        print(f"{persona.dni}\t{persona.nombre}\t{persona.apellido}\t{persona.edad}\t")
    while True: #pide dni
        dni_consultar = input("Ingrese el dni a consultar o escriba 'fin' para salir: ")
        if dni_consultar == "fin":
            break
        elif dni_consultar.isdigit():
            for persona in lista_personas:
                if dni_consultar == persona.dni:
                    persona.rango_edad()
                    return
                else:
                    print("No existe ese DNI")
        else:
            print("El dni es numérico")