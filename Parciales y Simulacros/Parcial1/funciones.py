Alumnos= [["maria", "camila"],[20, 18],["maria@ejemplo.com", "camila@ejemplo.com"]]
Materias= ["Química", "Física", "Matemática", "Lengua"]

def lista_alumnos(Alumnos):
    print("\t------------------------------------")
    print("\t| Alumno |  Edad  |      Mail      |")
    print("\t------------------------------------")
    for i in range(len(Alumnos[0])):
        print(f"\t{Alumnos[0][i]}   -   {Alumnos[1][i]}  -  {Alumnos[2][i]}") #se muestran todas las listas que están dentro de la lista grande

def agregar_alumno():
    while True:
        alumno= input("Ingrese el nombre del alumno: ")
        if alumno.isalpha(): #verifica que no ingrese símbolos
            if alumno not in Alumnos[0]: #si ese nombre no se encuentra repetido lo agrega
                Alumnos[0].append(alumno) #lo agrega a la lista con su usuario
                print(f"Se ingresó {alumno} a la lista")
                while True:
                    try:
                        edad= int(input("Ingrese la edad entre 10 y 18 años: "))
                        if edad >= 10 and edad <= 18: #verifica el rango de edad solicitado
                            Alumnos[1].append(edad) #lo agrega a la lista con su edad
                            print(f"Se ingresó la edad {edad} del alumno {alumno} a la lista")
                            break
                        else:
                            print("No puedes ingresar edades en ese rango")
                    except:
                        print("Error")
                            
                while True:
                    try:
                        mail= input("Ingrese el email: ")
                        if "@" not in mail: #verifica que ingrese un @ en el campo email
                            print("Debes ingresar un correo válido")
                        else:
                            Alumnos[2].append(mail) #lo agrega a la lista con su email
                            print(f"Se ingresó correctamente el mail {mail} del alumno {alumno} a la lista")
                            print("Su lista nueva es: ")
                            lista_alumnos(Alumnos) #llama al método que lista a los alumnos
                            break
                    except:
                        print("Error")
                break              
            else:
                print("Ese alumno ya se encuentra registrado")
        else:
            print("No puedes ingresar símbolos ni números")
    
def lista_materias():
    print("\t------------")
    print(f"\t| Materias  |")
    print("\t------------")
    for i in range(len(Materias)): #recorre la lista Materias
        print (f"\t {Materias[i]}") #Muestra los elementos de la lista uno abajo del otro

def editar_edad():
    while True:
        alumno = input("Nombre del alumno a modificar la edad: ")
        if alumno in Alumnos[0]: #verifica que el nombre del alumno ingresado se encuentre en los nombres alumnos
            while True: #si se encuentra en la lista ingresa al while para modificar la edad
                try:
                    edad= int(input("Ingrese la edad nueva: "))
                    if edad > 9 and edad < 19: #comprueba el rango de edad solicitado
                        Alumnos[1][Alumnos[0].index(alumno)] = edad #cambia la edad del alumno indicado por la nueva edad ingresada
                        print(f"Se modifico con éxito la edad. Tu nueva lista es:")
                        lista_alumnos(Alumnos)
                        break
                    else:
                        print("No puedes ingresar edades en ese rango")   
                except:
                    print("Debe ingresar un valor numerico")
            break
        else:
            print("No existe ese alumno")
        

def agregar_materias():
    while True:
        try:
            materia= input("Ingrese la materia o escribe fin para terminar: ").capitalize()
            if materia.isalpha(): #sacar en caso de que ingrese materias con más de una palabra
                if materia not in Materias: #verifica que la materia no se encuentre ya en la lista
                    Materias.append(materia) #si no se encuentra en la lista la agrega
                    print(f"Se ingresó {materia} con éxito a la lista. Tu nueva lista de materias es: ")
                    lista_materias()
                    break
                elif materia == "fin":
                    break
                else:
                    print("Esa materia ya se encuentra")
            else:
                print("No puedes ingresar símbolos ni números")   
        except:
            print("Dato erroneo")

