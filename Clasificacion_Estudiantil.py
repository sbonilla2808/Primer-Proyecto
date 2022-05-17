
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

    @staticmethod
    def ask_grade():
        grade_correct = False
        while not grade_correct:
            try:
                grade = int(input("Write the note: \n"))
            except ValueError:
                print("Only numbers are allowed.")
                continue

            if not (0<=grade<=100):
                print("Wrong, the note only goes from 0 to 100.")
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
            print(f'columns {columns}')
            lines[row] = ",".join(columns)
        with open(self.filename, 'w') as dbfile:
            dbfile.writelines(lines)

    def allows_more_grades(self, row):
        with open(self.filename, 'r') as verifica:
            lines = verifica.readlines()
            line = lines[row]
            columns = line.split(',')
            grades = columns[3:]
            if len(grades) < 3:
                return None
            if len(grades)>=5:
                return False
            return True

#########Escoge las notas mas altas
    #Evaluate Nota 1:
    def evaluate_grade_1(self, row):
        with open(self.filename, "r") as verifica:
            lines = verifica.readlines()
            line = lines[row]
            columns = line
            grades = columns[3:]
            nota_1 = grades[22:24]
            nota_2 = grades[25:27]
            nota_3 = grades[28:30]
            nota_4 = grades[31:33]
        a = True
        b = True
        c = True
        if nota_1 > nota_2:
            return a
        if nota_1 > nota_3:
            return b
        if nota_1 > nota_4:
            return c
        else:
            return False
    
    #Evaluate Nota 2
    def evaluate_grade_2(self, row):
        with open(self.filename, "r") as verifica:
            lines = verifica.readlines()
            line = lines[row]
            columns = line
            grades = columns[3:]
            nota_1 = grades[22:24]
            nota_2 = grades[25:27]
            nota_3 = grades[28:30]
            nota_4 = grades[31:33]
        a = True
        b = True
        c = True
        if nota_2 > nota_1:
            return a
        if nota_2 > nota_3:
            return b
        if nota_2 > nota_4:
            return c
        else:
            return False

    def evaluate_grade_3(self, row):
        with open(self.filename, "r") as verifica:
            lines = verifica.readlines()
            line = lines[row]
            columns = line
            grades = columns[3:]
            nota_1 = grades[22:24]
            nota_2 = grades[25:27]
            nota_3 = grades[28:30]
            nota_4 = grades[31:33]

        a = True
        b = True
        c = True
        if nota_3 > nota_1:
            return a
        if nota_3 > nota_2:
            return b
        if nota_13 > nota_4:
            return c
        else:
            return False

    def evaluate_grade_4(self, row):
        with open(self.filename, "r") as verifica:
            lines = verifica.readlines()
            line = lines[row]
            columns = line
            grades = columns[3:]
            nota_1 = grades[22:24]
            nota_2 = grades[25:27]
            nota_3 = grades[28:30]
            nota_4 = grades[31:33]

        a = True
        b = True
        c = True
        if nota_3 > nota_1:
            return a
        if nota_3 > nota_2:
            return b
        if nota_13 > nota_4:
            return c
        else:
            return False


##########Llamada las Def():
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
        
        if db.allows_more_grades(row) is False:
            print(f"Verificando notas ")
            break
        elif db.allows_more_grades(row) is True:
            pass
        elif db.allows_more_grades(row) is None:
            print("No se puede calificar por que tiene menos de 3 notas")
            break
        nota = Utils.ask_grade() 
        db.append_grade(row, nota)

    ####grades####
    db.evaluate_grade_1(row)
    db.evaluate_grade_2(row)  
    db.evaluate_grade_3(row)
    db.evaluate_grade_4(row)

    a = True
    b = True
    c = True
    while True:
        #Nota 1 vs 2::
        if db.evaluate_grade_1(row) == a:
            print("La Nota 1 es mayor que la Nota 2.")
            pass
        else:
            print("La nota 2 es mayor que la 1")
            pass

        if db.evaluate_grade_1(row) == b:
            print("La Nota 1 es mayor que la Nota 3.")
            pass
        else:
            print("La nota 3 es mayor que la 1")
            pass

        if db.evaluate_grade_1(row) == c:
            print("La Nota 1 es mayor que la Nota 4.")
            pass
        else:
            print("La nota 4 es mayor que la 1")
            pass

        #Nota 2 vs 1::
        if db.evaluate_grade_1(row) == a:
            print("La Nota 2 es mayor que la Nota 1.")
            pass
        else:
            print("La nota 1 es mayor que la 2")
            pass

        if db.evaluate_grade_1(row) == b:
            print("La Nota 2 es mayor que la Nota 3.")
            pass
        else:
            print("La nota 3 es mayor que la 2")
            pass

        if db.evaluate_grade_1(row) == c:
            print("La Nota 2 es mayor que la Nota 4.")
            pass
        else:
            print("La nota 4 es mayor que la 2")
            pass

        #Nota 3 vs 1::
        if db.evaluate_grade_1(row) == a:
            print("La Nota 3 es mayor que la Nota 1.")
            pass
        else:
            print("La nota 1 es mayor que la 3")
            pass

        if db.evaluate_grade_1(row) == b:
            print("La Nota 3 es mayor que la Nota 2.")
            pass
        else:
            print("La nota 2 es mayor que la 3")
            pass

        if db.evaluate_grade_1(row) == c:
            print("La Nota 3 es mayor que la Nota 4.")
            pass
        else:
            print("La nota 4 es mayor que la 3 ")
            pass

        #Nota 4 vs 1::
        if db.evaluate_grade_1(row) == a:
            print("La Nota 4 es mayor que la Nota 1.")
            pass
        else:
            print("La nota 1 es mayor que la 4")
            pass

        if db.evaluate_grade_1(row) == b:
            print("La Nota 4 es mayor que la Nota 2.")
            pass
        else:
            print("La nota 2 es mayor que la 4")
            pass

        if db.evaluate_grade_1(row) == c:
            print("La Nota 4 es mayor que la Nota 3.")
            pass
        else:
            print("La nota 3 es mayor que la 4")
            pass
        break

insert_grade()
