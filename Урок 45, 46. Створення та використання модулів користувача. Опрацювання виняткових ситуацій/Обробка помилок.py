s = []
while True:
    try:
        n = int(input("Введіть натуральне число або нуль для завершення "))
    except ValueError:
        print("Ви неправильно увели число")
    else:
        if n < 0:
           print("Ви неправильно увели число")
           continue
        if n == 0:
            break
        s.append(n)
print("Середнє арифметичне всіх уведених чисел")
sum = 0
count = len(s)
for x in s:
    sum += x
avg = sum / count
print(avg)

    
    
