from io import open

consultar = ""
cedula = ""
nombre = ""
apellido = ""
nota = ""
print("\n" "Bienvenido, ingresa tu ID, el ID solo puede contener numeros. \n")

def broo():
    ID_LENGTH = 9
    while True :
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
    cedula = id

    print("\n" "Bienvenido, en este espacio debes registrar tu nombre, en el nombre solo se permiten letras. \n")

    while True:
        nuevo_nombre = str(input("Escriba su nombre: \n"))
        
        demas_letras = nuevo_nombre[1::]
        primera_letra = nuevo_nombre[0]

        #VALIDAR NUMEROS
        if nuevo_nombre.isdigit():
            print("Solo se permiten letras")
            continue
        if nuevo_nombre.isalpha():
            pass
        else:
            print("Solo se permiten letras.")
            continue

        #VALIDAR MAYUS_MINIS
        if not primera_letra.isupper():
            print("La primera letra debe ser mayuscula") 
            continue

        if not demas_letras.islower():
            print("Solo la primera letra puede ser mayuscula")
            continue
       
        if primera_letra.isupper and demas_letras.islower():
            print("Nombre guardado")
            break

    nombre = nuevo_nombre

    while True:
        nuevo_apellido = str(input("Escriba su apellido: \n"))
    
        demas_letras = nuevo_apellido[1::]
        primera_letra = nuevo_apellido[0]

        if nuevo_apellido.isdigit():
            print("Solo se permiten letras")
            continue
        if nuevo_apellido.isalpha():
            pass
        else:
            print("Solo se permiten letras.")
            continue

        #VALIDAR MAYUS_MINIS
        if not primera_letra.isupper():
            print("La primera letra debe ser mayuscula") 
            continue

        if not demas_letras.islower():
            print("Solo la primera letra puede ser mayuscula")
            continue
    
        if primera_letra.isupper and demas_letras.islower():
            print("Apellido guardado")
            break  
    apellido = nuevo_apellido

    with open("Excel_Bases.csv","a") as archivo_texto: 
        archivo_texto.write(str(cedula)+",")
        archivo_texto.write(str(nombre)+",")
        archivo_texto.write(str(apellido)+",")
        archivo_texto.write("\n")

broo()




