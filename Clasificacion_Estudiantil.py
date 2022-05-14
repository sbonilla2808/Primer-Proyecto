
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
        print("Correct ID")
        pass
    
insert_grade()
