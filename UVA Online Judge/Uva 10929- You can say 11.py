while True:
    try:
        n = str(input())
        m = len(n)
        s = 0
        for i in range(m):
            s = s*10 + int(n[i])
            s = s%11
        if n==0:
            break
        elif s==0:
            print("%d is a multiple of 11." %int(n))
        else:
           print("%d is not a multiple of 11." %int(n))
    except EOFError:
        break
