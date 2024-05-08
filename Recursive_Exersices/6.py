def pow(x, n):
    if(n == 1):
        return x
    else:
        return x * pow(x, n-1)
    
x = int(input("Enter a number: "))
n = int(input("Enter a number for power: "))
print(pow(x, n))