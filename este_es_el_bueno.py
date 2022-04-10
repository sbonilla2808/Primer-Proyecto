#########imprimir######################

from io import open

archivo_texto = open("excel_Bases.csv","a")


ID_LENGTH = 9
# usuario introduce su id
print("\n Bienvenido, ingresa tu ID, el ID solo puede contener numeros. \n")
while True:
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


archivo_texto.write(id)



###########################################################



  
print("\n Bienvenido, en este espacio debes registrar tu nombre, en el nombre solo se permiten letras. \n")

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
        
    archivo_texto.write(nombre)

new_func()


###################################


def new_func2():
    while True:
                ####APELLIDO####

        apellido = str(input("Escriba su apellido: \n"))
        ###VARIABLES###
        demas_letras = apellido[1::]
        primera_letra = apellido[0]

        #VALIDAR NUMEROS
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

    archivo_texto.write(apellido)  

new_func2()

archivo_texto.close()

#######################################
#valida el id
########REAAAAD########################

imprime = open("excel_Bases.csv","r")

texto = imprime.read()

def bienid():
    while True:
        try:
          id2 = str(int(input("Escribe tu ID: \n")))
        except ValueError:
          print("Solo se permiten numeros.")
          continue

        if len(str(id2)) > ID_LENGTH:
          print("Incorrecto, tienes numeros de mas.")
          continue

        if len(str(id2)) < ID_LENGTH:
          print("Incorrecto, te faltan numeros.")
          continue

        if id2 in texto:
            print("ID correcto.")
            break
        else:
            print("ID invalido, el ID no esta en la base de datos.")
            continue

imprime.close()
bienid()


##############NOTAS########################### 

archivo_texto2 = open("excel_Bases.csv","a")

NOTA_LENGTH = 0
NOTA_2 = 100
# usuario introduce su id
print("\n Bienvenido a la seccion de notas, las notas solo pueden contener numeros entre 0 y 100. \n")

while True:
    try:
        notas = str(int(input("Inserte la nota: \n")))
    except ValueError:
        print("Solo se permiten numeros.")
        continue

    if int(notas) < 0:
        print("Nota invalida.")
        continue

    if int(notas) == 0:
        print("Nota guardada.")
        break

    if int(notas) > 100:
        print("Nota invalida.")
        continue

    else:
        print("Nota guardada")
        break

    #if not (notas) in archivo_texto2:
        #pass
    #else:
        #print("No se permiten mas notas, espacios llenos")

texto2 = archivo_texto2.write(notas)

archivo_texto2.close()