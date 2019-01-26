from math import *
while True:
    n = int(input())
    if not n:
        break
    flag = int(0)
    if n<0:
        flag = int(1)
        n = abs(n)
    p = 0
    while 1 << p <= n:
        p += 1
    print("p = %d" %p)
    for i in range(p, 0, -1):
        n1 = int(pow(n,1.0/i))
        if n1**i==n:
            if flag==0 or i%2==1:
                print(i)
            else:
                print("1")
            break
