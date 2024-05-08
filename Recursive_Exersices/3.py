def power(x, n):
    if(n == 0):
        return 1
    else:
        return (x * (power(x, n-1)))

while(True):
    x = int(input("Enter a number for base: "))
    n = int(input("Enter a number for exp: "))
    
    if(x == -1 or n == -1):
        break
    
    else:
        print(power(x, n))
    