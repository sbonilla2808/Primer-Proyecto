from io import open

archivo_texto = open("Data_Bases","r")

texto = archivo_texto.read()

archivo_texto.close()

print(texto)