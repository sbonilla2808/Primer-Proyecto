class Utils():

    @staticmethod
    def ask_id():
        id_correct = False
        while not id_correct:
            try:
                user_id = int(input("Write the student id to be evaluate: \n"))
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

    def verifica_grades(self, row):
        with open(self.filename, 'r') as verifica:
            lines = verifica.readlines()
            line = lines[row]
            columns = line.split(',')
            grades = columns[3:]
            if len(grades) <=3:
                return None
            if len(grades)>=3:
                return False
            return True

    def evaluate_grades(self, row):
        with open(self.filename, "r") as verifica:
            lines = verifica.readlines()
            line = lines[row]
            columns = line
            grades = columns[3:]
            nota_1 = grades[22:24]
            nota_2 = grades[25:27]
            nota_3 = grades[28:30]
            nota_4 = grades[31:33]

        if nota_1 > nota_2 and nota_1 > nota_3 and  nota_4 < nota_1:
            return True

        # 1 < x < 20
        #     True:
        #     return True
        # else:
        #     False


def valida_id_y_notas():
    row = -1
    db = Db('Excel_Bases.csv')
    while row < 1:
        cedula = Utils.ask_id()
        row = db.find_id_in_db(cedula)
        if db.find_id_in_db(cedula) is False:
            print(f'The id {cedula} was not found')
            continue
        print("Correct ID")
        if db.verifica_grades(row) is False:
            print("Verificando Notas")
            pass
        elif db.verifica_grades(row) is None:
            print("No tiene suficientes notas para ser calificado.")
            break

valida_id_y_notas()

def notas_altas():
    row = 1
    db = Db('Excel_Bases.csv')
    db.evaluate_grades(row)
    if db.evaluate_grades is True:
        print("si es mayor")
    else:
        print("Es menor")
notas_altas()