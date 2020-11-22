rowCount = int(input("Уведіть кількість рядків "))
colCount = int(input("Уведіть кількість стовпців "))
mas = []
for r in range(rowCount):
    print("Уводимо рядок ", r)
    tmpMas = []
    for с in range(colCount):
        tmpMas.append(int(input()))
    mas.append(tmpMas)

for r in range(rowCount):
    for c in range(colCount):
        print('{:<7}'.format(mas[r][c]), end="")
    print()


        
