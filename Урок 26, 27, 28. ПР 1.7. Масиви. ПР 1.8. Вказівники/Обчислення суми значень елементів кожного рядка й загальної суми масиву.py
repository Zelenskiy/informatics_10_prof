mas = [[34, 23 ,6 ,9],[35, 11, 54, 23], [15 ,40, 3, 44]]

for r in range(len(mas)):
    for c in range(len(mas[r])):
        print (mas[r][c], end="\t")
    print()

#Обчислення суми значень елементів кожного рядка й загальної суми масиву
sum = 0
for r in range(len(mas)):
    sum = 0
    for c in range(len(mas[r])):
        sum += mas[r][c]
    print("Сума всіх значень рядка ",r, " дорівнює",  sum)



