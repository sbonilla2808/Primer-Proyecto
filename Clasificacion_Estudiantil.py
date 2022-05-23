import re

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

    def allows_more_grades(self, row):
        with open(self.filename, 'r') as verifica:
            lines = verifica.readlines()
            line = lines[row]
            columns = line.split(',')
            grades = columns[3:]
            if len(grades)<2:
                return None
            if len(grades)>=5:
                return False
            

def llamadas_y_notas():
    row = -1
    db = Db('Excel_Bases.csv')
    while row < 1:
        cedula = Utils.ask_id()
        row = db.find_id_in_db(cedula)
        if db.find_id_in_db(cedula) is False:
            print(f'The id {cedula} was not found')
            continue
        print("Correct ID")
        pass
        db.allows_more_grades(row)
        if db.allows_more_grades(row) is False:
            break
        elif db.allows_more_grades(row) is None:
            print("No tiene suficientes notas para ser calificado.")
            break
    with open("Excel_Bases.csv", 'r') as verifica:
        lines = verifica.readlines()
        line = lines[row]
        columns = line.split(',')
        grades = columns[3:]
        notamax = sorted(grades[0:4])
        notas_altas = notamax[1:4]

        notas = []
        for nota_alta in notas_altas:
            notas.append(int(nota_alta))
        
        print(notas)
llamadas_y_notas()



