""" try:
    fichero = open("Algoritmos y estructuras de datos I.txt", 'r')#fichero = open ("archivo.txt",'r')
    print(fichero.read()) #para leer línea por línea
    fichero.close()
except:
    print("no existe el archivo") """ 


# lee el fichero caracter por caracter
try:
    fichero = open("Algoritmos y estructuras de datos I.txt", 'r')
    caracter = fichero.readline(1) #para leer caracter por caracter
    while caracter != "":
      print(caracter)
      caracter = fichero.readline(1)
    fichero.close()
except:
    print("no existe el archivo") 
    