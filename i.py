def fac(a):
    l = 1
    for i in range(1,int(a+1)):
        l *=i
    return int(l)
while True:
    try:
        x = input().split(" ")
        n,m = x
        z = int(n)-int(m)
        if int(n)==0 and int(m)==0:
            break
        c = fac(int(n))/(fac(int(z))*fac(int(m)))
        print("%d things taken %d at a time is %d exactly." %(int(n),int(m),int(c)))
    except EOFError:
        break
    
