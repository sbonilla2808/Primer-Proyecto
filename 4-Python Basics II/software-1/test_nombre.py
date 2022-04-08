print("\n Bienvenido, en este espacio debes registrar tu nombre, en el nombre solo se permiten letras. \n")

def new_func():

    while True:
        a = str(input("Escriba su nombre: \n"))
        ###VARIABLES###
        demas_letras = a[1::]
        primera_letra = a[0]

        #VALIDAR NUMEROS
        if a.isdigit():
            print("Solo se permiten letras")
            continue
        if a.isalpha():
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

new_func()