s = []
while (True):
     try:
        n = int(input("Уведіть ціле число: "))
        if n == 0:
            break
        else:
            s.append(n)
     except ValueError:
         print("Уведіть ціле число")
print(s)



