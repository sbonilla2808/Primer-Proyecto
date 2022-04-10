from io import open

ID_LENGTH = 9
# usuario introduce su id

print("\n" "Bienvenido, ingresa tu ID, el ID solo puede contener numeros. \n")
while True:
    try:
        id = str(int(input("Escribe tu ID: \n")))
    except ValueError:
        print("Solo se permiten numeros.")
        continue

    if len(str(id)) > ID_LENGTH:
        print("Incorrecto, tienes numeros de mas.")
        continue

    if len(str(id)) < ID_LENGTH:
        print("Incorrecto, te faltan numeros.")
        continue
    
    print("El ID es valido. Guardado.")
    break    

with open("excel_Bases.csv","a") as archivo_texto: 
    archivo_texto.write(str(id)+",")

