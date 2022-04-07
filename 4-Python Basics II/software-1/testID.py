ID_LENGTH = 9

# usuario mete su id
while True:
    try:
        id = int(input("Escribe tu ID: \n"))
    except ValueError:
        print("Debes escribir un número, el ID no puede contener letras ni caracteres.")
        continue

    if len(str(id)) > ID_LENGTH:
        print("Debes escribir un ID valido, tienes numeros de mas.")
        continue

    if len(str(id)) < ID_LENGTH:
        print("Debes escribir un ID valido, al ID le faltan numeros.")
        continue
    
    print("ID valido, sigamos con lo que sigue...")
    break    
