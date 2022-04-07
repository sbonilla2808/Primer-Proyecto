#Usuario Introduce Nombre
def new_func():

    while True:
        
        a = str(input("Escriba su nombre \n"))
        demas_letras = a[1::]
        primera_letra = a[0]
        
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