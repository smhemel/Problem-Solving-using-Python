import math
n = int(input())
while (n>=0):
    x = input().split(" ")
    x1,x2,x3 = x
    total = 0
    a = 1
    b = 2
    c = 0
    for i in range(1,int(x1)):
        c = a+b
        a = b
        b = c
    total = (int(x2)**c)
    total = int(total)%int(x3)
    print(total)
    n-=1
