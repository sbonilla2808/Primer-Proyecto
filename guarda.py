def notas_altas():
    db = Db('Excel_Bases.csv')
    row = -1
    db.verifica_grades(row)
    db.evaluate_grade_1(row)
    db.evaluate_grade_2(row)  
    db.evaluate_grade_3(row)
    db.evaluate_grade_4(row)

    while True:
        if db.verifica_grades(row) is None:
            print("No se puede calificar por que tiene menos de 3 notas")
            return
        #Nota 1 vs 2::
        if db.evaluate_grade_1(row) == True:
            print("La Nota 1 es mayor que la Nota 2.")
            pass
        else:
            print("La nota 2 es mayor que la 1")
            pass

        if db.evaluate_grade_1(row) == True:
            print("La Nota 1 es mayor que la Nota 3.")
            pass
        else:
            print("La nota 3 es mayor que la 1")
            pass

        if db.evaluate_grade_1(row) == True:
            print("La Nota 1 es mayor que la Nota 4.")
            pass
        else:
            print("La nota 4 es mayor que la 1")
            pass

        #Nota 2 vs 1::
        if db.evaluate_grade_1(row) == True:
            print("La Nota 2 es mayor que la Nota 1.")
            pass
        else:
            print("La nota 1 es mayor que la 2")
            pass

        if db.evaluate_grade_1(row) == True:
            print("La Nota 2 es mayor que la Nota 3.")
            pass
        else:
            print("La nota 3 es mayor que la 2")
            pass

        if db.evaluate_grade_1(row) == True:
            print("La Nota 2 es mayor que la Nota 4.")
            pass
        else:
            print("La nota 4 es mayor que la 2")
            pass

        #Nota 3 vs 1::
        if db.evaluate_grade_1(row) == True:
            print("La Nota 3 es mayor que la Nota 1.")
            pass
        else:
            print("La nota 1 es mayor que la 3")
            pass

        if db.evaluate_grade_1(row) == True:
            print("La Nota 3 es mayor que la Nota 2.")
            pass
        else:
            print("La nota 2 es mayor que la 3")
            pass

        if db.evaluate_grade_1(row) == True:
            print("La Nota 3 es mayor que la Nota 4.")
            pass
        else:
            print("La nota 4 es mayor que la 3 ")
            pass

        #Nota 4 vs 1::
        if db.evaluate_grade_1(row) == True:
            print("La Nota 4 es mayor que la Nota 1.")
            pass
        else:
            print("La nota 1 es mayor que la 4")
            pass

        if db.evaluate_grade_1(row) == True:
            print("La Nota 4 es mayor que la Nota 2.")
            pass
        else:
            print("La nota 2 es mayor que la 4")
            pass

        if db.evaluate_grade_1(row) == True:
            print("La Nota 4 es mayor que la Nota 3.")
            pass
        else:
            print("La nota 3 es mayor que la 4")
            pass
        break
notas_altas()