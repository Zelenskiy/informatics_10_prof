mas = [[34, 54 ,6 , 9],
       [35, 11, 54, 23],
       [15 ,40, 3,  44]]

for r in range(len(mas)):
    for c in range(len(mas[r])):
        print (mas[r][c], end="\t")
    print()

#Обчислення кількості заданого елемента в масиві
x = int(input("Який елемент шукаємо? "))
count = 0
for r in range(len(mas)):
    for c in range(len(mas[r])):
        if mas[r][c] == x:
            count += 1
print("Кількість елементів ",x, " у масиві дорівнює",  count)




