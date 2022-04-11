
print("\n" "Bienvenido a la seccion de regristro, debes introducir un ID que ya este registrado en la base de datos.")

ID_LENGTH = 9
def bienid():
    file = open('excel_Bases.csv', 'r')

    lines = []

    for line in file:
        lines.append(line[:len(line)-0])
        #lines.append(line.split(","))
        #print(lines)

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






"""
file = open('excel_Bases.csv', 'r')

output = file.read()

print(output)

file.close()



file = open('excel_Bases.csv', 'r')

lines = []

for line in file:
    lines.append(line.split(","))
    print(line.split(","))


file.close()

print(lines)

#Reference: http://www.easypythondocs.com/fileaccess.html
"""