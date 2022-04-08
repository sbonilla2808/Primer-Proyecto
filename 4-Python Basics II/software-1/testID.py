ID_LENGTH = 9
# usuario introduce su id
print("\n Bienvenido, ingresa tu ID, el ID solo puede contener numeros. \n")
while True:
    try:
        id = int(input("Escribe tu ID: \n"))
    except ValueError:
        print("Solo se permiten numeros.")
        continue

    if id.isdigit():
        print("Solo se permiten letras")
        continue

    if id.isalpha():
        print("Solo se permiten numeros.")
        continue
    if id.isalnum():
        pass

    if len(str(id)) > ID_LENGTH:
        print("Incorrecto, tienes numeros de mas.")
        continue

    if len(str(id)) < ID_LENGTH:
        print("Incorrecto, te faltan numeros.")
        continue
    
    print("El ID es valido. Guardado.")
    break    