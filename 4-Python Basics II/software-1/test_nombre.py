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




"""
n = 0



while True:
    try:
        nombre = int(input("Escribe tu nombre \n"))
    except ValueError:
        print("Debes escribir un nombre valido, el nombre no puede contener numeros ni caracteres.")
        continue

    if (id) > n:
        print("Los numeros no son validos.")
        continue

    if (id) < n:
        print("Los numeros no son validos.")
        continue
    
    print("Nombre guardado")
    break    
"""

 