print("##############################################")
print("                                              ")


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
    
    print("El ID es valido. Guardado.")
    break    



print("##############################################")
print("                                              ")

 
def new_func():

    while True:
        a = str(input("Escriba su nombre: \n"))
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


print("##############################################")
print("                                              ")

 