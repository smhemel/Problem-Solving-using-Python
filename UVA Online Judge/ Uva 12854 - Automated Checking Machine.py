while True:
    try:
        x = input().split(' ')
        y = input().split(' ')
        a,b,c,d,e = x
        A,B,C,D,E = y
        if (int(a)==int(A) or int(b)==int(B) or int(c)==int(C) or int(d)==int(D) or int(e)==int(E)):
            print("N")
        else:
            print("Y")
    except EOFError:
        break
