def func(n):
    if(n == 1):
        return 1
    else:
        return (n-1) + func(n-1)
    
while(True):
    n = int(input("Enter number: "))
    if( n == -1):
        print("Output: Finished")
        break
    else:
        print("Output: ", func(n))