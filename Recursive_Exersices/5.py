def sum(n):
    if(n == 1):
        return 1
    else:
        return(sum(n-1) + n)

while(True):
    n = int(input("Enter a number for n: "))
    if(n == -1):
        break
    elif(n < -1):
        print("Enter positive numbers only")
        continue

    print("sum of ", n, "is: ", sum(n))
    