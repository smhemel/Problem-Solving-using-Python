while True:
    try:
        n = int(input())
        suma = 0
        a = 1
        b = 1
        if(n==1 or n==2):
            print("1")
        else:
            for i in range(2,n):
                suma = int(a)+int(b)
                a = int(b)
                b = int(suma)
                i+=1
            print(suma)
    except EOFError:
        break
