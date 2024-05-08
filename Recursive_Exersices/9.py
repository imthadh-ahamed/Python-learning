def func(n):
    if(n == 1):
        return 2
    else:
        return func(n-1)/2

while(True):
    n = int(input("Enter a number: "))
    if(n == -1):
        break
    else:
        print(func(n))