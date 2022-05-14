
class Utils():

    @staticmethod
    def ask_id():
        id_correct = False
        while not id_correct:
            try:
                user_id = int(input("Escribe el ID del estudiante: \n"))
            except ValueError:
                print("Solo se permiten numeros.")
                continue

            if user_id > 999999999:
                print("Incorrecto, tienes numeros de mas.")
                continue

            if user_id < 100000000:
                print("Incorrecto, te faltan numeros.")
                continue
            id_correct = True
        return str(user_id)

    @staticmethod
    def ask_grade():
        grade_correct = False
        while not grade_correct:
            try:
                grade = int(input("Escribe la nota: \n"))
            except ValueError:
                print("Solo se permiten numeros.")
                continue

            if not (0<=grade<=100):
                print("Incorrecto, la nota solo va de 0 a 100.")
                continue

            grade_correct = True
        return grade


class Db():

    def __init__(self, filename):
        self.filename = filename

    
    def find_id_in_db(self, cedula):
        with open(self.filename, 'r') as dbfile:
            row = 0
            lines = dbfile.readlines()
            for line in lines:
                #print(line)
                columns = line.split(',')
                #print(columns)
                if cedula==columns[0]:
                    return row
                row += 1
            return False
            row = -1
            return row

    def append_grade(self, row, grade):
        with open(self.filename, 'r') as dbfile:
            lines = dbfile.readlines()
            if row >=len(lines) or row<1:
                print(f"invalid Row {row}, nothing done")
                return
            line = lines[row]
            columns = line.split(',')
            grades = columns[3:]
            if len(grades)>=5:
                print("no more grades allowed")
                return
            print("Grade Save")
            columns = columns[:-1]+ [str(grade), "\n"]
            #print(f'columns {columns}')
            lines[row] = ",".join(columns)
        with open(self.filename, 'w') as dbfile:
            dbfile.writelines(lines)

    def allows_more_grades(self, row):
        with open(self.filename, 'r') as verifica:
            lines = verifica.readlines()
            line = lines[row]
            columns = line.split(',')
            grades = columns[3:]
            if len(grades)>=5:
                return False
            return True



def insert_grade():
    row = -1
    db = Db('Excel_Bases.csv')
    while row < 1:
        cedula = Utils.ask_id()
        row = db.find_id_in_db(cedula)
        if db.find_id_in_db(cedula) is False:
            print(f'The id {cedula} was not found')
            break
        print("Correct ID")
        pass
        db.allows_more_grades(row)
        if db.allows_more_grades(row) is False:
            print("No more grades"[::1])
            break
        elif db.allows_more_grades(row) is True:
            pass
        nota = Utils.ask_grade() 
        db.append_grade(row, nota)
    
insert_grade()
