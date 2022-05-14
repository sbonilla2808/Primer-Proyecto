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
        print(f'grades {grades}')
        columns = columns[:-1]+ [str(grade), "\n"]
        print(f'columns {columns}')
        lines[row] = ",".join(columns)
    with open(self.filename, 'w') as dbfile:
        dbfile.writelines(lines)