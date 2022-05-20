row = -1
with open("Excel_Bases.csv", 'r') as verifica:
    lines = verifica.readlines()
    line = lines[row]
    columns = line.split(',')
    grades = columns[3:]
    nota_1 = lines[22:24]
    nota_2 = grades[25:27]
    nota_3 = grades[28:30]
    nota_4 = grades[31:33]

print(nota_1)

print(columns)
print(lines[3:])



