def new_func():

    while True:
        a = str(input("Escriba su nombre \n"))
        ###VARIABLES###
        demas_letras = a[1::]
        primera_letra = a[0]

        #VALIDAR NUMEROS
        if a.isalpha():
            pass
        else:
            print("No se permiten numeros")
        #VALIDAR MAYUS_MINIS
        if not primera_letra.isupper():
            print("La primera letra debe ser mayuscula") 
            continue

        if not demas_letras.islower():
            print("Solo la primer letra puede ser mayuscula")
            continue
       
        if primera_letra.isupper and demas_letras.islower():
            print("Nombre guardado")
            break      

new_func()