while True:
    try:
        n = int(input())
        a = 0
        b = 1
        c = 0
        for i in range(1,n):
            c = a+b
            a = b
            b = c
        print("The Fibonacci number for %d is %d" %(n,c))
    except EOFError:
        break
