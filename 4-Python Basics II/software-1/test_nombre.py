from io import open

print("\n")
print("Bienvenido, en este espacio debes registrar tu nombre, en el nombre solo se permiten letras. \n")

def new_func():

    while True:
        ####NOMBRE####
        nombre = str(input("Escriba su nombre: \n"))
        
        demas_letras = nombre[1::]
        primera_letra = nombre[0]

        #VALIDAR NUMEROS
        if nombre.isdigit():
            print("Solo se permiten letras")
            continue
        if nombre.isalpha():
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
    with open("excel_Bases.csv","a") as archivo_texto2: 
        archivo_texto2.write(str(nombre)+",")
new_func()

def new_func2():
    while True:
        ####APELLIDO####

        apellido = str(input("Escriba su apellido: \n"))
       
        demas_letras = apellido[1::]
        primera_letra = apellido[0]

        if apellido.isdigit():
            print("Solo se permiten letras")
            continue
        if apellido.isalpha():
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

    with open("excel_Bases.csv","a") as archivo_texto2: 
        archivo_texto2.write(str(apellido)+",")
new_func2()
