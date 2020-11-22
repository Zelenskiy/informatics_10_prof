rowCount = int(input("Уведіть кількість рядків "))
colCount = int(input("Уведіть кількість стовпців "))
mas = []
for r in range(rowCount):
    print("Уводимо рядок ", r)
    tmpMas = []
    for с in range(colCount):
        tmpMas.append(int(input()))
    mas.append(tmpMas)
print (mas)

        
