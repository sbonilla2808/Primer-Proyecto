import os

o_esto = os.listdir("archivos/")
print(o_esto)

def new_func():
    option_1 = 1
    option_2 = 2

    while True:
        print("Escribe el numero correspondiente segun lo que quieres hacer")
        try:
            a = str(int(input("Que quires hacer:\n (1) Buscar un archivo por nombre. \n (2) Ver todos los archivos \n")))
        except ValueError:
            print("Solo se permiten numeros.")
            continue

        if not str(int(a)) == 2:
            print("Incorrecto, el numero no esta en las opciones.")
            continue

        if not str(int(a)) == 1:
            print("Incorrecto, el numero no esta en las opciones.")
            continue

        if a == option_1:
            b = input("Escribe el nombre del archivo: \n")

            #nombre_archivo = "archivos/proba_1.txt"
            #print(os.path.isfile(nombre_archivo))
            break

        if a == option_2:
            b = input("Escribe el nombre del archivo: \n")
            nombre_archivo = "archivos/proba_1.txt", "archivos/proba_2.proba_2.txt", "archivos/proba_3.proba_3.txt"
            print(os.path.isfile(nombre_archivo))
            break
        find()
            
new_func()