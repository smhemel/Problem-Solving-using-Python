while True:
    try:
        n = int(input())
        if n==0:
            break
        else:
            if n>9:
                y = (n*10)/9
                x = int(y)-1
                if n%9==0:
                    print("%d %d" %(x,y))
                else:
                    print(int(y))
    except EOFError:
        break
