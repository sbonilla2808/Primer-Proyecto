####################################################################
#print("\n" "Bienvenido a la seccion de regristro, debes introducir un ID que ya este registrado en la base de datos.")

ID_LENGTH = 9
def bienid():
    file = open('Excel_Bases.csv', 'r')

    lines = []

    for line in file:
        lines.append(line[:len(line)-0])
        lines.append(line.split(","))
        columns = line.split(',')
        grades = columns[3:7]
        print(grades)
        if len(grades)>=5:
            print("Hay 5 notas")
            return
        if len(grades)<=3:
            print("no tiene suficientes notas")
            break
        else:
            pass
        

bienid()
"""
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

        if id2 in lines[1]:
            print("ID correcto.")
            break
        else:
            print("ID invalido, el ID no esta en la base de datos.")
            continue

    file.close()

bienid()
####################################################################

##############NOTAS########################### 

archivo_texto2 = open("excel_Bases.csv","a")
# usuario introduce su id
print("\n" "Bienvenido a la seccion de notas, las notas solo pueden contener numeros entre 0 y 100. \n" )

#########NOTA 1##############
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

with open("excel_Bases.csv","a") as archivo_texto: 
    texto2 = archivo_texto2.write(str(notas1)+",")



"""
