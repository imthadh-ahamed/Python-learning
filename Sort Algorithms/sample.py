def multiply(M, n):
    if n == 1:
        return M
    else:
        return M + multiply(M, n - 1)

while True:
    M = int(input("Enter a number for M: "))

    if M == -1:
       break

    n = int(input("Enter a number for n: "))

    print("Multiplication of", M, "and", n, "is:", multiply(M, n))
    

