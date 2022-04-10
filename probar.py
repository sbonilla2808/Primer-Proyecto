
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



