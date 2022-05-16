#################################################################################
class Utils():

    @staticmethod
    def ask_id():
        id_correct = False
        while not id_correct:
            try:
                user_id = int(input("Write the ID of the student you want to evaluate: \n"))
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
                #print(line)
                columns = line.split(',')
                #print(columns)
                if cedula==columns[0]:
                    return row
                row += 1
            return False
            row = -1
            return row

def insert_grade():
    row = -1
    db = Db('Excel_Bases.csv')
    while row < 1:
        cedula = Utils.ask_id()
        row = db.find_id_in_db(cedula)
        if db.find_id_in_db(cedula) is False:
            print(f'The id {cedula} was not found')
            break
        print("ID Found.")
        pass
    
insert_grade()

####################################################################################
file1 = open("Excel_Bases.csv", "r")
leer = file1.read()
lines = file1.readlines()
line = leer
columns = line.split(',')
grades = columns[3:]

file1.close()
####################################################################################
def bienid():
    base = open('Excel_Bases.csv', 'r')

    lines = []

    for line in base:
        lines.append(line[:len(line)-0])
        lines.append(line.split(","))
        columns = line.split(',')
        grades = columns[3:7]
        if len(grades)>=5:
            print("Hay 4 notas")
            break
    base.close()

bienid()
#####################################################################################

# 
# 
# class Utils():
# 
    # @staticmethod
    # def ask_id():
        # id_correct = False
        # while not id_correct:
            # try:
                # user_id = int(input("Write the student ID: \n"))
            # except ValueError:
                # print("Only numbers are allowed.")
                # continue
# 
            # if user_id > 999999999:
                # print("Wrong, you have extra numbers.")
                # continue
# 
            # if user_id < 100000000:
                # print("Wrong, you are missing numbers.")
                # continue
            # id_correct = True
        # return str(user_id)
# 
    # @staticmethod
    # def ask_grade():
        # grade_correct = False
        # while not grade_correct:
            # try:
                # grade = int(input("Write the note: \n"))
            # except ValueError:
                # print("Only numbers are allowed.")
                # continue
# 
            # if not (0<=grade<=100):
                # print("Wrong, the note only goes from 0 to 100.")
                # continue
# 
            # grade_correct = True
        # return grade
# 
# 
# class Db():
# 
    # def __init__(self, filename):
        # self.filename = filename
# 
    # 
    # def find_id_in_db(self, cedula):
        # with open(self.filename, 'r') as dbfile:
            # row = 0
            # lines = dbfile.readlines()
            # for line in lines:
                # print(line)
                # # columns = line.split(',')
                # print(columns)
                # if cedula==columns[0]:
                    # return row
                # row += 1
            # return False
            # row = -1
            # return row
# 
    # def append_grade(self, row, grade):
        # with open(self.filename, 'r') as dbfile:
            # lines = dbfile.readlines()
            # if row >=len(lines) or row<1:
                # print(f"Invalid Row {row}, nothing done")
                # return
            # line = lines[row]
            # columns = line.split(',')
            # grades = columns[3:]
            # if len(grades)>=5:
                # print("No more grades allowed")
                # return
            # print("Grade Save")
            # columns = columns[:-1]+ [str(grade), "\n"]
#             print(f'columns {columns}')
#             # lines[row] = ",".join(columns)
#         # with open(self.filename, 'w') as dbfile:
#             # dbfile.writelines(lines)
# # 
#     # def allows_more_grades(self, row):
#         # with open(self.filename, 'r') as verifica:
#             # lines = verifica.readlines()
#             # line = lines[row]
#             # columns = line.split(',')
#             # grades = columns[3:]
#             print(columns[3:4])
#             # nota1 = columns[3:4]
#             # nota2 = columns[4:5]
#             # nota3 = columns[5:6]
#             # nota4 = columns[6:7]
#             print(nota1)
#             print(nota2)
#             print(nota3)
#             print(nota4)
#             # crea_una_lista = nota1+nota2+nota3+nota4
#             # print(crea_una_lista)
#             # 
# # 
# # 
# # 
# 
# def insert_grade():
    # row = -1
    # db = Db('Excel_Bases.csv')
    # while row < 1:
        # cedula = Utils.ask_id()
        # row = db.find_id_in_db(cedula)
        # if db.find_id_in_db(cedula) is False:
            # print(f'The id {cedula} was not found')
            # break
        # print("Correct ID")
        # pass
        # db.allows_more_grades(row)
        # if db.allows_more_grades(row) is False:
            # print("No more grades"[::1])
            # break
        # elif db.allows_more_grades(row) is True:
            # pass
        # nota = Utils.ask_grade() 
        # db.append_grade(row, nota)
    # 
# insert_grade()
