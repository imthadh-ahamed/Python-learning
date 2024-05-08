def sumcube(n):
    if(n == 1):
        return 1
    else:
        return(sumcube(n-1) + (n*n*n))
    
while(True):
    n = int(input("Enter a number for n: "))
    if(n == -1):
        break
    else:
        print("Summation of ", sumcube(n))
    