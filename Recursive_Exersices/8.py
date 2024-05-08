def func(n):
    if(n == 1):
        return 1
    else:
        return n + func(n-1)
    
while(True):
    n = int(input("Enter a number: "))
    if(n == -1):
        break
    else:
        print(func(n))