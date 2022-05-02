
name = input("What is your name: ")
edad = int(input("Edad: "))
cedu = input("numero de ID: ")
a = [
     "nombre:", name,
     "ID", cedu,
     "edad:", edad,
]
EDAD_A = 18
while True:
    if int(edad) < EDAD_A:
        print("Eres menor de edad, el programa no puede seguir.")
        break
    else:
        pass
    c = str(input("What is your name: "))
    if c in a:
        print("Right")
        pass
    else:
        print("Wrong")
        continue
    d = str(input("What is your ID: "))
    if d in a:
        print("Right")
        break
    else:
        print("Wrong")
        continue
        
