
shoppingList = [702790071]

file = open('excel_Bases.csv', 'r')

leer = file.read()

for shoppingList in leer:
    print(leer)
    



file.close()






"""
file = open('excel_Bases.csv', 'r')

output = file.read()

print(output)

file.close()



file = open('excel_Bases.csv', 'r')

lines = []

for line in file:
    lines.append(line.split(","))
    print(line.split(","))


file.close()

print(lines)

#Reference: http://www.easypythondocs.com/fileaccess.html
"""