# usuario mete su nombre

def new_func():

    while True:
        
        a = str(input("Escriba su nombre \n"))

        primera_letra = a[0]
        if not primera_letra.isupper():
            print("La primera letra debe ser mayuscula") 
            continue

        demas_letras = a[:1]
        if demas_letras.isupper():
            print("Solo la primera letra puede ser mayuscula") 
            continue

        if a.isupper():
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

 