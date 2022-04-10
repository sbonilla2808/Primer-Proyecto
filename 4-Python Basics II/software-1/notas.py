


################
# valida el id #
################

from logging.config import IDENTIFIER


ID_LENGTH = 9
def bienid():

    with open("excel_Bases.csv","r") as archivo_texto2: 
        archivo_texto2.read()

    while True:
        try:
          id2 = str(int(input("Escribe tu ID: \n")))
        except ValueError:
          print("Solo se permiten numeros.")
          continue

        if len(str(id2)) > ID_LENGTH:
          print("Incorrecto, tienes numeros de mas.")
          continue

        if len(str(id2)) < ID_LENGTH:
          print("Incorrecto, te faltan numeros.")
          continue

        if id2 in archivo_texto2:
            print("ID correcto.")
            break
        else:
            print("ID invalido, el ID no esta en la base de datos.")
            continue

bienid()





##############NOTAS########################### 

archivo_texto2 = open("excel_Bases.csv","a")
# usuario introduce su id
print("\n Bienvenido a la seccion de notas, las notas solo pueden contener numeros entre 0 y 100. \n")

#########NOTA 1
while True:
    try:
        notas1 = str(int(input("Inserte la nota: \n")))
    except ValueError:
        print("Solo se permiten numeros.")
        continue

    if int(notas1) < 0:
        print("Nota invalida.")
        continue

    if int(notas1) == 0:
        print("Nota guardada.")
        break

    if int(notas1) > 100:
        print("Nota invalida.")
        continue

    else:
        print("Nota guardada")
        break

#########NOTA 2
while True:
    try:
        notas2 = str(int(input("Inserte la nota: \n")))
    except ValueError:
        print("Solo se permiten numeros.")
        continue

    if int(notas2) < 0:
        print("Nota invalida.")
        continue

    if int(notas2) == 0:
        print("Nota guardada.")
        break

    if int(notas2) > 100:
        print("Nota invalida.")
        continue

    else:
        print("Nota guardada")
        break

#########NOTA 3
while True:
    try:
        notas3 = str(int(input("Inserte la nota: \n")))
    except ValueError:
        print("Solo se permiten numeros.")
        continue

    if int(notas3) < 0:
        print("Nota invalida.")
        continue

    if int(notas3) == 0:
        print("Nota guardada.")
        break

    if int(notas3) > 100:
        print("Nota invalida.")
        continue

    else:
        print("Nota guardada")
        break

#########NOTA 4
while True:
    try:
        notas4 = str(int(input("Inserte la nota: \n")))
    except ValueError:
        print("Solo se permiten numeros.")
        continue

    if int(notas4) < 0:
        print("Nota invalida.")
        continue

    if int(notas4) == 0:
        print("Nota guardada.")
        break

    if int(notas4) > 100:
        print("Nota invalida.")
        continue

    else:
        print("Nota guardada")
        break

with open("excel_Bases.csv","a") as archivo_texto: 
   
    texto2 = archivo_texto2.write(notas1)
    texto2 = archivo_texto2.write(notas2)
    texto2 = archivo_texto2.write(notas3)
    texto2 = archivo_texto2.write(notas4)

