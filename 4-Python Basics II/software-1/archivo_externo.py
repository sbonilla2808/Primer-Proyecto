from io import open

archivo_texto = open("Data_Bases","w")

frase1 = "Bienevenido a la Base de Datos \n"

ID_LENGTH = 9
# usuario introduce su id
print("Bienvenido, ingresa tu ID, el ID solo puede contener numeros. \n")

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

############################
archivo_texto.write(frase1)
archivo_texto.write(id)





archivo_texto.close()





