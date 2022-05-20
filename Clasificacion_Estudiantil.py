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

    def append_grade(self, row, grade):
        with open(self.filename, 'r') as dbfile:
            lines = dbfile.readlines()
            if row >=len(lines) or row<1:
                print(f"Invalid Row {row}, nothing done")
                return
            line = lines[row]
            columns = line.split(',')
            grades = columns[3:]
            if len(grades)>=5:
                print("No more grades allowed")
                return
            print("Grade Save")
            columns = columns[:-1]+ [str(grade), "\n"]
            lines[row] = ",".join(columns)
        with open(self.filename, 'w') as dbfile:
            dbfile.writelines(lines)

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
            

def insert_grade():
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
        if db.allows_more_grades(row) is None:
            print("No tiene suficientes notas para ser calificado")
        break
    
    with open("Excel_Bases.csv", 'r') as verifica:
        lines = verifica.readlines()
        line = lines[row]
        columns = line.split(',')
        grades = columns[3:]
        nota_1 = grades[0:1]
        nota_2 = grades[1:2]
        nota_3 = grades[2:3]
        nota_4 = grades[3:4]
            
    print(f"Invalid Row {nota_1}, {nota_2}, {nota_3}, {nota_4}, nothing done")
                
insert_grade()