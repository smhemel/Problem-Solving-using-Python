def modPow(x, y, n):
    if y==0:
        return 1
    elif y==1:
        return x%n
    elif y%2==1:
        p = modPow(x, y-1, n)
        return (p*x)%n
    else:
        p = modPow(x, y>>1,n)
        return (p*p)%n
test = int(input())
for i in range(test):
    x, y, n = map(int,input().split(" "))
    print(modPow(x, y, n))
