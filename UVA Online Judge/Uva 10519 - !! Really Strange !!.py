while True:
    try:
        n = int(input())
        if n==0:
            print("1")
        elif n==1:
            print("2")
        else:
            print((n*n)-(n-2))
    except EOFError:
        break
