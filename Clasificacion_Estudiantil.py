import re
from io import open 

class Utils():

    @staticmethod
    def ask_id():
        id_correct = False
        while not id_correct:
            try:
                user_id = int(input("Write the student ID: \n"))
            except ValueError:
                print("Only numbers are allowed.")
                continue

            if user_id > 999999999:
                print("Wrong, you have extra numbers.")
                continue

            if user_id < 100000000:
                print("Wrong, you are missing numbers.")
                continue
            id_correct = True
        return str(user_id)

class Db():

    def __init__(self, filename):
        self.filename = filename
    
    def find_id_in_db(self, cedula):
        with open(self.filename, 'r') as dbfile:
            row = 0
            lines = dbfile.readlines()
            for line in lines:
                columns = line.split(',')
                if cedula==columns[0]:
                    return row
                row += 1
            return False
            row = -1
            return row

    def contador_de_notas(self, row):
        with open(self.filename, 'r') as verifica:
            lines = verifica.readlines()
            line = lines[row]
            columns = line.split(',')
            grades = columns[3:]
        COMPARA = 3
        if len(grades) <= COMPARA:
            return False
        if len(grades)> COMPARA:
            return True
    
    def promedio(self, row):
        with open(self.filename, 'r') as verifica:
            lines = verifica.readlines()
            line = lines[row]
            columns = line.split(',')
            grades = columns[3:]
            notamax = sorted(grades[0:4])
            notas_altas = notamax[1:4]
            total = 0
            for nota_alta in notas_altas:
                total += int(nota_alta)
            promedio_1 = total/3
        return promedio_1
    
    def califica_estudiante(self, row, promedio):
        db = Db('Excel_Bases.csv')
        db.promedio(row)
        REPROBADO = 55
        CONVOCATORIA = 56 # DEL 56 AL 65 
        APROBADO = 65
        if promedio <= REPROBADO:
            print("REPROBADO")
            return False # FALSE == REPROBADO
        if promedio > CONVOCATORIA:
            if promedio < APROBADO:
                print("CONVOCATORIA")
                return None # NONE == CONVOCATORIA
        if promedio >= APROBADO:
            print("APROVADO")
            return True # TRUE == APROBADO
            

    def append_promedio(self, row, promedio):
        db = Db('Excel_Bases.csv')
        db.promedio(row)
        with open(self.filename, 'r') as dbfile:
            lines = dbfile.readlines()
            line = lines[row]
            columns = line.split(",")
            COMPARA = 8
            if len(columns) < COMPARA:
                columns = columns[:6]+ [""]
            if len(columns) >= COMPARA:
                pass
            columns = columns[0:7]+ [str(float(promedio)), "\n"]
            lines[row] = ",".join(columns)
        with open(self.filename, 'w') as dbfile:
            dbfile.writelines(lines)
    
    #def append_calificacion():

def valida_id():
    row = -1
    db = Db('Excel_Bases.csv')
    while row < 1:
        cedula = Utils.ask_id()
        row = db.find_id_in_db(cedula)
        if db.find_id_in_db(cedula) is False:
            print(f'The id {cedula} was not found')
            continue
        pass
        db.contador_de_notas(row)
        promedio = db.promedio(row)
        if db.contador_de_notas(row) is True:
            print(f"El promedio es: {promedio}")
            pass
        if db.contador_de_notas(row) is False:
            print("No tiene suficientes notas para ser calificado.")
            break
        db.append_promedio(row, promedio)
        db.califica_estudiante(row, promedio)
valida_id()
