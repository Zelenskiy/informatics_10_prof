def fact(n):
    print("!")
    if n == 0:
        return 1
    else:        
        return fact(n-1) * n

n = int(input("n = "))    
f = fact(n)
print (n, "! = ", f, sep="")


