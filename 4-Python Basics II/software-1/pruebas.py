########################################################################################################################################


print("Bienvenido a este nuevo programa \n ")
print("Condiciones y privacidad: debes registrar tu informacion personal para continuar. (Tu informacion personal no sera compartida ni revlada a terceros, eso solo de uso oficial para este programa.)")
while True:
    print("                                              ")
    print("Aceptas las condiciones?, si es asi escribe: acepto. De lo contrario vuelve cuando estes listo. \n")
    print("                                              ")
    aceptas = input("Responde: ")
    acepto = "acepto"
    if aceptas == acepto:
        pass
    else:
        print("Debes aceptar para continuar.")
        continue


########################################################################################################################################


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


########################################################################################################################################
#######CONTRASEÑA#######


print("Debes crear una contraseña que por seguridad contenga tanto letras como numeros \n")
contraseña = input("Escribe tu nueva contraseña: \n")
print("Contraseña guardada, por favor no la olvides")


#####################################
id_guardado = id
#####################################
contraseña_guardada = contraseña
#####################################

########################################################################################################################################

print("Debes regist")

while True:
        a = str(input("Escriba su primer nombre: \n"))
        ###VARIABLES###
        demas_letras = a[1::]
        primera_letra = a[0]

        #VALIDAR NUMEROS
        if a.isalpha():
            pass
        else:
            print("No se permiten numeros ni espacios")
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


#############
nombre_guardado = a
#############

########################################################################################################################################

 





