from io import open

consultar = ""
cedula = ""
nombre = ""
apellido = ""
print("Welcome, enter your ID, the ID can only contain numbers. \n")

def registro():
    ID_LENGTH = 9
    while True :
        try:
            id = str(int(input("Write the student ID: \n")))
        except ValueError:
            print("Only numbers are allowed.")
            continue

        if len(str(id)) > ID_LENGTH:
            print("Wrong, you have extra numbers.")
            continue

        if len(str(id)) < ID_LENGTH:
            print("Wrong, you are missing numbers")
            continue
        
        print("The ID is valid. Saved.")
        break    
    cedula = id

    print("\n" "Welcome, in this space you must register your name, only letters are allowed in the name. \n")

    while True:
        nuevo_nombre = str(input("Write your name: \n"))
        
        demas_letras = nuevo_nombre[1::]
        primera_letra = nuevo_nombre[0]

        #VALIDAR NUMEROS
        if nuevo_nombre.isdigit():
            print("Only letters are allowed")
            continue
        if nuevo_nombre.isalpha():
            pass
        else:
            print("Only letters are allowed.")
            continue

        #VALIDAR MAYUS_MINIS
        if not primera_letra.isupper():
            print("The first letter must be uppercase") 
            continue

        if not demas_letras.islower():
            print("Only the first letter can be capitalized")
            continue
       
        if primera_letra.isupper and demas_letras.islower():
            print("Name Save")
            break

    nombre = nuevo_nombre

    while True:
        nuevo_apellido = str(input("Write your lastname: \n"))
    
        demas_letras = nuevo_apellido[1::]
        primera_letra = nuevo_apellido[0]

        if nuevo_apellido.isdigit():
            print("Only letters are allowed")
            continue
        if nuevo_apellido.isalpha():
            pass
        else:
            print("Only letters are allowed.")
            continue

        #VALIDAR MAYUS_MINIS
        if not primera_letra.isupper():
            print("The first letter must be uppercase") 
            continue

        if not demas_letras.islower():
            print("Only the first letter can be capitalized")
            continue
    
        if primera_letra.isupper and demas_letras.islower():
            print("Lastname Save")
            break  
    apellido = nuevo_apellido

    with open("Excel_Bases.csv","a") as archivo_texto: 
        archivo_texto.write(str(cedula)+",")
        archivo_texto.write(str(nombre)+",")
        archivo_texto.write(str(apellido)+",")
        archivo_texto.write("\n")
registro()