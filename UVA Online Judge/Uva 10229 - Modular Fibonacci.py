import math
def fib(n):
    i = h = int(1)
    j = k = int(0)
    while int(n)>0:
        if n%2==1:
            t = int(j)*int(h)
            j = int(i)*int(h) + int(j)*int(k) + int(t)
            i = int(i)*int(k) + int(t)
        t = int(h)*int(h)
        h = 2*int(k)*int(h) + int(t)
        k = int(k)*int(k) + int(t)
        n = int(n)/2
    return int(j)
while True:
    try:
        n,m = map(int,input().split(" "))
        f = fib(n)
        print(f)
        p = pow(2,n)
        ans = int(f) % int(p)
        print(ans)
    except EOFError:
        break
