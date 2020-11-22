'''
1 2 3 4 5 6 7  8
1 1 2 3 5 8 13 21


'''
def fibo(n):
    if n < 3:
        return 1
    else:
        print(n)
        return fibo(n-1) + fibo(n-2)

n = int(input("n = "))    
f = fibo(n)
print ("f(", n, ") = ", f, sep="")


