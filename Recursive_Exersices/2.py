def Fibonacci(n):
    if(n <= 1):
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
    
while(True):
    n = int(input("Enter a number: "))
    if(n == -1):
        break
    else:
        print("Fibonacci of ", n, "is: ", Fibonacci(n))
    