mas = [[34, 23 ,6 ,9],[35, 11, 54, 23], [15 ,40, 3, 44]]

for r in range(len(mas)):
    for c in range(len(mas[r])):
        print (mas[r][c], end="\t")
    print()

#Обчислення загальної суми й середнього значення елементів масиву
sum = 0
for r in range(len(mas)):
    for c in range(len(mas[r])):
        sum += mas[r][c]
print("Сума всіх значень ", sum)
count = len(mas) * len(mas[0])
avg = sum / count
print ("Середнє значення ", avg)


