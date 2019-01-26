while True:
    try:
        n,m = map(int,input().split(" "))
        if m<=1:
            break
        s = n
        suma = 0
        while s>=m:
            b = int(s)/int(m)
            r = int(s)%int(m)
            s = int(b)+int(r)
            suma = suma+b
        print(int(suma)+n)
    except EOFError:
        break
#uncomplete
